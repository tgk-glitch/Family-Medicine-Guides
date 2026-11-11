// Keep every page at its current address (counselling.html, not /counselling/),
// so existing links, bookmarks and QR codes keep working.
// The OSCE page is only published while "showOsce" is true in src/_data/site.json.
export default {
  permalink: (data) => {
    if (data.page.filePathStem === "/osce" && !(data.site && data.site.showOsce)) return false;
    return `${data.page.filePathStem}.html`;
  },
};
