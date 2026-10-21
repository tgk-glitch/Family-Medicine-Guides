/* ── helpers ─────────────────────────────────────────────── */
function csAr(){ return !!(window.fmgIsArabic && window.fmgIsArabic()); }
function csT(en, ar){ return csAr() ? ar : en; }
function csFill(sel, opts){
  var keep = sel.value;
  var html = '';
  for (var i=0;i<opts.length;i++){ html += '<option value="'+opts[i][0]+'">'+csT(opts[i][1], opts[i][2])+'</option>'; }
  sel.innerHTML = html;
  if (keep !== '' && keep !== undefined){ sel.value = keep; }
  if (sel.selectedIndex < 0){ sel.selectedIndex = 0; }
}
window.fmgLangHooks = window.fmgLangHooks || [];

/* ── 1 · Strategy chooser ────────────────────────────────── */
(function(){
  var prob = document.getElementById('chProblem');
  var stage = document.getElementById('chStage');
  var out = document.getElementById('chResult');
  if (!prob || !stage || !out) return;
  var PROBS = [
    ['beh', 'A health behaviour — tobacco, diet, activity, weight, substance use', 'سلوك صحي — التبغ أو الغذاء أو النشاط أو الوزن أو تعاطي المواد'],
    ['adh', 'Adherence — medication, monitoring, follow-up', 'الالتزام — الأدوية أو المتابعة الذاتية أو المواعيد'],
    ['psy', 'Emotional or psychosocial distress — stress, grief, a life event', 'ضيق عاطفي أو نفسي اجتماعي — ضغوط أو حزن أو حدث حياتي']
  ];
  var STAGES = [
    ['pc', 'Not considering change in the next 6 months', 'لا يفكر في التغيير خلال الأشهر الستة القادمة'],
    ['c',  'Thinking about it in the next 6 months, but undecided', 'يفكر فيه خلال الأشهر الستة القادمة لكنه متردد'],
    ['p',  'Planning to start within 30 days', 'يخطط للبدء خلال 30 يومًا'],
    ['a',  'Has already changed — less than 6 months ago', 'غيّر بالفعل — منذ أقل من 6 أشهر'],
    ['m',  'Has kept the change for more than 6 months', 'حافظ على التغيير أكثر من 6 أشهر']
  ];
  var R = {
    pc: { st:['Precontemplation','ما قبل التفكير'],
          lead:['Brief motivational interviewing + the 5 R’s','مقابلة تحفيزية مختصرة + الـ 5R’s'], link:'#mi',
          goal:['Raise awareness without pressure, respect the choice, and keep the door open. Offer written information.','ارفع الوعي دون ضغط، واحترم اختياره، وأبقِ الباب مفتوحًا. قدّم معلومات مكتوبة.'],
          say:['“Would it be all right if we talked about this for a minute? You can tell me if now isn’t a good time.”','«هل تمانع أن نتحدث في هذا لدقيقة؟ أخبرني إن لم يكن الوقت مناسبًا.»'] },
    c:  { st:['Contemplation','التفكير'],
          lead:['Motivational interviewing — decisional balance','المقابلة التحفيزية — ميزان القرار'], link:'#mi',
          goal:['Draw out both sides in the patient’s own words and develop discrepancy with what matters to them.','استخرج الجانبين بكلمات المريض نفسه، وابنِ التباين مع ما يهمّه.'],
          say:['“What do you get out of it — and what worries you about it?”','«ما الذي يعطيك إياه — وما الذي يقلقك منه؟»'] },
    p:  { st:['Preparation','الاستعداد'],
          lead:['Five A’s — Assist and Arrange (or FRAMES with a menu)','الخطوات الخمس — ساعد ورتِّب (أو FRAMES مع قائمة خيارات)'], link:'#five-as',
          goal:['Agree a concrete plan and a start date, anticipate barriers, add medication where indicated, and book follow-up.','اتفقا على خطة وتاريخ بدء محددين، وتوقّعا العقبات، وأضف الدواء عند الحاجة، واحجز المتابعة.'],
          say:['“Which day in the next few weeks would suit you best to start?”','«أي يوم في الأسابيع القادمة يناسبك أكثر للبدء؟»'] },
    a:  { st:['Action','الفعل'],
          lead:['Reinforce and problem-solve (Five A’s — Arrange)','عزّز وحلّ المشكلات (الخطوات الخمس — رتِّب)'], link:'#five-as',
          goal:['Affirm success, build self-efficacy, and plan for the triggers they have not met yet.','أشِد بالنجاح، وابنِ الكفاءة الذاتية، وخطّط للمحفزات التي لم يواجهها بعد.'],
          say:['“What has been the hardest moment so far, and how did you get through it?”','«ما أصعب لحظة مرّت عليك حتى الآن، وكيف تجاوزتها؟»'] },
    m:  { st:['Maintenance','المحافظة'],
          lead:['Relapse prevention','منع الانتكاس'], link:'#stages',
          goal:['Normalise lapses as part of change, credit the patient’s effort, and agree what to do if a slip happens.','طبِّع الهفوات بوصفها جزءًا من التغيير، وانسب الفضل لجهد المريض، واتفقا على ما يفعله إن تعثّر.'],
          say:['“One slip doesn’t cancel months of effort. What would help you get straight back on track?”','«زلّة واحدة لا تمحو شهورًا من الجهد. ما الذي يساعدك على العودة فورًا؟»'] }
  };
  function render(){
    csFill(prob, PROBS); csFill(stage, STAGES);
    calc();
  }
  function calc(){
    var pv = prob.value, sv = stage.value, ar = csAr(), i = ar ? 1 : 0;
    var html;
    if (pv === 'psy'){
      html = '<span class="lead">' + csT('Lead with BATHE','ابدأ بـ BATHE') + '</span>'
        + csT('Stage of change matters less here — start by understanding the situation and how the patient is coping. Screen with PHQ-9 / GAD-7 and look for red flags.',
              'مرحلة التغيير أقل أهمية هنا — ابدأ بفهم الموقف وكيف يتكيّف المريض. افحص بـ PHQ-9 / GAD-7 وابحث عن العلامات التحذيرية.')
        + '<span class="say">' + csT('“What has been going on in your life?”','«ما الذي يجري في حياتك هذه الأيام؟»') + '</span>'
        + '<span class="sub"><a href="#bathe">' + csT('Go to BATHE →','انتقل إلى BATHE ←') + '</a> · <a href="' + (ar ? 'mental-health.html?lang=ar' : 'mental-health.html') + '#depression">' + csT('PHQ-9 / GAD-7','PHQ-9 / GAD-7') + '</a></span>';
      out.style.borderColor = '#9C4F2E';
    } else {
      var r = R[sv];
      var lead = r.lead[i];
      if (pv === 'adh' && sv === 'p'){ lead = csT('FRAMES — feedback with the patient’s own numbers, then a menu','FRAMES — تغذية راجعة بأرقام المريض نفسه، ثم قائمة خيارات'); }
      html = '<span class="lead">' + csT('Stage: ','المرحلة: ') + r.st[i] + ' — ' + lead + '</span>'
        + r.goal[i]
        + '<span class="say">' + r.say[i] + '</span>'
        + '<span class="sub"><a href="' + r.link + '">' + csT('Read the section →','اقرأ القسم ←') + '</a>'
        + (sv === 'pc' || sv === 'c' ? csT(' · Re-ask at every visit — stage can change within one consultation.',' · أعد السؤال في كل زيارة — فقد تتغير المرحلة خلال الاستشارة الواحدة.') : '')
        + '</span>';
      out.style.borderColor = (sv === 'pc') ? '#C98A2C' : '#9C4F2E';
    }
    out.innerHTML = html;
  }
  prob.addEventListener('change', calc);
  stage.addEventListener('change', calc);
  window.fmgLangHooks.push(render);
  render();
})();

