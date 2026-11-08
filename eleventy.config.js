// Eleventy configuration for Family Medicine Guides.
// Pages live in src/. Shared pieces (menu, footer credit) live in src/_includes/.
// The finished website is written to _site/ — that folder is what goes online.
export default function (eleventyConfig) {
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
