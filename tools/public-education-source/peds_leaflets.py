"""Parent leaflets that go with the Pediatric ER Doses page (peds-er.html).

1. fever-medicine-child : paracetamol and ibuprofen at home, dose by weight
2. spacer-nebulizer     : using a spacer or a nebulizer at home

Dose table: paracetamol 15 mg/kg, ibuprofen 10 mg/kg, rounded DOWN to the
nearest 0.5 mL (0.1 mL for drops), so every dose sits between 12.5 and 15 mg/kg
(paracetamol) and at 10 mg/kg (ibuprofen). Checked by script on 8 Nov 2026.
"""

FEVER_SOURCES = [
    "National Institute for Health and Care Excellence. Fever in under 5s: assessment and initial management (NG143), 2019, updated 2021",
    "Sullivan JE, Farrar HC; AAP Section on Clinical Pharmacology and Therapeutics. Fever and antipyretic use in children. Pediatrics 2011;127:580–7",
    "Product information: paracetamol oral suspension 120 mg/5 mL and 250 mg/5 mL, paracetamol drops 100 mg/mL, ibuprofen oral suspension 100 mg/5 mL",
    "British National Formulary for Children (BNFc): paracetamol and ibuprofen",
]
SPACER_SOURCES = [
    "Global Initiative for Asthma (GINA). Global Strategy for Asthma Management and Prevention, 2026 update",
    "Al-Moamary MS, et al. The Saudi Initiative for Asthma (SINA) — 2021 update. Ann Thorac Med 2021;16:4–56",
    "Cates CJ, et al. Holding chambers (spacers) versus nebulisers for beta-agonist treatment of acute asthma. Cochrane Database Syst Rev 2013",
    "Product information: salbutamol, ipratropium and budesonide nebules; spacer and nebulizer manufacturer instructions",
]

DOSE_HDR_EN = ["Child's weight", "Paracetamol drops 100 mg/mL", "Paracetamol syrup 120 mg/5 mL", "Paracetamol syrup 250 mg/5 mL", "Ibuprofen syrup 100 mg/5 mL"]
DOSE_HDR_AR = ["وزن الطفل", "قطرة باراسيتامول 100 ملغ/مل", "شراب باراسيتامول 120 ملغ/5 مل", "شراب باراسيتامول 250 ملغ/5 مل", "شراب إيبوبروفين 100 ملغ/5 مل"]
# weight kg, drops mL, 120/5 mL, 250/5 mL, ibuprofen mL
_ROWS = [(6, "0.9", "3.5", "1.5", "3"), (8, "1.2", "5", "2", "4"),
         (10, "1.5", "6", "3", "5"), (12, "1.8", "7.5", "3.5", "6"), (15, "—", "9", "4.5", "7.5"),
         (20, "—", "12.5", "6", "10"), (25, "—", "15.5", "7.5", "12.5"), (30, "—", "18.5", "9", "15")]
DOSE_ROWS_EN = [[f"{w} kg", d if d == "—" else d + " mL", a + " mL", b + " mL", i + " mL"] for w, d, a, b, i in _ROWS]
DOSE_ROWS_AR = [[f"{w} كغ", d if d == "—" else d + " مل", a + " مل", b + " مل", i + " مل"] for w, d, a, b, i in _ROWS]

REV = {"en": "November 2026", "ar": "نوفمبر 2026"}
NEXT = {"en": "November 2027, or sooner if guidance changes", "ar": "نوفمبر 2027، أو قبل ذلك إذا تغيّرت التوصيات"}

PEDS_LEAFLETS = []

