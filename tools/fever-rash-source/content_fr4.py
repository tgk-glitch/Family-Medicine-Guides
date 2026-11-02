from h import ul, ol, p, tbl, blk

# ─────────────────────────────────────────────────────────────
# 9 · SCARLET FEVER
# ─────────────────────────────────────────────────────────────
SCARLET = dict(
    id='scarlet',
    h_en='Scarlet fever (group A streptococcus)',
    h_ar='الحمّى القرمزية (العقدية المجموعة A)',
    sub_en='Sore throat, sandpaper rash, strawberry tongue — treat with penicillin and watch for invasive disease',
    sub_ar='التهاب حلق، وطفح كورق الصنفرة، ولسان الفراولة — يُعالج بالبنسلين مع مراقبة المرض الغازي',
    blocks=[
        blk('glance', 'scarlet-at-a-glance', 'At a glance', 'لمحة سريعة',
            ul([
                '<b>Cause:</b> group A <i>Streptococcus pyogenes</i> (GAS) producing erythrogenic (pyrogenic) exotoxins, usually from pharyngitis, sometimes from skin or wound infection.',
                '<b>Who:</b> mainly 3–15 years; spread by droplets and close contact in households and classrooms. Large rises in scarlet fever and invasive GAS (iGAS) were seen in many countries in 2022–23.',
                '<b>Course:</b> abrupt fever, sore throat, headache, abdominal pain, vomiting → within 12–48 h a fine red rash.',
                '<b>Why treat:</b> to shorten illness, reduce spread, and prevent <b>suppurative complications</b> and <b>acute rheumatic fever</b>.',
                '<b>Infectious:</b> until 24 h of effective antibiotics. <b>Droplet precautions.</b>',
            ]),
            ul([
                '<b>المسبب:</b> العقدية المقيّحة المجموعة A التي تفرز ذيفانات خارجية مولِّدة للحُمامى، غالبًا من التهاب البلعوم، وأحيانًا من عدوى جلدية أو جرح.',
                '<b>من يصاب:</b> أساسًا من 3 إلى 15 سنة؛ وتنتشر بالرذاذ والتلامس القريب في البيوت والفصول. وقد شهدت دول كثيرة في 2022–2023 ارتفاعًا كبيرًا في الحمّى القرمزية والعدوى العقدية الغازية.',
                '<b>المسار:</b> حمّى مفاجئة، والتهاب حلق، وصداع، وألم بطن، وقيء ← خلال 12–48 ساعة طفح أحمر ناعم.',
                '<b>لماذا نعالج:</b> لتقصير المرض، وتقليل الانتشار، والوقاية من <b>المضاعفات القيحية</b> و<b>الحمّى الروماتيزمية الحادة</b>.',
                '<b>فترة العدوى:</b> حتى 24 ساعة من مضاد حيوي فعّال. <b>احتياطات الرذاذ.</b>',
            ]),
            figs=['scarlet', 'strawberry']),
        blk('features', 'scarlet-features', 'Clinical features', 'الصورة السريرية',
            ul([
                '<b>Rash:</b> diffuse, fine, pinpoint erythema that feels like <b>sandpaper</b>; starts on the neck and chest, spreads to trunk and limbs; blanches. Easier to feel than see on darker skin.',
                '<b>Pastia lines:</b> darker red lines in skin folds (elbows, armpits, groin). <b>Circumoral pallor:</b> flushed cheeks with a pale ring round the mouth.',
                '<b>Tongue:</b> white coating with red papillae (“white strawberry”), then peeling to a bright red “strawberry tongue” by day 4–5. Tonsils red and swollen, sometimes exudate; palatal petechiae; tender anterior cervical nodes.',
                '<b>Desquamation</b> of fingertips, palms and soles 1–3 weeks later — expected, not a new problem (but consider Kawasaki disease if fever persisted).',
            ]),
            ul([
                '<b>الطفح:</b> حُمامى منتشرة ناعمة نقطية <b>كملمس ورق الصنفرة</b>؛ تبدأ في الرقبة والصدر وتنتشر إلى الجذع والأطراف؛ وتبيضّ بالضغط. يُحسّ بها أسهل مما تُرى على البشرة الداكنة.',
                '<b>خطوط باستيا:</b> خطوط حمراء أغمق في ثنيات الجلد (المرفقان والإبطان والمغبن). <b>الشحوب حول الفم:</b> وجنتان متوردتان مع حلقة شاحبة حول الفم.',
                '<b>اللسان:</b> طبقة بيضاء مع حليمات حمراء («فراولة بيضاء»)، ثم يتقشّر إلى «لسان فراولة» أحمر زاهٍ بحلول اليوم 4–5. واللوزتان حمراوان متورمتان، وأحيانًا مع نضحة؛ ونَمَشات في الحنك؛ وعقد رقبية أمامية مؤلمة.',
                '<b>تقشّر</b> أطراف الأصابع والكفين والقدمين بعد 1–3 أسابيع — متوقع وليس مشكلة جديدة (لكن فكّر في داء كاواساكي إن استمرت الحمّى).',
            ])),
        blk('dx', 'scarlet-dx', 'Diagnosis', 'التشخيص',
            ul([
                '<b>Throat swab:</b> rapid antigen detection test (RADT) or culture. In children, a negative RADT is backed up by culture (AAP, IDSA); a positive RADT needs no culture.',
                'Scarlet fever with a typical rash and pharyngitis can be treated on clinical grounds where testing is not available (UKHSA, NICE).',
                'Do not test children under 3 years for pharyngitis routinely — GAS and rheumatic fever are rare at this age — unless a sibling has GAS or there is scarlet fever.',
            ]),
            ul([
                '<b>مسحة الحلق:</b> اختبار المستضد السريع أو المزرعة. عند الأطفال، يُدعَم الاختبار السريع السلبي بالمزرعة (الأكاديمية الأمريكية لطب الأطفال وجمعية الأمراض المعدية الأمريكية)&rlm;؛ والاختبار السريع الإيجابي لا يحتاج إلى مزرعة.',
                'يمكن علاج الحمّى القرمزية النموذجية بطفحها والتهاب بلعومها على أساس سريري حين لا يتوفر الفحص (UKHSA وNICE)&rlm;.',
                'لا تفحص روتينيًا الأطفال دون 3 سنوات لالتهاب البلعوم — فالعقديات والحمّى الروماتيزمية نادرة في هذا العمر — ما لم يكن لدى أحد الإخوة عدوى عقدية أو ظهرت حمّى قرمزية.',
            ])),
        blk('mx', 'scarlet-mx', 'Management', 'العلاج',
            tbl(['Drug', 'Child dose', 'Duration'], [
                ['<b>Amoxicillin</b> (first line, palatable)', '50 mg/kg once daily (max 1,000 mg), or 25 mg/kg twice daily (max 500 mg/dose)', '10 days'],
                ['<b>Penicillin V</b>', '≤27 kg: 250 mg 2–3 times a day; &gt;27 kg: 500 mg 2–3 times a day', '10 days'],
                ['<b>Benzathine penicillin G</b> IM (adherence doubtful)', '≤27 kg: 600,000 units; &gt;27 kg: 1.2 million units', 'Single dose'],
                ['Penicillin allergy, not anaphylactic: <b>cefalexin</b>', '20 mg/kg twice daily (max 500 mg/dose)', '10 days'],
                ['Anaphylactic allergy: <b>clindamycin</b>', '7 mg/kg 3 times a day (max 300 mg/dose)', '10 days'],
                ['or <b>azithromycin</b>', '12 mg/kg once daily (max 500 mg)', '5 days'],
            ])
            + p('Doses per IDSA 2012 and AHA; check your local formulary. Macrolide resistance in GAS is common in some regions — use when penicillin cannot be.')
            + ul([
                '<b>Non-pharmacological:</b> fluids, soft cold foods, paracetamol or ibuprofen for pain, rest; separate cups and towels; hand hygiene at home; replace the toothbrush after 24 h of treatment.',
                '<b>Return to school</b> 24 hours after the first antibiotic dose.',
                '<b>Contacts:</b> no routine prophylaxis. Test and treat symptomatic contacts. Where there is an iGAS case in the household, public health may advise prophylaxis.',
            ]),
            tbl(['الدواء', 'جرعة الطفل', 'المدة'], [
                ['<b>أموكسيسيلين</b> (الخيار الأول، مستساغ)', '50 ملغ/كغ مرة يوميًا (بحد أقصى 1,000 ملغ)، أو 25 ملغ/كغ مرتين يوميًا (بحد أقصى 500 ملغ للجرعة)', '10 أيام'],
                ['<b>بنسلين V</b>', '27 كغ أو أقل: 250 ملغ 2–3 مرات يوميًا؛ أكثر من 27 كغ: 500 ملغ 2–3 مرات يوميًا', '10 أيام'],
                ['<b>بنزاثين بنسلين G</b> عضليًا (عند الشك في الالتزام)', '27 كغ أو أقل: 600,000 وحدة؛ أكثر من 27 كغ: 1.2 مليون وحدة', 'جرعة واحدة'],
                ['حساسية بنسلين غير تأقية: <b>سيفالكسين</b>', '20 ملغ/كغ مرتين يوميًا (بحد أقصى 500 ملغ للجرعة)', '10 أيام'],
                ['حساسية تأقية: <b>كليندامايسين</b>', '7 ملغ/كغ 3 مرات يوميًا (بحد أقصى 300 ملغ للجرعة)', '10 أيام'],
                ['أو <b>أزيثرومايسين</b>', '12 ملغ/كغ مرة يوميًا (بحد أقصى 500 ملغ)', '5 أيام'],
            ])
            + p('الجرعات وفق جمعية الأمراض المعدية الأمريكية (2012) وجمعية القلب الأمريكية؛ راجع دليل الأدوية المحلي. مقاومة العقديات للماكروليدات شائعة في بعض المناطق — استخدمها حين يتعذر البنسلين.')
            + ul([
                '<b>غير دوائي:</b> سوائل، وأطعمة طرية باردة، وباراسيتامول أو إيبوبروفين للألم، وراحة؛ وأكواب ومناشف منفصلة؛ ونظافة اليدين في البيت؛ واستبدال فرشاة الأسنان بعد 24 ساعة من العلاج.',
                '<b>العودة إلى المدرسة</b> بعد 24 ساعة من أول جرعة مضاد حيوي.',
                '<b>المخالطون:</b> لا وقاية روتينية. افحص المخالطين الذين لديهم أعراض وعالجهم. وعند وجود حالة عدوى عقدية غازية في البيت قد تنصح الصحة العامة بالوقاية الدوائية.',
            ])),
        blk('flag', 'scarlet-igas', '🚩 Invasive group A streptococcus', '🚩 العدوى العقدية الغازية',
            ul([
                'Escalate if the child gets <b>worse instead of better</b> after 24–48 h of antibiotics, or develops: very high or persistent fever, severe limb or muscle pain, a rapidly spreading red area, breathing difficulty, drowsiness, or signs of shock.',
                'Recent <b>varicella</b> is the classic risk factor — another reason to avoid NSAIDs in chickenpox.',
                'iGAS includes streptococcal toxic shock syndrome, necrotising fasciitis, empyema and bacteraemia. It is notifiable.',
            ]),
            ul([
                'صعّد الحالة إن <b>ساءت بدل أن تتحسن</b> بعد 24–48 ساعة من المضاد الحيوي، أو ظهرت: حمّى شديدة الارتفاع أو مستمرة، أو ألم شديد في طرف أو العضلات، أو منطقة حمراء سريعة الانتشار، أو صعوبة تنفس، أو نعاس، أو علامات صدمة.',
                '<b>الجديري</b> الحديث عامل خطر كلاسيكي — وسبب آخر لتجنب مضادات الالتهاب غير الستيرويدية في الجديري.',
                'تشمل العدوى العقدية الغازية متلازمة الصدمة السمّية العقدية، والتهاب اللفافة الناخر، والدبيلة، وتجرثم الدم. ويجب الإبلاغ عنها.',
            ])),
        blk('special', 'scarlet-special', 'Complications and special populations', 'المضاعفات والفئات الخاصة',
            ul([
                '<b>Suppurative:</b> otitis media, sinusitis, peritonsillar or retropharyngeal abscess, cervical lymphadenitis.',
                '<b>Non-suppurative:</b> <b>acute rheumatic fever</b> 1–5 weeks later (prevented by treatment started within 9 days of symptom onset), <b>post-streptococcal glomerulonephritis</b> 1–3 weeks later (not prevented by antibiotics — check urine and blood pressure if there is haematuria, oedema or hypertension), PANDAS (debated).',
                '<b>Pregnancy:</b> amoxicillin and penicillin are safe. A household case is a reason for a postpartum woman to know the signs of puerperal sepsis.',
                '<b>Immunocompromised and children with recent varicella:</b> lower threshold for review and admission.',
            ]),
            ul([
                '<b>قيحية:</b> التهاب الأذن الوسطى، والتهاب الجيوب، والخراج حول اللوزة أو خلف البلعوم، والتهاب العقد اللمفية الرقبية.',
                '<b>غير قيحية:</b> <b>الحمّى الروماتيزمية الحادة</b> بعد 1–5 أسابيع (يمنعها العلاج إذا بدأ خلال 9 أيام من بدء الأعراض)، و<b>التهاب كبيبات الكلى التالي للعقديات</b> بعد 1–3 أسابيع (لا تمنعه المضادات الحيوية — افحص البول والضغط عند وجود بول دموي أو وذمة أو ارتفاع ضغط)، ومتلازمة PANDAS (موضع جدل).',
                '<b>الحمل:</b> الأموكسيسيلين والبنسلين آمنان. ووجود حالة في البيت سبب لتعرف المرأة بعد الولادة علامات حمّى النفاس.',
                '<b>ضعيفو المناعة والأطفال المصابون حديثًا بالجديري:</b> عتبة أدنى للمراجعة وإدخال المستشفى.',
            ])),
    ])

