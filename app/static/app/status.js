/* App status page: shows whether this device has the app saved for offline use. */
(function () {
  "use strict";
  var $ = function (id) { return document.getElementById(id); };
  var isIOS = /iPad|iPhone|iPod/.test(navigator.userAgent) || (navigator.platform === "MacIntel" && navigator.maxTouchPoints > 1);
  var standalone = window.matchMedia("(display-mode: standalone)").matches || navigator.standalone === true;

  function row(k, v, cls) {
    var r = document.createElement("div"); r.className = "row";
    var a = document.createElement("span"); a.className = "k"; a.textContent = k;
    var b = document.createElement("span"); b.className = "v " + (cls || ""); b.textContent = v;
    r.appendChild(a); r.appendChild(b); $("rows").appendChild(r);
  }
  function summary(text, cls) { var s = $("summary"); s.textContent = text; s.className = "big " + cls; }

  function ask(worker, msg, key) {
    return new Promise(function (resolve) {
      var done = false;
      function onMsg(e) { if (e.data && e.data[key] !== undefined) { done = true; navigator.serviceWorker.removeEventListener("message", onMsg); resolve(e.data[key]); } }
      navigator.serviceWorker.addEventListener("message", onMsg);
      worker.postMessage(msg);
      setTimeout(function () { if (!done) { navigator.serviceWorker.removeEventListener("message", onMsg); resolve(null); } }, 60000);
    });
  }

  async function check() {
    $("rows").textContent = "";
    var info = { ua: navigator.userAgent, standalone: standalone, online: navigator.onLine, secure: window.isSecureContext };
    row("Opened as", standalone ? "Installed app" : "Browser tab", standalone ? "ok" : "warn");
    row("Internet", navigator.onLine ? "Online" : "Offline", navigator.onLine ? "ok" : "warn");

    if (!("serviceWorker" in navigator) || !window.isSecureContext) {
      row("Offline support", "Not available here", "bad");
      summary("This browser can’t save the app. Open the address in Safari (iPhone/iPad) or Chrome/Edge.", "bad");
      $("details").textContent = JSON.stringify(info, null, 1);
      return;
    }
    var reg = await navigator.serviceWorker.getRegistration("/");
    var worker = reg && (reg.active || reg.waiting || reg.installing);
    info.sw = reg ? { active: !!reg.active, waiting: !!reg.waiting, installing: !!reg.installing } : null;
    row("Offline helper", reg && reg.active ? "Running" : reg ? "Starting…" : "Not installed", reg && reg.active ? "ok" : "bad");
    row("Controls this page", navigator.serviceWorker.controller ? "Yes" : "No (reload once)", navigator.serviceWorker.controller ? "ok" : "warn");

    var st = worker ? await ask(worker, "status", "status") : null;
    if (st) {
      var savedN = st.total - st.missing.length;
      row("Files saved", savedN + " of " + st.total, st.missing.length ? "warn" : "ok");
      row("App version", st.version);
      info.missing = st.missing;
    }
    if (navigator.storage && navigator.storage.estimate) {
      try { var est = await navigator.storage.estimate(); row("Space used", (est.usage / 1048576).toFixed(1) + " MB"); } catch (_) {}
    }
    if (navigator.storage && navigator.storage.persisted) {
      try { var p = await navigator.storage.persisted(); row("Protected from clean-up", p ? "Yes" : (isIOS && standalone ? "Yes (Home Screen app)" : "No"), p || (isIOS && standalone) ? "ok" : "warn"); } catch (_) {}
    }

    if (!reg || !reg.active) summary(navigator.onLine ? "Not saved yet. Stay online, wait 30 seconds, then tap “Check again”." : "Not saved on this device yet. Connect to the internet and open the app once.", "bad");
    else if (st && st.missing.length) summary(st.missing.length + " file(s) not saved yet. Stay online and tap “Save missing files now”.", "warn");
    else if (!standalone && isIOS) summary("Saved in this browser — but for the real offline app, add it to the Home Screen (Share → Add to Home Screen) and open it from the icon once while online.", "warn");
    else summary("Ready for offline use ✓", "ok");
    $("details").textContent = JSON.stringify(info, null, 1);
  }

  $("reload").addEventListener("click", function () { check(); });
  $("save").addEventListener("click", async function () {
    var btn = this; btn.disabled = true; btn.textContent = "Saving…";
    try {
      if (navigator.storage && navigator.storage.persist) { try { await navigator.storage.persist(); } catch (_) {} }
      var reg = await navigator.serviceWorker.getRegistration("/");
      var worker = reg && reg.active;
      if (worker) await ask(worker, "saveMissing", "saved");
      else if (reg) await reg.update();
    } catch (_) {}
    btn.disabled = false; btn.textContent = "Save missing files now";
    check();
  });
  check();
})();
