from h import ul, ol, p, tbl, blk

# ─────────────────────────────────────────────────────────────
# 3 · FIVE A'S
# ─────────────────────────────────────────────────────────────
FIVE_AS = dict(
    id='five-as',
    h_en='The Five A’s',
    h_ar='الخطوات الخمس (5A’s)',
    sub_en='Ask · Advise · Assess · Assist · Arrange — a stepwise protocol for patients ready to hear advice',
    sub_ar='اسأل · انصح · قيِّم · ساعد · رتِّب — بروتوكول متدرّج للمرضى المستعدين لسماع النصيحة',
    blocks=[
        blk('glance', 'five-as-at-a-glance', 'At a glance', 'لمحة سريعة',
            ul([
                '<b>What it is:</b> a five-step protocol from the U.S. Public Health Service tobacco guideline, since applied to alcohol, weight and adherence.',
                '<b>Best for:</b> patients who are receptive and mainly lack information or a plan.',
                '<b>Evidence:</b> associated with less smoking and alcohol use and modest weight loss (SORT B); endorsed by the USPSTF.',
                '<b>Key finding:</b> the last two steps — Assist and Arrange — are the ones most often skipped and the ones that carry much of the effect.',
            ]),
            ul([
                '<b>ما هي:</b> بروتوكول من خمس خطوات مصدره دليل خدمة الصحة العامة الأمريكية لعلاج التبغ، ثم طُبّق على الكحول والوزن والالتزام.',
                '<b>الأنسب لـ:</b> المريض المتقبّل الذي ينقصه أساسًا معلومة أو خطة.',
                '<b>الدليل:</b> مرتبطة بتدخين وكحول أقل ونزول متواضع في الوزن (SORT B)، وتوصي بها فرقة الخدمات الوقائية الأمريكية (USPSTF).',
                '<b>النتيجة الأهم:</b> الخطوتان الأخيرتان — المساعدة والترتيب — هما الأكثر إهمالًا، وهما تحملان جزءًا كبيرًا من الأثر.',
            ])),
        blk('features', 'five-as-steps', 'The five steps', 'الخطوات الخمس',
            tbl(['Step', 'What you do', 'In practice'], [
                ['<b>Ask</b>', 'Identify the behaviour, every visit, in specific terms', '“How many cigarettes a day — and do you use shisha or vape as well?” · structured tools: Fagerström, CAGE/AUDIT-C'],
                ['<b>Advise</b>', 'Clear, strong, personalised advice in factual terms — linked to why they came today', '“As your doctor, I recommend stopping completely. Your cough and this chest infection are exactly what smoking does.” Use “I recommend”, not “you should”.'],
                ['<b>Assess</b>', 'What does the patient know, and are they willing to try now?', '“What do you know about how smoking affects your diabetes?” · “Would you be willing to try quitting in the next month?”'],
                ['<b>Assist</b>', 'For the willing: a plan, medication, support and written material. For the unwilling: a motivational intervention (the 5 R’s)', 'Set a quit date, prescribe, refer to a cessation clinic, give the leaflet'],
                ['<b>Arrange</b>', 'Schedule follow-up — in person, by phone or virtually', '“I’d like to see you a week after your quit date to see how it’s going.”'],
            ], wide=True),
            tbl(['الخطوة', 'ماذا تفعل', 'في التطبيق'], [
                ['<b>اسأل (Ask)</b>', 'حدِّد السلوك في كل زيارة وبعبارات محددة', '«كم سيجارة في اليوم؟ وهل تستخدم الشيشة أو السيجارة الإلكترونية أيضًا؟» · أدوات منظّمة: فاغرستروم، CAGE/AUDIT-C'],
                ['<b>انصح (Advise)</b>', 'نصيحة واضحة قوية مخصّصة بلغة الحقائق — مرتبطة بسبب حضوره اليوم', '«بصفتي طبيبك أنصحك بالتوقف تمامًا. كحّتك والتهاب صدرك هذا من آثار التدخين بالضبط.» قل «أنصحك» لا «يجب عليك».'],
                ['<b>قيِّم (Assess)</b>', 'ماذا يعرف المريض، وهل هو مستعد للمحاولة الآن؟', '«ماذا تعرف عن تأثير التدخين على السكري عندك؟» · «هل أنت مستعد لتجرّب الإقلاع خلال الشهر القادم؟»'],
                ['<b>ساعد (Assist)</b>', 'للمستعد: خطة ودواء ودعم ومواد مكتوبة. لغير المستعد: تدخل تحفيزي (الـ 5R’s)', 'حدّد يوم الإقلاع، اكتب الوصفة، أحِل إلى عيادة الإقلاع، سلّمه النشرة'],
                ['<b>رتِّب (Arrange)</b>', 'حدّد موعد المتابعة — حضوريًا أو هاتفيًا أو افتراضيًا', '«أحب أن أراك بعد أسبوع من يوم إقلاعك لنرى كيف تسير الأمور.»'],
            ], wide=True)),
        blk('evidence', 'five-as-evidence', 'Evidence', 'الدليل',
            ul([
                '<b>Physician advice alone works.</b> In a review of 26 trials (n ≈ 22,000), cessation at ≥6 months was 8.0% with physician advice versus 4.8% without (RR 1.76) — even a single session under 20 minutes helped (USPSTF 2021).',
                '<b>Advice plus pharmacotherapy and behavioural support roughly doubles quit rates</b> over usual care (15.2% vs 8.6%; RR 1.83).',
                '<b>In an emergency-department study</b>, a brief intervention using some of the A’s took a median of 7 minutes and was followed by 3.3 fewer binge-drinking episodes a month, versus 1.5 with standard care.',
                '<b>For weight, “Arrange” mattered:</b> weight loss at 3 months (about 1.5 kg) occurred only when the counselling included arranging follow-up; the first four A’s alone changed self-reported diet a little but not weight.',
            ]),
            ul([
                '<b>نصيحة الطبيب وحدها تنفع.</b> في مراجعة لـ 26 تجربة (نحو 22,000 مشارك) كان معدل الإقلاع بعد 6 أشهر فأكثر 8.0% مع نصيحة الطبيب مقابل 4.8% بدونها (نسبة الخطر 1.76) — وحتى جلسة واحدة أقل من 20 دقيقة أفادت (USPSTF 2021).',
                '<b>النصيحة مع الدواء والدعم السلوكي تضاعف تقريبًا معدلات الإقلاع</b> مقارنة بالرعاية المعتادة (15.2% مقابل 8.6%؛ نسبة الخطر 1.83).',
                '<b>في دراسة بقسم الطوارئ</b> استغرق تدخل مختصر يستخدم بعض الخطوات 7 دقائق في المتوسط، وتلاه انخفاض قدره 3.3 نوبات شرب مفرط شهريًا مقابل 1.5 مع الرعاية المعتادة.',
                '<b>في الوزن كانت خطوة «رتِّب» فارقة:</b> لم يحدث نزول الوزن بعد 3 أشهر (نحو 1.5 كغ) إلا حين شمل الإرشاد ترتيب المتابعة؛ أما الخطوات الأربع الأولى وحدها فغيّرت الغذاء المُبلَّغ عنه قليلًا دون الوزن.',
            ])),
        blk('mx', 'five-as-5rs', 'Not ready yet? The 5 R’s', 'غير مستعد بعد؟ الـ 5R’s',
            tbl(['R', 'Ask the patient to consider…'], [
                ['<b>Relevance</b>', 'Why quitting matters to <i>them</i> — their health, family, faith, finances'],
                ['<b>Risks</b>', 'The short- and long-term consequences that concern them most'],
                ['<b>Rewards</b>', 'What they would gain — breath, taste, money, being a model for their children'],
                ['<b>Roadblocks</b>', 'What stands in the way, and what might help with each'],
                ['<b>Repetition</b>', 'Raise it again at every visit; most people need several attempts'],
            ]),
            tbl(['R', 'اطلب من المريض أن يتأمل…'], [
                ['<b>الصلة (Relevance)</b>', 'لماذا يهمّه هو الإقلاع — صحته، أسرته، دينه، ماله'],
                ['<b>المخاطر (Risks)</b>', 'العواقب القريبة والبعيدة التي تقلقه أكثر'],
                ['<b>المكاسب (Rewards)</b>', 'ما سيكسبه — النَّفَس، التذوق، المال، أن يكون قدوة لأبنائه'],
                ['<b>العوائق (Roadblocks)</b>', 'ما الذي يقف في الطريق، وما الذي قد يساعد في كل منها'],
                ['<b>التكرار (Repetition)</b>', 'افتح الموضوع في كل زيارة؛ أغلب الناس يحتاجون عدة محاولات'],
            ])),
        blk('special', 'five-as-vba', 'Only 30 seconds? Very brief advice', 'لديك 30 ثانية فقط؟ النصيحة المختصرة جدًا',
            ul([
                '<b>Ask</b> — and record — smoking status.',
                '<b>Advise</b> that the most effective way to stop is with support and medication.',
                '<b>Act</b> — offer the referral or prescription as the default (“I’ll book you with the cessation clinic” rather than “would you like…?”).',
                'WHO’s first tobacco-cessation guideline (2024) recommends <b>brief advice of about 30 seconds to 3 minutes, offered routinely</b> by health workers — no one is too busy for this.',
            ]),
            ul([
                '<b>اسأل</b> عن حالة التدخين — ووثّقها.',
                '<b>انصح</b> بأن أنجع طريقة للإقلاع هي مع الدعم والدواء.',
                '<b>تصرّف</b> — اعرض الإحالة أو الوصفة على أنها الخيار التلقائي («سأحجز لك في عيادة الإقلاع» بدل «هل تحب أن…؟»).',
                'توصي أول إرشادات لمنظمة الصحة العالمية لعلاج الإقلاع عن التبغ (2024) بـ <b>نصيحة مختصرة مدتها نحو 30 ثانية إلى 3 دقائق تُقدَّم روتينيًا</b> من العاملين الصحيين — لا أحد أكثر انشغالًا من هذا.',
            ])),
        blk('trap', 'five-as-traps', '⚠ Traps', '⚠ أخطاء',
            ul([
                'Stopping after Advise. Without Assist and Arrange, the visit is a lecture.',
                'Generic advice. Link it to the presenting complaint or a number the patient cares about (HbA1c, blood pressure, peak flow).',
                'Asking only about cigarettes — shisha, medwakh, vapes and smokeless tobacco go unrecorded unless you name them.',
            ]),
            ul([
                'التوقف بعد «انصح». بلا «ساعد» و«رتِّب» تصبح الزيارة محاضرة.',
                'النصيحة العامة. اربطها بسبب الزيارة أو برقم يهمّ المريض (السكر التراكمي، ضغط الدم، ذروة الجريان).',
                'السؤال عن السجائر فقط — الشيشة والمدواخ والسيجارة الإلكترونية والتبغ غير المُدخَّن لا تُوثَّق ما لم تسمِّها.',
            ])),
        blk('local', 'five-as-local', '⌖ Local context', '⌖ السياق المحلي',
            ul([
                '<b>“Arrange” has a ready-made route:</b> Ministry of Health smoking-cessation clinics, bookable in person or virtually through the <b>Sehhaty</b> app. Book it with the patient before they leave.',
                'Add tobacco status — all products — to the problem list so it is asked about at every visit, not only in chest clinics.',
            ]),
            ul([
                '<b>لخطوة «رتِّب» طريق جاهز:</b> عيادات الإقلاع عن التدخين التابعة لوزارة الصحة، ويمكن حجزها حضوريًا أو افتراضيًا عبر تطبيق <b>صحتي</b>. احجز مع المريض قبل أن يغادر.',
                'أضف حالة استخدام التبغ — بكل منتجاته — إلى قائمة المشكلات لتُسأل في كل زيارة، لا في عيادات الصدر فقط.',
            ])),
    ])