# ===================================================================== FEVER MEDICINE
PEDS_LEAFLETS.append(dict(
    slug="fever-medicine-child",
    tone="#B0392C", tone_soft="#FBEDEA",
    topic_en="Children's health", topic_ar="صحة الطفل",
    guide="peds-er.html",
    title_en="Fever and pain medicine for your child",
    title_ar="خافض الحرارة والمسكّن لطفلك",
    sub_en="The right dose for your child's weight — and when to get help",
    sub_ar="الجرعة الصحيحة حسب وزن طفلك، ومتى تطلب المساعدة",
    card_en="Paracetamol and ibuprofen by weight, measuring the dose, how often, and warning signs.",
    card_ar="الباراسيتامول والإيبوبروفين حسب الوزن، قياس الجرعة، عدد المرات، وعلامات الخطر.",
    sources=FEVER_SOURCES, reviewed=REV, next_review=NEXT,
    en=[
        ('key', "The 5 things to remember", [
            "Fever helps the body fight infection. Medicine is to make your child <b>comfortable</b>, not to bring the number down.",
            "Give the dose by your child's <b>weight</b>, using the <b>syringe</b> that comes with the medicine. Never a kitchen spoon.",
            "Paracetamol: every 4–6 hours, <b>no more than 4 doses</b> in 24 hours. Ibuprofen: every 6–8 hours, <b>no more than 3 doses</b> in 24 hours.",
            "<b>Check the strength</b> on the bottle. Syrups and drops come in different strengths.",
            "Under <b>3 months</b> with a temperature of 38 °C or more: see a doctor <b>now</b>.",
        ]),
        ('h', "Which medicine should I use?"),
        ('ul', [
            "<b>Paracetamol</b> (Adol, Panadol, Fevadol): from birth. Ask a doctor first for a baby under 3 months.",
            "<b>Ibuprofen</b> (Brufen, Nurofen): from 3 months and 5 kg. Not if your child is dehydrated, has kidney problems or chickenpox.",
            "Use <b>one</b> medicine. Switch only if your child is still upset before the next dose is due. Never give both at once.",
            "Different brand names can be the <b>same medicine</b>. Never give two paracetamol products.",
        ]),
        ('h', "How much do I give?"),
        ('table', DOSE_HDR_EN, DOSE_ROWS_EN),
        ('p', "Find the weight closest to your child's, <b>without going over it</b>. Over 30 kg: ask your doctor or pharmacist."),
        ('break',),
        ('tip', "Good to know", [
            "Light clothes and a comfortable room are enough. No heavy blankets.",
            "Do not sponge with cold water or alcohol. It makes children shiver and does not help.",
            "Offer drinks often. Breastfeed as usual.",
        ]),
        ('help', "Get help now — call 997 or go to the emergency department if your child:", [
            "Is under 3 months old with a temperature of 38 °C or more.",
            "Is very sleepy, floppy, or hard to wake.",
            "Is breathing fast or hard, or grunting.",
            "Has a rash that does not fade when you press a glass on it.",
            "Has a fit (seizure), a stiff neck, or has had too much medicine by mistake.",
        ]),
        ('h', "See a doctor soon (or call 937 for advice) if:"),
        ('ul', [
            "The fever lasts more than 5 days.",
            "Your child is drinking much less or passing much less urine.",
            "You are worried, or your child seems to be getting worse.",
        ]),
        ('plan', "My child's plan", [
            ("Weight (kg) and date weighed", 1),
            ("Medicine and strength · dose (mL) · how often · most doses in 24 h", 1),
        ]),
        ('log', "Doses given", ["#", "Day and time", "Medicine", "Dose (mL)"], 3),
    ],
    ar=[
        ('key', "5 أمور تذكّرها", [
            "الحرارة تساعد الجسم على مقاومة العدوى. الدواء هدفه <b>راحة طفلك</b>، لا خفض الرقم.",
            "أعطِ الجرعة حسب <b>وزن</b> طفلك، باستخدام <b>المحقنة</b> المرفقة مع الدواء، وليس ملعقة المطبخ.",
            "الباراسيتامول: كل 4–6 ساعات، <b>4 جرعات كحدّ أقصى</b> في 24 ساعة. الإيبوبروفين: كل 6–8 ساعات، <b>3 جرعات كحدّ أقصى</b> في 24 ساعة.",
            "<b>تأكّد من التركيز</b> المكتوب على العبوة، فالشراب والقطرة لهما تركيزات مختلفة.",
            "إذا كان عمر طفلك <b>أقل من 3 أشهر</b> وحرارته 38 درجة أو أكثر، فاعرضه على الطبيب <b>فورًا</b>.",
        ]),
        ('h', "أيّ دواء أستخدم؟"),
        ('ul', [
            "<b>الباراسيتامول</b> (أدول، بنادول، فيفادول): منذ الولادة، واستشر الطبيب أولًا للرضيع دون 3 أشهر.",
            "<b>الإيبوبروفين</b> (بروفين، نوروفين): من عمر 3 أشهر ووزن 5 كغ، ولا يُعطى مع الجفاف أو أمراض الكلى أو جدري الماء.",
            "استخدم دواءً <b>واحدًا</b>، ولا تنتقل إلى الآخر إلا إذا بقي طفلك متضايقًا قبل موعد الجرعة التالية. ولا تعطِ الدواءين معًا.",
            "قد تكون الأسماء التجارية المختلفة <b>للدواء نفسه</b>، فلا تعطِ منتجَين فيهما باراسيتامول.",
        ]),
        ('h', "كم أعطي؟"),
        ('table', DOSE_HDR_AR, DOSE_ROWS_AR),
        ('p', "اختر الوزن الأقرب إلى وزن طفلك <b>دون أن تتجاوزه</b>. وإذا زاد الوزن على 30 كغ، فاسأل الطبيب أو الصيدلي."),
        ('break',),
        ('tip', "معلومات مفيدة", [
            "تكفي الملابس الخفيفة وغرفة معتدلة، دون بطانيات ثقيلة.",
            "لا تمسح جسمه بالماء البارد أو الكحول، فهذا يسبّب الرجفة ولا يفيد.",
            "أكثِر من السوائل، واستمري في الرضاعة الطبيعية.",
        ]),
        ('help', "اطلب المساعدة فورًا: اتصل بـ 997 أو اذهب إلى الطوارئ إذا كان طفلك:", [
            "عمره أقل من 3 أشهر وحرارته 38 درجة أو أكثر.",
            "نعسانًا جدًا، أو مرتخيًا، أو يصعب إيقاظه.",
            "يتنفس بسرعة أو بصعوبة، أو يئنّ مع التنفس.",
            "لديه طفح جلدي لا يختفي عند الضغط عليه بكأس زجاجية.",
            "أصيب بتشنّج، أو تيبّس في الرقبة، أو أخذ جرعة زائدة من الدواء بالخطأ.",
        ]),
        ('h', "راجع الطبيب قريبًا (أو اتصل بـ 937 للاستشارة) إذا:"),
        ('ul', [
            "استمرت الحرارة أكثر من 5 أيام.",
            "قلّ شرب طفلك أو تبوّله كثيرًا.",
            "كنت قلقًا، أو بدا أن حالة طفلك تسوء.",
        ]),
        ('plan', "خطة طفلي", [
            ("الوزن (كغ) وتاريخ الوزن", 1),
            ("الدواء وتركيزه · الجرعة (مل) · كل كم ساعة · أقصى عدد في 24 ساعة", 1),
        ]),
        ('log', "الجرعات المعطاة", ["#", "اليوم والوقت", "الدواء", "الجرعة (مل)"], 3),
    ],
))