# ─────────────────────────────────────────────────────────────
# 10 · IMPETIGO
# ─────────────────────────────────────────────────────────────
IMPETIGO = dict(
    id='impetigo',
    h_en='Impetigo',
    h_ar='القوباء',
    sub_en='The commonest bacterial skin infection in children — usually no fever, always contagious',
    sub_ar='أشيع عدوى جلدية جرثومية عند الأطفال — غالبًا بلا حمّى، ودائمًا معدية',
    blocks=[
        blk('glance', 'impetigo-at-a-glance', 'At a glance', 'لمحة سريعة',
            ul([
                '<b>Cause:</b> <i>Staphylococcus aureus</i> (most cases) and/or group A streptococcus. Spread by touch, towels, toys; worse in heat and humidity.',
                '<b>Non-bullous (about 70%):</b> red macule → short-lived vesicle or pustule → <b>golden “honey-coloured” crusts</b>, around the nose and mouth and on the limbs. Little or no fever.',
                '<b>Bullous:</b> <i>S. aureus</i> exfoliative toxin; <b>flaccid, clear bullae</b> that burst and leave a thin brown crust with a collarette of scale — mainly infants, on the trunk, nappy area and skin folds. May have fever and malaise.',
                '<b>Ecthyma:</b> deeper, punched-out ulcers with a thick crust — usually GAS; heals with scarring.',
                '<b>Infectious:</b> until lesions crust and heal, or 24–48 h after starting antibiotics. <b>Contact precautions.</b>',
            ]),
            ul([
                '<b>المسبب:</b> المكورات العنقودية الذهبية (معظم الحالات) و/أو العقديات المجموعة A. وتنتشر باللمس والمناشف والألعاب؛ وتزداد مع الحر والرطوبة.',
                '<b>غير الفقاعية (نحو 70%):</b> لطخة حمراء ← حويصلة أو بثرة قصيرة العمر ← <b>قشور ذهبية «بلون العسل»</b>، حول الأنف والفم وعلى الأطراف. حمّى قليلة أو معدومة.',
                '<b>الفقاعية:</b> ذيفان التقشّر من المكورات العنقودية الذهبية؛ <b>فقاعات رخوة صافية</b> تنفجر تاركة قشرة بنية رقيقة مع طوق من القشور — عند الرضّع غالبًا، على الجذع ومنطقة الحفاض وثنيات الجلد. وقد تصاحبها حمّى وتوعك.',
                '<b>الإكثيما:</b> قرح أعمق كأنها مثقوبة مع قشرة سميكة — غالبًا بالعقديات؛ وتلتئم بندبة.',
                '<b>فترة العدوى:</b> حتى تتقشّر الآفات وتلتئم، أو 24–48 ساعة بعد بدء المضاد الحيوي. <b>احتياطات التلامس.</b>',
            ]),
            figs=['impetigo']),
        blk('mx', 'impetigo-mx', 'Management (NICE NG153)', 'العلاج (دليل NICE رقم NG153)',
            tbl(['Situation', 'First choice', 'Alternative'], [
                ['<b>Localised non-bullous</b>, not systemically unwell, not high risk', '<b>Hydrogen peroxide 1% cream</b> 2–3 times a day for 5 days (not near the eyes)', 'If unsuitable: <b>fusidic acid 2%</b> 3 times a day for 5 days; <b>mupirocin 2%</b> if fusidic-acid resistance suspected or MRSA'],
                ['<b>Widespread</b>, bullous, or systemically unwell / high risk of complications', '<b>Oral flucloxacillin</b> 4 times a day for 5 days: 1 month–1 year 62.5–125 mg; 2–9 years 125–250 mg; 10–17 years 250–500 mg', 'Penicillin allergy: <b>clarithromycin</b> twice a day for 5 days (by weight); <b>erythromycin</b> in pregnancy'],
                ['<b>MRSA</b> suspected or confirmed', 'Per culture and local guidance — e.g. clindamycin, or co-trimoxazole (not under 6 weeks)', ''],
            ], wide=True)
            + ul([
                '<b>Do not combine</b> a topical and an oral antibiotic. Extend to 7 days only if needed; swab for culture if it fails to respond or recurs.',
                'Cefalexin (25–50 mg/kg/day in 2–4 doses) is a common alternative where flucloxacillin suspension is not available or not tolerated (AAP, IDSA).',
                '<b>Non-pharmacological:</b> gently soak off crusts with warm soapy water; pat dry with a <b>separate towel</b>; keep nails short; wash hands after touching lesions; wash towels, bedding and toys hot; do not share razors, flannels or sports kit.',
                '<b>Recurrent impetigo:</b> swab nose for <i>S. aureus</i> carriage in the child and family; decolonisation per local guidance; treat underlying eczema, scabies or head lice.',
            ]),
            tbl(['الحالة', 'الخيار الأول', 'البديل'], [
                ['<b>موضعية غير فقاعية</b>، دون إعياء جهازي، وليست عالية الخطورة', '<b>كريم بيروكسيد الهيدروجين 1%</b> 2–3 مرات يوميًا لمدة 5 أيام (بعيدًا عن العينين)', 'إن لم يناسب: <b>حمض الفوسيديك 2%</b> 3 مرات يوميًا لمدة 5 أيام؛ و<b>الموبيروسين 2%</b> عند الاشتباه بمقاومة حمض الفوسيديك أو بالعنقوديات المقاومة للميثيسيلين'],
                ['<b>منتشرة</b>، أو فقاعية، أو مع إعياء جهازي / خطر عالٍ للمضاعفات', '<b>فلوكلوكساسيلين فموي</b> 4 مرات يوميًا لمدة 5 أيام: من شهر إلى سنة 62.5–125 ملغ؛ 2–9 سنوات 125–250 ملغ؛ 10–17 سنة 250–500 ملغ', 'حساسية البنسلين: <b>كلاريثرومايسين</b> مرتين يوميًا لمدة 5 أيام (حسب الوزن)؛ و<b>إريثرومايسين</b> في الحمل'],
                ['اشتباه أو تأكيد <b>العنقوديات المقاومة للميثيسيلين</b>', 'حسب المزرعة والإرشادات المحلية — مثل الكليندامايسين، أو الكوتريموكسازول (لا يُعطى دون 6 أسابيع)', ''],
            ], wide=True)
            + ul([
                '<b>لا تجمع</b> بين مضاد حيوي موضعي وآخر فموي. مدّد العلاج إلى 7 أيام عند الحاجة فقط؛ وخذ مسحة للمزرعة إن لم تستجب أو تكررت.',
                'السيفالكسين (25–50 ملغ/كغ يوميًا مقسّمة على 2–4 جرعات) بديل شائع حين لا يتوفر معلّق الفلوكلوكساسيلين أو لا يُحتمل (الأكاديمية الأمريكية لطب الأطفال وجمعية الأمراض المعدية الأمريكية).',
                '<b>غير دوائي:</b> انقع القشور برفق بماء دافئ وصابون وأزلها؛ وجفّف بالتربيت بـ<b>منشفة منفصلة</b>؛ وأبقِ الأظافر قصيرة؛ واغسل اليدين بعد لمس الآفات؛ واغسل المناشف والمفارش والألعاب بماء ساخن؛ ولا تتشاركوا الشفرات أو المناشف الصغيرة أو ملابس الرياضة.',
                '<b>القوباء المتكررة:</b> خذ مسحة من الأنف للكشف عن حمل المكورات العنقودية الذهبية عند الطفل والأسرة؛ وإزالة الاستعمار وفق الإرشادات المحلية؛ وعالج الإكزيما أو الجرب أو القمل المصاحب.',
            ])),
        blk('special', 'impetigo-special', 'Complications and special populations', 'المضاعفات والفئات الخاصة',
            ul([
                '<b>Complications:</b> cellulitis, lymphangitis, SSSS (from toxin-producing staph), <b>post-streptococcal glomerulonephritis</b> (impetigo does <b>not</b> cause rheumatic fever), scarlet fever, scarring with ecthyma.',
                '<b>Newborns:</b> bullous impetigo can spread quickly in nurseries and progress to SSSS — treat systemically and isolate.',
                '<b>Pregnancy:</b> topical hydrogen peroxide or fusidic acid; erythromycin if oral treatment is needed.',
                '<b>Immunocompromised or eczema:</b> oral treatment earlier; consider eczema herpeticum (punched-out erosions, fever) — that needs aciclovir, not antibiotics.',
            ]),
            ul([
                '<b>المضاعفات:</b> التهاب النسيج الخلوي، والتهاب الأوعية اللمفية، ومتلازمة الجلد المسموط العنقودية (من العنقوديات المفرزة للذيفان)، و<b>التهاب كبيبات الكلى التالي للعقديات</b> (القوباء <b>لا</b> تسبب الحمّى الروماتيزمية)، والحمّى القرمزية، والندبات مع الإكثيما.',
                '<b>حديثو الولادة:</b> قد تنتشر القوباء الفقاعية بسرعة في الحضانات وتتطور إلى متلازمة الجلد المسموط — عالجها جهازيًا واعزل الطفل.',
                '<b>الحمل:</b> بيروكسيد الهيدروجين أو حمض الفوسيديك موضعيًا؛ والإريثرومايسين إن لزم العلاج الفموي.',
                '<b>ضعيفو المناعة أو المصابون بالإكزيما:</b> علاج فموي أبكر؛ وفكّر في الإكزيما الهربسية (تآكلات كأنها مثقوبة مع حمّى) — وهي تحتاج إلى أسيكلوفير لا إلى مضاد حيوي.',
            ])),
    ])

