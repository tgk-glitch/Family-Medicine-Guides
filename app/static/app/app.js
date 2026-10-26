/* Family Medicine Guides — private app helper (loaded on every page of the app build).
 * - registers the offline service worker
 * - shows "Update ready" when a new version has been published
 * - offers "Install app" where the browser supports it
 * - shows a small "Private preview" badge and an offline indicator
 * Labels follow the page language (English / Arabic). */
(function () {
  "use strict";
  var isAr = function () { return /^ar/i.test(document.documentElement.lang || ""); };
  var t = function (en, ar) { return isAr() ? ar : en; };

  function el(tag, cls, text) {
    var n = document.createElement(tag);
    n.className = cls;
    if (text) n.textContent = text;
    return n;
  }

  // ---- badge (private preview · offline) ----
  var badge = el("div", "fmgapp-badge");
  badge.setAttribute("role", "status");
  badge.setAttribute("aria-live", "polite");
  var hideTimer = null;
  function paintBadge() {
    badge.dataset.offline = navigator.onLine ? "0" : "1";
    // Online: show briefly, then fade out so it never covers content. Offline: keep it visible.
    badge.classList.remove("fmgapp-hidden");
    clearTimeout(hideTimer);
    if (navigator.onLine) hideTimer = setTimeout(function () { badge.classList.add("fmgapp-hidden"); }, 4000);
    badge.textContent = navigator.onLine
      ? t("Private preview", "نسخة خاصة للمعاينة")
      : t("Offline · saved copy", "دون اتصال · نسخة محفوظة");
  }

  // ---- toast with an action button ----
  var toast = null;
  function showToast(message, actionLabel, onAction) {
    if (toast) toast.remove();
    toast = el("div", "fmgapp-toast");
    toast.setAttribute("role", "status");
    toast.appendChild(el("span", "fmgapp-toast-msg", message));
    if (actionLabel) {
      var b = el("button", "fmgapp-toast-btn", actionLabel);
      b.type = "button";
      b.addEventListener("click", onAction);
      toast.appendChild(b);
    }
    var x = el("button", "fmgapp-toast-x", "×");
    x.type = "button";
    x.setAttribute("aria-label", t("Close", "إغلاق"));
    x.addEventListener("click", function () { toast.remove(); toast = null; });
    toast.appendChild(x);
    document.body.appendChild(toast);
  }

  // ---- install prompt (Chrome, Edge, Android) ----
  var deferred = null;
  window.addEventListener("beforeinstallprompt", function (e) {
    e.preventDefault();
    deferred = e;
    try { if (localStorage.getItem("fmgAppInstallDismissed") === "1") return; } catch (_) {}
    showToast(t("Install Family Medicine Guides as an app?", "تثبيت أدلة طب الأسرة كتطبيق؟"),
      t("Install", "تثبيت"), function () {
        if (!deferred) return;
        deferred.prompt();
        deferred.userChoice.then(function (c) {
          if (c.outcome !== "accepted") { try { localStorage.setItem("fmgAppInstallDismissed", "1"); } catch (_) {} }
          deferred = null;
          if (toast) { toast.remove(); toast = null; }
        });
      });
  });

  // ---- service worker + updates ----
  function watchForUpdate(reg) {
    function offer(worker) {
      showToast(t("A new version is ready.", "يتوفر إصدار جديد."), t("Update", "تحديث"), function () {
        worker.postMessage("skipWaiting");
      });
    }
    if (reg.waiting && navigator.serviceWorker.controller) offer(reg.waiting);
    reg.addEventListener("updatefound", function () {
      var w = reg.installing;
      if (!w) return;
      w.addEventListener("statechange", function () {
        if (w.state === "installed") {
          if (navigator.serviceWorker.controller) offer(w);
          else showToast(t("Saved for offline use.", "حُفظ التطبيق للاستخدام دون اتصال."));
        }
      });
    });
  }

  if ("serviceWorker" in navigator && window.isSecureContext) {
    var reloading = false;
    navigator.serviceWorker.addEventListener("controllerchange", function () {
      if (reloading) return;
      reloading = true;
      location.reload();
    });
    window.addEventListener("load", function () {
      navigator.serviceWorker.register("/sw.js", { scope: "/" }).then(function (reg) {
        watchForUpdate(reg);
        // Check for a new version when the app comes back to the foreground.
        document.addEventListener("visibilitychange", function () {
          if (document.visibilityState === "visible") reg.update().catch(function () {});
        });
      }).catch(function () { /* offline install not available; site still works */ });
    });
  }

  function start() {
    paintBadge();
    document.body.appendChild(badge);
    window.addEventListener("online", paintBadge);
    window.addEventListener("offline", paintBadge);
    // Re-label when the page switches language.
    new MutationObserver(paintBadge).observe(document.documentElement, { attributes: true, attributeFilter: ["lang"] });
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", start);
  else start();
})();