# ===================================================================== SPACER + NEBULIZER
PEDS_LEAFLETS.append(dict(
    slug="spacer-nebulizer",
    tone="#2C7A6B", tone_soft="#E8F3F0",
    topic_en="Breathing medicines", topic_ar="أدوية التنفس",
    guide="peds-er.html#nebs",
    title_en="Using a spacer or a nebulizer at home",
    title_ar="استخدام البخاخ مع الحجرة (السبيسر) أو جهاز البخار في المنزل",
    sub_en="Get the medicine into the lungs — and know when to get help",
    sub_ar="أوصل الدواء إلى الرئتين، واعرف متى تطلب المساعدة",
    card_en="Spacer steps, nebulizer steps, cleaning, triggers at home, and warning signs.",
    card_ar="خطوات استخدام الحجرة، خطوات جهاز البخار، التنظيف، مثيرات الربو في المنزل، وعلامات الخطر.",
    sources=SPACER_SOURCES, reviewed=REV, next_review=NEXT,
    en=[
        ('key', "The 5 things to remember", [
            "An inhaler with a <b>spacer</b> works as well as a nebulizer for most attacks, and it is quicker.",
            "<b>Shake</b> the inhaler before <b>every</b> puff. Put in <b>one puff at a time</b>.",
            "Use a <b>mask</b> until about 4–5 years old, then a <b>mouthpiece</b>.",
            "In a nebulizer, use only the medicines and amounts your doctor wrote, and only <b>saline from the pharmacy</b>.",
            "If the reliever is needed <b>more often than every 4 hours</b>, see a doctor today.",
        ]),
        ('h', "How do I use the spacer?"),
        ('ol', [
            "Take off the cap and <b>shake</b> the inhaler well.",
            "Push the inhaler into the back of the spacer.",
            "Place the mask over the nose and mouth with a good seal, or put the mouthpiece between the lips.",
            "Press the inhaler <b>once</b>.",
            "Let your child take <b>5–6 slow breaths</b> in and out (or one deep breath and hold for 10 seconds if older).",
            "Wait 30–60 seconds, shake again, and repeat for each puff the doctor prescribed.",
        ]),
        ('h', "How do I use the nebulizer?"),
        ('ol', [
            "Wash your hands. Sit your child upright.",
            "Twist open the plastic vial (nebule) and squeeze all of it into the cup.",
            "If your doctor told you to, add saline up to the amount written on your plan.",
            "Fit the mask or mouthpiece and switch the machine on.",
            "Your child breathes normally until the mist stops and the machine sputters, about <b>5–10 minutes</b>.",
            "After a steroid nebule (budesonide), wipe your child's face and rinse the mouth with water.",
        ]),
        ('break',),
        ('h', "How do I keep them clean?"),
        ('ul', [
            "<b>Spacer:</b> once a week, wash in warm soapy water, do not rinse, and let it dry in the air. Rubbing it with a towel makes the medicine stick to the sides.",
            "<b>Nebulizer cup and mask:</b> after each use, rinse in warm water, shake off, and air-dry. Wash with soap once a day.",
            "Each child should have their own spacer, mask and nebulizer cup.",
        ]),
        ('tip', "Common triggers in Saudi homes", [
            "<b>Incense (bakhoor, oud) and tobacco or shisha smoke</b>. Keep them away from your child, including in the car.",
            "<b>Dust storms</b>: keep windows closed and your child indoors.",
            "Dust, cockroaches and pets in the bedroom; strong perfumes and cleaning sprays.",
        ]),
        ('help', "Get help now — call 997 or go to the emergency department if your child:", [
            "Is too breathless to talk, feed or play.",
            "Has blue or grey lips.",
            "Has the skin between or under the ribs sucking in hard.",
            "Is very sleepy or confused.",
            "Does not improve after the reliever, or needs it again within 1–2 hours.",
        ]),
        ('p', "While you wait for help, keep giving the reliever as your child's asthma action plan says."),
        ('plan', "My child's plan", [
            ("Reliever, and how many puffs or which nebule", 1),
            ("Preventer, and how often", 1),
            ("Mask or mouthpiece · saline top-up (mL)", 1),
        ]),
    ],
    ar=[
        ('key', "5 أمور تذكّرها", [
            "البخاخ مع <b>الحجرة (السبيسر)</b> يعمل مثل جهاز البخار في معظم النوبات، وهو أسرع.",
            "<b>رُجّ</b> البخاخ قبل <b>كل</b> بخّة، وضع <b>بخّة واحدة في كل مرة</b>.",
            "استخدم <b>القناع</b> حتى عمر 4–5 سنوات تقريبًا، ثم <b>القطعة الفموية</b>.",
            "في جهاز البخار، استخدم فقط الأدوية والكميات التي كتبها الطبيب، و<b>المحلول الملحي من الصيدلية</b> فقط.",
            "إذا احتاج طفلك دواء الإسعاف <b>أكثر من مرة كل 4 ساعات</b>، فراجع الطبيب اليوم.",
        ]),
        ('h', "كيف أستخدم الحجرة (السبيسر)؟"),
        ('ol', [
            "انزع الغطاء و<b>رُجّ</b> البخاخ جيدًا.",
            "أدخل البخاخ في الطرف الخلفي للحجرة.",
            "ضع القناع على الأنف والفم بإحكام، أو ضع القطعة الفموية بين الشفتين.",
            "اضغط البخاخ <b>مرة واحدة</b>.",
            "دع طفلك يأخذ <b>5–6 أنفاس هادئة</b> شهيقًا وزفيرًا (أو نفسًا عميقًا واحدًا ويحبسه 10 ثوانٍ إن كان أكبر سنًا).",
            "انتظر 30–60 ثانية، ثم رُجّ البخاخ مرة أخرى، وكرّر لكل بخّة وصفها الطبيب.",
        ]),
        ('h', "كيف أستخدم جهاز البخار؟"),
        ('ol', [
            "اغسل يديك، وأجلس طفلك معتدلًا.",
            "افتح عبوة الدواء البلاستيكية الصغيرة بالتدوير، واعصر محتواها كله في الكأس.",
            "إذا طلب منك الطبيب، فأضف المحلول الملحي حتى الكمية المكتوبة في خطتك.",
            "ركّب القناع أو القطعة الفموية، ثم شغّل الجهاز.",
            "يتنفس طفلك بشكل طبيعي حتى يتوقف الرذاذ ويبدأ الجهاز بالتقطّع، نحو <b>5–10 دقائق</b>.",
            "بعد عبوة الكورتيزون (بوديسونايد)، امسح وجه طفلك واشطف فمه بالماء.",
        ]),
        ('break',),
        ('h', "كيف أحافظ على نظافتها؟"),
        ('ul', [
            "<b>الحجرة:</b> مرة كل أسبوع، اغسلها بماء دافئ وصابون، ولا تشطفها، واتركها تجفّ في الهواء. مسحها بالمنشفة يجعل الدواء يلتصق بجدرانها.",
            "<b>كأس جهاز البخار والقناع:</b> بعد كل استخدام، اشطفهما بماء دافئ، وانفضهما، واتركهما يجفّان في الهواء. واغسلهما بالصابون مرة يوميًا.",
            "لكل طفل حجرته وقناعه وكأس جهازه الخاص.",
        ]),
        ('tip', "مثيرات شائعة في البيوت السعودية", [
            "<b>البخور والعود ودخان السجائر والشيشة</b>. أبعدها عن طفلك، وفي السيارة أيضًا.",
            "<b>العواصف الترابية</b>: أغلق النوافذ وأبقِ طفلك داخل المنزل.",
            "الغبار والصراصير والحيوانات الأليفة في غرفة النوم، والعطور القوية وبخاخات التنظيف.",
        ]),
        ('help', "اطلب المساعدة فورًا: اتصل بـ 997 أو اذهب إلى الطوارئ إذا كان طفلك:", [
            "يلهث لدرجة أنه لا يستطيع الكلام أو الرضاعة أو اللعب.",
            "شفتاه زرقاوان أو رماديتان.",
            "الجلد بين الأضلاع أو تحتها ينسحب إلى الداخل بقوة.",
            "نعسانًا جدًا أو مشوّش الذهن.",
            "لم يتحسّن بعد دواء الإسعاف، أو احتاجه مرة أخرى خلال 1–2 ساعة.",
        ]),
        ('p', "أثناء انتظار المساعدة، استمر في إعطاء دواء الإسعاف كما في خطة الربو المكتوبة لطفلك."),
        ('plan', "خطة طفلي", [
            ("دواء الإسعاف، وعدد البخّات أو نوع العبوة", 1),
            ("الدواء الوقائي، وعدد مراته", 1),
            ("قناع أو قطعة فموية · كمية المحلول الملحي (مل)", 1),
        ]),
    ],
))
