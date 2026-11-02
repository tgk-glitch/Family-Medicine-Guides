from h import ul, ol, p, tbl, blk

# ─────────────────────────────────────────────────────────────
# 3 · MEASLES
# ─────────────────────────────────────────────────────────────
MEASLES = dict(
    id='measles',
    h_en='Measles (rubeola)',
    h_ar='الحصبة',
    sub_en='The most contagious infection in this list — and the one with the most deaths',
    sub_ar='أشد أمراض هذه القائمة عدوى — وأكثرها وفيات',
    blocks=[
        blk('glance', 'measles-at-a-glance', 'At a glance', 'لمحة سريعة',
            ul([
                '<b>Cause:</b> measles virus (paramyxovirus), spread by airborne particles. Up to 9 in 10 non-immune contacts are infected.',
                '<b>Who:</b> unvaccinated or under-vaccinated children, infants too young for MMR, travellers and their contacts. Global measles cases have risen since 2022 as vaccine coverage fell during and after the pandemic.',
                '<b>Course:</b> 2–4 days of prodrome (high fever, <b>cough, coryza, conjunctivitis</b>), then <b>Koplik spots</b>, then the rash on about day 3–5 of fever.',
                '<b>Why it matters:</b> pneumonia, encephalitis, death — and <b>“immune amnesia”</b>, loss of existing immunity to other infections for months to years.',
                '<b>Infectious:</b> 4 days before to 4 days after rash onset. <b>Airborne precautions.</b>',
            ]),
            ul([
                '<b>المسبب:</b> فيروس الحصبة (من الفيروسات المخاطانية)، وينتشر بالجسيمات المحمولة جوًا. يُصاب ما يصل إلى 9 من كل 10 مخالطين غير محصَّنين.',
                '<b>من يصاب:</b> الأطفال غير المطعَّمين أو ناقصو التطعيم، والرضّع الأصغر من سنّ لقاح MMR، والمسافرون ومخالطوهم. وقد ارتفعت حالات الحصبة عالميًا منذ 2022 مع تراجع التغطية باللقاح خلال الجائحة وبعدها.',
                '<b>المسار:</b> 2–4 أيام من الأعراض البادئة (حمّى عالية، و<b>سعال، وزكام، والتهاب ملتحمة</b>)، ثم <b>بقع كوبليك</b>، ثم الطفح في اليوم 3–5 من الحمّى تقريبًا.',
                '<b>لماذا يهم:</b> الالتهاب الرئوي، والتهاب الدماغ، والوفاة — و<b>«فقدان الذاكرة المناعية»</b>، أي فقدان المناعة الموجودة ضد أمراض أخرى لأشهر أو سنوات.',
                '<b>فترة العدوى:</b> من 4 أيام قبل بدء الطفح إلى 4 أيام بعده. <b>احتياطات هوائية.</b>',
            ]),
            figs=['measles', 'koplik']),
        blk('features', 'measles-features', 'Clinical features', 'الصورة السريرية',
            ul([
                '<b>Prodrome:</b> fever rising to 39–40 °C, harsh cough, runny nose, red watery eyes with photophobia; the child looks miserable.',
                '<b>Koplik spots:</b> tiny white-grey spots on a red base on the buccal mucosa opposite the lower molars, 1–2 days before the rash and fading as it appears. Pathognomonic, but often missed.',
                '<b>Rash:</b> red, blotchy, maculopapular; starts at the hairline and behind the ears, spreads down the face, trunk and limbs over 3 days, becoming <b>confluent</b>. Fever peaks as the rash spreads.',
                '<b>Resolution:</b> the rash fades in the same order, leaving brownish staining and fine peeling. A child still febrile after day 3–4 of rash has a complication until proven otherwise.',
                '<b>Modified measles</b> in partly immune people (infants with maternal antibody, after immunoglobulin, vaccinated people): milder, shorter, sometimes without the full prodrome.',
            ]),
            ul([
                '<b>الأعراض البادئة:</b> حمّى ترتفع إلى 39–40 °م، وسعال خشن، وسيلان أنف، وعينان حمراوان دامعتان مع رهاب الضوء؛ ويبدو الطفل منهكًا.',
                '<b>بقع كوبليك:</b> بقع صغيرة بيضاء رمادية على قاعدة حمراء في الغشاء المخاطي للخد مقابل الأضراس السفلية، قبل الطفح بيوم أو يومين، وتختفي مع ظهوره. مميِّزة للمرض لكنها كثيرًا ما تفوت.',
                '<b>الطفح:</b> أحمر بقعي لطخي حطاطي؛ يبدأ عند منبت الشعر وخلف الأذنين، وينتشر نزولًا إلى الوجه والجذع والأطراف خلال 3 أيام، ويصبح <b>متكتّلًا</b>. تبلغ الحمّى ذروتها مع انتشار الطفح.',
                '<b>الزوال:</b> يتلاشى الطفح بالترتيب نفسه، تاركًا تصبّغًا بنيًا وتقشرًا دقيقًا. الطفل الذي تستمر حرارته بعد اليوم 3–4 من الطفح لديه مضاعفة حتى يثبت العكس.',
                '<b>الحصبة المعدَّلة</b> عند جزئيي المناعة (الرضّع بأجسام أمهاتهم المضادة، وبعد الغلوبيولين المناعي، والمطعَّمون): أخف وأقصر، وقد تغيب فيها الأعراض البادئة الكاملة.',
            ])),
        blk('dx', 'measles-dx', 'Diagnosis', 'التشخيص',
            ul([
                '<b>Suspect measles:</b> fever + maculopapular rash + at least one of cough, coryza or conjunctivitis.',
                '<b>Confirm:</b> <b>RT-PCR</b> on a throat or nasopharyngeal swab (best within 3 days of rash, positive up to 10–14 days) <b>plus</b> urine for PCR, <b>and</b> serum measles IgM (may be negative in the first 72 h of rash — repeat if needed).',
                'Collect samples at the first visit and <b>notify public health the same day</b> — do not wait for results.',
                'Baseline in sick children: full blood count (lymphopenia, low platelets), chest X-ray if breathing is affected, electrolytes if dehydrated.',
            ]),
            ul([
                '<b>اشتبه في الحصبة:</b> حمّى + طفح لطخي حطاطي + واحد على الأقل من السعال أو الزكام أو التهاب الملتحمة.',
                '<b>للتأكيد:</b> <b>تفاعل البوليميراز العكسي (RT-PCR)</b> على مسحة من الحلق أو البلعوم الأنفي (الأفضل خلال 3 أيام من الطفح، ويبقى إيجابيًا حتى 10–14 يومًا) <b>إضافة إلى</b> عيّنة بول للفحص نفسه، <b>و</b>الغلوبيولين المناعي IgM للحصبة في المصل (قد يكون سلبيًا في أول 72 ساعة من الطفح — كرّره عند الحاجة).',
                'خذ العيّنات في الزيارة الأولى و<b>أبلغ الصحة العامة في اليوم نفسه</b> — لا تنتظر النتائج.',
                'للأطفال المرضى: تعداد الدم الكامل (نقص اللمفاويات وانخفاض الصفيحات)، وصورة الصدر إن تأثر التنفس، والأملاح إن كان الطفل جافًا.',
            ])),
        blk('mx', 'measles-mx', 'Management', 'العلاج',
            '<p><b>There is no specific antiviral.</b> Treatment is supportive, vitamin A, and treating complications.</p>'
            + ul([
                '<b>Vitamin A for every child with measles</b> (WHO, CDC, AAP), orally once daily for 2 days: <b>under 6 months 50,000 IU; 6–11 months 100,000 IU; 12 months and over 200,000 IU</b>. Give a third dose 2–4 weeks later if there are signs of vitamin A deficiency (eye changes). It lowers mortality and eye damage.',
                '<b>Fever and comfort:</b> paracetamol 15 mg/kg every 4–6 h (max 4 doses a day) or ibuprofen 10 mg/kg every 6–8 h if not dehydrated; oral fluids little and often; dim light for photophobia; clean the eyes with cooled boiled water.',
                '<b>Antibiotics only for bacterial complications</b> — otitis media, pneumonia — not as prophylaxis.',
                '<b>Admit</b> if breathing difficulty, dehydration, drowsiness or seizures, age under 1 year with poor feeding, malnutrition, pregnancy or immunocompromise.',
                'Ribavirin is sometimes used in severe disease in the immunocompromised but is not licensed for measles and lacks trial evidence — specialist decision only.',
            ])
            + '<p><b>Non-pharmacological:</b> isolate at home for 4 days after rash onset, keep away from pregnant women, infants and the immunocompromised; give a list of contacts to public health.</p>',
            '<p><b>لا يوجد مضاد فيروسات نوعي.</b> العلاج داعم، مع فيتامين A، وعلاج المضاعفات.</p>'
            + ul([
                '<b>فيتامين A لكل طفل مصاب بالحصبة</b> (منظمة الصحة العالمية، وCDC، والأكاديمية الأمريكية لطب الأطفال)، بالفم مرة يوميًا لمدة يومين: <b>دون 6 أشهر 50,000 وحدة؛ 6–11 شهرًا 100,000 وحدة؛ 12 شهرًا فأكثر 200,000 وحدة</b>. أعطِ جرعة ثالثة بعد 2–4 أسابيع إن ظهرت علامات نقص فيتامين A (تغيّرات العين). يخفّض الوفيات وتضرر العين.',
                '<b>الحمّى والراحة:</b> باراسيتامول 15 ملغ/كغ كل 4–6 ساعات (4 جرعات يوميًا كحد أقصى) أو إيبوبروفين 10 ملغ/كغ كل 6–8 ساعات إن لم يكن الطفل جافًا؛ سوائل بالفم قليلًا وكثيرًا؛ إضاءة خافتة لرهاب الضوء؛ ونظّف العينين بماء مغليّ مبرَّد.',
                '<b>المضادات الحيوية للمضاعفات الجرثومية فقط</b> — التهاب الأذن الوسطى والالتهاب الرئوي — لا وقائيًا.',
                '<b>أدخل المستشفى</b> عند صعوبة التنفس، أو الجفاف، أو النعاس أو التشنجات، أو العمر دون سنة مع ضعف الرضاعة، أو سوء التغذية، أو الحمل، أو ضعف المناعة.',
                'يُستخدم الريبافيرين أحيانًا في المرض الشديد عند ضعيفي المناعة، لكنه غير مرخَّص للحصبة ويفتقر إلى أدلة من التجارب — بقرار اختصاصي فقط.',
            ])
            + '<p><b>غير دوائي:</b> العزل في البيت 4 أيام بعد بدء الطفح، والإبعاد عن الحوامل والرضّع وضعيفي المناعة؛ وسلّم قائمة المخالطين للصحة العامة.</p>'),
        blk('special', 'measles-special', 'Special populations and contacts', 'الفئات الخاصة والمخالطون',
            ul([
                '<b>Pregnancy:</b> measles does not cause a congenital syndrome like rubella, but raises the risk of <b>miscarriage, stillbirth, preterm birth and severe maternal pneumonia</b>. A non-immune pregnant contact gets <b>IV immunoglobulin 400 mg/kg within 6 days</b> of exposure. MMR is contraindicated in pregnancy; give it after delivery.',
                '<b>Infants under 6 months</b> exposed: intramuscular immunoglobulin 0.5 mL/kg (max 15 mL) within 6 days. <b>Infants 6–11 months:</b> MMR within 72 h is preferred (does not count toward the routine doses — repeat at 12 and 18 months).',
                '<b>Immunocompromised</b> (whatever their vaccine history): IV immunoglobulin 400 mg/kg within 6 days. They can develop <b>giant-cell pneumonia or encephalitis without a rash</b>, and shed virus for weeks — airborne precautions for the whole illness.',
                '<b>Unvaccinated contacts aged 12 months and over:</b> MMR within <b>72 hours</b> of first exposure; if more than 72 h but within 6 days, immunoglobulin (if the person is high risk). Exclude unvaccinated contacts from school or work from day 5 to day 21 after exposure.',
                '<b>Malnourished children</b> have the highest mortality — vitamin A and nutritional support are essential.',
            ]),
            ul([
                '<b>الحمل:</b> لا تسبب الحصبة متلازمة خلقية كالحصبة الألمانية، لكنها ترفع خطر <b>الإجهاض، وولادة جنين ميت، والولادة المبكرة، والالتهاب الرئوي الشديد عند الأم</b>. تتلقى الحامل المخالطة غير المحصَّنة <b>غلوبيولين مناعيًا وريديًا 400 ملغ/كغ خلال 6 أيام</b> من التعرّض. لقاح MMR ممنوع في الحمل؛ ويُعطى بعد الولادة.',
                '<b>الرضّع دون 6 أشهر</b> المعرَّضون: غلوبيولين مناعي عضلي 0.5 مل/كغ (بحد أقصى 15 مل) خلال 6 أيام. <b>الرضّع 6–11 شهرًا:</b> يُفضَّل لقاح MMR خلال 72 ساعة (ولا يُحتسب ضمن الجرعات الروتينية — تُعاد في 12 و18 شهرًا).',
                '<b>ضعيفو المناعة</b> (أيًّا كان تاريخ تطعيمهم): غلوبيولين مناعي وريدي 400 ملغ/كغ خلال 6 أيام. قد يصابون <b>بالتهاب رئوي بالخلايا العملاقة أو التهاب دماغ دون طفح</b>، ويطرحون الفيروس لأسابيع — احتياطات هوائية طوال المرض.',
                '<b>المخالطون غير المطعَّمين بعمر 12 شهرًا فأكثر:</b> لقاح MMR خلال <b>72 ساعة</b> من أول تعرّض؛ وإن تجاوزت 72 ساعة وكانت ضمن 6 أيام فالغلوبيولين المناعي (إن كان الشخص عالي الخطورة). يُستبعد المخالطون غير المطعَّمين من المدرسة أو العمل من اليوم 5 إلى اليوم 21 بعد التعرّض.',
                '<b>الأطفال سيئو التغذية</b> أعلى وفيات — فيتامين A والدعم الغذائي أساسيان.',
            ])),
        blk('comp', 'measles-complications', 'Complications', 'المضاعفات',
            ul([
                '<b>Common:</b> otitis media (about 1 in 10), diarrhoea, pneumonia (about 1 in 20 — the main cause of death in children), laryngotracheobronchitis, keratitis and blindness in vitamin A deficiency.',
                '<b>Acute encephalitis:</b> about 1 in 1,000, days after the rash; may leave deafness or intellectual disability.',
                '<b>Subacute sclerosing panencephalitis (SSPE):</b> fatal, 7–10 years later; risk is highest when measles occurs in infancy (estimates around 1 in 600–1,400 under age 5). This is why infants must be protected.',
                '<b>Death:</b> 1–3 per 1,000 cases in high-income settings; much higher with malnutrition.',
            ]),
            ul([
                '<b>شائعة:</b> التهاب الأذن الوسطى (نحو 1 من 10)، والإسهال، والالتهاب الرئوي (نحو 1 من 20 — السبب الرئيسي للوفاة عند الأطفال)، والتهاب الحنجرة والرغامى والقصبات، والتهاب القرنية والعمى مع نقص فيتامين A.',
                '<b>التهاب الدماغ الحاد:</b> نحو 1 من 1,000، بعد الطفح بأيام؛ وقد يترك صممًا أو إعاقة ذهنية.',
                '<b>التهاب الدماغ الشامل المصلِّب تحت الحاد (SSPE)&rlm;:</b> قاتل، بعد 7–10 سنوات؛ ويكون الخطر أعلى عند الإصابة في الرضاعة (تقديرات نحو 1 من 600–1,400 دون 5 سنوات). ولهذا تجب حماية الرضّع.',
                '<b>الوفاة:</b> 1–3 لكل 1,000 حالة في البلدان مرتفعة الدخل؛ وأعلى بكثير مع سوء التغذية.',
            ])),
        blk('tell', 'measles-tell', 'What to tell the family', 'ماذا تقول للأسرة',
            ul([
                '“Measles spreads through the air, even after the person has left the room. Please keep your child at home for 4 days after the rash started.”',
                '“Keep your child away from anyone pregnant, any baby under one, and anyone with a weak immune system — and tell me if any of them were near your child.”',
                '“Come back straight away if breathing gets fast or hard, if your child becomes drowsy or has a fit, or if the fever is still there 3 days after the rash.”',
            ]),
            ul([
                '«تنتشر الحصبة في الهواء، حتى بعد مغادرة المريض للغرفة. أبقِ طفلك في البيت 4 أيام بعد بدء الطفح.»',
                '«أبعِد طفلك عن أي حامل، وأي رضيع دون السنة، وأي شخص ضعيف المناعة — وأخبرني إن كان أحدهم قريبًا منه.»',
                '«عُد فورًا إن صار التنفس سريعًا أو صعبًا، أو أصبح طفلك نعسانًا أو أصابته نوبة تشنج، أو بقيت الحمّى بعد 3 أيام من الطفح.»',
            ])),
    ])

