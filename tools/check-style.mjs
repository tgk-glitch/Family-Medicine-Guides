// Style check for Family Medicine Guides. Run with: npm run check
//
// Fails (exit code 1) if any page, include, script or leaflet source contains:
//   1. an em dash (the long dash, U+2014), typed or as an HTML entity;
//   2. a hospital or employer name, or an email address, in the public pages.
//
// It only reads files. It changes nothing and needs no extra packages.
import { readdirSync, readFileSync, statSync } from "node:fs";
import { join, extname, relative } from "node:path";

const ROOT = new URL("..", import.meta.url).pathname;
const SCAN = ["src", "tools", "README.md", "eleventy.config.js", "package.json"];
const TEXT = new Set([".html", ".js", ".mjs", ".json", ".md", ".css", ".py", ".liquid", ".txt"]);
const SKIP = new Set(["node_modules", "_site", ".git", "_out"]);

const EM = String.fromCharCode(0x2014);
const DASH = new RegExp(EM + "|&mdash;|&#8212;|&#x2014;|\\\\u2014", "gi");
// Public pages must not name the hospital or employer, or show an email address.
// (Region names are not checked here, because a Hajj or Umrah guide may need them. Check those by eye.)
const PRIVATE = /\b(PMBAH|MNGHA|National Guard|Prince Mohammed Bin Abdulaziz)\b|mailto:|[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}/gi;

function* walk(path) {
  const st = statSync(path);
  if (st.isDirectory()) {
    for (const name of readdirSync(path)) {
      if (!SKIP.has(name)) yield* walk(join(path, name));
    }
  } else if (TEXT.has(extname(path))) {
    yield path;
  }
}

const problems = [];
for (const entry of SCAN) {
  for (const file of walk(join(ROOT, entry))) {
    const rel = relative(ROOT, file);
    if (rel === "tools/check-style.mjs") continue;
    const lines = readFileSync(file, "utf8").split("\n");
    lines.forEach((line, i) => {
      for (const m of line.matchAll(DASH)) {
        problems.push(`${rel}:${i + 1}  em dash  ...${line.slice(Math.max(0, m.index - 30), m.index + 30).trim()}...`);
      }
      if (rel.startsWith("src/")) {
        for (const m of line.matchAll(PRIVATE)) {
          problems.push(`${rel}:${i + 1}  affiliation or email: "${m[0]}"`);
        }
      }
    });
  }
}

if (problems.length) {
  console.error(`Style check failed: ${problems.length} problem(s)\n`);
  for (const p of problems.slice(0, 200)) console.error("  " + p);
  if (problems.length > 200) console.error(`  ... and ${problems.length - 200} more`);
  console.error("\nReplace an em dash with a colon, comma, semicolon, full stop or parentheses.");
  console.error("In page titles use |. In an empty table cell use -. En dashes are for ranges only (6–11 years).");
  process.exit(1);
}
console.log("Style check passed: no em dashes, no affiliation or email in public pages.");
