from h import ul, ol, p, tbl, blk

# ─────────────────────────────────────────────────────────────
# 5 · MOTIVATIONAL INTERVIEWING
# ─────────────────────────────────────────────────────────────
MI = dict(
    id='mi',
    h_en='Motivational interviewing',
    h_ar='المقابلة التحفيزية',
    sub_en='For the ambivalent patient — help them voice their own reasons for change',
    sub_ar='للمريض المتردد — ساعده على أن يعبّر بنفسه عن أسبابه للتغيير',
    blocks=[
        blk('glance', 'mi-at-a-glance', 'At a glance', 'لمحة سريعة',
            ul([
                '<b>What it is:</b> a collaborative conversation style for strengthening a person’s own motivation and commitment to change (Miller and Rollnick).',
                '<b>Why it exists:</b> counsellors who used empathy, understanding and objective information got better results than those who relied on confrontation.',
                '<b>Best for:</b> patients who are ambivalent or not interested in changing.',
                '<b>Evidence:</b> SORT A in primary care for weight, blood pressure and alcohol. Across medical conditions, about <b>10–15% added benefit</b> over usual care; benefits shown with <b>one to three 15–20-minute sessions</b>.',
                '<b>Learnable:</b> basic skills have been acquired in about 2 hours of training; the overall spirit takes longer.',
            ]),
            ul([
                '<b>ما هي:</b> أسلوب حوار تعاوني يقوّي دافعية الشخص والتزامه الذاتي بالتغيير (ميلر ورولنيك).',
                '<b>لماذا نشأت:</b> المرشدون الذين استخدموا التعاطف والتفهّم والمعلومة الموضوعية حققوا نتائج أفضل ممن اعتمدوا على المواجهة.',
                '<b>الأنسب لـ:</b> المريض المتردد أو غير المهتم بالتغيير.',
                '<b>الدليل:</b> SORT A في الرعاية الأولية للوزن وضغط الدم والكحول. وعبر الحالات الطبية المختلفة نحو <b>10–15% فائدة إضافية</b> مقارنة بالرعاية المعتادة، مع فوائد ظهرت في <b>جلسة إلى ثلاث جلسات مدة كل منها 15–20 دقيقة</b>.',
                '<b>قابلة للتعلّم:</b> اكتُسبت المهارات الأساسية في نحو ساعتين من التدريب؛ أما روحها العامة فتحتاج وقتًا أطول.',
            ])),
        blk('features', 'mi-spirit', 'The spirit and the four tasks', 'الروح والمهام الأربع',
            '<p><b>Spirit</b> — the attitude that makes the techniques work:</p>' + ul([
                '<b>Partnership</b> — you are working with the patient, not on them.',
                '<b>Acceptance</b> — absolute worth, accurate empathy, support for autonomy, and affirmation.',
                '<b>Compassion</b> — acting in the patient’s interest.',
                '<b>Empowerment / evocation</b> — drawing out the patient’s own strengths and reasons rather than installing yours. The 4th edition (2023) frames this as empowerment, with evocation folded into it.',
            ]) + '<p><b>Four tasks</b> (called “processes” in earlier editions):</p>' + tbl(['Task', 'The question it answers'], [
                ['<b>Engaging</b>', 'Can we walk together? — rapport and a working relationship'],
                ['<b>Focusing</b>', 'Where are we going? — agree the target behaviour'],
                ['<b>Evoking</b>', 'Why go there? — draw out the patient’s own motivation'],
                ['<b>Planning</b>', 'How will we get there? — commitment and a concrete plan'],
            ]) + p('Resist the <b>fixing reflex</b> (formerly the “righting reflex”): the urge to correct the patient and argue for change.'),
            '<p><b>الروح</b> — الموقف الذي يجعل التقنيات تعمل:</p>' + ul([
                '<b>الشراكة</b> — أنت تعمل مع المريض لا عليه.',
                '<b>التقبّل</b> — القيمة المطلقة للشخص، والتعاطف الدقيق، ودعم الاستقلالية، والإشادة.',
                '<b>الرحمة</b> — التصرف لمصلحة المريض.',
                '<b>التمكين / الاستخراج</b> — استخراج نقاط قوة المريض وأسبابه هو لا غرس أسبابك. الطبعة الرابعة (2023) تصوغ هذا بوصفه «تمكينًا» يتضمن «الاستخراج».',
            ]) + '<p><b>المهام الأربع</b> (سُمّيت «عمليات» في الطبعات السابقة):</p>' + tbl(['المهمة', 'السؤال الذي تجيب عنه'], [
                ['<b>الإشراك (Engaging)</b>', 'هل يمكن أن نسير معًا؟ — الثقة وعلاقة العمل'],
                ['<b>التركيز (Focusing)</b>', 'إلى أين نتجه؟ — الاتفاق على السلوك المستهدف'],
                ['<b>الاستخراج (Evoking)</b>', 'لماذا نذهب إلى هناك؟ — استخراج دافعية المريض الذاتية'],
                ['<b>التخطيط (Planning)</b>', 'كيف سنصل؟ — الالتزام وخطة محددة'],
            ]) + p('قاوم <b>نزعة الإصلاح</b> (سُمّيت سابقًا «نزعة التصحيح»): الرغبة في تصحيح المريض والجدال لصالح التغيير.')),
        blk('mx', 'mi-oars', 'Core skills: OARS and Elicit–Provide–Elicit', 'المهارات الأساسية: OARS واستخرج–قدِّم–استخرج',
            tbl(['Skill', 'Example', 'Purpose'], [
                ['<b>O</b>pen questions', '“How do you see your smoking these days?”', 'Elicit the patient’s agenda and values'],
                ['<b>A</b>ffirmations', '“You’ve already cut down from 30 to 15 — that took real effort.”', 'Highlight strengths and past success'],
                ['<b>R</b>eflections', '“You’re worried about your breathing, and smoking is also how you unwind after work.”', 'Show you have heard; steer back if the visit drifts'],
                ['<b>S</b>ummaries', '“So you’ve tried before, the evenings were hardest, and now with the baby coming you want to try again.”', 'Tie it together and set up the next step'],
                ['<b>Elicit–Provide–Elicit</b>', '“What do you already know about…?” → “Would it be OK if I added something?” → “What do you make of that?”', 'Give information without triggering defensiveness'],
            ], wide=True) + ul([
                '<b>Aim for about two reflections per question.</b>',
                'Use <b>“and”</b> rather than “but” when you hold both sides of the ambivalence.',
                '<b>Develop discrepancy</b> when the patient does not connect the behaviour with what matters to them: “How does smoking fit with wanting to see your grandchildren grow up?”',
            ]),
            tbl(['المهارة', 'مثال', 'الغرض'], [
                ['<b>O</b> الأسئلة المفتوحة', '«كيف ترى تدخينك هذه الأيام؟»', 'استخراج أولويات المريض وقيمه'],
                ['<b>A</b> الإشادة', '«خفّضت من 30 إلى 15 سيجارة — هذا تطلّب جهدًا حقيقيًا.»', 'إبراز نقاط القوة والنجاحات السابقة'],
                ['<b>R</b> العبارات العاكسة', '«أنت قلق على تنفّسك، والتدخين أيضًا وسيلتك للاسترخاء بعد العمل.»', 'إظهار أنك سمعته؛ وإعادة الحوار لمساره إن تشتّت'],
                ['<b>S</b> التلخيص', '«إذن جرّبت من قبل، والمساء كان الأصعب، والآن مع قدوم المولود تريد أن تحاول مرة أخرى.»', 'ربط الحديث وتمهيد الخطوة التالية'],
                ['<b>استخرج–قدِّم–استخرج</b>', '«ماذا تعرف عن…؟» ← «هل تسمح أن أضيف شيئًا؟» ← «ما رأيك فيما قلته؟»', 'تقديم المعلومة دون إثارة الدفاعية'],
            ], wide=True) + ul([
                '<b>اجعل الهدف نحو عبارتين عاكستين لكل سؤال.</b>',
                'استخدم <b>«و»</b> بدل «لكن» حين تعكس طرفي التردد معًا.',
                '<b>ابنِ التباين</b> حين لا يربط المريض بين السلوك وما يهمّه: «كيف يتّسق التدخين مع رغبتك في أن ترى أحفادك يكبرون؟»',
            ])),
        blk('tool', 'tool-ruler', 'Readiness ruler', 'مسطرة الاستعداد', '', ''),
        blk('dx', 'mi-change-talk', 'Hearing change talk', 'التقاط «حديث التغيير»',
            ul([
                '<b>Preparatory change talk — DARN:</b> Desire (“I want to…”), Ability (“I could…”), Reasons (“It would help my…”), Need (“I have to…”).',
                '<b>Mobilising change talk — CAT:</b> Commitment (“I will…”), Activation (“I’m ready to…”), Taking steps (“I bought the patches”).',
                '<b>When you hear it, respond with EARS:</b> ask to Elaborate, Affirm, Reflect, Summarise — so the patient hears themselves argue for change.',
                '<b>Sustain talk</b> (reasons not to change) is normal — reflect it, don’t argue with it. <b>Discord</b> (tension in the relationship) is a signal to slow down, emphasise autonomy and shift focus.',
            ]),
            ul([
                '<b>حديث التغيير التمهيدي — DARN:</b> الرغبة («أريد أن…»)، القدرة («أستطيع أن…»)، الأسباب («سيفيد…»)، الحاجة («لا بد أن…»).',
                '<b>حديث التغيير التعبوي — CAT:</b> الالتزام («سوف…»)، التهيؤ («أنا جاهز لـ…»)، اتخاذ خطوات («اشتريت اللصقات»).',
                '<b>حين تسمعه استجب بـ EARS:</b> اطلب التوسّع، وأشِد، واعكس، ولخّص — ليسمع المريض نفسه وهو يدافع عن التغيير.',
                '<b>حديث الاستمرار</b> (أسباب عدم التغيير) أمر طبيعي — اعكسه ولا تجادله. أما <b>التنافر</b> (توتر في العلاقة) فإشارة لتبطئ وتؤكد استقلالية المريض وتغيّر محور الحديث.',
            ])),
        blk('evidence', 'mi-evidence', 'Evidence — read it critically', 'الدليل — اقرأه بعين ناقدة',
            ul([
                'Meta-analyses in medical settings support MI for alcohol, weight, blood pressure and HIV viral load, with modest but real effects.',
                '<b>Smoking is the exception to quote carefully.</b> The 2019 Cochrane review (37 trials, &gt;15,000 people) found low-certainty evidence and <b>no clear benefit</b> of MI over no treatment, as an add-on, or versus other support. Higher-intensity MI looked better than lower-intensity, but this did not survive removal of trials at high risk of bias.',
                'Practical reading: MI is the right <b>way to talk</b> with an ambivalent smoker; it is not a substitute for medication and structured cessation support once the patient is ready.',
            ]),
            ul([
                'تدعم التحليلات التجميعية في البيئات الطبية المقابلة التحفيزية في الكحول والوزن وضغط الدم والحمل الفيروسي لفيروس نقص المناعة، بآثار متواضعة لكنها حقيقية.',
                '<b>التدخين استثناء يجب ذكره بحذر.</b> وجدت مراجعة كوكرين 2019 (37 تجربة، أكثر من 15,000 شخص) دليلًا منخفض اليقين و<b>لا فائدة واضحة</b> للمقابلة التحفيزية مقارنة بعدم التدخل، أو كإضافة، أو مقارنة بدعم آخر. بدت الجرعة الأعلى أفضل من الأقل، لكن ذلك لم يصمد بعد استبعاد التجارب عالية خطر التحيّز.',
                'القراءة العملية: المقابلة التحفيزية هي <b>الطريقة الصحيحة للحديث</b> مع المدخن المتردد، لكنها ليست بديلًا عن الدواء والدعم المنظّم للإقلاع حين يصبح المريض مستعدًا.',
            ])),
        blk('trap', 'mi-traps', '⚠ Traps', '⚠ أخطاء',
            ul([
                'Closed question after closed question.',
                'Arguing for change — it pulls sustain talk out of the patient.',
                'Thinking MI simply means “being nice”. It is directional: you are listening for, and strengthening, change talk.',
                'Asking “why haven’t you stopped?” — it invites defence. Ask “why might you want to?”',
            ]),
            ul([
                'سؤال مغلق يتلوه سؤال مغلق.',
                'الجدال لصالح التغيير — يستخرج من المريض حديث الاستمرار.',
                'الظن أن المقابلة التحفيزية تعني «اللطف» فقط. هي موجَّهة: أنت تصغي لحديث التغيير وتقوّيه.',
                'سؤال «لماذا لم تتوقف؟» — يدعو للدفاع. اسأل «لماذا قد ترغب في ذلك؟»',
            ])),
        blk('local', 'mi-local', '⌖ Local context', '⌖ السياق المحلي',
            ul([
                '<b>Values that commonly carry discrepancy here:</b> children and parents, being a role model in the family, health as a trust from God (amanah), and the ability to perform prayer, fasting and pilgrimage comfortably.',
                '<b>Let the patient name the religious reason</b> — reflecting it back is powerful; preaching it is not, and can feel shaming.',
                '<b>Ramadan is ready-made self-efficacy evidence</b>: a month of daily abstinence from smoking and food during daylight hours proves the patient can go without.',
            ]),
            ul([
                '<b>قيم يتولّد منها التباين عادة هنا:</b> الأبناء والوالدان، وأن يكون قدوة في أسرته، والصحة أمانة من الله، والقدرة على أداء الصلاة والصيام والحج براحة.',
                '<b>دع المريض هو من يذكر السبب الديني</b> — عكسه له مؤثر جدًا؛ أما الوعظ به فلا، وقد يُشعره بالخجل.',
                '<b>رمضان دليل جاهز على الكفاءة الذاتية</b>: شهر من الامتناع اليومي عن التدخين والطعام في ساعات النهار يثبت أن المريض قادر على الاستغناء.',
            ])),
        blk('exam', 'mi-exam', '✎ Board pearl — the MI station', '✎ لؤلؤة البورد — محطة المقابلة التحفيزية',
            ul([
                'Score points visibly: open with an open question; use at least two reflections; ask permission before information; elicit the patient’s own reasons; finish with a summary and “What would you like to do next?”',
                'If the simulated patient pushes back, reflect and emphasise choice (“It’s your decision”) — never argue.',
            ]),
            ul([
                'اكسب الدرجات بوضوح: ابدأ بسؤال مفتوح؛ استخدم عبارتين عاكستين على الأقل؛ اطلب الإذن قبل المعلومة؛ استخرج أسباب المريض الخاصة؛ واختم بتلخيص وسؤال «ماذا تحب أن تفعل بعد ذلك؟»',
                'إن قاوم المريض المُحاكي فاعكس كلامه وأكّد حرية الاختيار («القرار قرارك») — ولا تجادل أبدًا.',
            ])),
    ])