# ─────────────────────────────────────────────────────────────
# 4 · RUBELLA
# ─────────────────────────────────────────────────────────────
RUBELLA = dict(
    id='rubella',
    h_en='Rubella (German measles)',
    h_ar='الحصبة الألمانية (الحُمَيراء)',
    sub_en='A mild illness in the child — a devastating one for the fetus',
    sub_ar='مرض خفيف عند الطفل — ومدمِّر للجنين',
    blocks=[
        blk('glance', 'rubella-at-a-glance', 'At a glance', 'لمحة سريعة',
            ul([
                '<b>Cause:</b> rubella virus (togavirus), spread by respiratory droplets.',
                '<b>Course:</b> up to half of infections have no symptoms. Mild fever, <b>tender post-auricular and suboccipital lymph nodes</b> (often before the rash), then a pink maculopapular rash for about 3 days.',
                '<b>Why it matters:</b> infection in early pregnancy causes <b>congenital rubella syndrome (CRS)</b> — the reason rubella vaccination exists.',
                '<b>Infectious:</b> 7 days before to 7 days after rash onset. <b>Droplet precautions.</b>',
            ]),
            ul([
                '<b>المسبب:</b> فيروس الحصبة الألمانية (من الفيروسات الطخائية)، وينتشر بالرذاذ التنفسي.',
                '<b>المسار:</b> ما يصل إلى نصف الإصابات بلا أعراض. حمّى خفيفة، و<b>تضخم مؤلم في العقد اللمفية خلف الأذن وتحت القذال</b> (غالبًا قبل الطفح)، ثم طفح وردي لطخي حطاطي نحو 3 أيام.',
                '<b>لماذا يهم:</b> الإصابة في أوائل الحمل تسبب <b>متلازمة الحصبة الألمانية الخلقية</b> — وهي سبب وجود لقاح الحصبة الألمانية.',
                '<b>فترة العدوى:</b> من 7 أيام قبل بدء الطفح إلى 7 أيام بعده. <b>احتياطات الرذاذ.</b>',
            ]),
            figs=['rubella']),
        blk('features', 'rubella-features', 'Clinical features', 'الصورة السريرية',
            ul([
                '<b>Rash:</b> pink, discrete (less confluent than measles), starts on the face and spreads to the trunk within 24 h; fades by day 3 in the same order. May itch in older children.',
                '<b>Forchheimer spots:</b> small red spots on the soft palate in some patients (not specific — also seen in scarlet fever and EBV).',
                '<b>Arthralgia or arthritis</b> of fingers, wrists and knees — common in adolescent girls and women, lasting up to a month.',
                'The child is usually <b>well</b>; high fever or a toxic child should prompt another diagnosis.',
            ]),
            ul([
                '<b>الطفح:</b> وردي ومتفرّق (أقل تكتّلًا من الحصبة)، يبدأ في الوجه وينتشر إلى الجذع خلال 24 ساعة؛ ويتلاشى بحلول اليوم الثالث بالترتيب نفسه. وقد يسبب حكة عند الأطفال الأكبر.',
                '<b>بقع فورشهايمر:</b> بقع حمراء صغيرة على الحنك الرخو عند بعض المرضى (غير نوعية — تُرى أيضًا في الحمّى القرمزية وفيروس إبشتاين-بار).',
                '<b>ألم المفاصل أو التهابها</b> في الأصابع والرسغين والركبتين — شائع عند المراهقات والنساء، ويستمر حتى شهر.',
                'يكون الطفل عادة <b>بحال جيدة</b>؛ والحمّى العالية أو الطفل شديد الإعياء يوجّهان إلى تشخيص آخر.',
            ])),
        blk('dx', 'rubella-dx', 'Diagnosis', 'التشخيص',
            ul([
                'Clinical diagnosis is unreliable — confirm every suspected case: <b>serum rubella IgM</b> (best 5 or more days after rash onset) and <b>RT-PCR</b> on a throat or nasopharyngeal swab.',
                '<b>In pregnancy:</b> rubella IgG and IgM together with <b>IgG avidity testing</b>, interpreted with the regional virology laboratory — false-positive IgM is common.',
                'Notify public health on suspicion.',
            ]),
            ul([
                'التشخيص السريري غير موثوق — أكّد كل حالة مشتبهة: <b>الغلوبيولين المناعي IgM للحصبة الألمانية في المصل</b> (الأفضل بعد 5 أيام أو أكثر من بدء الطفح) و<b>RT-PCR</b> على مسحة من الحلق أو البلعوم الأنفي.',
                '<b>في الحمل:</b> الغلوبيولين المناعي IgG وIgM معًا مع <b>اختبار شدة ارتباط IgG</b>، وتُفسَّر مع مختبر الفيروسات الإقليمي — فالنتيجة الإيجابية الكاذبة لـ IgM شائعة.',
                'أبلغ الصحة العامة عند الاشتباه.',
            ])),
        blk('mx', 'rubella-mx', 'Management', 'العلاج',
            ul([
                '<b>Supportive:</b> paracetamol or ibuprofen for fever and joint pain, fluids, rest.',
                '<b>No antiviral</b> and no role for antibiotics.',
                '<b>Exclude from school or nursery</b> and keep away from pregnant women for 7 days after rash onset (UKHSA: 5 days for schools).',
                'Check the vaccine status of all household members and offer MMR to anyone without two documented doses (except pregnant women).',
            ]),
            ul([
                '<b>داعم:</b> باراسيتامول أو إيبوبروفين للحمّى وألم المفاصل، وسوائل، وراحة.',
                '<b>لا مضاد فيروسات</b> ولا دور للمضادات الحيوية.',
                '<b>استبعاد من المدرسة أو الحضانة</b> وإبعاد عن الحوامل 7 أيام بعد بدء الطفح (UKHSA: 5 أيام للمدارس).',
                'راجع حالة تطعيم كل أفراد الأسرة، وقدّم لقاح MMR لكل من لا يملك جرعتين موثّقتين (عدا الحوامل).',
            ])),
        blk('special', 'rubella-pregnancy', 'Pregnancy and the fetus', 'الحمل والجنين',
            tbl(['Gestation at infection', 'Risk to the fetus'], [
                ['Before 11 weeks', 'Up to <b>90%</b> — multiple defects, miscarriage, stillbirth'],
                ['11–16 weeks', 'About 10–20% — mainly deafness'],
                ['16–20 weeks', 'Low — occasional deafness'],
                ['After 20 weeks', 'Rare; growth restriction at most'],
            ])
            + ul([
                '<b>CRS:</b> sensorineural deafness, cataracts or glaucoma, congenital heart disease (patent ductus arteriosus, peripheral pulmonary stenosis), microcephaly, growth restriction, “blueberry muffin” rash, later diabetes and thyroid disease.',
                '<b>A pregnant woman exposed to rubella:</b> check rubella IgG straight away. Immune — reassure. Not immune or unknown — repeat serology at 3–4 weeks and refer to fetal medicine if infection is confirmed.',
                '<b>Immunoglobulin after exposure is not routinely recommended</b> — it may reduce maternal symptoms but does not reliably prevent fetal infection. It is considered only in rare cases, after specialist counselling.',
                '<b>MMR is contraindicated in pregnancy</b>; avoid pregnancy for 1 month after MMR. Inadvertent vaccination in pregnancy is <b>not</b> a reason to terminate — no case of CRS from the vaccine has been documented. Vaccinate non-immune women after delivery, before discharge.',
                '<b>Infants with CRS</b> shed virus for up to a year: contact precautions, and keep away from pregnant staff and visitors.',
            ]),
            tbl(['عمر الحمل عند الإصابة', 'الخطر على الجنين'], [
                ['قبل 11 أسبوعًا', 'حتى <b>90%</b> — تشوّهات متعددة، وإجهاض، وولادة جنين ميت'],
                ['11–16 أسبوعًا', 'نحو 10–20% — الصمم أساسًا'],
                ['16–20 أسبوعًا', 'منخفض — صمم أحيانًا'],
                ['بعد 20 أسبوعًا', 'نادر؛ تأخر النمو على الأكثر'],
            ])
            + ul([
                '<b>متلازمة الحصبة الألمانية الخلقية:</b> صمم حسّي عصبي، وساد أو زرق، وعيوب خلقية في القلب (القناة الشريانية السالكة وتضيّق الشريان الرئوي المحيطي)، وصغر الرأس، وتأخر النمو، وطفح «كعكة التوت»، ولاحقًا السكري وأمراض الغدة الدرقية.',
                '<b>حامل تعرّضت للحصبة الألمانية:</b> افحص الغلوبيولين المناعي IgG فورًا. محصَّنة — طمئنها. غير محصَّنة أو مجهولة — أعد الفحص المصلي بعد 3–4 أسابيع وأحِلها إلى طب الأجنة إن تأكدت الإصابة.',
                '<b>لا يوصى روتينيًا بالغلوبيولين المناعي بعد التعرّض</b> — قد يخفف أعراض الأم لكنه لا يمنع إصابة الجنين بشكل موثوق. ولا يُنظر فيه إلا في حالات نادرة بعد استشارة اختصاصية.',
                '<b>لقاح MMR ممنوع في الحمل</b>؛ وتُتجنّب الحمل شهرًا بعد اللقاح. التطعيم غير المقصود أثناء الحمل <b>ليس</b> سببًا لإنهائه — لم تُوثَّق أي حالة متلازمة خلقية من اللقاح. طعّم غير المحصَّنات بعد الولادة وقبل الخروج من المستشفى.',
                '<b>الرضّع المصابون بالمتلازمة الخلقية</b> يطرحون الفيروس حتى سنة: احتياطات تلامس، وإبعاد عن العاملات والزائرات الحوامل.',
            ])),
        blk('tell', 'rubella-tell', 'What to tell the family', 'ماذا تقول للأسرة',
            ul([
                '“For your child this is a mild illness. The danger is to unborn babies — so please keep your child away from anyone who is or might be pregnant for one week after the rash started.”',
                '“If anyone pregnant has been close to your child, ask her to contact her doctor today for a blood test.”',
            ]),
            ul([
                '«هذا مرض خفيف لطفلك. الخطر على الأجنة — فأبعِد طفلك عن أي امرأة حامل أو قد تكون حاملًا أسبوعًا بعد بدء الطفح.»',
                '«إن كانت امرأة حامل قريبة من طفلك، فاطلب منها التواصل مع طبيبها اليوم لإجراء فحص دم.»',
            ])),
    ])

