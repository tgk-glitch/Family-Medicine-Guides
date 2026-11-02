from h import ul, ol, p, tbl, blk

# ─────────────────────────────────────────────────────────────
# 6 · VARICELLA & ZOSTER
# ─────────────────────────────────────────────────────────────
VARICELLA = dict(
    id='varicella',
    h_en='Chickenpox (varicella) and shingles (zoster)',
    h_ar='الجديري المائي (الحماق) والحزام الناري (الهربس النطاقي)',
    sub_en='Usually benign in healthy children — dangerous in newborns, pregnancy, adults and the immunocompromised',
    sub_ar='حميد غالبًا عند الأطفال الأصحاء — وخطير عند حديثي الولادة والحوامل والبالغين وضعيفي المناعة',
    blocks=[
        blk('glance', 'varicella-at-a-glance', 'At a glance', 'لمحة سريعة',
            ul([
                '<b>Cause:</b> varicella-zoster virus (VZV). Primary infection is chickenpox; the virus then lies dormant in sensory ganglia and can reactivate as shingles.',
                '<b>Spread:</b> airborne and by direct contact with vesicle fluid. About 9 in 10 susceptible household contacts are infected. Shingles spreads only by contact with the lesions (and causes chickenpox, not shingles, in the contact).',
                '<b>Course:</b> mild prodrome, then crops of itchy spots that pass through <b>macule → papule → vesicle (“dewdrop on a rose petal”) → crust</b>, with lesions at different stages at the same time. Mainly on the trunk, face and scalp; also in the mouth.',
                '<b>Infectious:</b> 1–2 days before the rash until every lesion has crusted. <b>Airborne + contact precautions.</b>',
            ]),
            ul([
                '<b>المسبب:</b> فيروس الحماق النطاقي. الإصابة الأولى هي الجديري المائي؛ ثم يكمن الفيروس في العقد العصبية الحسية وقد ينشط مجددًا على شكل حزام ناري.',
                '<b>الانتشار:</b> بالهواء وبالتلامس المباشر مع سائل الحويصلات. يُصاب نحو 9 من كل 10 مخالطين غير محصَّنين في البيت. أما الحزام الناري فلا ينتقل إلا بلمس الآفات (ويسبب للمخالط جديريًا لا حزامًا ناريًا).',
                '<b>المسار:</b> أعراض بادئة خفيفة، ثم دفعات من بقع حاكّة تمرّ بمراحل <b>لطخة ← حطاطة ← حويصلة («قطرة ندى على بتلة وردة») ← قشرة</b>، مع آفات في مراحل مختلفة في الوقت نفسه. أكثرها على الجذع والوجه وفروة الرأس؛ وفي الفم أيضًا.',
                '<b>فترة العدوى:</b> من 1–2 يوم قبل الطفح حتى تتقشّر كل الآفات. <b>احتياطات هوائية + تلامس.</b>',
            ]),
            figs=['varicella', 'zoster']),
        blk('dx', 'varicella-dx', 'Diagnosis', 'التشخيص',
            ul([
                '<b>Clinical</b> in typical cases.',
                '<b>PCR of vesicle fluid or a scraped crust</b> when the picture is atypical (vaccinated child, immunocompromised, suspected smallpox-like illness or mpox) or when a high-risk contact’s management depends on it.',
                'Varicella IgG on the <b>contact</b> (pregnant woman, immunocompromised) to decide on prophylaxis — results within 24–48 h.',
                '<b>Breakthrough varicella</b> in vaccinated children: usually under 50 lesions, mostly papules rather than vesicles, little fever — still infectious.',
            ]),
            ul([
                '<b>سريري</b> في الحالات النموذجية.',
                '<b>PCR على سائل الحويصلة أو كشط قشرة</b> عندما تكون الصورة غير نمطية (طفل مطعَّم، أو ضعيف المناعة، أو اشتباه بمرض شبيه بالجدري أو بجدري القردة)، أو حين يتوقف علاج مخالط عالي الخطورة على ذلك.',
                'الغلوبيولين المناعي IgG للجديري عند <b>المخالط</b> (الحامل، أو ضعيف المناعة) لتقرير الوقاية — النتيجة خلال 24–48 ساعة.',
                '<b>الجديري الاختراقي</b> عند الأطفال المطعَّمين: عادة أقل من 50 آفة، وأغلبها حطاطات لا حويصلات، وحمّى قليلة — لكنه يبقى معديًا.',
            ])),
        blk('mx', 'varicella-mx', 'Management', 'العلاج',
            '<p><b>Healthy child under 12 years:</b> supportive care only.</p>'
            + ul([
                '<b>Fever and pain: paracetamol.</b> <b>Avoid ibuprofen and other NSAIDs</b> (NICE CKS) — linked to severe skin and soft-tissue infection, including necrotising fasciitis with group A streptococcus. <b>Never aspirin</b> (Reye syndrome).',
                '<b>Itch:</b> calamine or emollient cooling lotions; an oral antihistamine at night (e.g. chlorphenamine from age 1 year, per formulary); lukewarm baths; loose cotton clothes.',
                '<b>Prevent scratching:</b> short clean nails, mittens at night for infants.',
                '<b>Fluids</b>; sugar-free ice lollies help mouth ulcers.',
            ])
            + '<p><b>Oral aciclovir</b> — start <b>within 24 hours</b> of rash onset — for people at higher risk of severe disease: <b>age 13 years and over</b>, chronic skin or lung disease, long-term salicylates, short or intermittent oral or inhaled corticosteroids, and <b>secondary cases in the same household</b> (they get a higher viral dose).</p>'
            + tbl(['Group', 'Treatment'], [
                ['Child (2 years and over), when indicated', 'Aciclovir 20 mg/kg (max 800 mg) orally 4 times a day for 5 days'],
                ['Adolescent ≥13 years / adult', 'Aciclovir 800 mg 5 times a day for 7 days (or valaciclovir 1 g 3 times a day for 7 days)'],
                ['<b>Pregnant woman</b>, presenting within 24 h of rash', 'Oral aciclovir 800 mg 5 times a day for 7 days (RCOG, UKHSA); admit if chest symptoms, neurological signs, haemorrhagic rash or dense lesions'],
                ['<b>Immunocompromised</b> or <b>neonate</b>, or any severe case', '<b>IV aciclovir 10 mg/kg every 8 hours</b> (dose by age and renal function, per formulary) for 7–10 days — admit'],
            ])
            + '<p><b>Shingles in a child:</b> usually mild and self-limiting in healthy children (often after chickenpox in infancy or in utero). Treat with aciclovir if immunocompromised, if the <b>eye</b> is involved (Hutchinson sign — vesicles on the tip of the nose — means urgent ophthalmology review) or if severe.</p>',
            '<p><b>طفل سليم دون 12 سنة:</b> رعاية داعمة فقط.</p>'
            + ul([
                '<b>للحمّى والألم: باراسيتامول.</b> <b>تجنّب الإيبوبروفين وغيره من مضادات الالتهاب غير الستيرويدية</b> (NICE CKS)&rlm; — لارتباطها بعدوى شديدة في الجلد والأنسجة الرخوة، منها التهاب اللفافة الناخر بالعقديات المجموعة A. <b>ولا أسبرين أبدًا</b> (متلازمة راي).',
                '<b>للحكة:</b> الكالامين أو المستحضرات المرطّبة المبرّدة؛ ومضاد هيستامين فموي ليلًا (مثل الكلورفينامين من عمر سنة، وفق دليل الأدوية)؛ وحمّامات فاترة؛ وملابس قطنية واسعة.',
                '<b>منع الحكّ:</b> أظافر قصيرة نظيفة، وقفازات ليلًا للرضّع.',
                '<b>السوائل</b>؛ والمثلجات الخالية من السكر تريح قرح الفم.',
            ])
            + '<p><b>الأسيكلوفير الفموي</b> — يُبدأ <b>خلال 24 ساعة</b> من بدء الطفح — لمن هم أعلى خطرًا للمرض الشديد: <b>عمر 13 سنة فأكثر</b>، وأمراض الجلد أو الرئة المزمنة، والساليسيلات طويلة الأمد، والكورتيزون الفموي أو المستنشق قصير الأمد أو المتقطع، و<b>الحالات الثانوية في البيت نفسه</b> (لتلقيها جرعة فيروسية أعلى).</p>'
            + tbl(['الفئة', 'العلاج'], [
                ['طفل (سنتان فأكثر) عند وجود داعٍ', 'أسيكلوفير 20 ملغ/كغ (بحد أقصى 800 ملغ) بالفم 4 مرات يوميًا لمدة 5 أيام'],
                ['مراهق 13 سنة فأكثر / بالغ', 'أسيكلوفير 800 ملغ 5 مرات يوميًا لمدة 7 أيام (أو فالاسيكلوفير 1 غ 3 مرات يوميًا لمدة 7 أيام)'],
                ['<b>امرأة حامل</b> تراجع خلال 24 ساعة من الطفح', 'أسيكلوفير فموي 800 ملغ 5 مرات يوميًا لمدة 7 أيام (الكلية الملكية لأطباء النساء والتوليد وUKHSA)&rlm;؛ وأدخِلها المستشفى عند أعراض صدرية، أو علامات عصبية، أو طفح نزفي، أو آفات كثيفة'],
                ['<b>ضعيف المناعة</b> أو <b>حديث الولادة</b>، أو أي حالة شديدة', '<b>أسيكلوفير وريدي 10 ملغ/كغ كل 8 ساعات</b> (الجرعة حسب العمر ووظيفة الكلى، وفق دليل الأدوية) لمدة 7–10 أيام — إدخال المستشفى'],
            ])
            + '<p><b>الحزام الناري عند الطفل:</b> خفيف غالبًا ويشفى ذاتيًا عند الأطفال الأصحاء (وكثيرًا ما يأتي بعد جديري في الرضاعة أو داخل الرحم). يُعالج بالأسيكلوفير عند ضعف المناعة، أو إصابة <b>العين</b> (علامة هتشنسون — حويصلات على طرف الأنف — تعني مراجعة عيون عاجلة)، أو الشدة.</p>'),
        blk('special', 'varicella-special', 'Special populations and post-exposure prophylaxis', 'الفئات الخاصة والوقاية بعد التعرّض',
            ul([
                '<b>Pregnancy — the mother:</b> varicella pneumonia is more severe in pregnancy, especially in the third trimester and in smokers.',
                '<b>Pregnancy — the fetus:</b> <b>fetal varicella syndrome</b> (limb hypoplasia, skin scarring, eye and brain damage) after maternal infection in the first 20 weeks — about <b>0.4% before 13 weeks and 2% at 13–20 weeks</b>. Refer to fetal medicine; detailed ultrasound 5 weeks after infection.',
                '<b>Newborn:</b> if the mother’s rash starts <b>5 days before to 2 days after delivery</b>, the baby has no maternal antibody and faces severe neonatal varicella (historic mortality up to 30%) — VariZIG for the baby, and IV aciclovir if lesions appear.',
                '<b>Immunocompromised:</b> risk of progressive, disseminated varicella with pneumonia, hepatitis and encephalitis — IV aciclovir, admit, airborne + contact precautions.',
            ])
            + tbl(['Exposed person', 'What to do'], [
                ['Healthy, non-immune, aged 12 months and over', '<b>Varicella vaccine within 3–5 days</b> of exposure (best within 72 h); counts as dose 1'],
                ['Immunocompromised, non-immune', '<b>VariZIG</b> 125 IU/10 kg IM (minimum 62.5 IU, max 625 IU) <b>as soon as possible, up to 10 days</b> after exposure'],
                ['Newborn of a mother with onset 5 days before to 2 days after delivery', 'VariZIG as soon as possible'],
                ['Preterm infant in hospital: ≥28 weeks with a non-immune mother; or &lt;28 weeks or ≤1,000 g regardless of maternal immunity', 'VariZIG'],
                ['<b>Pregnant woman</b>, non-immune (IgG negative)', 'US (CDC): VariZIG within 10 days. UK (UKHSA 2024, RCOG): <b>oral aciclovir 800 mg 4 times a day or valaciclovir 1 g 3 times a day for 7 days, starting on day 7 after exposure</b> (up to day 14). Follow the national pathway available to you.'],
                ['If VariZIG is not available', 'IV immunoglobulin 400 mg/kg, or (AAP Red Book option) oral aciclovir 20 mg/kg 4 times a day for 7 days, starting 7–10 days after exposure'],
            ]),
            ul([
                '<b>الحمل — الأم:</b> الالتهاب الرئوي الجديري أشد في الحمل، خاصة في الثلث الأخير وعند المدخّنات.',
                '<b>الحمل — الجنين:</b> <b>متلازمة الجديري الجنيني</b> (نقص تنسّج الأطراف، وندبات الجلد، وتضرر العين والدماغ) بعد إصابة الأم في أول 20 أسبوعًا — نحو <b>0.4% قبل 13 أسبوعًا و2% بين 13 و20 أسبوعًا</b>. أحِلها إلى طب الأجنة؛ مع تصوير مفصّل بالموجات فوق الصوتية بعد 5 أسابيع من الإصابة.',
                '<b>حديث الولادة:</b> إن بدأ طفح الأم <b>بين 5 أيام قبل الولادة ويومين بعدها</b>، فلا أجسام مضادة من الأم لدى الطفل ويواجه جديريًا وليديًا شديدًا (بلغت الوفيات تاريخيًا 30%) — VariZIG للطفل، وأسيكلوفير وريدي إن ظهرت الآفات.',
                '<b>ضعيف المناعة:</b> خطر الجديري المترقي المنتشر مع التهاب الرئة والكبد والدماغ — أسيكلوفير وريدي، وإدخال المستشفى، واحتياطات هوائية + تلامس.',
            ])
            + tbl(['الشخص المعرَّض', 'ماذا تفعل'], [
                ['سليم وغير محصَّن، بعمر 12 شهرًا فأكثر', '<b>لقاح الجديري خلال 3–5 أيام</b> من التعرّض (الأفضل خلال 72 ساعة)&rlm;؛ ويُحتسب الجرعة الأولى'],
                ['ضعيف المناعة وغير محصَّن', '<b>VariZIG</b> بجرعة 125 وحدة لكل 10 كغ عضليًا (بحد أدنى 62.5 وحد أقصى 625 وحدة) <b>بأسرع ما يمكن، حتى 10 أيام</b> بعد التعرّض'],
                ['حديث ولادة لأم بدأ طفحها بين 5 أيام قبل الولادة ويومين بعدها', 'VariZIG بأسرع ما يمكن'],
                ['خديج في المستشفى: 28 أسبوعًا فأكثر وأمه غير محصَّنة؛ أو أقل من 28 أسبوعًا أو 1,000 غ أو أقل أيًّا كانت مناعة الأم', 'VariZIG'],
                ['<b>امرأة حامل</b> غير محصَّنة (IgG سلبي)', 'الولايات المتحدة (CDC)&rlm;: VariZIG خلال 10 أيام. المملكة المتحدة (UKHSA 2024 والكلية الملكية)&rlm;: <b>أسيكلوفير فموي 800 ملغ 4 مرات يوميًا أو فالاسيكلوفير 1 غ 3 مرات يوميًا لمدة 7 أيام، بدءًا من اليوم السابع بعد التعرّض</b> (حتى اليوم 14). اتبع المسار الوطني المتاح لك.'],
                ['إن لم يتوفر VariZIG', 'غلوبيولين مناعي وريدي 400 ملغ/كغ، أو (خيار الكتاب الأحمر للأكاديمية الأمريكية لطب الأطفال) أسيكلوفير فموي 20 ملغ/كغ 4 مرات يوميًا لمدة 7 أيام، يبدأ بعد 7–10 أيام من التعرّض'],
            ])),
        blk('comp', 'varicella-complications', 'Complications', 'المضاعفات',
            ul([
                '<b>Secondary bacterial skin infection</b> (<i>S. aureus</i>, group A streptococcus) — the most common; watch for <b>new fever after day 3–4</b>, spreading redness, pain out of proportion: <b>invasive GAS or necrotising fasciitis</b> until proven otherwise.',
                '<b>Pneumonia</b> (adults, pregnancy, immunocompromised), <b>cerebellar ataxia</b> (about 1 week after rash, usually recovers), encephalitis, hepatitis, thrombocytopenia.',
                '<b>Reye syndrome</b> with aspirin; <b>stroke</b> (post-varicella arteriopathy) in the following months — rare.',
            ]),
            ul([
                '<b>العدوى الجلدية الجرثومية الثانوية</b> (المكورات العنقودية الذهبية، والعقديات المجموعة A)&rlm; — الأكثر شيوعًا؛ انتبه إلى <b>حمّى جديدة بعد اليوم 3–4</b>، واحمرار منتشر، وألم لا يتناسب مع المظهر: <b>عدوى عقدية غازية أو التهاب لفافة ناخر</b> حتى يثبت العكس.',
                '<b>الالتهاب الرئوي</b> (البالغون، والحوامل، وضعيفو المناعة)، و<b>الرنح المخيخي</b> (بعد الطفح بنحو أسبوع، ويتعافى غالبًا)، والتهاب الدماغ، والتهاب الكبد، ونقص الصفيحات.',
                '<b>متلازمة راي</b> مع الأسبرين؛ و<b>السكتة الدماغية</b> (اعتلال الشرايين بعد الجديري) في الأشهر التالية — نادرة.',
            ])),
        blk('tell', 'varicella-tell', 'What to tell the family', 'ماذا تقول للأسرة',
            ul([
                '“Use paracetamol for fever, not ibuprofen, and never aspirin.”',
                '“Your child can go back to school when every spot has crusted over — usually about 5 days.”',
                '“Come back if a spot becomes very red, hot, swollen or painful, if the fever comes back after getting better, or if your child is short of breath, unsteady, or very sleepy.”',
                '“Tell anyone pregnant, any new mother, and anyone on cancer treatment or steroids who was near your child — they may need a test or medicine.”',
            ]),
            ul([
                '«استخدم الباراسيتامول للحمّى، لا الإيبوبروفين، ولا الأسبرين أبدًا.»',
                '«يمكن لطفلك العودة إلى المدرسة حين تتقشّر كل البقع — بعد نحو 5 أيام عادة.»',
                '«عُد إن صارت إحدى البقع شديدة الاحمرار أو ساخنة أو متورمة أو مؤلمة، أو عادت الحمّى بعد تحسّن، أو ضاق نفَس طفلك، أو اختلّ توازنه، أو صار نعسانًا جدًا.»',
                '«أخبِر كل حامل، وكل أم وضعت حديثًا، وكل من يتلقى علاج السرطان أو الكورتيزون ممن اقتربوا من طفلك — فقد يحتاجون إلى فحص أو دواء.»',
            ])),
    ])

