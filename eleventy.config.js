// Eleventy configuration for Family Medicine Guides.
// Pages live in src/. Shared pieces (menu, footer credit) live in src/_includes/.
// The finished website is written to _site/ — that folder is what goes online.
//
// Private app build: FMG_APP=1 adds the app layer from app/plugin.js
// (offline mode, install-as-app, self-hosted fonts, strict security policy).
// Without FMG_APP the output is exactly the public website.
const appPlugin = process.env.FMG_APP === "1" ? (await import("./app/plugin.js")).default : null;

export default function (eleventyConfig) {
  if (appPlugin) eleventyConfig.addPlugin(appPlugin);
  // Copy these as they are, without processing.
  eleventyConfig.addPassthroughCopy("src/downloads");
  eleventyConfig.addPassthroughCopy("src/search-index.js");
  // eleventyConfig.addPassthroughCopy("src/assets");  // turn on when an assets folder is added

  return {
    dir: { input: "src", includes: "_includes", output: "_site" },
    templateFormats: ["html", "md", "liquid"],
    htmlTemplateEngine: "liquid",
    markdownTemplateEngine: "liquid",
  };
}