# ─────────────────────────────────────────────────────────────
# 5 · MUMPS
# ─────────────────────────────────────────────────────────────
MUMPS = dict(
    id='mumps',
    h_en='Mumps',
    h_ar='النكاف',
    sub_en='Not a rash illness, but it travels with this group — fever, parotid swelling and preventable complications',
    sub_ar='ليس مرضًا طفحيًا، لكنه يرافق هذه المجموعة — حمّى وتورّم الغدة النكفية ومضاعفات يمكن الوقاية منها',
    blocks=[
        blk('glance', 'mumps-at-a-glance', 'At a glance', 'لمحة سريعة',
            ul([
                '<b>Cause:</b> mumps virus (paramyxovirus), spread by saliva and respiratory droplets.',
                '<b>Course:</b> 1–2 days of fever, headache, malaise, then <b>parotitis</b> — painful swelling in front of and below the ear that lifts the earlobe and blurs the angle of the jaw. Bilateral in about 3 in 4. Up to a third of infections are subclinical.',
                '<b>Outbreaks</b> still occur in vaccinated adolescents and young adults living close together (schools, universities, dormitories), because protection wanes.',
                '<b>Infectious:</b> 2 days before to 5 days after swelling begins. <b>Droplet precautions.</b>',
            ]),
            ul([
                '<b>المسبب:</b> فيروس النكاف (من الفيروسات المخاطانية)، وينتشر باللعاب والرذاذ التنفسي.',
                '<b>المسار:</b> 1–2 يوم من الحمّى والصداع والتوعك، ثم <b>التهاب الغدة النكفية</b> — تورّم مؤلم أمام الأذن وتحتها يرفع شحمة الأذن ويُخفي زاوية الفك. ثنائي الجانب في نحو 3 من 4. وما يصل إلى ثلث الإصابات بلا أعراض واضحة.',
                '<b>لا تزال الفاشيات</b> تحدث عند المراهقين والشباب المطعَّمين الذين يعيشون متقاربين (المدارس والجامعات والسكن الجماعي)، لأن الحماية تضعف مع الوقت.',
                '<b>فترة العدوى:</b> من يومين قبل بدء التورّم إلى 5 أيام بعده. <b>احتياطات الرذاذ.</b>',
            ]),
            figs=['mumps']),
        blk('dx', 'mumps-dx', 'Diagnosis', 'التشخيص',
            ul([
                '<b>Preferred test: RT-PCR on a buccal swab</b> — massage the parotid for about 30 seconds, then swab the opening of Stensen’s duct (opposite the upper second molar), ideally within 3 days of swelling.',
                '<b>Serum mumps IgM</b> in addition — but it is often <b>negative in vaccinated people</b>, so a negative IgM does not exclude mumps.',
                'Serum amylase may be raised (salivary or pancreatic). Ultrasound helps when the swelling is unilateral or atypical (stone, abscess, lymph node).',
                '<b>Differential:</b> bacterial parotitis (pus from the duct, very tender — <i>S. aureus</i>), salivary stone, cervical lymphadenitis, other viruses (influenza, EBV, parainfluenza, HIV).',
            ]),
            ul([
                '<b>الفحص المفضَّل: RT-PCR على مسحة من باطن الخد</b> — دلّك الغدة النكفية نحو 30 ثانية، ثم امسح فتحة قناة ستنسن (مقابل الضرس العلوي الثاني)، ويُفضَّل خلال 3 أيام من التورّم.',
                '<b>الغلوبيولين المناعي IgM للنكاف في المصل</b> إضافة إلى ذلك — لكنه كثيرًا ما يكون <b>سلبيًا عند المطعَّمين</b>، فالنتيجة السلبية لا تنفي النكاف.',
                'قد يرتفع الأميلاز في المصل (لعابي أو بنكرياسي). ويفيد التصوير بالموجات فوق الصوتية عندما يكون التورّم في جانب واحد أو غير نمطي (حصاة، خراج، عقدة لمفية).',
                '<b>التشخيص التفريقي:</b> التهاب النكفية الجرثومي (قيح من القناة وألم شديد — المكورات العنقودية الذهبية)، وحصاة لعابية، والتهاب العقد اللمفية الرقبية، وفيروسات أخرى (الإنفلونزا، وإبشتاين-بار، ونظيرة الإنفلونزا، وفيروس نقص المناعة البشري).',
            ])),
        blk('mx', 'mumps-mx', 'Management', 'العلاج',
            ul([
                '<b>Supportive:</b> paracetamol or ibuprofen, plenty of fluids, soft food; avoid sour drinks and foods that stimulate saliva and pain; warm or cold compresses.',
                '<b>Orchitis:</b> analgesia, scrotal support, cold packs, rest. Steroids do not prevent subfertility.',
                '<b>Exclude</b> from school or nursery for 5 days after the swelling starts.',
                '<b>No effective post-exposure prophylaxis.</b> In an outbreak, public health may offer a <b>third MMR dose</b> to people in the affected group (ACIP 2017).',
            ]),
            ul([
                '<b>داعم:</b> باراسيتامول أو إيبوبروفين، وسوائل وافرة، وطعام ليّن؛ وتجنّب المشروبات والأطعمة الحامضة التي تحفّز اللعاب والألم؛ وكمادات دافئة أو باردة.',
                '<b>التهاب الخصية:</b> مسكنات، ورافعة للصفن، وكمادات باردة، وراحة. لا تمنع الستيرويدات ضعف الخصوبة.',
                '<b>استبعاد</b> من المدرسة أو الحضانة 5 أيام بعد بدء التورّم.',
                '<b>لا توجد وقاية فعّالة بعد التعرّض.</b> وفي الفاشيات قد تقدّم الصحة العامة <b>جرعة ثالثة من لقاح MMR</b> للفئة المتأثرة (اللجنة الاستشارية الأمريكية للتطعيم، 2017).',
            ])),
        blk('comp', 'mumps-complications', 'Complications and special populations', 'المضاعفات والفئات الخاصة',
            ul([
                '<b>Orchitis:</b> in up to 30% of unvaccinated post-pubertal males (much less if vaccinated); usually unilateral; testicular atrophy is common but sterility is rare.',
                '<b>Oophoritis and mastitis</b> in post-pubertal females.',
                '<b>Aseptic meningitis</b> (often benign), rarely encephalitis; <b>pancreatitis</b>; <b>sensorineural deafness</b>, usually one-sided and permanent — check hearing if the child complains.',
                '<b>Pregnancy:</b> mumps in the first trimester may increase the risk of miscarriage; it does not cause birth defects. MMR is not given in pregnancy.',
                '<b>Immunocompromised and unvaccinated:</b> no specific treatment; ensure household contacts are vaccinated.',
            ]),
            ul([
                '<b>التهاب الخصية:</b> عند ما يصل إلى 30% من الذكور غير المطعَّمين بعد البلوغ (أقل بكثير عند المطعَّمين)؛ غالبًا في جانب واحد؛ ضمور الخصية شائع لكن العقم نادر.',
                '<b>التهاب المبيض والثدي</b> عند الإناث بعد البلوغ.',
                '<b>التهاب السحايا العقيم</b> (غالبًا حميد)، ونادرًا التهاب الدماغ؛ و<b>التهاب البنكرياس</b>؛ و<b>الصمم الحسي العصبي</b>، غالبًا في جانب واحد ودائم — افحص السمع إن اشتكى الطفل.',
                '<b>الحمل:</b> قد يزيد النكاف في الثلث الأول خطر الإجهاض؛ ولا يسبب تشوهات خلقية. لا يُعطى لقاح MMR في الحمل.',
                '<b>ضعيفو المناعة وغير المطعَّمين:</b> لا علاج نوعي؛ وتأكد من تطعيم المخالطين في البيت.',
            ])),
        blk('trap', 'mumps-trap', 'Trap', 'خطأ شائع',
            p('Some teaching notes say PCR is “not used” for mumps. The opposite is true: <b>buccal-swab RT-PCR is the preferred confirmatory test</b> (CDC), and IgM alone misses many cases in vaccinated people.'),
            p('تقول بعض الملخصات التعليمية إن فحص PCR «لا يُستخدم» في النكاف. والصحيح عكس ذلك: <b>RT-PCR على مسحة باطن الخد هو فحص التأكيد المفضَّل</b> (CDC)&rlm;، وفحص IgM وحده يفوّت كثيرًا من الحالات عند المطعَّمين.')),
    ])