# ─────────────────────────────────────────────────────────────
# 7 · ROSEOLA
# ─────────────────────────────────────────────────────────────
ROSEOLA = dict(
    id='roseola',
    h_en='Roseola infantum (sixth disease)',
    h_ar='الوردية الطفلية (المرض السادس)',
    sub_en='High fever in a well baby, then a rash as the fever breaks',
    sub_ar='حمّى عالية عند رضيع بحال جيدة، ثم طفح مع انكسار الحمّى',
    blocks=[
        blk('glance', 'roseola-at-a-glance', 'At a glance', 'لمحة سريعة',
            ul([
                '<b>Cause:</b> human herpesvirus 6B (sometimes HHV-7), usually caught from the saliva of family members.',
                '<b>Who:</b> 6 months to 2 years; almost all children are infected by age 3.',
                '<b>Course:</b> <b>3–5 days of high fever</b> (often &gt;39.5 °C) in a child who looks surprisingly well, then, as the fever falls, a <b>rose-pink, blanching, non-itchy rash</b> on the trunk spreading to the neck and face, gone in 1–2 days.',
                '<b>Clues:</b> Nagayama spots (red papules on the soft palate and uvula), mild cervical nodes, eyelid swelling, irritability; the anterior fontanelle may bulge.',
                'HHV-6 is a leading cause of <b>febrile seizures</b> in children under 2.',
            ]),
            ul([
                '<b>المسبب:</b> فيروس الهربس البشري 6B (وأحيانًا 7)، ويُلتقط غالبًا من لعاب أفراد الأسرة.',
                '<b>من يصاب:</b> من 6 أشهر إلى سنتين؛ ويكاد يُصاب كل الأطفال قبل سن 3 سنوات.',
                '<b>المسار:</b> <b>3–5 أيام من حمّى عالية</b> (غالبًا أعلى من 39.5 °م) عند طفل يبدو بحال جيدة على غير المتوقع، ثم مع هبوط الحرارة يظهر <b>طفح وردي يبيضّ بالضغط ولا يسبب حكة</b> على الجذع وينتشر إلى الرقبة والوجه، ويزول خلال 1–2 يوم.',
                '<b>مفاتيح التشخيص:</b> بقع ناغاياما (حطاطات حمراء على الحنك الرخو واللهاة)، وعقد رقبية خفيفة، وتورّم الجفنين، وتهيّج؛ وقد يبرز اليافوخ الأمامي.',
                'فيروس الهربس البشري 6 من الأسباب الرئيسية <b>للتشنجات الحرارية</b> دون سن سنتين.',
            ]),
            figs=['roseola']),
        blk('mx', 'roseola-mx', 'Diagnosis and management', 'التشخيص والعلاج',
            ul([
                '<b>Clinical diagnosis</b> once the rash appears. Before the rash, it is a fever without a source — assess as such: <b>urine test</b> to exclude UTI in a febrile infant, and the <a href="urgent-care.html#febrile-infant">febrile infant pathway</a> if under 3 months.',
                '<b>A bulging fontanelle with fever needs meningitis excluded</b> — do not attribute it to roseola without assessment.',
                '<b>Supportive:</b> paracetamol or ibuprofen for comfort (they do not prevent febrile seizures), fluids, light clothing.',
                '<b>Febrile seizure:</b> explain, safety-net, and teach parents first aid; a first seizure, a prolonged or focal seizure, or a child who does not recover quickly needs same-day assessment.',
                '<b>Precautions:</b> standard. No exclusion once the child is well.',
                '<b>Immunocompromised</b> (transplant recipients): HHV-6 reactivation can cause encephalitis, hepatitis and marrow suppression — specialist care.',
            ]),
            ul([
                '<b>التشخيص سريري</b> بعد ظهور الطفح. وقبل الطفح هي حمّى مجهولة المصدر — تُقيَّم على هذا الأساس: <b>فحص البول</b> لاستبعاد التهاب المسالك عند الرضيع المحموم، و<a href="urgent-care.html#febrile-infant">مسار الرضيع المحموم</a> دون 3 أشهر.',
                '<b>اليافوخ البارز مع الحمّى يستلزم استبعاد التهاب السحايا</b> — لا تنسبه إلى الوردية دون تقييم.',
                '<b>داعم:</b> باراسيتامول أو إيبوبروفين للراحة (ولا يمنعان التشنجات الحرارية)، وسوائل، وملابس خفيفة.',
                '<b>التشنج الحراري:</b> اشرح، وأعطِ تعليمات أمان، وعلّم الوالدين الإسعاف الأولي؛ والنوبة الأولى أو المطوّلة أو البؤرية أو الطفل الذي لا يتعافى سريعًا يحتاج إلى تقييم في اليوم نفسه.',
                '<b>الاحتياطات:</b> قياسية. لا استبعاد بعد التعافي.',
                '<b>ضعيفو المناعة</b> (متلقو زراعة الأعضاء): قد يسبب نشاط فيروس الهربس البشري 6 التهاب الدماغ والكبد وتثبيط النخاع — رعاية اختصاصية.',
            ])),
        blk('trap', 'roseola-trap', 'Trap', 'خطأ شائع',
            p('A rash that appears after amoxicillin was started for “tonsillitis” in a feverish toddler is often roseola, not a drug allergy. Ask exactly when the fever stopped and the rash started before labelling the child penicillin-allergic.'),
            p('الطفح الذي يظهر بعد بدء الأموكسيسيلين لـ«التهاب لوزتين» عند طفل صغير محموم كثيرًا ما يكون وردية لا حساسية دوائية. اسأل بدقة متى توقفت الحمّى ومتى بدأ الطفح قبل أن تصف الطفل بأنه مصاب بحساسية البنسلين.')),
    ])