# ─────────────────────────────────────────────────────────────
# 6 · BATHE
# ─────────────────────────────────────────────────────────────
BATHE = dict(
    id='bathe',
    h_en='BATHE',
    h_ar='BATHE',
    sub_en='Background · Affect · Troubles · Handling · Empathy — psychosocial care in about five minutes',
    sub_ar='الخلفية · المشاعر · المشكلات · التعامل · التعاطف — رعاية نفسية اجتماعية في نحو خمس دقائق',
    blocks=[
        blk('glance', 'bathe-at-a-glance', 'At a glance', 'لمحة سريعة',
            ul([
                '<b>What it is:</b> a structured set of questions and statements designed for primary care’s time limits (Stuart and Lieberman, <i>The Fifteen Minute Hour</i>).',
                '<b>Best for:</b> stress, distress, adjustment problems, somatic presentations and psychosocial issues.',
                '<b>Why it matters:</b> at least half of all mental-health encounters happen in primary care.',
                '<b>Evidence:</b> SORT B — higher patient satisfaction than usual care across several settings.',
            ]),
            ul([
                '<b>ما هو:</b> مجموعة منظّمة من الأسئلة والعبارات صُممت لحدود الوقت في الرعاية الأولية (ستيوارت وليبرمان، <i>ساعة الخمس عشرة دقيقة</i>).',
                '<b>الأنسب لـ:</b> الضغوط والضيق ومشكلات التكيّف والشكاوى الجسدية ذات المنشأ النفسي والقضايا النفسية الاجتماعية.',
                '<b>لماذا يهم:</b> نصف لقاءات الصحة النفسية على الأقل تحدث في الرعاية الأولية.',
                '<b>الدليل:</b> SORT B — رضا أعلى لدى المرضى مقارنة بالرعاية المعتادة في عدة بيئات.',
            ])),
        blk('features', 'bathe-steps', 'The five steps', 'الخطوات الخمس',
            tbl(['Step', 'First visit', 'Follow-up visit', 'Why'], [
                ['<b>B</b>ackground', '“What’s been going on in your life?”', '“What has happened since we last met?”', 'Focuses on the present situation, not a full history'],
                ['<b>A</b>ffect', '“How do you feel about that?” — or offer words: “Some people would feel angry, or exhausted. Does either fit?”', '“How are you feeling about it now — the same, or different?”', 'Names the emotion; helps patients who struggle to put feelings into words'],
                ['<b>T</b>roubles', '“What troubles you most about it?”', '“Last time the hardest part was ___. How is that now?”', 'Focuses the remaining minutes; avoids assumptions'],
                ['<b>H</b>andling', '“How are you managing?”', '“How could you approach it this week?”', 'Mobilises coping'],
                ['<b>E</b>mpathy', '“That sounds really hard.”', '“That sounds difficult — and you’re still here working on it.”', 'Closes the conversation with understanding'],
            ], wide=True),
            tbl(['الخطوة', 'الزيارة الأولى', 'زيارة المتابعة', 'لماذا'], [
                ['<b>B</b> الخلفية', '«ما الذي يجري في حياتك هذه الأيام؟»', '«ماذا حدث منذ لقائنا الأخير؟»', 'يركّز على الوضع الحالي لا على سيرة كاملة'],
                ['<b>A</b> المشاعر', '«كيف تشعر تجاه ذلك؟» — أو اقترح كلمات: «بعض الناس يشعرون بالغضب أو الإنهاك. هل ينطبق أحدهما؟»', '«كيف تشعر تجاهه الآن — كما كان أم تغيّر؟»', 'يسمّي الانفعال؛ ويساعد من يصعب عليه وصف مشاعره'],
                ['<b>T</b> المشكلات', '«ما أكثر ما يزعجك في الأمر؟»', '«المرة الماضية كان أصعب ما في الأمر ___. كيف هو الآن؟»', 'يركّز ما تبقّى من الوقت؛ ويمنع الافتراضات'],
                ['<b>H</b> التعامل', '«كيف تتدبّر الأمر؟»', '«كيف يمكن أن تتعامل معه هذا الأسبوع؟»', 'يستنهض مهارات التكيّف'],
                ['<b>E</b> التعاطف', '«يبدو هذا صعبًا فعلًا.»', '«يبدو صعبًا — ومع ذلك ما زلت تعمل عليه.»', 'يختم الحوار بالتفهّم'],
            ], wide=True)),
        blk('mx', 'bathe-handling', 'Making it work', 'كيف تجعله ينجح',
            ul([
                '<b>Background is not a full history.</b> Avoid the open-ended “tell me more about that” — it can consume the visit.',
                '<b>Don’t assume the trouble.</b> A patient whose marriage is ending may be most afraid of how to manage financially, not of the loss itself.',
                '<b>Match coping to controllability.</b> For a solvable problem, problem-focused coping (information, a plan). For the uncontrollable — a death, a terminal diagnosis — emotion-focused coping (support, meaning, activities that help get through) is associated with less distress.',
                '<b>Combine with medication</b> where a disorder is present, monitor the response, and refer if brief counselling achieves little.',
            ]),
            ul([
                '<b>الخلفية ليست سيرة مرضية كاملة.</b> تجنّب عبارة «حدّثني أكثر» المفتوحة — قد تستهلك الزيارة كلها.',
                '<b>لا تفترض المشكلة.</b> مريض ينتهي زواجه قد يكون أكثر خوفه من تدبير أموره المادية لا من الفقد نفسه.',
                '<b>طابِق التكيّف مع القابلية للتحكم.</b> للمشكلة القابلة للحل: تكيّف يركّز على المشكلة (معلومة، خطة). ولما لا يمكن التحكم فيه — وفاة، أو تشخيص مرض عضال — يرتبط التكيّف المركّز على المشاعر (الدعم، والمعنى، والأنشطة التي تعين على العبور) بضيق أقل.',
                '<b>اجمعه مع الدواء</b> حين يوجد اضطراب، وراقب الاستجابة، وأحِل إن لم يحقق الإرشاد المختصر إلا القليل.',
            ])),
        blk('special', 'bathe-special', 'Where to use it', 'أين تستخدمه',
            ul([
                'Frequent attenders and recurrent unexplained physical symptoms.',
                'Straight after breaking bad news.',
                '<b>Caregiver strain</b> — very common in multigenerational households caring for an older parent or a child with disability.',
                '<b>Diabetes distress</b> and the burden of any chronic disease.',
                'Life events: divorce, job loss, bereavement, a new baby.',
            ]),
            ul([
                'كثيرو المراجعة وأصحاب الأعراض الجسدية المتكررة غير المفسَّرة.',
                'مباشرة بعد إبلاغ خبر سيئ.',
                '<b>إرهاق مقدّمي الرعاية</b> — شائع جدًا في الأسر الممتدة التي ترعى والدًا مسنًا أو طفلًا ذا إعاقة.',
                '<b>ضيق السكري</b> وعبء أي مرض مزمن.',
                'أحداث الحياة: الطلاق، فقد العمل، الوفاة، قدوم مولود.',
            ])),
        blk('local', 'bathe-local', '⌖ Local context', '⌖ السياق المحلي',
            ul([
                'Distress here often arrives as headache, fatigue, chest tightness or pain. BATHE lets you open the emotional door without a label the patient may reject.',
                '<b>Religious coping is emotion-focused coping.</b> When the patient raises it, affirm it as a strength and build on it.',
            ]),
            ul([
                'كثيرًا ما يأتي الضيق هنا في صورة صداع أو إرهاق أو ضيق في الصدر أو ألم. يتيح لك BATHE فتح الباب العاطفي دون مسمّى قد يرفضه المريض.',
                '<b>التكيّف الديني تكيّف مركّز على المشاعر.</b> حين يذكره المريض، أكّد أنه نقطة قوة وابنِ عليه.',
            ])),
    ])
