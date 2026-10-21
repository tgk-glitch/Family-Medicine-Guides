// Keep every page at its current address (counselling.html, not /counselling/),
// so existing links, bookmarks and QR codes keep working.
export default {
  permalink: (data) => `${data.page.filePathStem}.html`,
};