# ─────────────────────────────────────────────────────────────
# 11 · DO NOT MISS
# ─────────────────────────────────────────────────────────────
DONTMISS = dict(
    id='do-not-miss',
    h_en='Do-not-miss and look-alikes',
    h_ar='ما لا يجب أن يفوتك والحالات المشابهة',
    sub_en='Hand, foot and mouth disease, meningococcal disease, Kawasaki disease, SSSS, dengue and mpox',
    sub_ar='مرض اليد والقدم والفم، والمكورات السحائية، وداء كاواساكي، ومتلازمة الجلد المسموط العنقودية، وحمّى الضنك، وجدري القردة',
    blocks=[
        blk('flag', 'meningococcal', '🚩 Meningococcal disease — minutes matter', '🚩 المرض بالمكورات السحائية — الدقائق مهمة',
            ul([
                '<b>Fever + non-blanching rash = give antibiotics now.</b> Early signs are non-specific (fever, leg pain, cold hands and feet, abnormal skin colour); the rash may start blanching and become petechial, then purpuric (<b>purpura fulminans</b>). Neck stiffness and photophobia are often absent in infants.',
                '<b>In primary care, before transfer</b> (do not delay transfer): <b>IM or IV benzylpenicillin</b> — under 1 year 300 mg, 1–9 years 600 mg, 10 years and over 1.2 g (NICE NG240) — or <b>ceftriaxone</b> 80 mg/kg (max 4 g) IV/IM if available. Only a history of anaphylaxis to penicillin is a reason to withhold.',
                'Call an ambulance; give oxygen and fluids for shock en route if trained and equipped.',
                '<b>Droplet precautions</b> until 24 h of antibiotics; surgical mask for anyone examining the throat or intubating.',
                '<b>Close contacts</b> (household, kissing, nursery dorms) get chemoprophylaxis <b>within 24 h</b>, arranged with public health: <b>ciprofloxacin</b> single oral dose (under 5 years 30 mg/kg max 125 mg; 5–11 years 250 mg; 12 years and over 500 mg) — usable in children and pregnancy (UKHSA) — or <b>rifampicin</b> 10 mg/kg (max 600 mg; 5 mg/kg under 1 month) twice daily for 2 days, or <b>ceftriaxone</b> IM single dose (under 15 years 125 mg; 15 and over 250 mg; preferred in pregnancy in US guidance).',
            ]),
            ul([
                '<b>حمّى + طفح لا يبيضّ بالضغط = أعطِ المضاد الحيوي الآن.</b> العلامات المبكرة غير نوعية (حمّى، وألم الساقين، وبرودة اليدين والقدمين، ولون جلد غير طبيعي)&rlm;؛ وقد يبدأ الطفح مبيضًّا بالضغط ثم يصبح نَمَشيًا ثم فُرفُريًا (<b>الفرفرية الصاعقة</b>). وكثيرًا ما يغيب تيبّس الرقبة ورهاب الضوء عند الرضّع.',
                '<b>في الرعاية الأولية قبل النقل</b> (دون تأخير النقل): <b>بنزيل بنسلين عضليًا أو وريديًا</b> — دون سنة 300 ملغ، 1–9 سنوات 600 ملغ، 10 سنوات فأكثر 1.2 غ (NICE NG240)&rlm; — أو <b>سيفترياكسون</b> 80 ملغ/كغ (بحد أقصى 4 غ) وريديًا أو عضليًا إن توفر. لا يمنع إعطاءه إلا تاريخ تأق من البنسلين.',
                'اطلب الإسعاف؛ وأعطِ الأكسجين والسوائل للصدمة أثناء النقل إن كنت مدرّبًا ومجهّزًا.',
                '<b>احتياطات الرذاذ</b> حتى 24 ساعة من المضاد الحيوي؛ وكمامة جراحية لكل من يفحص الحلق أو يُجري التنبيب.',
                '<b>المخالطون المقرّبون</b> (أهل البيت، والتقبيل، والمبيت في الحضانة) يتلقون وقاية دوائية <b>خلال 24 ساعة</b> بالتنسيق مع الصحة العامة: <b>سيبروفلوكساسين</b> جرعة فموية واحدة (دون 5 سنوات 30 ملغ/كغ بحد أقصى 125 ملغ؛ 5–11 سنة 250 ملغ؛ 12 سنة فأكثر 500 ملغ) — ويُستخدم للأطفال وفي الحمل (UKHSA)&rlm; — أو <b>ريفامبيسين</b> 10 ملغ/كغ (بحد أقصى 600 ملغ؛ 5 ملغ/كغ دون شهر) مرتين يوميًا لمدة يومين، أو <b>سيفترياكسون</b> عضليًا جرعة واحدة (دون 15 سنة 125 ملغ؛ 15 سنة فأكثر 250 ملغ؛ والمفضّل في الحمل في الإرشادات الأمريكية).',
            ])),
        blk('ddx', 'kawasaki', 'Kawasaki disease', 'داء كاواساكي',
            ul([
                '<b>Fever for 5 days or more</b> plus at least 4 of 5: <b>bilateral non-exudative conjunctival injection</b> (sparing the limbus); <b>red cracked lips, strawberry tongue</b>; <b>polymorphous rash</b>; <b>red or swollen hands and feet</b> (later peeling of fingertips); <b>cervical node ≥1.5 cm</b>, usually one-sided.',
                '<b>Incomplete Kawasaki</b> (fewer criteria) is common in <b>infants under 6 months</b> — they are also at highest risk of coronary aneurysms. Fever ≥7 days in an infant with no explanation should prompt CRP, ESR, FBC, albumin, ALT, urine and echocardiography.',
                '<b>Treatment (AHA 2024 update):</b> <b>IV immunoglobulin 2 g/kg</b> as a single infusion, ideally within 10 days of fever onset, plus <b>aspirin</b> (moderate or high dose until afebrile, then low dose 3–5 mg/kg/day until echo is normal at 4–6 weeks). <b>High-risk patients</b> (age ≤6 months, coronary z-score ≥2.5 at diagnosis, shock or macrophage activation) may receive <b>adjunctive corticosteroids or infliximab</b> from the start. Echo at diagnosis, 1–2 weeks and 4–6 weeks.',
                'After IVIG, <b>delay MMR and varicella vaccines for 11 months</b>; give inactivated influenza vaccine to children on aspirin (Reye risk with influenza or varicella).',
                '<b>Primary care role:</b> recognise and refer the same day. Standard precautions — it is not contagious.',
            ]),
            ul([
                '<b>حمّى 5 أيام أو أكثر</b> مع 4 على الأقل من 5: <b>احمرار الملتحمتين في الجانبين دون نضحة</b> (مع سلامة حافة القرنية)؛ و<b>شفتان حمراوان متشققتان ولسان فراولة</b>؛ و<b>طفح متعدد الأشكال</b>؛ و<b>احمرار أو تورّم اليدين والقدمين</b> (ثم تقشّر أطراف الأصابع لاحقًا)؛ و<b>عقدة رقبية 1.5 سم أو أكبر</b>، غالبًا في جانب واحد.',
                '<b>داء كاواساكي غير المكتمل</b> (معايير أقل) شائع عند <b>الرضّع دون 6 أشهر</b> — وهم أيضًا الأعلى خطرًا لأمهات الدم التاجية. والحمّى 7 أيام أو أكثر عند رضيع دون تفسير تستوجب: البروتين المتفاعل C، وسرعة الترسيب، وتعداد الدم، والألبومين، وإنزيم ALT، والبول، وتخطيط صدى القلب.',
                '<b>العلاج (تحديث جمعية القلب الأمريكية 2024):</b> <b>غلوبيولين مناعي وريدي 2 غ/كغ</b> بتسريب واحد، ويُفضَّل خلال 10 أيام من بدء الحمّى، مع <b>الأسبرين</b> (جرعة متوسطة أو عالية حتى زوال الحمّى، ثم جرعة منخفضة 3–5 ملغ/كغ يوميًا حتى يصبح صدى القلب طبيعيًا بعد 4–6 أسابيع). <b>المرضى عالو الخطورة</b> (العمر 6 أشهر أو أقل، أو مؤشر z التاجي 2.5 أو أكثر عند التشخيص، أو الصدمة، أو تنشيط البلاعم) قد يتلقون <b>الكورتيزون أو الإنفليكسيماب إضافةً</b> منذ البداية. صدى القلب عند التشخيص، وبعد 1–2 أسبوع، وبعد 4–6 أسابيع.',
                'بعد الغلوبيولين المناعي الوريدي <b>أجّل لقاحي MMR والجديري 11 شهرًا</b>؛ وأعطِ لقاح الإنفلونزا المعطَّل للأطفال الذين يتناولون الأسبرين (خطر متلازمة راي مع الإنفلونزا أو الجديري).',
                '<b>دور الرعاية الأولية:</b> التعرّف والإحالة في اليوم نفسه. احتياطات قياسية — فالمرض غير معدٍ.',
            ]),
            figs=['kawasaki']),
        blk('ddx', 'ssss', 'Staphylococcal scalded skin syndrome (SSSS)', 'متلازمة الجلد المسموط العنقودية',
            ul([
                '<b>Who:</b> mainly under 5 years (immature kidneys clear the toxin poorly); outbreaks in neonatal units.',
                '<b>Picture:</b> fever, irritability, <b>exquisitely tender</b> red skin starting around the mouth, eyes and flexures, then large flaccid blisters and sheets of superficial peeling; <b>positive Nikolsky sign</b>; radial crusting around the mouth. <b>Mucous membranes are spared</b> (unlike SJS/TEN).',
                '<b>Management:</b> admit. <b>IV anti-staphylococcal antibiotic</b> (flucloxacillin, or cefazolin) with <b>clindamycin</b> to reduce toxin production; vancomycin if MRSA is likely. Fluids, analgesia, temperature control, non-adherent dressings and emollients. <b>No corticosteroids.</b> Swab the likely source (nose, umbilicus, conjunctiva).',
                '<b>Contact precautions</b> for the whole illness. Heals without scarring in 1–2 weeks.',
            ]),
            ul([
                '<b>من يصاب:</b> أساسًا دون 5 سنوات (الكليتان غير الناضجتين تتخلصان من الذيفان ببطء)؛ وتحدث فاشيات في وحدات حديثي الولادة.',
                '<b>الصورة:</b> حمّى، وتهيّج، وجلد أحمر <b>شديد الإيلام</b> يبدأ حول الفم والعينين والثنيات، ثم فقاعات رخوة كبيرة وتقشّر سطحي في صفائح؛ و<b>علامة نيكولسكي إيجابية</b>؛ وقشور شعاعية حول الفم. <b>الأغشية المخاطية سليمة</b> (بخلاف متلازمة ستيفنز-جونسون وانحلال البشرة السمّي).',
                '<b>العلاج:</b> إدخال المستشفى. <b>مضاد حيوي وريدي مضاد للعنقوديات</b> (فلوكلوكساسيلين أو سيفازولين) مع <b>الكليندامايسين</b> لخفض إنتاج الذيفان؛ والفانكومايسين إن كانت العنقوديات المقاومة للميثيسيلين محتملة. مع السوائل، والمسكنات، وضبط الحرارة، وضمادات غير لاصقة، ومرطبات. <b>لا كورتيزون.</b> وخذ مسحة من المصدر المحتمل (الأنف، أو السرة، أو الملتحمة).',
                '<b>احتياطات التلامس</b> طوال المرض. ويلتئم الجلد دون ندبات خلال 1–2 أسبوع.',
            ]),
            figs=['ssss']),
        blk('ddx', 'hfmd', 'Hand, foot and mouth disease (enterovirus)', 'مرض اليد والقدم والفم (الفيروسات المعوية)',
            ul([
                '<b>Cause:</b> coxsackievirus A16, A6 and enterovirus A71; under-5s; summer and autumn outbreaks in nurseries.',
                '<b>Picture:</b> low fever, sore mouth with <b>ulcers on the tongue, gums and palate</b>, then <b>grey oval vesicles on a red base</b> on palms, soles, buttocks and sometimes knees. CA6 can cause widespread or atypical vesicles and <b>nail shedding</b> weeks later.',
                '<b>Management:</b> supportive — paracetamol or ibuprofen, cold drinks and soft food, and <b>watch hydration</b> (refusing fluids is the main reason for admission).',
                '<b>Red flags (EV-A71):</b> myoclonic jerks, ataxia, persistent vomiting, drowsiness, rapid breathing — brainstem encephalitis and pulmonary oedema.',
                '<b>Pregnancy:</b> usually mild; infection near term can cause neonatal infection — tell the obstetric team. <b>Precautions:</b> standard + contact for nappy-wearing children; virus is shed in stool for weeks — handwashing after nappy changes. No exclusion if the child is well.',
            ]),
            ul([
                '<b>المسبب:</b> فيروسات كوكساكي A16 وA6 والفيروس المعوي A71&rlm;؛ دون 5 سنوات؛ وفاشيات صيفية وخريفية في الحضانات.',
                '<b>الصورة:</b> حمّى خفيفة، وألم في الفم مع <b>قرح على اللسان واللثة والحنك</b>، ثم <b>حويصلات رمادية بيضاوية على قاعدة حمراء</b> على الكفين والقدمين والإليتين وأحيانًا الركبتين. وقد يسبب كوكساكي A6 حويصلات منتشرة أو غير نمطية و<b>سقوط الأظافر</b> بعد أسابيع.',
                '<b>العلاج:</b> داعم — باراسيتامول أو إيبوبروفين، ومشروبات باردة وطعام طري، و<b>مراقبة الترطيب</b> (رفض السوائل هو السبب الرئيسي لإدخال المستشفى).',
                '<b>علامات الخطر (الفيروس المعوي A71):</b> رمعات عضلية، ورنح، وقيء مستمر، ونعاس، وتنفس سريع — التهاب جذع الدماغ والوذمة الرئوية.',
                '<b>الحمل:</b> خفيف غالبًا؛ والإصابة قرب موعد الولادة قد تسبب عدوى وليدية — أبلغ فريق التوليد. <b>الاحتياطات:</b> قياسية + تلامس للأطفال بالحفاضات؛ ويُطرح الفيروس في البراز لأسابيع — غسل اليدين بعد تغيير الحفاض. لا استبعاد إن كان الطفل بحال جيدة.',
            ]),
            figs=['hfmd']),
        blk('ddx', 'dengue', 'Dengue', 'حمّى الضنك',
            ul([
                '<b>Where:</b> endemic in western and south-western Saudi Arabia (Jeddah, Makkah, Jazan, and surrounding areas), and in travellers from South and South-East Asia, Africa and Latin America.',
                '<b>Picture:</b> sudden high fever, severe headache, retro-orbital pain, myalgia (“breakbone”), vomiting, flushed skin; a positive <b>tourniquet test</b> and petechiae. A convalescent rash — “<b>white islands in a sea of red</b>” — often itchy.',
                '<b>The danger comes as the fever falls</b> (critical phase, day 3–7): plasma leak, shock, bleeding. WHO <b>warning signs</b>: abdominal pain or tenderness, persistent vomiting, fluid accumulation, mucosal bleeding, lethargy or restlessness, liver enlargement &gt;2 cm, rising haematocrit with a rapid fall in platelets. Any warning sign → admit.',
                '<b>Test:</b> NS1 antigen and/or RT-PCR in the first 5–7 days; IgM after day 5. FBC daily in the critical phase.',
                '<b>Management:</b> <b>paracetamol only</b> — <b>no ibuprofen, NSAIDs or aspirin</b>; oral fluids; daily review during the critical phase. Standard precautions; protect the patient from mosquito bites while febrile (to prevent local spread).',
                '<b>Pregnancy:</b> higher risk of severe dengue, preterm birth and vertical transmission near term — refer.',
            ]),
            ul([
                '<b>أين:</b> متوطنة في غرب المملكة وجنوبها الغربي (جدة ومكة وجازان وما حولها)، وعند المسافرين القادمين من جنوب آسيا وجنوب شرقها وأفريقيا وأمريكا اللاتينية.',
                '<b>الصورة:</b> حمّى عالية مفاجئة، وصداع شديد، وألم خلف العينين، وألم عضلي («تكسير العظام»)، وقيء، واحمرار الجلد؛ مع <b>اختبار العاصبة</b> إيجابي ونَمَشات. وطفح النقاهة — «<b>جزر بيضاء في بحر أحمر</b>» — كثيرًا ما يسبب حكة.',
                '<b>الخطر يأتي مع هبوط الحمّى</b> (المرحلة الحرجة، اليوم 3–7): تسرّب البلازما، والصدمة، والنزف. <b>علامات الإنذار</b> عند منظمة الصحة العالمية: ألم البطن أو إيلامه، والقيء المستمر، وتجمّع السوائل، ونزف الأغشية المخاطية، والخمول أو التململ، وتضخم الكبد أكثر من 2 سم، وارتفاع الهيماتوكريت مع هبوط سريع في الصفيحات. أي علامة إنذار ← إدخال المستشفى.',
                '<b>الفحص:</b> مستضد NS1 و/أو RT-PCR في أول 5–7 أيام؛ وIgM بعد اليوم الخامس. وتعداد دم يومي في المرحلة الحرجة.',
                '<b>العلاج:</b> <b>باراسيتامول فقط</b> — <b>لا إيبوبروفين ولا مضادات التهاب غير ستيرويدية ولا أسبرين</b>؛ وسوائل بالفم؛ ومراجعة يومية في المرحلة الحرجة. احتياطات قياسية؛ واحمِ المريض من لدغ البعوض أثناء الحمّى (لمنع الانتشار المحلي).',
                '<b>الحمل:</b> خطر أعلى لحمّى الضنك الشديدة والولادة المبكرة وانتقال العدوى للجنين قرب الولادة — أحِلها.',
            ]),
            figs=['dengue']),
        blk('ddx', 'mpox', 'Mpox', 'جدري القردة (إمبوكس)',
            ul([
                '<b>Status:</b> clade I outbreaks continue in central and east Africa with spread to other regions; WHO still reports it as a graded emergency. Cases in the Eastern Mediterranean Region have been sporadic (none reported in June 2026). Children are affected mainly in household clusters in endemic areas.',
                '<b>Picture:</b> fever, headache, <b>marked lymphadenopathy</b> (a clue against varicella), then lesions that evolve together — macule → papule → deep-seated, firm, often <b>umbilicated</b> vesicle or pustule → crust — on the face, palms and soles, mouth and genitals.',
                '<b>Test:</b> PCR on a lesion swab (two swabs, vigorous). Notify public health on suspicion.',
                '<b>Precautions:</b> contact + droplet with an N95 respirator, eye protection, single room; cover lesions; isolate at home until all crusts have fallen off.',
                '<b>Treatment:</b> supportive; skin, eye and pain care. <b>Tecovirimat did not shorten healing in trials</b> (PALM007 clade I, STOMP clade II) — reserve for severe disease or the immunocompromised under specialist protocols. Vaccine (MVA-BN) for contacts and people at risk per national guidance.',
                '<b>Pregnancy:</b> risk of miscarriage, stillbirth and congenital infection; <b>immunocompromised</b> and young children have more severe disease.',
            ]),
            ul([
                '<b>الوضع:</b> تستمر فاشيات الفرع الأول في وسط أفريقيا وشرقها مع انتشار إلى مناطق أخرى؛ ولا تزال منظمة الصحة العالمية تصنّفها طارئة مُدرَّجة. أما الحالات في إقليم شرق المتوسط فمتفرقة (لم تُبلَّغ أي حالة في يونيو 2026). ويصاب الأطفال غالبًا ضمن تجمعات أسرية في المناطق الموبوءة.',
                '<b>الصورة:</b> حمّى، وصداع، و<b>تضخم واضح في العقد اللمفية</b> (مفتاح يبعد الجديري)، ثم آفات تتطور معًا — لطخة ← حطاطة ← حويصلة أو بثرة عميقة صلبة كثيرًا ما تكون <b>مسرّية</b> ← قشرة — على الوجه والكفين والقدمين والفم والأعضاء التناسلية.',
                '<b>الفحص:</b> PCR على مسحة من الآفة (مسحتان، بقوة). أبلغ الصحة العامة عند الاشتباه.',
                '<b>الاحتياطات:</b> تلامس + رذاذ مع كمامة N95، وواقٍ للعينين، وغرفة مفردة؛ وغطِّ الآفات؛ والعزل في البيت حتى تسقط كل القشور.',
                '<b>العلاج:</b> داعم؛ والعناية بالجلد والعينين والألم. <b>لم يقصّر التيكوفيريمات مدة الالتئام في التجارب</b> (PALM007 للفرع الأول، وSTOMP للفرع الثاني) — ويُحفظ للمرض الشديد أو لضعيفي المناعة وفق بروتوكولات اختصاصية. واللقاح (MVA-BN) للمخالطين ومن هم في خطر وفق الإرشادات الوطنية.',
                '<b>الحمل:</b> خطر الإجهاض وولادة جنين ميت والعدوى الخلقية؛ و<b>ضعيفو المناعة</b> وصغار الأطفال يصابون بمرض أشد.',
            ]),
            figs=['mpox']),
        blk('trap', 'do-not-miss-traps', 'Look-alikes that are not infections', 'حالات مشابهة ليست عدوى',
            ul([
                '<b>Drug reactions:</b> morbilliform drug eruption (days 4–14 of a new drug), DRESS (fever, facial swelling, eosinophilia, liver involvement — 2–8 weeks after anticonvulsants, allopurinol, sulfonamides), <b>SJS/TEN</b> (painful skin, blisters <b>with mucosal erosions</b>) — stop the drug and refer urgently.',
                '<b>IgA vasculitis (HSP):</b> palpable purpura on the legs and buttocks in a well child, with joint pain, abdominal pain — check urine and blood pressure.',
                '<b>ITP and leukaemia:</b> petechiae without fever, or with pallor, bone pain, nodes or hepatosplenomegaly — FBC and film the same day.',
                '<b>MIS-C</b> (after SARS-CoV-2): fever, rash, abdominal pain, shock — overlaps with Kawasaki disease; manage in hospital.',
            ]),
            ul([
                '<b>التفاعلات الدوائية:</b> الطفح الدوائي الشبيه بالحصبة (في اليوم 4–14 من دواء جديد)، ومتلازمة DRESS (حمّى، وتورّم الوجه، وكثرة الحمضات، وإصابة الكبد — بعد 2–8 أسابيع من مضادات الصرع أو الألوبيورينول أو السلفوناميدات)، و<b>متلازمة ستيفنز-جونسون / انحلال البشرة السمّي</b> (جلد مؤلم وفقاعات <b>مع تآكلات مخاطية</b>) — أوقف الدواء وأحِل فورًا.',
                '<b>التهاب الأوعية بالغلوبيولين A (فرفرية هينوخ-شونلاين):</b> فرفرية مجسوسة على الساقين والإليتين عند طفل بحال جيدة، مع ألم المفاصل وألم البطن — افحص البول والضغط.',
                '<b>نقص الصفيحات المناعي وابيضاض الدم:</b> نَمَشات دون حمّى، أو مع شحوب وألم عظام وعقد أو تضخم الكبد والطحال — تعداد دم كامل ولطاخة في اليوم نفسه.',
                '<b>المتلازمة الالتهابية متعددة الأجهزة عند الأطفال (MIS-C)</b> (بعد كوفيد-19): حمّى، وطفح، وألم بطن، وصدمة — تتداخل مع داء كاواساكي؛ وتُدار في المستشفى.',
            ])),
    ])
