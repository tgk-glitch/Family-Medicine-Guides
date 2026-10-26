// Builds the private app into _site/ (works the same on Windows, macOS and Linux).
process.env.FMG_APP = "1";
const { Eleventy } = await import("@11ty/eleventy");
const elev = new Eleventy();
await elev.write();
