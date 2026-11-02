"""Parent leaflet: fever and rash in children (EN/AR). Same block format as
tools/public-education-source/leaflet_content.py."""

FEVER_RASH = dict(
    slug="fever-rash",
    tone="#9B3D5A", tone_soft="#F7ECF0",
    topic_en="Children's health", topic_ar="صحة الأطفال",
    guide="fever-rash.html",
    title_en="Fever and rash in children",
    title_ar="الحمّى والطفح الجلدي عند الأطفال",
    sub_en="How to care for your child at home, protect others — and know when to get help",
    sub_ar="كيف تعتني بطفلك في البيت، وتحمي الآخرين، وتعرف متى تطلب المساعدة",
    card_en="The glass test, care at home, how long to stay off school, who to protect, and warning signs.",
    card_ar="اختبار الكأس، والرعاية في البيت، ومدة الغياب عن المدرسة، ومن تحميه، وعلامات الخطر.",
    sources=[
        "CDC. Isolation precautions guideline, Appendix A: type and duration of precautions (2007, updated 2023)",
        "UK Health Security Agency. Health protection in children and young people's settings — exclusion table (updated September 2026)",
        "NICE. Fever in under 5s (NG143); Meningitis and meningococcal disease (NG240, 2024); Impetigo (NG153)",
        "American Academy of Pediatrics. Red Book 2024–2027",
        "Ministry of Health, Saudi Arabia. National immunization schedule (Sehhaty)",
    ],
    en=[
        ('key', "The 5 things to remember", [
            "Most rashes with fever are caused by viruses and get better on their own.",
            "Do the <b>glass test</b>. If the spots do not fade under a glass, <b>go to the emergency department now</b>.",
            "For fever, use <b>paracetamol</b>. <b>Never give aspirin</b> to children. Do not give ibuprofen for chickenpox.",
            "Keep your child at home and <b>away from pregnant women and newborn babies</b> until your doctor says it is safe.",
            "Check your child has had <b>all their vaccines</b>, including two doses of MMR.",
        ]),
        ('h', "The glass test"),
        ('p', "Press the side of a clear glass firmly on the spots. If you can still see the spots through the glass, "
              "this can be a sign of a serious infection called meningococcal disease (meningitis). "
              "Go to the emergency department or call 997 straight away. On darker skin, check the palms, soles and inside the eyelids."),
        ('h', "Common rashes in children"),
        ('table', ["Illness", "What you may see", "Stay off nursery or school"], [
            ["Measles", "High fever, cough, runny nose, red eyes, then a blotchy rash from the face down", "4 days from the start of the rash"],
            ["Chickenpox", "Itchy spots that turn into blisters, then scabs", "Until all spots have scabbed (about 5 days)"],
            ["Scarlet fever", "Sore throat, red rough “sandpaper” rash, red tongue", "24 hours after starting antibiotics"],
            ["Impetigo", "Sores with yellow-brown crusts, often around the nose and mouth", "Until crusted, or 2 days after starting antibiotics"],
            ["Slapped cheek (fifth disease)", "Bright red cheeks, then a lacy rash on arms and legs", "No need once the rash appears"],
            ["Roseola", "High fever for 3–5 days, then a pink rash as the fever goes", "No need once well"],
            ["Hand, foot and mouth", "Mouth ulcers and small blisters on hands and feet", "No need if well enough"],
        ]),
        ('break',),
        ('h', "Caring for your child at home"),
        ('ul', [
            "Give <b>small drinks often</b> — water, milk or breast milk. Cold drinks help a sore mouth.",
            "Use <b>paracetamol</b> if your child is uncomfortable. Follow the dose on the pack for their age or weight.",
            "Dress your child in light clothes. For itchy spots, use calamine lotion and keep nails short.",
            "Wash hands often and use a separate towel. Finish all the antibiotic if your doctor gives one.",
        ]),
        ('tip', "Protect others", [
            "<b>Pregnant women</b> who have been near your child should call their doctor today — some rashes can harm an unborn baby.",
            "Keep your child away from <b>newborn babies</b> and anyone with <b>weak immunity</b> (for example, on cancer treatment or steroids).",
            "<b>Call the clinic before you come</b>, so staff can keep other patients safe in the waiting room.",
        ]),
        ('help', "Get help now — call 997 or go to the emergency department if your child:", [
            "Has spots that do <b>not fade</b> with the glass test.",
            "Is very sleepy, hard to wake, confused, or floppy.",
            "Has a fit (seizure), a stiff neck, or fast or difficult breathing.",
            "Has cold hands and feet with a high fever, or is not passing urine.",
            "Is <b>under 3 months old</b> with a temperature of 38 °C or more.",
        ]),
        ('h', "See your doctor today if:"),
        ('ul', [
            "The fever lasts <b>5 days or more</b>, especially with red eyes, red lips or swollen hands and feet.",
            "Your child is not drinking enough, or a spot becomes very red, swollen or painful.",
            "Your child has <b>sickle cell disease</b> or weak immunity and becomes pale or tired.",
            "You live in or visited an area with <b>dengue</b> and your child has fever with body pain — do not give ibuprofen.",
        ]),
        ('plan', "My plan", [
            ("What the doctor thinks my child has", 1),
            ("Medicine and dose", 1),
            ("Back to school on", 1),
        ]),
    ],
    ar=[
        ('key', "خمس نقاط تذكّرها", [
            "معظم حالات الطفح مع الحمّى سببها فيروسات، وتتحسن من تلقاء نفسها.",
            "قم <b>باختبار الكأس</b>. إذا لم تختفِ البقع تحت الكأس، <b>فاذهب إلى الطوارئ فورًا</b>.",
            "للحمّى استخدم <b>الباراسيتامول</b>. <b>لا تعطِ الأسبرين للأطفال أبدًا</b>، ولا تعطِ الإيبوبروفين في الجديري.",
            "أبقِ طفلك في البيت و<b>بعيدًا عن الحوامل والمواليد</b> حتى يقول الطبيب إن ذلك آمن.",
            "تأكد أن طفلك أخذ <b>كل تطعيماته</b>، ومنها جرعتان من لقاح MMR (الحصبة والنكاف والحصبة الألمانية).",
        ]),
        ('h', "اختبار الكأس"),
        ('p', "اضغط جانب كأس زجاجي شفاف بقوة على البقع. إذا بقيت البقع ظاهرة من خلال الكأس، "
              "فقد تكون علامة على عدوى خطيرة تسمى المكورات السحائية (التهاب السحايا). "
              "اذهب إلى الطوارئ أو اتصل بـ 997 فورًا. وعلى البشرة الداكنة افحص باطن الكفين والقدمين وداخل الجفنين."),
        ('h', "أشهر أنواع الطفح عند الأطفال"),
        ('table', ["المرض", "ما قد تلاحظه", "الغياب عن الحضانة أو المدرسة"], [
            ["الحصبة", "حمّى عالية، وسعال، وسيلان الأنف، واحمرار العينين، ثم طفح بقعي يبدأ من الوجه وينزل", "4 أيام من بداية الطفح"],
            ["الجديري المائي", "بقع تسبب الحكة تتحول إلى فقاعات ثم قشور", "حتى تتقشّر كل البقع (نحو 5 أيام)"],
            ["الحمّى القرمزية", "التهاب الحلق، وطفح أحمر خشن كورق الصنفرة، ولسان أحمر", "24 ساعة بعد بدء المضاد الحيوي"],
            ["القوباء", "قروح عليها قشور صفراء بنية، غالبًا حول الأنف والفم", "حتى تتقشّر، أو يومين بعد بدء المضاد الحيوي"],
            ["الخد المصفوع (المرض الخامس)", "خدّان أحمران زاهيان، ثم طفح شبكي على الذراعين والساقين", "لا داعي بعد ظهور الطفح"],
            ["الوردية", "حمّى عالية 3–5 أيام، ثم طفح وردي مع زوال الحمّى", "لا داعي بعد التعافي"],
            ["مرض اليد والقدم والفم", "قرح في الفم وفقاعات صغيرة على اليدين والقدمين", "لا داعي إن كان بحال جيدة"],
        ]),
        ('break',),
        ('h', "رعاية طفلك في البيت"),
        ('ul', [
            "أعطِه <b>رشفات صغيرة كثيرًا</b> — ماء أو حليب أو حليب الأم. والمشروبات الباردة تريح الفم المتقرح.",
            "استخدم <b>الباراسيتامول</b> إذا كان طفلك متضايقًا، واتبع الجرعة المكتوبة على العلبة حسب عمره أو وزنه.",
            "ألبس طفلك ملابس خفيفة. وللبقع المسببة للحكة استخدم غسول الكالامين، وأبقِ الأظافر قصيرة.",
            "اغسل اليدين كثيرًا واجعل لطفلك منشفة خاصة. وأكمل المضاد الحيوي كاملًا إذا وصفه الطبيب.",
        ]),
        ('tip', "احمِ الآخرين", [
            "على <b>الحامل</b> التي كانت قريبة من طفلك الاتصال بطبيبها اليوم؛ فبعض أنواع الطفح قد تضر الجنين.",
            "أبعِد طفلك عن <b>المواليد</b> وعن كل من لديه <b>مناعة ضعيفة</b> (مثل من يتلقى علاج السرطان أو الكورتيزون).",
            "<b>اتصل بالعيادة قبل الحضور</b> ليحمي العاملون المرضى الآخرين في غرفة الانتظار.",
        ]),
        ('help', "اطلب المساعدة فورًا: اتصل بـ 997 أو اذهب إلى الطوارئ إذا كان طفلك:", [
            "لديه بقع <b>لا تختفي</b> باختبار الكأس.",
            "نعسانًا جدًا، أو يصعب إيقاظه، أو مشوّشًا، أو مرتخي الجسم.",
            "أصابته نوبة تشنج، أو تيبّس في الرقبة، أو يتنفس بسرعة أو بصعوبة.",
            "يداه وقدماه باردتان مع حمّى عالية، أو لا يتبول.",
            "<b>عمره أقل من 3 أشهر</b> وحرارته 38 °م أو أكثر.",
        ]),
        ('h', "راجع طبيبك اليوم إذا:"),
        ('ul', [
            "استمرت الحمّى <b>5 أيام أو أكثر</b>، خاصة مع احمرار العينين أو الشفتين أو تورّم اليدين والقدمين.",
            "لم يشرب طفلك ما يكفي، أو صارت إحدى البقع شديدة الاحمرار أو متورمة أو مؤلمة.",
            "كان طفلك مصابًا <b>بفقر الدم المنجلي</b> أو ضعف المناعة وأصبح شاحبًا أو متعبًا.",
            "تسكن في منطقة فيها <b>حمّى الضنك</b> أو زرتها، ولدى طفلك حمّى مع آلام في الجسم — ولا تعطِه الإيبوبروفين.",
        ]),
        ('plan', "خطتي", [
            ("ما يرى الطبيب أن طفلي مصاب به", 1),
            ("الدواء والجرعة", 1),
            ("موعد العودة إلى المدرسة", 1),
        ]),
    ],
)
