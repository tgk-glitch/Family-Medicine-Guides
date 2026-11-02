<!-- FMG-I18N-JS:START -->
<script>
(function(){
  window.fmgLangHooks = window.fmgLangHooks || [];
  var root = document.documentElement;
  window.fmgIsArabic = function(){ return root.getAttribute('data-lang') === 'ar'; };
  window.fmgSetLang = function(lang, persist){
    lang = (lang === 'ar') ? 'ar' : 'en';
    root.setAttribute('data-lang', lang);
    root.setAttribute('lang', lang);
    root.setAttribute('dir', lang === 'ar' ? 'rtl' : 'ltr');
    if (persist !== false){ try { localStorage.setItem('fmgLang', lang); } catch(e){} }
    var btns = document.querySelectorAll('[data-fmg-lang]');
    for (var i=0;i<btns.length;i++){ btns[i].setAttribute('aria-pressed', btns[i].getAttribute('data-fmg-lang') === lang ? 'true' : 'false'); }
    for (var j=0;j<window.fmgLangHooks.length;j++){ try { window.fmgLangHooks[j](lang); } catch(e){} }
  };
  var start = 'en', q = null;
  try { q = new URLSearchParams(location.search).get('lang'); } catch(e){}
  if (q === 'ar' || q === 'en'){ start = q; }
  else { try { start = localStorage.getItem('fmgLang') || 'en'; } catch(e){} }
  var btns = document.querySelectorAll('[data-fmg-lang]');
  for (var i=0;i<btns.length;i++){
    btns[i].addEventListener('click', function(){ window.fmgSetLang(this.getAttribute('data-fmg-lang')); });
  }
  window.fmgSetLang(start, q ? false : true);
})();
</script>
<!-- FMG-I18N-JS:END -->