/* ── 2 · Readiness ruler ─────────────────────────────────── */
(function(){
  var imp = document.getElementById('rulImp'), conf = document.getElementById('rulConf');
  var iv = document.getElementById('rulImpV'), cv = document.getElementById('rulConfV');
  var out = document.getElementById('rulResult');
  if (!imp || !conf || !out) return;
  function whyQ(x){
    if (x === 0) return csT('“What would have to happen for it to matter even a little to you?”','«ما الذي يجب أن يحدث ليصبح الأمر مهمًا لك ولو قليلًا؟»');
    var low = Math.max(0, x - 3);
    return csT('“Why are you at ' + x + ' and not ' + low + '?”', '«لماذا أنت عند ' + x + ' وليس ' + low + '؟»');
  }
  function upQ(x){
    if (x >= 10) return csT('“What makes you so sure?”','«ما الذي يجعلك واثقًا إلى هذا الحد؟»');
    var up = Math.min(10, x + 2);
    return csT('“What would it take to move you from ' + x + ' to ' + up + '?”', '«ما الذي يلزم لينقلك من ' + x + ' إلى ' + up + '؟»');
  }
  function calc(){
    var I = parseInt(imp.value,10), C = parseInt(conf.value,10);
    iv.textContent = I; cv.textContent = C;
    var lead, body, ask, col;
    if (I <= 4){
      lead = csT('Work on importance first','اعمل على الأهمية أولًا');
      body = csT('Importance is 4 or below. Explore values and develop discrepancy; use Elicit–Provide–Elicit to offer information. Planning now would be premature.',
                 'الأهمية 4 أو أقل. استكشف القيم وابنِ التباين؛ واستخدم «استخرج–قدِّم–استخرج» لتقديم المعلومة. التخطيط الآن سابق لأوانه.');
      ask = whyQ(I); col = '#C98A2C';
    } else if (C <= 4){
      lead = csT('Important, but low confidence — build self-efficacy','مهم لكن الثقة منخفضة — ابنِ الكفاءة الذاتية');
      body = csT('Importance is 5 or above while confidence is 4 or below. Recall past successes, offer a menu of supports, and agree a small first step.',
                 'الأهمية 5 أو أكثر بينما الثقة 4 أو أقل. استحضر نجاحات سابقة، وقدّم قائمة من وسائل الدعم، واتفقا على خطوة أولى صغيرة.');
      ask = upQ(C); col = '#C98A2C';
    } else if (I >= 7 && C >= 7){
      lead = csT('Ready to plan','جاهز للتخطيط');
      body = csT('Both are 7 or above. Move to planning: a start date, the support and medication to use, and follow-up.',
                 'كلاهما 7 أو أكثر. انتقل إلى التخطيط: تاريخ البدء، ووسائل الدعم والدواء، والمتابعة.');
      ask = csT('“What would be a good first step for you?”','«ما الخطوة الأولى المناسبة لك؟»'); col = '#1F5C55';
    } else {
      lead = csT('Keep evoking — both rulers are in the middle','واصل الاستخراج — المسطرتان في المنتصف');
      body = csT('Neither score is low, but they are not yet both 7 or above. Ask about each ruler and reflect the change talk you hear.',
                 'لا توجد درجة منخفضة، لكنهما لم تبلغا معًا 7 أو أكثر. اسأل عن كل مسطرة واعكس حديث التغيير الذي تسمعه.');
      ask = (I <= C) ? whyQ(I) : upQ(C); col = '#9C4F2E';
    }
    out.innerHTML = '<span class="lead">' + lead + '</span>' + body + '<span class="say">' + ask + '</span>'
      + '<span class="sub">' + csT('Always ask why the number is not lower — never why it is not higher. The answer is change talk.',
                                   'اسأل دائمًا لماذا ليس الرقم أقل — لا لماذا ليس أعلى؛ فالجواب يكون حديث تغيير.') + '</span>';
    out.style.borderColor = col;
  }
  imp.addEventListener('input', calc);
  conf.addEventListener('input', calc);
  window.fmgLangHooks.push(calc);
  calc();
})();

