"""Home monitoring records — 2-page guide + 2-page record the patient fills in
and brings to every visit. English and Arabic. Western digits throughout.

Extra block types (see build_leaflets.render_blocks):
  ('break', 'record')          start of the record pages (also printed alone as a refill)
  ('strip', title, label)      slim coloured page header for record pages
  ('fields', [(label,), (label, 'wide')])
  ('hint', text)
  ('grid', title, header, rows, {widths, h, eg})
  ('clinic', title, [labels])  "For the clinic" box
  ('tiers', [(now|today|visit, title, [items])])
  ('lines', title, n)
"""

# =========================================================================== BLOOD PRESSURE
BP = dict(
    slug="home-blood-pressure",
    tone="#1F5C55", tone_soft="#E8F0EE",
    topic_en="Blood pressure", topic_ar="ضغط الدم",
    guide="categories.html#cat-cardio",
    record=True,
    title_en="Checking your blood pressure at home",
    title_ar="قياس ضغط الدم في المنزل",
    sub_en="How to measure, how to write it down, and when to get help — with a record to bring to every visit",
    sub_ar="كيف تقيس، وكيف تسجّل، ومتى تطلب المساعدة — مع سجل تُحضره في كل زيارة",
    card_en="How to measure and record, when a reading is urgent, and a 2-page record to fill in and bring to every visit.",
    card_ar="طريقة القياس والتسجيل، ومتى تكون القراءة طارئة، وسجل من صفحتين تملؤه وتُحضره في كل زيارة.",
    sources=[
        "Jones DW, et al. 2025 AHA/ACC/multisociety guideline for the prevention, detection, evaluation and management of high blood pressure in adults. Circulation / Hypertension 2025",
        "Mancia G, et al. 2023 ESH guidelines for the management of arterial hypertension. J Hypertens 2023;41:1874–2071",
        "Stergiou GS, et al. 2021 European Society of Hypertension practice guidelines for office and out-of-office blood pressure measurement. J Hypertens 2021;39:1293–302",
        "NICE NG136. Hypertension in adults: diagnosis and management (updated 2023)",
        "STRIDE BP. International list of validated blood pressure monitors (stridebp.org)",
    ],
    en=[
        ('key', "The 5 things to remember", [
            "Use a validated <b>upper-arm cuff</b> — not a wrist device or smartwatch.",
            "<b>Sit quietly for 5 minutes</b>, then take <b>2 readings, 1 minute apart</b>.",
            "Before each visit, measure <b>morning and evening for 7 days</b>.",
            "Write down <b>every</b> reading, high or low. Bring this record, your device and your medicines to every visit.",
            "<b>180/120 or higher</b> with chest pain, weakness or trouble speaking — <b>call 997</b>.",
        ]),
        ('h', "Why check at home?"),
        ('p', "Blood pressure is often higher at the clinic than at home. Home readings show your usual blood pressure "
              "and help your doctor decide on your treatment."),
        ('h', "Which device should I use?"),
        ('ul', [
            "An automatic <b>upper-arm</b> monitor that is <b>validated</b> — ask your doctor or pharmacist, or check the STRIDE BP list.",
            "The cuff must fit your arm. A large arm needs a large cuff.",
            "Wrist monitors and smartwatches are not accurate enough yet.",
        ]),
        ('h', "How do I measure correctly?"),
        ('table', ["Before", "During"], [
            ["No coffee, tea, smoking, shisha or exercise for 30 minutes.", "Sit with your back supported and both feet flat on the floor."],
            ["Empty your bladder.", "Do not cross your legs."],
            ["Sit quietly for 5 minutes.", "Rest your arm on a table at the level of your heart."],
            ["In the morning: measure before your medicines and before breakfast.", "Cuff on bare skin, just above the elbow. Do not talk."],
        ]),
        ('p', "Use the same arm each time — the one your doctor tells you. If the monitor shows a heart symbol for an "
              "irregular heartbeat, write <b>IHB</b> in the notes."),
        ('break',),
        ('h', "When should I measure?"),
        ('table', ["When", "How often"], [
            ["The 7 days before each visit", "Every day: <b>2 readings in the morning</b> and <b>2 in the evening</b>."],
            ["After a change in your blood pressure medicine", "The same 7-day plan, when your doctor tells you."],
            ["When your blood pressure is under control", "1–2 days a week, or the 7 days before each visit — as your doctor advises."],
            ["When you feel unwell (dizzy, headache)", "Measure, write it down with how you feel, and follow the box below."],
        ]),
        ('h', "How do I write it down?"),
        ('ul', [
            "Write the date and <b>every</b> reading exactly as shown, high or low, as top/bottom — for example <b>128/82</b>. Do not round.",
            "Use the notes to say if you missed a medicine, felt unwell, or the monitor showed IHB.",
            "Do not change your medicines because of one reading. Bring the record — and your monitor or app — to your visit.",
        ]),
        ('h', "What do my numbers mean?"),
        ('p', "For most adults the target is <b>below 130/80</b>. Some people need a lower target and some older adults a higher one — your doctor will write yours on the record."),
        ('tiers', [
            ('now', "Call 997 or go to the emergency department", [
                "<b>180/120 or higher</b> with chest pain, shortness of breath, weakness or numbness, trouble speaking, "
                "confusion, sudden change in vision, or a sudden severe headache.",
                "You faint.",
            ]),
            ('today', "Contact your clinic today (or call 937)", [
                "<b>180/120 or higher</b> again after resting 5 minutes, and you feel well.",
                "Top number <b>below 90</b>, or you feel dizzy or faint when you stand up.",
            ]),
            ('visit', "Bring to your next visit", [
                "Most readings above your target.",
                "Side effects of your medicines, or questions.",
            ]),
        ]),
        ('break', 'record'),
        ('strip', "My blood pressure record", "Bring to every visit"),
        ('fields', [("Name",), ("File number",), ("Arm used (right / left)",), ("Cuff size",),
                    ("My target (written by my doctor)", 'wide'), ("My blood pressure medicines and times", 'wide')]),
        ('hint', "Write each reading as top/bottom (for example 128/82). Morning: before medicines and breakfast. Evening: before dinner."),
        ('grid', "The 7 days before my visit", ["Day", "Date", "Morning 1", "Morning 2", "Evening 1", "Evening 2", "Notes"],
         ['1', '2', '3', '4', '5', '6', '7'],
         {'widths': [7, 11, 14, 14, 14, 14, 26], 'h': 19, 'eg': ["e.g.", "15/10", "136/86", "132/84", "128/80", "126/80", "missed evening tablet"]}),
        ('clinic', "For the clinic", ["Average of days 2–7", "Number of readings", "Reviewed by / date"]),
        ('break',),
        ('strip', "Between visits", "Bring to every visit"),
        ('hint', "Use this page for readings on other days — when your doctor asks, when you feel unwell, or after a medicine change."),
        ('grid', "", ["Date", "Time", "Reading", "Pulse", "Medicines taken today? (✓ / ✗)", "How I felt / notes"],
         14, {'widths': [12, 10, 15, 10, 15, 38], 'h': 12.4}),
        ('lines', "Questions for my next visit", 3),
    ],
    ar=[
        ('key', "خمس نقاط تذكّرها", [
            "استخدم جهازًا معتمدًا علميًا <b>بكُمّ على أعلى الذراع</b>، لا جهاز معصم ولا ساعة ذكية.",
            "<b>اجلس بهدوء 5 دقائق</b>، ثم خذ <b>قراءتين بينهما دقيقة</b>.",
            "قبل كل زيارة، قِس <b>صباحًا ومساءً مدة 7 أيام</b>.",
            "سجّل <b>كل</b> قراءة، مرتفعة كانت أو منخفضة، وأحضر هذا السجل وجهازك وأدويتك في كل زيارة.",
            "إذا كانت القراءة <b>180/120 أو أكثر</b> مع ألم في الصدر أو ضعف أو صعوبة في الكلام، <b>فاتصل بـ 997</b>.",
        ]),
        ('h', "لماذا أقيس الضغط في المنزل؟"),
        ('p', "غالبًا ما يكون الضغط في العيادة أعلى منه في المنزل. تُظهر قراءات المنزل ضغطك المعتاد، "
              "وتساعد طبيبك على اتخاذ قرار العلاج."),
        ('h', "أي جهاز أستخدم؟"),
        ('ul', [
            "جهاز آلي يوضع على <b>أعلى الذراع</b>، <b>معتمد علميًا</b>؛ اسأل طبيبك أو الصيدلي، أو راجع قائمة STRIDE BP.",
            "يجب أن يناسب الكُمّ ذراعك؛ فالذراع الكبيرة تحتاج إلى كُمّ كبير.",
            "أجهزة المعصم والساعات الذكية ليست دقيقة بما يكفي حتى الآن.",
        ]),
        ('h', "كيف أقيس بطريقة صحيحة؟"),
        ('table', ["قبل القياس", "أثناء القياس"], [
            ["لا قهوة ولا شاي ولا تدخين ولا شيشة ولا رياضة قبل القياس بـ 30 دقيقة.", "اجلس وظهرك مسنود وقدماك على الأرض."],
            ["أفرغ المثانة.", "لا تضع ساقًا على ساق."],
            ["اجلس بهدوء 5 دقائق.", "ضع ذراعك على طاولة بمستوى القلب."],
            ["في الصباح: قِس قبل الأدوية وقبل الإفطار.", "ضع الكُمّ على الجلد مباشرة فوق المرفق، ولا تتكلم."],
        ]),
        ('p', "استخدم الذراع نفسها في كل مرة، وهي التي يحددها طبيبك. وإذا ظهرت على الجهاز علامة قلب تشير إلى "
              "عدم انتظام النبض، فاكتب <b>IHB</b> في الملاحظات."),
        ('break',),
        ('h', "متى أقيس؟"),
        ('table', ["متى؟", "كم مرة؟"], [
            ["الأيام السبعة التي تسبق كل زيارة", "كل يوم: <b>قراءتان صباحًا</b> و<b>قراءتان مساءً</b>."],
            ["بعد تغيير دواء الضغط", "الخطة نفسها لمدة 7 أيام، عندما يطلب طبيبك."],
            ["عندما يكون الضغط منضبطًا", "يوم أو يومان في الأسبوع، أو الأيام السبعة قبل كل زيارة، حسب نصيحة طبيبك."],
            ["عندما تشعر بتعب (دوخة أو صداع)", "قِس، وسجّل القراءة مع ما تشعر به، واتبع الإرشادات أدناه."],
        ]),
        ('h', "كيف أسجّل القراءات؟"),
        ('ul', [
            "اكتب التاريخ و<b>كل</b> قراءة كما تظهر تمامًا، مرتفعة أو منخفضة، بصيغة الأعلى/الأدنى مثل <b>128/82</b>، ولا تقرّب الأرقام.",
            "اكتب في الملاحظات إذا نسيت دواءً، أو شعرت بتعب، أو ظهرت علامة IHB.",
            "لا تغيّر أدويتك بسبب قراءة واحدة، وأحضر السجل (وجهازك أو تطبيقه) في زيارتك.",
        ]),
        ('h', "ماذا تعني قراءاتي؟"),
        ('p', "الهدف لمعظم البالغين <b>أقل من 130/80</b>، وقد يحتاج بعض الناس إلى هدف أقل وبعض كبار السن إلى هدف أعلى، وسيكتب طبيبك هدفك في السجل."),
        ('tiers', [
            ('now', "اتصل بـ 997 أو اذهب إلى الطوارئ", [
                "<b>180/120 أو أكثر</b> مع ألم في الصدر، أو ضيق في النفس، أو ضعف أو خدر، أو صعوبة في الكلام، "
                "أو تشوّش، أو تغيّر مفاجئ في النظر، أو صداع شديد مفاجئ.",
                "إذا أُغمي عليك.",
            ]),
            ('today', "تواصل مع عيادتك اليوم (أو اتصل بـ 937)", [
                "<b>180/120 أو أكثر</b> مرة أخرى بعد الراحة 5 دقائق، وأنت تشعر بأنك بخير.",
                "الرقم الأعلى <b>أقل من 90</b>، أو تشعر بدوخة أو بأنك ستفقد الوعي عند الوقوف.",
            ]),
            ('visit', "أحضره في زيارتك القادمة", [
                "معظم القراءات أعلى من هدفك.",
                "أعراض جانبية للأدوية، أو أسئلة لديك.",
            ]),
        ]),
        ('break', 'record'),
        ('strip', "سجل ضغط الدم", "أحضره في كل زيارة"),
        ('fields', [("الاسم",), ("رقم الملف",), ("الذراع المستخدمة (يمين / يسار)",), ("مقاس الكُمّ",),
                    ("هدفي (يكتبه الطبيب)", 'wide'), ("أدوية الضغط وأوقاتها", 'wide')]),
        ('hint', "اكتب كل قراءة بصيغة الأعلى/الأدنى (مثل 128/82). الصباح: قبل الأدوية والإفطار. المساء: قبل العشاء."),
        ('grid', "الأيام السبعة قبل زيارتي", ["اليوم", "التاريخ", "صباحًا 1", "صباحًا 2", "مساءً 1", "مساءً 2", "ملاحظات"],
         ['1', '2', '3', '4', '5', '6', '7'],
         {'widths': [7, 11, 14, 14, 14, 14, 26], 'h': 19, 'eg': ["مثال", "15/10", "136/86", "132/84", "128/80", "126/80", "نسيت حبة المساء"]}),
        ('clinic', "للعيادة", ["متوسط الأيام 2 إلى 7", "عدد القراءات", "راجعه / التاريخ"]),
        ('break',),
        ('strip', "بين الزيارات", "أحضره في كل زيارة"),
        ('hint', "استخدم هذه الصفحة للقراءات في الأيام الأخرى: عندما يطلب طبيبك، أو عندما تشعر بتعب، أو بعد تغيير دواء."),
        ('grid', "", ["التاريخ", "الوقت", "القراءة", "النبض", "أخذت أدويتي اليوم؟ (✓ / ✗)", "ماذا شعرت / ملاحظات"],
         14, {'widths': [12, 10, 15, 10, 15, 38], 'h': 12.4}),
        ('lines', "أسئلة لزيارتي القادمة", 3),
    ],
)