# ─────────────────────────────────────────────────────────────
# 4 · FRAMES
# ─────────────────────────────────────────────────────────────
FRAMES = dict(
    id='frames',
    h_en='FRAMES',
    h_ar='FRAMES',
    sub_en='Feedback · Responsibility · Advice · Menu · Empathy · Self-efficacy — a brief intervention built for harm reduction',
    sub_ar='التغذية الراجعة · المسؤولية · النصيحة · قائمة الخيارات · التعاطف · الكفاءة الذاتية — تدخل مختصر مصمَّم لتقليل الضرر',
    blocks=[
        blk('glance', 'frames-at-a-glance', 'At a glance', 'لمحة سريعة',
            ul([
                '<b>What it is:</b> a six-element brief intervention, originally for alcohol misuse; the forerunner of motivational interviewing.',
                '<b>Where it shines:</b> when the patient may not accept abstinence but will accept <b>less harm</b> — and when objective numbers (labs, readings) can carry the message.',
                '<b>Also used for:</b> stroke-risk reduction, cannabis use in young people, adherence.',
                '<b>Evidence:</b> SORT B — reductions in alcohol-related risk behaviour and in cannabis use.',
                '<b>Always begin by asking permission</b> to share information; it keeps the patient in control and lowers defensiveness.',
            ]),
            ul([
                '<b>ما هو:</b> تدخل مختصر من ستة عناصر وُضع أصلًا لإساءة استخدام الكحول، وهو سلف المقابلة التحفيزية.',
                '<b>أين يتألق:</b> حين لا يقبل المريض الامتناع التام لكنه يقبل <b>ضررًا أقل</b> — وحين تستطيع الأرقام الموضوعية (التحاليل والقراءات) حمل الرسالة.',
                '<b>يُستخدم أيضًا في:</b> خفض خطر السكتة الدماغية، وتعاطي القنّب لدى الشباب، والالتزام العلاجي.',
                '<b>الدليل:</b> SORT B — تراجع في سلوكيات الخطر المرتبطة بالكحول وفي تعاطي القنّب.',
                '<b>ابدأ دائمًا بطلب الإذن</b> قبل مشاركة المعلومة؛ فهذا يُبقي المريض صاحب القرار ويقلّل دفاعيته.',
            ])),
        blk('features', 'frames-elements', 'The six elements', 'العناصر الستة',
            tbl(['Element', 'What you do', 'Example'], [
                ['<b>F</b>eedback', 'Personal risk, factually — results, scores, readings against normal', '“Your HbA1c is 9.4 — the target we agreed is under 7. Can I show you what that means for your eyes and kidneys?”'],
                ['<b>R</b>esponsibility', 'Make clear the choice is the patient’s', '“Whether and how you change this is your decision — I’m here to help either way.”'],
                ['<b>A</b>dvice', 'Clear, neutral advice anchored to an objective standard', '“Stopping completely would be best for you; cutting down would still help.”'],
                ['<b>M</b>enu', 'Several options to choose from', '“Some people do best with medication, some with the clinic’s support sessions, some with both. Which sounds closest to you?”'],
                ['<b>E</b>mpathy', 'Warm, reflective, non-judgemental', '“With everything you’re carrying at work right now, a big change feels like a lot.”'],
                ['<b>S</b>elf-efficacy', 'Build confidence from past success', '“You fasted through Ramadan without a cigarette in daylight hours. That tells me you can do this.”'],
            ], wide=True),
            tbl(['العنصر', 'ماذا تفعل', 'مثال'], [
                ['<b>F</b> التغذية الراجعة', 'الخطر الشخصي بلغة الحقائق — النتائج والدرجات والقراءات مقارنة بالطبيعي', '«السكر التراكمي عندك 9.4 — والهدف الذي اتفقنا عليه أقل من 7. هل تسمح أن أوضح لك ماذا يعني هذا لعينيك وكليتيك؟»'],
                ['<b>R</b> المسؤولية', 'وضّح أن الاختيار للمريض', '«هل تغيّر وكيف تغيّر، هذا قرارك أنت — وأنا هنا لأساعدك في كل الأحوال.»'],
                ['<b>A</b> النصيحة', 'نصيحة واضحة محايدة مستندة إلى معيار موضوعي', '«التوقف التام هو الأفضل لك، وحتى التقليل سيفيدك.»'],
                ['<b>M</b> قائمة الخيارات', 'عدة خيارات يختار منها', '«بعض الناس ينجحون أكثر مع الدواء، وبعضهم مع جلسات دعم العيادة، وبعضهم مع الاثنين. أيّها أقرب إليك؟»'],
                ['<b>E</b> التعاطف', 'دفء وعكس للمشاعر بلا إطلاق أحكام', '«مع كل ما تحمله في عملك هذه الأيام، تغيير كبير يبدو حِملًا ثقيلًا.»'],
                ['<b>S</b> الكفاءة الذاتية', 'ابنِ الثقة على نجاحات سابقة', '«صمتَ رمضان كله دون سيجارة في ساعات النهار. هذا يقول لي إنك قادر.»'],
            ], wide=True)),
        blk('evidence', 'frames-evidence', 'Evidence', 'الدليل',
            ul([
                'In a randomised trial of brief physician advice for problem drinkers, the FRAMES-based intervention was associated with <b>40–50% lower alcohol intake</b> and fewer alcohol-related arrests and road crashes.',
                'A French cluster-randomised trial (CANABIC) applying FRAMES in primary care found <b>reduced cannabis use</b> at 6 months in patients up to 18 years old, while use rose among adolescents receiving routine care.',
                '<b>Choice matters:</b> offering a menu increases adherence and satisfaction — FRAMES builds shared decision-making into the structure.',
                'For some patients, <b>simply seeing their own number</b> beside the normal range is enough to start change.',
            ]),
            ul([
                'في تجربة عشوائية لنصيحة طبية مختصرة لمن يعانون مشكلات الشرب، ارتبط التدخل المبني على FRAMES بـ <b>انخفاض 40–50% في كمية الكحول</b> وبعدد أقل من حالات القبض وحوادث الطرق المرتبطة بالكحول.',
                'وجدت تجربة فرنسية عنقودية عشوائية (CANABIC) طبّقت FRAMES في الرعاية الأولية <b>انخفاضًا في تعاطي القنّب</b> بعد 6 أشهر لدى المرضى حتى عمر 18 سنة، بينما ارتفع التعاطي لدى المراهقين الذين تلقوا الرعاية المعتادة.',
                '<b>الاختيار مهم:</b> تقديم قائمة خيارات يرفع الالتزام والرضا — وFRAMES يبني القرار المشترك في صلب هيكله.',
                'عند بعض المرضى يكفي <b>أن يرى رقمه هو</b> بجانب المعدل الطبيعي ليبدأ التغيير.',
            ])),
        blk('special', 'frames-special', 'Where FRAMES fits in Saudi practice', 'أين يناسب FRAMES في الممارسة السعودية',
            ul([
                '<b>Chronic-disease feedback</b> — HbA1c, home BP, LDL-C, eGFR, weight trend. The numbers do the persuading; you supply the meaning.',
                '<b>Khat chewing</b> (notably in the south-west), stimulant misuse, and <b>alcohol</b> — where abstinence may not be accepted at first, harm reduction is still progress. Disclosure is low because of legal and social consequences: ask privately, without judgement, and state what is and is not confidential.',
                '<b>Adherence</b> — the menu element is ideal for insulin, statins and inhalers, where several reasonable regimens exist.',
            ]),
            ul([
                '<b>التغذية الراجعة في الأمراض المزمنة</b> — السكر التراكمي، وضغط الدم المنزلي، وكوليسترول LDL، ووظائف الكلى، ومسار الوزن. الأرقام تُقنع؛ وأنت تشرح معناها.',
                '<b>مضغ القات</b> (لا سيما في الجنوب الغربي)، وإساءة استخدام المنشطات، و<b>الكحول</b> — حين لا يُقبل الامتناع التام في البداية، يبقى تقليل الضرر تقدمًا. يقلّ الإفصاح بسبب العواقب القانونية والاجتماعية: اسأل على انفراد، بلا أحكام، ووضّح ما هو سرّي وما ليس كذلك.',
                '<b>الالتزام العلاجي</b> — عنصر «قائمة الخيارات» مثالي للإنسولين والستاتين والبخاخات، حيث توجد عدة أنظمة معقولة.',
            ])),
        blk('trap', 'frames-traps', '⚠ Traps', '⚠ أخطاء',
            ul([
                '<b>Feedback used as a scare tactic</b> — fear without a plan produces avoidance.',
                '<b>A “menu” with one acceptable option</b> is an ultimatum, and patients notice.',
                'Skipping self-efficacy — information without confidence rarely becomes action.',
            ]),
            ul([
                '<b>استخدام التغذية الراجعة للتخويف</b> — الخوف بلا خطة يولّد التجنّب.',
                '<b>«قائمة خيارات» بخيار واحد مقبول</b> هي إنذار، والمرضى يلاحظون ذلك.',
                'إهمال الكفاءة الذاتية — المعلومة بلا ثقة نادرًا ما تتحول إلى فعل.',
            ])),
    ])