/* ── 3 · Heaviness of Smoking Index ──────────────────────── */
(function(){
  var t = document.getElementById('hsiT'), c = document.getElementById('hsiC');
  var out = document.getElementById('hsiResult');
  if (!t || !c || !out) return;
  var TT = [
    ['3', 'Within 5 minutes', 'خلال 5 دقائق'],
    ['2', '6–30 minutes', '6–30 دقيقة'],
    ['1', '31–60 minutes', '31–60 دقيقة'],
    ['0', 'After 60 minutes', 'بعد 60 دقيقة']
  ];
  var CC = [
    ['0', '10 or fewer', '10 أو أقل'],
    ['1', '11–20', '11–20'],
    ['2', '21–30', '21–30'],
    ['3', '31 or more', '31 أو أكثر']
  ];
  function render(){ csFill(t, TT); csFill(c, CC); calc(); }
  function calc(){
    var ts = parseInt(t.value,10), cs = parseInt(c.value,10), s = ts + cs;
    var band, col, plan;
    // 21 mg patch if >10 cigarettes/day (cs >= 1) or first cigarette within 30 min (ts >= 2)
    var strong = (cs >= 1 || ts >= 2);
    var patch = strong ? csT('21 mg/24 h patch','لصقة 21 ملغ/24 ساعة') : csT('14 mg/24 h patch','لصقة 14 ملغ/24 ساعة');
    if (s <= 1){ band = csT('Low dependence','اعتماد منخفض'); col = '#1F5C55';
      plan = csT('Behavioural support may be enough for some; if using NRT, a ' + patch + ' or a short-acting form alone is reasonable. Varenicline is also an option.',
                 'قد يكفي الدعم السلوكي لدى البعض؛ وإن استُخدمت بدائل النيكوتين فـ' + patch + ' أو شكل قصير المفعول وحده خيار معقول. وفارينيكلين خيار أيضًا.');
    } else if (s <= 4){ band = csT('Moderate dependence','اعتماد متوسط'); col = '#C98A2C';
      plan = csT('Offer varenicline, or combination NRT: ' + patch + ' plus gum, lozenge or inhaler for cravings. Add behavioural support.',
                 'اعرض فارينيكلين، أو بدائل النيكوتين المركّبة: ' + patch + ' مع علكة أو أقراص استحلاب أو جهاز استنشاق للرغبة الملحّة. وأضف الدعم السلوكي.');
    } else { band = csT('High dependence','اعتماد مرتفع'); col = '#B0392C';
      plan = csT('Varenicline or combination NRT (' + patch + ' plus a short-acting form), with structured support — book the cessation clinic. Withdrawal is likely to be marked: warn the patient in advance.',
                 'فارينيكلين أو بدائل النيكوتين المركّبة (' + patch + ' مع شكل قصير المفعول)، مع دعم منظّم — احجز عيادة الإقلاع. يُتوقع أن يكون الانسحاب واضحًا: نبّه المريض مسبقًا.');
    }
    out.innerHTML = '<span class="lead">HSI = ' + s + ' / 6 — ' + band + '</span>' + plan
      + '<span class="sub">' + csT('Bands: 0–1 low · 2–4 moderate · 5–6 high. A 21 mg patch is suggested when the patient smokes more than 10 a day or smokes within 30 minutes of waking.',
                                   'الفئات: 0–1 منخفض · 2–4 متوسط · 5–6 مرتفع. تُقترح لصقة 21 ملغ حين يدخن المريض أكثر من 10 سجائر يوميًا أو يدخن خلال 30 دقيقة من الاستيقاظ.') + '</span>';
    out.style.borderColor = col;
  }
  t.addEventListener('change', calc);
  c.addEventListener('change', calc);
  window.fmgLangHooks.push(render);
  render();
})();
