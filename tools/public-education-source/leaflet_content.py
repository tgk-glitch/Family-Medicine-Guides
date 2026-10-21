"""Patient leaflet content — three pilots, English and Arabic.

Each leaflet is a list of blocks. Block types:
  ('key', title, [items])          key-messages box at the top
  ('h', text)                      section heading (phrased as a question)
  ('p', text)
  ('ul', [items])
  ('table', [header], [[row], ...])
  ('help', title, [items])         red "get help" box
  ('tip', title, [items])          amber Saudi-context box
  ('plan', title, [(label, lines)])  fill-in box
  ('log', title, [header], nrows)  empty table to fill in
  ('break',)                        start page 2

Inline <b> is allowed. Keep sentences short: English target ≤ grade 8;
Arabic in simple MSA. Western digits throughout so numbers match the
patient's meter or cuff display.
"""

REVIEWED = {"en": "October 2026", "ar": "أكتوبر 2026"}
NEXT_REVIEW = {"en": "October 2027, or sooner if guidance changes",
               "ar": "أكتوبر 2027، أو قبل ذلك إذا تغيّرت التوصيات"}

LEAFLETS = []

# ===================================================================== IRON
LEAFLETS.append(dict(
    slug="iron-deficiency",
    tone="#8A3A4A", tone_soft="#F7ECEE",
    topic_en="Haematology", topic_ar="أمراض الدم",
    guide="categories.html#cat-heme",
    title_en="Low iron and anaemia",
    title_ar="نقص الحديد وفقر الدم",
    sub_en="How to take your iron tablets so they work — and when to get help",
    sub_ar="كيف تأخذ حبوب الحديد لتستفيد منها، ومتى تطلب المساعدة",
    card_en="Taking iron tablets well, iron-rich food, how long treatment lasts, and warning signs.",
    card_ar="طريقة أخذ حبوب الحديد، الأطعمة الغنية بالحديد، مدة العلاج، وعلامات الخطر.",
    sources=[
        "American Society of Hematology 2026 guideline on the diagnosis of iron deficiency. Blood Adv 2026. doi:10.1182/bloodadvances.2025015950",
        "Snook J, et al. British Society of Gastroenterology guidelines for the management of iron deficiency anaemia in adults. Gut 2021;70:2030–51",
        "DeLoughery TG, et al. AGA Clinical Practice Update on management of iron deficiency anemia. Clin Gastroenterol Hepatol 2024",
        "Iolascon A, et al. Recommendations for diagnosis, treatment and prevention of iron deficiency and iron deficiency anemia. HemaSphere 2024 (EHA)",
    ],
    en=[
        ('key', "The 5 things to remember", [
            "Iron tablets work best on an <b>empty stomach</b> with water or orange juice.",
            "Keep <b>tea, coffee, milk and antacids</b> at least 2 hours away from your iron.",
            "Black or dark green stool is <b>normal</b> on iron.",
            "Keep taking iron for about <b>3 months after</b> your blood count is normal.",
            "Keep iron tablets <b>away from children</b> — an overdose is dangerous.",
        ]),
        ('h', "What is iron deficiency anaemia?"),
        ('p', "Your body uses iron to make haemoglobin, the part of the blood that carries oxygen. "
              "When iron runs low, you make less haemoglobin. This is called anaemia."),
        ('p', "You may feel tired, short of breath, dizzy, or cold. Some people get headaches, hair fall, "
              "brittle nails, or a craving to chew ice. Some people feel nothing at all."),
        ('h', "Why does it happen?"),
        ('ul2', [
            "Heavy or long periods.",
            "Pregnancy and breastfeeding.",
            "Not enough iron in food.",
            "Slow blood loss from the stomach or bowel.",
            "Problems absorbing iron, such as coeliac disease.",
        ]),
        ('p', "Your doctor will look for the cause, not just treat the low number."),
        ('tip', "Before you start iron", [
            "In Saudi Arabia, <b>thalassaemia trait</b> is common. It can look like low iron on a blood count.",
            "Only take iron if a blood test (ferritin) shows your iron is low.",
            "If you had premarital screening, tell your doctor the result.",
        ]),
        ('h', "How do I take my iron tablets?"),
        ('ul', [
            "Take them as your doctor prescribed — <b>once a day or every other day</b>. Every other day works well for many people and is often easier on the stomach.",
            "Take them <b>1 hour before a meal</b>, with water or orange juice. Vitamin C helps your body take in iron.",
            "If they upset your stomach, take them with a small meal. Taking them with food is better than stopping.",
            "Leave <b>2 hours</b> between your iron and tea, coffee (including Arabic coffee), milk, calcium tablets, or antacids.",
            "Constipation? Drink more water and eat more fibre. Tell your doctor if it continues — another type of iron may suit you better.",
        ]),
        ('break',),
        ('h', "How long will I take iron?"),
        ('ul', [
            "Your doctor will usually check your blood again after about <b>4 weeks</b>.",
            "Haemoglobin rises first. Your iron stores fill up more slowly.",
            "Keep taking iron for about <b>3 months after</b> your haemoglobin is back to normal.",
        ]),
        ('h', "Which foods have iron?"),
        ('table', ["Foods with iron the body absorbs well", "Plant foods with iron"], [
            ["Red meat, liver (avoid liver if pregnant)", "Lentils, chickpeas, beans (ful)"],
            ["Chicken, turkey", "Dark green leafy vegetables"],
            ["Fish and seafood", "Fortified breakfast cereals"],
            ["", "Dates, raisins and dried apricots (a little)"],
        ]),
        ('p', "Eat plant iron with vitamin C — lemon, orange, tomato or peppers. "
              "Food alone usually cannot fix anaemia. You still need the tablets."),
        ('help', "Get help now — call 997 or go to the emergency department if you have:", [
            "Chest pain, severe shortness of breath, or fainting.",
            "Vomiting blood.",
            "Black, sticky, tar-like stool with dizziness. (Stool from iron is dark but formed, and you feel well.)",
            "Very heavy bleeding that soaks a pad every hour.",
        ]),
        ('h', "See your doctor soon if:"),
        ('ul', [
            "You feel no better after 4 weeks.",
            "Side effects stop you taking the tablets.",
            "Your periods are still very heavy.",
            "You lose weight without trying, or your bowel habit changes.",
        ]),
        ('plan', "My plan", [
            ("My iron tablet, dose and how often", 1),
            ("My next blood test", 1),
        ]),
    ],
    ar=[
        ('key', "خمس نقاط تذكّرها", [
            "تعمل حبوب الحديد أفضل على <b>معدة فارغة</b> مع الماء أو عصير البرتقال.",
            "اترك <b>الشاي والقهوة والحليب ومضادات الحموضة</b> قبل الحديد أو بعده بساعتين على الأقل.",
            "لون البراز الأسود أو الأخضر الداكن <b>طبيعي</b> مع الحديد.",
            "استمر في الحديد نحو <b>3 أشهر بعد</b> أن يعود تحليل الدم طبيعيًا.",
            "احفظ حبوب الحديد <b>بعيدًا عن الأطفال</b>؛ فالجرعة الزائدة خطيرة.",
        ]),
        ('h', "ما فقر الدم الناتج عن نقص الحديد؟"),
        ('p', "يحتاج الجسم إلى الحديد ليصنع الهيموغلوبين، وهو الجزء الذي يحمل الأكسجين في الدم. "
              "عندما ينقص الحديد يقلّ الهيموغلوبين، وهذا ما يسمّى فقر الدم (الأنيميا)."),
        ('p', "قد تشعر بالتعب أو ضيق النفس أو الدوخة أو البرد. وقد يعاني بعض الناس من الصداع، أو تساقط الشعر، "
              "أو تكسّر الأظافر، أو الرغبة في مضغ الثلج. وبعضهم لا يشعر بشيء."),
        ('h', "لماذا يحدث؟"),
        ('ul2', [
            "دورة شهرية غزيرة أو طويلة.",
            "الحمل والرضاعة.",
            "قلة الحديد في الطعام.",
            "نزف بطيء من المعدة أو الأمعاء.",
            "ضعف امتصاص الحديد، مثل مرض حساسية القمح (السيلياك).",
        ]),
        ('p', "سيبحث طبيبك عن السبب، ولن يكتفي بعلاج الرقم المنخفض."),
        ('tip', "قبل أن تبدأ الحديد", [
            "<b>حمل صفة الثلاسيميا</b> شائع في المملكة، وقد يشبه نقص الحديد في تحليل الدم.",
            "لا تأخذ الحديد إلا إذا أظهر تحليل الدم (مخزون الحديد «الفيريتين») أنه منخفض.",
            "إذا أجريت فحص ما قبل الزواج، فأخبر طبيبك بنتيجته.",
        ]),
        ('h', "كيف آخذ حبوب الحديد؟"),
        ('ul', [
            "خذها كما وصفها طبيبك: <b>مرة يوميًا أو يومًا بعد يوم</b>. أخذها يومًا بعد يوم يناسب كثيرًا من الناس، وغالبًا ما يكون أخفّ على المعدة.",
            "خذها <b>قبل الأكل بساعة</b> مع الماء أو عصير البرتقال، ففيتامين سي يساعد الجسم على امتصاص الحديد.",
            "إذا سبّبت لك اضطرابًا في المعدة، فخذها مع وجبة خفيفة. أخذها مع الطعام أفضل من التوقف عنها.",
            "اترك <b>ساعتين</b> بين الحديد وبين الشاي، والقهوة (ومنها القهوة العربية)، والحليب، وحبوب الكالسيوم، ومضادات الحموضة.",
            "إذا أصابك الإمساك، فاشرب ماءً أكثر وتناول أليافًا أكثر. وأخبر طبيبك إذا استمر، فقد يناسبك نوع آخر من الحديد.",
        ]),
        ('break',),
        ('h', "كم مدة العلاج بالحديد؟"),
        ('ul', [
            "يعيد طبيبك تحليل الدم عادةً بعد نحو <b>4 أسابيع</b>.",
            "يرتفع الهيموغلوبين أولًا، ثم يمتلئ مخزون الحديد ببطء.",
            "استمر في الحديد نحو <b>3 أشهر بعد</b> أن يعود الهيموغلوبين إلى الطبيعي.",
        ]),
        ('h', "ما الأطعمة الغنية بالحديد؟"),
        ('table', ["أطعمة يمتص الجسم حديدها جيدًا", "أطعمة نباتية فيها حديد"], [
            ["اللحم الأحمر والكبدة (تجنّبي الكبدة أثناء الحمل)", "العدس والحمص والفول"],
            ["الدجاج والديك الرومي", "الخضار الورقية الداكنة"],
            ["السمك والمأكولات البحرية", "حبوب الإفطار المدعّمة بالحديد"],
            ["", "التمر والزبيب والمشمش المجفف (كمية قليلة)"],
        ]),
        ('p', "تناول الحديد النباتي مع الليمون أو البرتقال أو الطماطم أو الفلفل (فيتامين سي). "
              "والطعام وحده لا يكفي غالبًا، فما زلت تحتاج إلى الحبوب."),
        ('help', "اطلب المساعدة فورًا: اتصل بـ 997 أو اذهب إلى الطوارئ إذا كان لديك:", [
            "ألم في الصدر، أو ضيق شديد في النفس، أو إغماء.",
            "قيء دم.",
            "براز أسود لزج يشبه القطران مع دوخة. (براز الحديد داكن لكنه متماسك، وتشعر معه بأنك بخير.)",
            "نزف غزير جدًا يملأ الفوطة كل ساعة.",
        ]),
        ('h', "راجع طبيبك قريبًا إذا:"),
        ('ul', [
            "لم تشعر بتحسّن بعد 4 أسابيع.",
            "منعتك الأعراض الجانبية من أخذ الحبوب، أو ما زالت الدورة الشهرية غزيرة جدًا.",
            "نقص وزنك دون قصد، أو تغيّرت عادة الإخراج لديك.",
        ]),
        ('plan', "خطتي", [
            ("نوع حبوب الحديد وجرعتها وعدد مراتها", 1),
            ("موعد التحليل القادم", 1),
        ]),
    ],
))

