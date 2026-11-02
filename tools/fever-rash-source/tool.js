/* ── Fever with rash: isolation, exclusion & contacts helper ── */
(function(){
  function ar(){ return !!(window.fmgIsArabic && window.fmgIsArabic()); }
  function t(en, a){ return ar() ? a : en; }
  window.fmgLangHooks = window.fmgLangHooks || [];

  /* image alt text follows the page language */
  function alts(){
    var imgs = document.querySelectorAll('img[data-alt-ar]');
    for (var i=0;i<imgs.length;i++){
      var im = imgs[i];
      if (!im.getAttribute('data-alt-en')) im.setAttribute('data-alt-en', im.getAttribute('alt') || '');
      im.setAttribute('alt', ar() ? im.getAttribute('data-alt-ar') : im.getAttribute('data-alt-en'));
    }
  }

  var sel = document.getElementById('ctDx');
  var out = document.getElementById('ctResult');
  var P = {
    air:  ['air',  'Airborne', 'هوائية'],
    drop: ['drop', 'Droplet', 'رذاذ'],
    con:  ['con',  'Contact', 'تلامس'],
    std:  ['std',  'Standard', 'قياسية']
  };
  var D = [
    { id:'measles', n:['Measles','الحصبة'], p:['air'],
      clinic:['Mask the child at the door, separate room with door closed, N95 for staff, see last; leave the room empty 2 h afterwards.','كمامة للطفل عند الباب، وغرفة منفصلة مغلقة، وكمامة N95 للعاملين، ويُفحص في النهاية؛ وتُترك الغرفة فارغة ساعتين بعده.'],
      dur:['4 days after rash onset (whole illness if immunocompromised).','4 أيام بعد بدء الطفح (طوال المرض لضعيف المناعة).'],
      home:['Off nursery or school for 4 days from rash onset.','غياب عن الحضانة أو المدرسة 4 أيام من بدء الطفح.'],
      risk:['Pregnant women, infants under 12 months, immunocompromised, unvaccinated.','الحوامل، والرضّع دون 12 شهرًا، وضعيفو المناعة، وغير المطعَّمين.'],
      pep:['MMR within 72 h (from 6 months); immunoglobulin within 6 days for infants under 6 months, non-immune pregnant women and the immunocompromised. Notify public health today.','لقاح MMR خلال 72 ساعة (من 6 أشهر)؛ وغلوبيولين مناعي خلال 6 أيام للرضّع دون 6 أشهر والحوامل غير المحصَّنات وضعيفي المناعة. أبلغ الصحة العامة اليوم.'] },
    { id:'varicella', n:['Chickenpox','الجديري المائي'], p:['air','con'],
      clinic:['Separate room, N95 for non-immune staff (immune staff preferred), gloves and gown.','غرفة منفصلة، وكمامة N95 للعاملين غير المحصَّنين (ويُفضَّل العاملون المحصَّنون)، وقفازات ورداء.'],
      dur:['Until all lesions have crusted.','حتى تتقشّر كل الآفات.'],
      home:['At least 5 days from rash onset and until all spots are crusted.','5 أيام على الأقل من بدء الطفح وحتى تتقشّر كل البقع.'],
      risk:['Pregnant women, newborns, immunocompromised, non-immune adolescents and adults.','الحوامل، وحديثو الولادة، وضعيفو المناعة، والمراهقون والبالغون غير المحصَّنين.'],
      pep:['Varicella vaccine within 3–5 days (from 12 months); VariZIG within 10 days for high-risk contacts; pregnant non-immune: VariZIG (US) or aciclovir/valaciclovir from day 7 (UK).','لقاح الجديري خلال 3–5 أيام (من 12 شهرًا)؛ وVariZIG خلال 10 أيام للمخالطين عالي الخطورة؛ والحامل غير المحصَّنة: VariZIG (أمريكا) أو أسيكلوفير/فالاسيكلوفير من اليوم السابع (بريطانيا).'] },
    { id:'zoster', n:['Shingles (healthy child, localised)','الحزام الناري (طفل سليم، موضعي)'], p:['std'],
      clinic:['Cover the lesions; standard precautions. Airborne + contact if disseminated or immunocompromised.','غطِّ الآفات؛ احتياطات قياسية. وهوائية + تلامس إن كان منتشرًا أو عند ضعيف المناعة.'],
      dur:['Until crusted.','حتى التقشّر.'],
      home:['Only if the rash is weeping and cannot be covered.','فقط إن كان الطفح راشحًا ولا يمكن تغطيته.'],
      risk:['Non-immune pregnant women and immunocompromised people who touch the lesions (they can catch chickenpox).','الحوامل غير المحصَّنات وضعيفو المناعة ممن يلمسون الآفات (قد يُصابون بالجديري).'],
      pep:['As for chickenpox, for non-immune high-risk contacts with direct contact.','كما في الجديري، للمخالطين غير المحصَّنين عالي الخطورة ذوي التلامس المباشر.'] },
    { id:'rubella', n:['Rubella','الحصبة الألمانية'], p:['drop'],
      clinic:['Surgical mask within 1–2 m, single room; non-immune pregnant staff must not care for the child.','كمامة جراحية ضمن 1–2 متر، وغرفة مفردة؛ ولا تعتني بالطفل العاملة الحامل غير المحصَّنة.'],
      dur:['7 days after rash onset.','7 أيام بعد بدء الطفح.'],
      home:['5 days from rash onset (UKHSA); 7 days (CDC). Keep away from pregnant women for 7 days.','5 أيام من بدء الطفح (UKHSA)؛ و7 أيام (CDC). وإبعاد عن الحوامل 7 أيام.'],
      risk:['Pregnant women — especially before 20 weeks (congenital rubella syndrome).','الحوامل — وخاصة قبل 20 أسبوعًا (متلازمة الحصبة الألمانية الخلقية).'],
      pep:['No effective PEP. Pregnant contacts: rubella IgG now and repeat in 3–4 weeks if not immune. MMR for non-immune non-pregnant contacts. Notify public health.','لا وقاية فعّالة بعد التعرّض. الحوامل المخالطات: IgG الآن، ويُعاد بعد 3–4 أسابيع إن لم تكن محصَّنة. ولقاح MMR للمخالطين غير المحصَّنين غير الحوامل. أبلغ الصحة العامة.'] },
    { id:'mumps', n:['Mumps','النكاف'], p:['drop'],
      clinic:['Surgical mask within 1–2 m, single room.','كمامة جراحية ضمن 1–2 متر، وغرفة مفردة.'],
      dur:['5 days after the swelling starts.','5 أيام بعد بدء التورّم.'],
      home:['5 days after onset of swelling.','5 أيام بعد بدء التورّم.'],
      risk:['Unvaccinated post-pubertal males (orchitis); pregnant women in the first trimester.','الذكور غير المطعَّمين بعد البلوغ (التهاب الخصية)؛ والحوامل في الثلث الأول.'],
      pep:['No effective PEP. Check MMR status of contacts; a third MMR dose may be offered in outbreaks.','لا وقاية فعّالة بعد التعرّض. راجع حالة MMR للمخالطين؛ وقد تُقدَّم جرعة ثالثة في الفاشيات.'] },
    { id:'scarlet', n:['Scarlet fever (GAS)','الحمّى القرمزية (العقديات)'], p:['drop'],
      clinic:['Surgical mask within 1–2 m until 24 h of antibiotics.','كمامة جراحية ضمن 1–2 متر حتى 24 ساعة من المضاد الحيوي.'],
      dur:['Until 24 h of effective antibiotics.','حتى 24 ساعة من مضاد حيوي فعّال.'],
      home:['24 hours after starting antibiotics.','24 ساعة بعد بدء المضاد الحيوي.'],
      risk:['Children with chickenpox at the same time, newborns, postpartum women, the elderly and immunocompromised (invasive GAS).','الأطفال المصابون بالجديري في الوقت نفسه، وحديثو الولادة، والنساء بعد الولادة، وكبار السن وضعيفو المناعة (العدوى العقدية الغازية).'],
      pep:['No routine prophylaxis; test and treat symptomatic contacts. Public health advises if there is invasive GAS in the household.','لا وقاية روتينية؛ افحص المخالطين الذين لديهم أعراض وعالجهم. وتنصح الصحة العامة عند وجود عدوى عقدية غازية في البيت.'] },
    { id:'impetigo', n:['Impetigo','القوباء'], p:['con'],
      clinic:['Gloves for contact with lesions; clean surfaces and toys.','قفازات عند لمس الآفات؛ وتنظيف الأسطح والألعاب.'],
      dur:['Until 24 h of effective therapy.','حتى 24 ساعة من علاج فعّال.'],
      home:['Until crusted and healed, or 48 h after starting antibiotics.','حتى تتقشّر وتلتئم، أو 48 ساعة بعد بدء المضاد الحيوي.'],
      risk:['Newborns (SSSS), children with eczema, household members sharing towels.','حديثو الولادة (متلازمة الجلد المسموط)، والأطفال المصابون بالإكزيما، وأفراد البيت الذين يتشاركون المناشف.'],
      pep:['None. Separate towels, hand hygiene, short nails; check siblings.','لا شيء. مناشف منفصلة، ونظافة اليدين، وأظافر قصيرة؛ وافحص الإخوة.'] },
    { id:'fifth', n:['Fifth disease (parvovirus B19)','المرض الخامس (الفيروس الصغير B19)'], p:['std'],
      clinic:['Standard once the rash has appeared. Droplet for 7 days if in aplastic crisis; whole stay if immunocompromised.','قياسية بعد ظهور الطفح. ورذاذ 7 أيام في نوبة اللاتنسّج؛ وطوال الإقامة لضعيف المناعة.'],
      dur:['Not infectious once the rash appears.','غير معدٍ بعد ظهور الطفح.'],
      home:['No exclusion.','لا استبعاد.'],
      risk:['Pregnant women (fetal anaemia, hydrops), children with sickle cell disease or other haemolytic anaemia, immunocompromised.','الحوامل (فقر الدم الجنيني والاستسقاء)، والأطفال المصابون بفقر الدم المنجلي أو غيره من فقر الدم الانحلالي، وضعيفو المناعة.'],
      pep:['None. Pregnant contacts: B19 IgG and IgM. Sickle cell contacts: know the signs of an aplastic crisis.','لا شيء. الحوامل المخالطات: IgG وIgM للفيروس B19. والمخالطون المصابون بفقر الدم المنجلي: معرفة علامات نوبة اللاتنسّج.'] },
    { id:'roseola', n:['Roseola','الوردية'], p:['std'],
      clinic:['Standard precautions.','احتياطات قياسية.'],
      dur:['—','—'],
      home:['No exclusion once well.','لا استبعاد بعد التعافي.'],
      risk:['Transplant recipients (HHV-6 reactivation).','متلقو زراعة الأعضاء (نشاط الهربس البشري 6).'],
      pep:['None.','لا شيء.'] },
    { id:'hfmd', n:['Hand, foot and mouth disease','مرض اليد والقدم والفم'], p:['std','con'],
      clinic:['Standard; contact precautions for nappy-wearing children.','قياسية؛ وتلامس للأطفال بالحفاضات.'],
      dur:['Whole illness; stool shedding for weeks.','طوال المرض؛ ويُطرح في البراز لأسابيع.'],
      home:['No exclusion if well enough.','لا استبعاد إن كان بحال جيدة.'],
      risk:['Newborns and women near term.','حديثو الولادة والنساء قرب موعد الولادة.'],
      pep:['None. Handwashing after nappy changes and toilet use.','لا شيء. غسل اليدين بعد تغيير الحفاض واستخدام الحمام.'] },
    { id:'mening', n:['Meningococcal disease','المرض بالمكورات السحائية'], p:['drop'],
      clinic:['Give parenteral antibiotics now and call an ambulance. Surgical mask for close examination.','أعطِ المضاد الحيوي بالحقن الآن واطلب الإسعاف. وكمامة جراحية للفحص القريب.'],
      dur:['Until 24 h of effective antibiotics.','حتى 24 ساعة من مضاد حيوي فعّال.'],
      home:['Until recovered.','حتى التعافي.'],
      risk:['Household and kissing contacts, nursery dormitory contacts.','أهل البيت ومن تبادل التقبيل، ومخالطو المبيت في الحضانة.'],
      pep:['Chemoprophylaxis within 24 h (ciprofloxacin, rifampicin or ceftriaxone) arranged with public health; vaccine if a vaccine-preventable serogroup.','وقاية دوائية خلال 24 ساعة (سيبروفلوكساسين أو ريفامبيسين أو سيفترياكسون) بالتنسيق مع الصحة العامة؛ واللقاح إن كانت المجموعة المصلية مما يقي منه اللقاح.'] },
    { id:'mpox', n:['Mpox','جدري القردة'], p:['con','drop'],
      clinic:['N95, eye protection, gown and gloves; single room; cover lesions.','كمامة N95، وواقٍ للعينين، ورداء وقفازات؛ وغرفة مفردة؛ وتغطية الآفات.'],
      dur:['Until all lesions have crusted and new skin has formed.','حتى تتقشّر كل الآفات ويتكوّن جلد جديد.'],
      home:['Until cleared by the treating clinician.','حتى يأذن الطبيب المعالج.'],
      risk:['Pregnant women, young children, immunocompromised.','الحوامل، وصغار الأطفال، وضعيفو المناعة.'],
      pep:['MVA-BN vaccine ideally within 4 days (up to 14) per national guidance. Notify public health.','لقاح MVA-BN يُفضَّل خلال 4 أيام (حتى 14) وفق الإرشادات الوطنية. أبلغ الصحة العامة.'] },
    { id:'kawasaki', n:['Kawasaki disease / dengue','داء كاواساكي / حمّى الضنك'], p:['std'],
      clinic:['Standard precautions — not spread person to person. Dengue: protect the patient from mosquito bites while febrile.','احتياطات قياسية — لا ينتقلان من شخص لآخر. حمّى الضنك: احمِ المريض من لدغ البعوض أثناء الحمّى.'],
      dur:['—','—'],
      home:['Until well.','حتى التعافي.'],
      risk:['Kawasaki: infants under 6 months (coronary aneurysms). Dengue: pregnant women, infants, people with a previous dengue infection.','كاواساكي: الرضّع دون 6 أشهر (أمهات الدم التاجية). الضنك: الحوامل، والرضّع، ومن أصيب بالضنك سابقًا.'],
      pep:['None. Dengue: remove standing water at home, use screens and repellent.','لا شيء. الضنك: إزالة المياه الراكدة في البيت، واستخدام الشبك والطاردات.'] }
  ];

  function render(){
    if (!sel || !out) return;
    var d = D[sel.selectedIndex] || D[0];
    var pills = '';
    for (var i=0;i<d.p.length;i++){ var q = P[d.p[i]]; pills += '<span class="fr-pill '+q[0]+'">'+t(q[1], q[2])+'</span>'; }
    var rows = [
      [t('Precautions','الاحتياطات'), pills],
      [t('In clinic','في العيادة'), t(d.clinic[0], d.clinic[1])],
      [t('Isolation lasts','مدة العزل'), t(d.dur[0], d.dur[1])],
      [t('Nursery / school','الحضانة / المدرسة'), t(d.home[0], d.home[1])],
      [t('Who at home is at risk','من في البيت معرَّض للخطر'), t(d.risk[0], d.risk[1])],
      [t('Contacts need','ما يحتاجه المخالطون'), t(d.pep[0], d.pep[1])]
    ];
    var h = '<dl>';
    for (var j=0;j<rows.length;j++){ h += '<dt>'+rows[j][0]+'</dt><dd>'+rows[j][1]+'</dd>'; }
    h += '</dl><span class="sub">'+t('Section links: ','روابط الأقسام: ')+'<a href="#precautions-table">'+t('precautions table','جدول الاحتياطات')+'</a> · <a href="#pep-summary">'+t('post-exposure prophylaxis','الوقاية بعد التعرّض')+'</a></span>';
    out.innerHTML = h;
  }
  function fill(){
    if (!sel) return;
    var keep = sel.selectedIndex < 0 ? 0 : sel.selectedIndex;
    var h = '';
    for (var i=0;i<D.length;i++){ h += '<option value="'+D[i].id+'">'+t(D[i].n[0], D[i].n[1])+'</option>'; }
    sel.innerHTML = h;
    sel.selectedIndex = keep;
    render();
  }
  if (sel){ sel.addEventListener('change', render); }
  window.fmgLangHooks.push(function(){ fill(); alts(); });
  fill(); alts();
})();