# =========================================================================== BLOOD GLUCOSE
GLUCOSE = dict(
    slug="home-blood-glucose",
    tone="#4A6B8A", tone_soft="#EDF2F7",
    topic_en="Diabetes", topic_ar="السكري",
    guide="categories.html#cat-endo",
    record=True,
    title_en="Checking your blood sugar at home",
    title_ar="قياس السكر في المنزل",
    sub_en="How to check, how to write it down, and when to get help — with a record to bring to every visit",
    sub_ar="كيف تقيس، وكيف تسجّل، ومتى تطلب المساعدة — مع سجل تُحضره في كل زيارة",
    card_en="How and when to check, targets, low sugar and sick days, when to go to the emergency department, and a 2-page record.",
    card_ar="كيف ومتى تقيس، والأهداف، وهبوط السكر وأيام المرض، ومتى تذهب إلى الطوارئ، وسجل من صفحتين.",
    sources=[
        "American Diabetes Association. Standards of Care in Diabetes — 2026, Sections 6 (glycemic goals, hypoglycemia, hyperglycemic crises, intercurrent illness) and 7 (diabetes technology). Diabetes Care 2026;49(Suppl 1); Summary of Revisions doi:10.2337/dc26-SREV",
        "Saudi Ministry of Health. Diabetes and being sick — health awareness (moh.gov.sa)",
        "Joint British Diabetes Societies. Sick day rules and SGLT2 inhibitor patient guidance (2025)",
        "IDF-DAR Practical Guidelines: Diabetes and Ramadan, 2021; 2026 risk calculator update",
    ],
    en=[
        ('key', "The 5 things to remember", [
            "<b>Wash and dry your hands</b> before every check.",
            "Write down <b>every</b> reading with the time, and whether it was before or after a meal.",
            "<b>Below 70</b>: take 15 g of fast sugar, then check again after 15 minutes.",
            "When sick: check <b>every 4 hours</b>, keep drinking, and <b>never stop insulin</b>.",
            "Bring this record, your meter and your medicines to <b>every visit</b>.",
        ]),
        ('h', "When should I check?"),
        ('table', ["My treatment", "Usual checks — your doctor may change this"], [
            ["Insulin with meals (several injections a day)", "Before meals and at bedtime; sometimes 2 hours after meals."],
            ["Long-acting insulin once a day, or gliclazide or glimepiride", "Before breakfast every day, and whenever you feel low or unwell."],
            ["Other tablets or weekly injections only", "As your doctor advises — often a few times a week."],
            ["Any treatment", "When you feel shaky, sweaty or confused; more often when sick or fasting (see the Ramadan leaflet). Before driving if you use insulin, gliclazide or glimepiride."],
        ], [42, 58]),
        ('h', "How do I check?"),
        ('ul', [
            "Wash your hands with soap and water and dry them — sugar on your fingers gives a false high.",
            "Use the side of a fingertip, and change fingers each time.",
            "Use strips that are in date. Use a new lancet each time, never share it, and put used lancets in a hard plastic bottle.",
            "Using a sensor (CGM)? Bring the app report, and keep your meter to check when a reading does not match how you feel.",
        ]),
        ('h', "What are my targets?"),
        ('table', ["When", "Usual target for many adults", "My target (set by my doctor)"], [
            ["Before meals", "80–130 mg/dL (4.4–7.2 mmol/L)", ""],
            ["1–2 hours after starting a meal", "Below 180 mg/dL (10.0 mmol/L)", ""],
        ], [28, 46, 26]),
        ('p', "Older adults and people prone to lows often have higher targets."),
        ('break',),
        ('h', "Low sugar: below 70 mg/dL"),
        ('ul', [
            "Signs: shaking, sweating, hunger, fast heartbeat, confusion. Some people feel nothing — check if unsure.",
            "Take <b>15 g of fast sugar</b>: 3 teaspoons of sugar in water, half a cup (120 ml) of regular juice, or glucose tablets. Always carry some with you.",
            "Check again after <b>15 minutes</b>. If still below 70, repeat. When it is above 70, eat a snack or your meal.",
            "Write every low on page 4, and tell your doctor.",
        ]),
        ('h', "Sick days"),
        ('ul', [
            "Check your sugar <b>every 4 hours</b>, day and night.",
            "Drink a glass of water or a sugar-free drink every hour.",
            "<b>Never stop insulin</b> — you may need more.",
            "Some tablets may need a pause while you cannot eat or drink, such as metformin, dapagliflozin or empagliflozin, "
            "and some blood pressure or water tablets. Only do this if your doctor has given you a sick-day plan.",
            "Type 1 diabetes, or sugar above 300: check ketones if you have strips.",
        ]),
        ('tiers', [
            ('now', "Call 997 or go to the emergency department", [
                "Low sugar that does not improve after 2 treatments, or the person is confused, very drowsy or fitting. "
                "Do not give food or drink to someone who cannot swallow.",
                "Vomiting, and you cannot keep fluids down.",
                "Sugar above 300 with tummy pain, vomiting, fast deep breathing or drowsiness — or medium or high ketones.",
                "On dapagliflozin or empagliflozin with vomiting, tummy pain or fast breathing — <b>even if your sugar is normal</b>.",
            ]),
            ('today', "Contact your clinic today (or call 937)", [
                "Sugar stays above 250, or before-meal readings stay above 240 for more than a day.",
                "Fever or illness for 2 days, or vomiting or diarrhoea for more than 6 hours.",
                "A low below 54, a low that needed someone's help, or 2 or more lows in a week.",
            ]),
            ('visit', "Bring to your next visit", [
                "Most readings above your target.",
                "Questions about your medicines, food, activity, or whether a sensor (CGM) could help you.",
            ]),
        ]),
        ('break', 'record'),
        ('strip', "My blood sugar record", "Bring to every visit"),
        ('fields', [("Name",), ("File number",), ("Type of diabetes",), ("My meter",),
                    ("My medicines and insulin doses", 'wide'), ("My targets (written by my doctor)", 'wide')]),
        ('hint', "Write readings in mg/dL. <b>Circle</b> any reading below 70. Write insulin doses or changes in the notes."),
        ('grid', "", ["Date", "Before breakfast", "After breakfast", "Before lunch", "After lunch", "Before dinner", "After dinner", "Bedtime", "Notes / insulin"],
         14, {'widths': [9, 10, 10, 10, 10, 10, 10, 10, 21], 'h': 11, 'eg': ["15/10", "118", "", "", "", "142", "", "126", "lunch out"]}),
        ('clinic', "For the clinic", ["Readings below 70 / below 54", "Average before breakfast", "Reviewed by / date"]),
        ('break',),
        ('strip', "Low sugar and sick days", "Bring to every visit"),
        ('grid', "Low sugar record (below 70)", ["Date and time", "Reading", "What happened / how I felt", "What I took", "Reading after 15 min", "Needed help? (yes / no)"],
         6, {'widths': [15, 10, 29, 18, 13, 15], 'h': 13.4}),
        ('grid', "Sick-day record", ["Date and time", "Sugar", "Ketones", "Drinks in the last 4 hours", "Medicines and insulin taken", "Notes"],
         6, {'widths': [15, 10, 11, 18, 23, 23], 'h': 13.4}),
        ('lines', "Questions for my next visit", 3),
    ],
    ar=[
        ('key', "خمس نقاط تذكّرها", [
            "<b>اغسل يديك وجفّفهما</b> قبل كل قياس.",
            "سجّل <b>كل</b> قراءة مع الوقت، وهل كانت قبل الأكل أم بعده.",
            "<b>أقل من 70</b>: خذ 15 غرامًا من سكر سريع، ثم أعد القياس بعد 15 دقيقة.",
            "عند المرض: قِس <b>كل 4 ساعات</b>، واستمر في الشرب، و<b>لا توقف الإنسولين أبدًا</b>.",
            "أحضر هذا السجل وجهازك وأدويتك في <b>كل زيارة</b>.",
        ]),
        ('h', "متى أقيس؟"),
        ('table', ["علاجي", "القياس المعتاد (قد يغيّره طبيبك)"], [
            ["إنسولين مع الوجبات (عدة حقن في اليوم)", "قبل الوجبات وعند النوم، وأحيانًا بعد الوجبات بساعتين."],
            ["إنسولين طويل المفعول مرة يوميًا، أو جليكلازايد أو جليميبرايد", "قبل الإفطار كل يوم، وكلما شعرت بهبوط أو تعب."],
            ["حبوب أخرى أو حقن أسبوعية فقط", "حسب نصيحة طبيبك، وغالبًا بضع مرات في الأسبوع."],
            ["أي علاج", "عند الرجفة أو التعرّق أو التشوّش، وأكثر عند المرض أو الصيام (انظر نشرة رمضان)، وقبل القيادة لمن يستخدم الإنسولين أو جليكلازايد أو جليميبرايد."],
        ], [42, 58]),
        ('h', "كيف أقيس؟"),
        ('ul', [
            "اغسل يديك بالماء والصابون وجفّفهما جيدًا؛ فالسكر على الأصابع يعطي قراءة مرتفعة غير صحيحة.",
            "استخدم جانب طرف الإصبع، وغيّر الإصبع في كل مرة.",
            "استخدم شرائط صالحة، وإبرة وخز جديدة في كل مرة لا تشاركها أحدًا، وضع الإبر المستعملة في علبة بلاستيكية صلبة.",
            "إذا كنت تستخدم حسّاسًا (قياس مستمر)، فأحضر تقرير التطبيق، واحتفظ بجهاز الوخز للتأكد عندما لا تتوافق القراءة مع ما تشعر به.",
        ]),
        ('h', "ما أهدافي؟"),
        ('table', ["متى؟", "الهدف المعتاد لكثير من البالغين", "هدفي (يحدده طبيبي)"], [
            ["قبل الوجبات", "80 إلى 130 ملغ/دسل (4.4 إلى 7.2 ملمول/لتر)", ""],
            ["بعد بدء الوجبة بساعة إلى ساعتين", "أقل من 180 ملغ/دسل (10.0 ملمول/لتر)", ""],
        ], [28, 46, 26]),
        ('p', "كبار السن ومن يتعرّضون للهبوط تكون أهدافهم غالبًا أعلى."),
        ('break',),
        ('h', "هبوط السكر: أقل من 70 ملغ/دسل"),
        ('ul', [
            "العلامات: رجفة، تعرّق، جوع، تسارع في ضربات القلب، تشوّش. وبعض الناس لا يشعرون بشيء، فقِس إذا لم تكن متأكدًا.",
            "خذ <b>15 غرامًا من سكر سريع</b>: 3 ملاعق صغيرة من السكر مذابة في الماء، أو نصف كوب (120 مل) من العصير العادي، أو أقراص الجلوكوز، واحملها معك دائمًا.",
            "أعد القياس بعد <b>15 دقيقة</b>، وإذا بقي أقل من 70 فكرّر. وعندما يرتفع فوق 70، تناول وجبة خفيفة أو وجبتك.",
            "سجّل كل هبوط في الصفحة 4، وأخبر طبيبك.",
        ]),
        ('h', "أيام المرض"),
        ('ul', [
            "قِس السكر <b>كل 4 ساعات</b> ليلًا ونهارًا.",
            "اشرب كوبًا من الماء أو مشروبًا خاليًا من السكر كل ساعة.",
            "<b>لا توقف الإنسولين أبدًا</b>؛ فقد تحتاج إلى جرعة أكبر.",
            "بعض الحبوب قد تحتاج إلى إيقاف مؤقت ما دمت لا تستطيع الأكل أو الشرب، مثل ميتفورمين وداباغليفلوزين وإمباغليفلوزين "
            "وبعض أدوية الضغط ومدرّات البول. لا تفعل ذلك إلا إذا أعطاك طبيبك خطة لأيام المرض.",
            "السكري من النوع الأول، أو السكر أعلى من 300: افحص الكيتونات إذا كانت لديك شرائطها.",
        ]),
        ('tiers', [
            ('now', "اتصل بـ 997 أو اذهب إلى الطوارئ", [
                "هبوط لا يتحسن بعد علاجه مرتين، أو أصبح الشخص مشوّشًا أو نعسانًا جدًا أو يتشنّج. "
                "لا تعطِ طعامًا أو شرابًا لمن لا يستطيع البلع.",
                "قيء مع عدم القدرة على شرب السوائل.",
                "سكر أعلى من 300 مع ألم في البطن أو قيء أو تنفّس سريع وعميق أو نعاس، أو كيتونات متوسطة أو عالية.",
                "إذا كنت تأخذ داباغليفلوزين أو إمباغليفلوزين وأصابك قيء أو ألم في البطن أو تنفّس سريع، <b>حتى لو كان السكر طبيعيًا</b>.",
            ]),
            ('today', "تواصل مع عيادتك اليوم (أو اتصل بـ 937)", [
                "بقي السكر أعلى من 250، أو بقيت قراءات ما قبل الأكل أعلى من 240 أكثر من يوم.",
                "حمّى أو مرض لمدة يومين، أو قيء أو إسهال لأكثر من 6 ساعات.",
                "هبوط أقل من 54، أو هبوط احتجت فيه إلى مساعدة غيرك، أو هبوطان أو أكثر في الأسبوع.",
            ]),
            ('visit', "أحضره في زيارتك القادمة", [
                "معظم القراءات أعلى من هدفك.",
                "أسئلة عن أدويتك أو طعامك أو نشاطك، أو هل يناسبك جهاز قياس مستمر (حسّاس).",
            ]),
        ]),
        ('break', 'record'),
        ('strip', "سجل السكر", "أحضره في كل زيارة"),
        ('fields', [("الاسم",), ("رقم الملف",), ("نوع السكري",), ("جهاز القياس",),
                    ("أدويتي وجرعات الإنسولين", 'wide'), ("أهدافي (يكتبها الطبيب)", 'wide')]),
        ('hint', "اكتب القراءات بوحدة ملغ/دسل. <b>ضع دائرة</b> حول أي قراءة أقل من 70. واكتب جرعات الإنسولين أو تغييراتها في الملاحظات."),
        ('grid', "", ["التاريخ", "قبل الإفطار", "بعد الإفطار", "قبل الغداء", "بعد الغداء", "قبل العشاء", "بعد العشاء", "عند النوم", "ملاحظات / إنسولين"],
         14, {'widths': [9, 10, 10, 10, 10, 10, 10, 10, 21], 'h': 11, 'eg': ["15/10", "118", "", "", "", "142", "", "126", "غداء خارج المنزل"]}),
        ('clinic', "للعيادة", ["القراءات أقل من 70 / أقل من 54", "متوسط ما قبل الإفطار", "راجعه / التاريخ"]),
        ('break',),
        ('strip', "الهبوط وأيام المرض", "أحضره في كل زيارة"),
        ('grid', "سجل هبوط السكر (أقل من 70)", ["التاريخ والوقت", "القراءة", "ماذا حدث / بماذا شعرت", "ماذا أخذت", "القراءة بعد 15 دقيقة", "احتجت مساعدة؟ (نعم / لا)"],
         6, {'widths': [15, 10, 29, 18, 13, 15], 'h': 13.4}),
        ('grid', "سجل أيام المرض", ["التاريخ والوقت", "السكر", "الكيتونات", "ما شربته في آخر 4 ساعات", "الأدوية والإنسولين", "ملاحظات"],
         6, {'widths': [15, 10, 11, 18, 23, 23], 'h': 13.4}),
        ('lines', "أسئلة لزيارتي القادمة", 3),
    ],
)