# ===================================================================== RAMADAN + DIABETES
LEAFLETS.append(dict(
    slug="ramadan-diabetes",
    tone="#4A6B8A", tone_soft="#EDF2F7",
    topic_en="Ramadan & diabetes", topic_ar="رمضان والسكري",
    guide="categories.html#cat-endo",
    title_en="Fasting Ramadan safely with diabetes",
    title_ar="صيام رمضان بأمان مع السكري",
    sub_en="Plan with your doctor, check your sugar, and know when to break your fast",
    sub_ar="خطّط مع طبيبك، وافحص السكر، واعرف متى تفطر",
    card_en="The pre-Ramadan visit, checking sugar while fasting, when to break the fast, suhoor and iftar.",
    card_ar="زيارة ما قبل رمضان، فحص السكر أثناء الصيام، متى تفطر، والسحور والإفطار.",
    sources=[
        "IDF-DAR Practical Guidelines: Diabetes and Ramadan. International Diabetes Federation & DAR International Alliance, 2021",
        "Afandi B, et al. The 2026 update of the IDF-DAR risk calculator for fasting in people with diabetes. J Diabetes Endocr Pract 2026;9(1)",
        "American Diabetes Association. Standards of Care in Diabetes — 2026, Section 5 (Rec 5.32 and Table 5.3, pre-fasting risk assessment) and Section 6 (hypoglycemia). Diabetes Care 2026;49(Suppl 1)",
        "Johns Hopkins Aramco Healthcare. Managing diabetes during fasting in Ramadan (patient guidance)",
    ],
    en=[
        ('key', "The 5 things to remember", [
            "See your doctor <b>6–8 weeks before Ramadan</b> to plan your fast and your medicines.",
            "Checking your sugar <b>does not break the fast</b>.",
            "Break your fast at once if sugar is <b>below 70</b> or <b>above 300 mg/dL</b>, or you feel unwell.",
            "Do not skip <b>suhoor</b>. Eat it as late as you can.",
            "Never change or stop your medicines on your own.",
        ]),
        ('h', "Can I fast?"),
        ('p', "Many people with diabetes fast safely. Some people face a high risk of harm. Your doctor will work out "
              "a risk score from your sugar control, your medicines, and your health."),
        ('p', "Fasting may <b>not</b> be safe if you are pregnant and have diabetes, have had severe or frequent low sugar, "
              "have had very high sugar or diabetic ketoacidosis, or have serious kidney or heart problems."),
        ('p', "Islam allows people not to fast when fasting may harm them. You can discuss this with your doctor and "
              "with a religious scholar you trust."),
        ('h', "How do I check my sugar while fasting?"),
        ('ul', [
            "A finger-prick test or a glucose sensor <b>does not break the fast</b>.",
            "Check more often than usual — your doctor will tell you how often.",
            "Good times to check: before suhoor, mid-morning, midday, mid-afternoon, before iftar, 2 hours after iftar.",
            "Check <b>any time</b> you feel shaky, sweaty, confused, or unwell.",
        ]),
        ('table', ["Your sugar reading", "What to do"], [
            ["Below 70 mg/dL (3.9 mmol/L)", "<b>Break your fast now.</b> Treat low sugar (see below)."],
            ["Above 300 mg/dL (16.7 mmol/L)", "<b>Break your fast now.</b> Drink water and contact your doctor."],
            ["Between these values", "Continue your fast if you feel well."],
        ]),
        ('h', "How do I treat low sugar?"),
        ('ul', [
            "Take <b>15 grams of fast sugar</b>: 3 teaspoons of sugar in water, or half a cup (120 ml) of regular juice.",
            "Check again after 15 minutes. If still below 70, repeat.",
            "When it is above 70, eat a small meal or snack.",
        ]),
        ('break',),
        ('h', "What should I eat?"),
        ('table', ["Suhoor", "Iftar"], [
            ["Eat as late as you can, just before Fajr.", "Break your fast with 1–3 dates and water."],
            ["Choose slow foods: brown bread, oats, ful or beans.", "Then a balanced plate: half vegetables, some protein, a small amount of rice or bread."],
            ["Add protein: eggs, labneh, cheese or yoghurt.", "Keep fried food (sambosa) and sweets (kunafa, qatayef) small and rare."],
            ["Drink plenty of water.", "Avoid sugary drinks such as Vimto and sweet juices."],
        ]),
        ('ul', [
            "Drink water often between iftar and suhoor.",
            "Taraweeh prayers count as activity. Avoid hard exercise while fasting, especially near iftar.",
        ]),
        ('h', "What about my medicines?"),
        ('ul', [
            "Some medicines need a <b>new dose or time</b> in Ramadan — especially insulin and tablets such as gliclazide or glimepiride.",
            "Some tablets, such as dapagliflozin or empagliflozin, need extra care with fluids.",
            "If you have type 1 diabetes, <b>never stop insulin</b>.",
            "After Ramadan, go back to your usual doses as your doctor advised. Take care with Eid sweets.",
        ]),
        ('help', "Get help now — call 997 or go to the emergency department if:", [
            "Your sugar stays below 70 after two treatments, or you become confused or very drowsy.",
            "You vomit and cannot keep fluids down.",
            "High sugar comes with tummy pain, vomiting, or fast deep breathing.",
            "You have signs of dehydration: very dry mouth, dizziness when standing, very little urine.",
        ]),
        ('plan', "My Ramadan plan", [
            ("My risk level (from my doctor)", 1),
            ("Medicines at suhoor", 1),
            ("Medicines at iftar", 1),
            ("My clinic phone number", 1),
        ]),
    ],
    ar=[
        ('key', "خمس نقاط تذكّرها", [
            "راجع طبيبك <b>قبل رمضان بـ 6 إلى 8 أسابيع</b> لتخطّط لصيامك وأدويتك.",
            "فحص السكر <b>لا يفطّر</b>.",
            "أفطر فورًا إذا كان السكر <b>أقل من 70</b> أو <b>أعلى من 300</b> ملغ/دسل، أو إذا شعرت بتعب.",
            "لا تترك <b>السحور</b>، وأخّره قدر ما تستطيع.",
            "لا تغيّر أدويتك ولا توقفها من نفسك.",
        ]),
        ('h', "هل أستطيع الصيام؟"),
        ('p', "كثير من مرضى السكري يصومون بأمان، لكن بعضهم معرّض لخطر كبير. سيحسب طبيبك درجة الخطر لديك "
              "بناءً على ضبط السكر والأدوية وحالتك الصحية."),
        ('p', "قد يكون الصيام <b>غير آمن</b> إذا كنتِ حاملًا ومصابة بالسكري، أو أصابك هبوط سكر شديد أو متكرر، "
              "أو ارتفاع شديد في السكر أو حماض كيتوني، أو لديك مشكلات خطيرة في الكلى أو القلب."),
        ('p', "أباح الإسلام الفطر لمن يضرّه الصيام. ويمكنك مناقشة ذلك مع طبيبك ومع عالم دين تثق به."),
        ('h', "كيف أفحص السكر وأنا صائم؟"),
        ('ul', [
            "وخز الإصبع أو جهاز قياس السكر المستمر (الحسّاس) <b>لا يفطّر</b>.",
            "افحص أكثر من المعتاد، وسيخبرك طبيبك بعدد المرات.",
            "أوقات مناسبة للفحص: قبل السحور، وفي منتصف الصباح، والظهر، والعصر، وقبل الإفطار، وبعد الإفطار بساعتين.",
            "افحص <b>في أي وقت</b> تشعر فيه برجفة أو تعرّق أو تشوّش أو تعب.",
        ]),
        ('table', ["قراءة السكر", "ماذا أفعل؟"], [
            ["أقل من 70 ملغ/دسل (3.9 ملمول/لتر)", "<b>أفطر الآن</b> وعالج الهبوط (انظر أدناه)."],
            ["أعلى من 300 ملغ/دسل (16.7 ملمول/لتر)", "<b>أفطر الآن</b> واشرب الماء وتواصل مع طبيبك."],
            ["بين هاتين القيمتين", "أكمل صيامك إذا كنت تشعر بأنك بخير."],
        ]),
        ('h', "كيف أعالج هبوط السكر؟"),
        ('ul', [
            "خذ <b>15 غرامًا من سكر سريع</b>: 3 ملاعق صغيرة من السكر مذابة في الماء، أو نصف كوب (120 مل) من العصير العادي.",
            "أعد الفحص بعد 15 دقيقة. وإذا بقي أقل من 70، فكرّر.",
            "عندما يرتفع فوق 70، تناول وجبة صغيرة.",
        ]),
        ('break',),
        ('h', "ماذا آكل؟"),
        ('table', ["السحور", "الإفطار"], [
            ["أخّره قدر ما تستطيع، قبيل الفجر.", "افطر على 1 إلى 3 تمرات مع الماء."],
            ["اختر أطعمة بطيئة الهضم: الخبز الأسمر، الشوفان، الفول أو البقوليات.", "ثم طبق متوازن: نصفه خضار، وبعض البروتين، وقليل من الأرز أو الخبز."],
            ["أضف البروتين: البيض أو اللبنة أو الجبن أو الزبادي.", "قلّل المقليات (السمبوسة) والحلويات (الكنافة والقطايف)."],
            ["اشرب ماءً كافيًا.", "تجنّب المشروبات السكرية مثل الفيمتو والعصائر المحلّاة."],
        ]),
        ('ul', [
            "اشرب الماء على فترات بين الإفطار والسحور.",
            "صلاة التراويح تُعدّ نشاطًا بدنيًا. تجنّب الرياضة الشاقة وأنت صائم، خاصةً قبيل الإفطار.",
        ]),
        ('h', "ماذا عن أدويتي؟"),
        ('ul', [
            "بعض الأدوية تحتاج إلى <b>تعديل الجرعة أو الوقت</b> في رمضان، خاصةً الإنسولين وحبوب مثل جليكلازايد وجليميبرايد.",
            "بعض الحبوب، مثل داباغليفلوزين وإمباغليفلوزين، تحتاج إلى عناية إضافية بشرب السوائل.",
            "إذا كان لديك السكري من النوع الأول، <b>فلا توقف الإنسولين أبدًا</b>.",
            "بعد رمضان، عُد إلى جرعاتك المعتادة كما نصحك طبيبك، وانتبه لحلويات العيد.",
        ]),
        ('help', "اطلب المساعدة فورًا: اتصل بـ 997 أو اذهب إلى الطوارئ إذا:", [
            "بقي السكر أقل من 70 بعد علاجه مرتين، أو أصبحت مشوّشًا أو نعسانًا جدًا.",
            "تقيّأت ولم تستطع شرب السوائل.",
            "صاحب ارتفاعَ السكر ألمٌ في البطن أو قيء أو تنفّس سريع وعميق.",
            "ظهرت علامات الجفاف: جفاف شديد في الفم، أو دوخة عند الوقوف، أو قلة شديدة في البول.",
        ]),
        ('plan', "خطتي في رمضان", [
            ("درجة الخطر (من طبيبي)", 1),
            ("أدوية السحور", 1),
            ("أدوية الإفطار", 1),
            ("رقم هاتف العيادة", 1),
        ]),
    ],
))

# ===================================================================== HOME MONITORING RECORDS
# The home BP leaflet became a guide + record (records_content.py), 15 Oct 2026.
from records_content import BP as _BP, GLUCOSE as _GLUCOSE
LEAFLETS += [_BP, _GLUCOSE]