# ─────────────────────────────────────────────────────────────
# 8 · FIFTH DISEASE
# ─────────────────────────────────────────────────────────────
FIFTH = dict(
    id='fifth',
    h_en='Fifth disease (erythema infectiosum, parvovirus B19)',
    h_ar='المرض الخامس (الحُمامى المُعدية — الفيروس الصغير B19)',
    sub_en='“Slapped cheek” — harmless in most children, important in pregnancy and in children with sickle cell disease',
    sub_ar='«الخد المصفوع» — غير مؤذٍ لمعظم الأطفال، ومهم في الحمل وعند الأطفال المصابين بفقر الدم المنجلي',
    blocks=[
        blk('glance', 'fifth-at-a-glance', 'At a glance', 'لمحة سريعة',
            ul([
                '<b>Cause:</b> parvovirus B19, spread by respiratory droplets (also blood products and mother to fetus). It infects red-cell precursors in the marrow.',
                '<b>Who:</b> school-age children (5–15 years); outbreaks in late winter and spring. The US and Europe saw a marked rise in 2024–25 (CDC health advisory, MMWR 2025).',
                '<b>Course:</b> mild fever, headache, coryza → about a week later, bright red <b>“slapped cheeks”</b> with circumoral pallor → a <b>lacy, reticular rash</b> on the arms, legs and trunk that can come and go for weeks with heat, exercise, sunlight or stress.',
                '<b>Key point:</b> the child is <b>infectious before the rash, not after it</b> — so by the time the diagnosis is made, the child can go to school.',
            ]),
            ul([
                '<b>المسبب:</b> الفيروس الصغير B19، وينتشر بالرذاذ التنفسي (وأيضًا بمنتجات الدم ومن الأم إلى الجنين). ويصيب سلائف الكريات الحمراء في النخاع.',
                '<b>من يصاب:</b> أطفال المدارس (5–15 سنة)&rlm;؛ وتكثر الفاشيات في أواخر الشتاء والربيع. وقد شهدت الولايات المتحدة وأوروبا ارتفاعًا ملحوظًا في 2024–2025 (تنبيه صحي من CDC، وتقرير MMWR 2025)&rlm;.',
                '<b>المسار:</b> حمّى خفيفة، وصداع، وزكام ← بعد نحو أسبوع، <b>«خدّان مصفوعان»</b> بلون أحمر زاهٍ مع شحوب حول الفم ← <b>طفح شبكي مخرّم</b> على الذراعين والساقين والجذع قد يظهر ويختفي لأسابيع مع الحرارة أو الرياضة أو الشمس أو التوتر.',
                '<b>النقطة الأساسية:</b> الطفل <b>معدٍ قبل الطفح، لا بعده</b> — فحين يُشخَّص يمكنه الذهاب إلى المدرسة.',
            ]),
            figs=['fifth']),
        blk('mx', 'fifth-mx', 'Diagnosis and management', 'التشخيص والعلاج',
            ul([
                '<b>Clinical</b> in a typical child. Confirm with <b>parvovirus B19 IgM</b> (and PCR) when it matters — pregnancy, haemolytic anaemia, immunocompromise, atypical rash (e.g. papular-purpuric “gloves and socks”).',
                '<b>Supportive:</b> paracetamol or ibuprofen for fever and joint pain; reassure that the recurring rash is not a relapse.',
                '<b>Adults</b> (especially women) more often get a symmetrical arthropathy of hands, wrists, knees — can last weeks.',
                '<b>No exclusion</b> once the rash has appeared. Inform pregnant staff and contacts so they can be tested.',
            ]),
            ul([
                '<b>سريري</b> عند الطفل النموذجي. ويُؤكَّد بالغلوبيولين المناعي <b>IgM للفيروس الصغير B19</b> (وPCR) حين يكون للأمر أهمية — الحمل، وفقر الدم الانحلالي، وضعف المناعة، والطفح غير النمطي (مثل نمط «القفازات والجوارب» الحطاطي الفرفري).',
                '<b>داعم:</b> باراسيتامول أو إيبوبروفين للحمّى وألم المفاصل؛ وطمئن الأسرة بأن تكرار الطفح ليس انتكاسة.',
                '<b>البالغون</b> (وخاصة النساء) يصابون أكثر باعتلال مفصلي متناظر في اليدين والرسغين والركبتين — قد يستمر أسابيع.',
                '<b>لا استبعاد</b> بعد ظهور الطفح. أبلغ العاملات والمخالطات الحوامل ليُجرين الفحص.',
            ])),
        blk('special', 'fifth-special', 'Special populations', 'الفئات الخاصة',
            ul([
                '<b>Pregnancy:</b> about half of women are already immune. Infection before 20 weeks carries a fetal loss risk of roughly 5–10%; the fetus can develop severe anaemia and <b>hydrops fetalis</b>. A pregnant contact should have <b>B19 IgG and IgM</b> tested promptly. If infected: refer to fetal medicine for <b>serial ultrasound with middle cerebral artery Doppler every 1–2 weeks for 8–12 weeks</b>; intrauterine transfusion is effective for hydrops. Parvovirus does not cause birth defects.',
                '<b>Sickle cell disease, thalassaemia, hereditary spherocytosis</b> (common in parts of Saudi Arabia, notably the Eastern Province and the south-west): B19 halts red-cell production and causes a <b>transient aplastic crisis</b> — sudden pallor, fatigue, falling haemoglobin with <b>reticulocytes near zero</b>. These children are highly infectious (droplet precautions for 7 days) and often need <b>transfusion</b>. Any febrile child with sickle cell disease and new pallor needs a same-day FBC and reticulocyte count.',
                '<b>Immunocompromised</b> (leukaemia, transplant, HIV): chronic infection with <b>pure red-cell aplasia</b>, usually without rash — treated with IV immunoglobulin; droplet precautions for the whole admission.',
            ]),
            ul([
                '<b>الحمل:</b> نحو نصف النساء محصَّنات مسبقًا. الإصابة قبل 20 أسبوعًا تحمل خطر فقد الجنين بنحو 5–10%&rlm;؛ وقد يصاب الجنين بفقر دم شديد و<b>استسقاء جنيني</b>. على الحامل المخالطة إجراء فحص <b>IgG وIgM للفيروس B19</b> سريعًا. وإن أصيبت: إحالة إلى طب الأجنة لـ<b>تصوير متكرر بالموجات فوق الصوتية مع دوبلر الشريان الدماغي الأوسط كل 1–2 أسبوع لمدة 8–12 أسبوعًا</b>&rlm;؛ ونقل الدم داخل الرحم فعّال في علاج الاستسقاء. ولا يسبب الفيروس تشوهات خلقية.',
                '<b>فقر الدم المنجلي والثلاسيميا وكثرة الكريات الكروية الوراثية</b> (شائعة في أجزاء من المملكة، لا سيما المنطقة الشرقية والجنوب الغربي): يوقف الفيروس إنتاج الكريات الحمراء ويسبب <b>نوبة لاتنسّج عابرة</b> — شحوب مفاجئ، وتعب، وهبوط الهيموغلوبين مع <b>شبكيات تقارب الصفر</b>. هؤلاء الأطفال شديدو العدوى (احتياطات رذاذ 7 أيام) وكثيرًا ما يحتاجون إلى <b>نقل دم</b>. كل طفل محموم مصاب بفقر الدم المنجلي مع شحوب جديد يحتاج إلى تعداد دم كامل وعدّ للشبكيات في اليوم نفسه.',
                '<b>ضعيفو المناعة</b> (ابيضاض الدم، وزراعة الأعضاء، وفيروس نقص المناعة)&rlm;: عدوى مزمنة مع <b>لاتنسّج الكريات الحمراء الصرف</b>، غالبًا دون طفح — تُعالج بالغلوبيولين المناعي الوريدي؛ واحتياطات رذاذ طوال الإقامة.',
            ])),
    ])
