---
language: Arabic (العربية)
code: ar
patterns: AR1-AR14
---

# Arabic language pack (حزمة العربية)

Loaded by `SKILL.md` when the text being edited is mostly Arabic. Read it together with the core skill; it does not replace anything there.

## Register (المستوى اللغوي)

Match the source. Default to فصحى معاصرة for articles, documentation, and formal posts. If the source or the user's sample is dialect (خليجي، نجدي، مصري، شامي، مغربي، عراقي، سوداني، يمني), stay in that dialect. Never "upgrade" dialect to فصحى or flatten a dialect word into its MSA synonym; that upgrade is itself an AI tell. Do not mix registers inside a paragraph unless the source does.

## What carries over from the core skill

Patterns 1-33 apply in Arabic too (inflated significance, rule of three, boldface, emojis, chatbot artifacts, hedging, and the rest). §14 applies with extra force: the em dash is rare in real Arabic typography, so it is a loud tell. The patterns below are the Arabic-specific ones, and the no-fabrication rule governs them exactly as it governs the English list.

## Arabic-specific patterns

### AR1. تضخيم الأهمية والإرث
**راقب:** نقطة تحوّل فارقة، علامة بارزة، بصمة لا تُمحى، إرث خالد، حجر الزاوية، مسيرة حافلة، شاهد على
**قبل:** يُعدّ افتتاح المكتبة عام 1989 نقطة تحوّل فارقة في مسيرة المدينة الثقافية، ليترك بصمة لا تُمحى في وجدان أبنائها.
**بعد:** افتُتحت المكتبة عام 1989.

### AR2. اللغة الترويجية (الحشو الإنشائي)
**راقب:** يزخر بـ، يتميّز بـ، غنيّ ومتنوّع، تحفة، جوهرة، منارة، لؤلؤة، ساحرة، خلّابة، عريق، يحتضن
**قبل:** تُعدّ صنعاء القديمة جوهرة معمارية تزخر بتاريخ عريق وتحتضن نسيجاً ثقافياً غنيّاً.
**بعد:** صنعاء القديمة مدينة تاريخية.

### AR3. ذيول التحليل ("مما يعكس")
**راقب:** مما يعكس، مما يبرز، مما يسهم في، مما يؤكد، الأمر الذي يعزز، ليجسّد، ليؤكد على، في خطوة تعكس
**Problem:** the Arabic twin of §3. A finished sentence gets a participial tail that adds interpretation nobody sourced.
**قبل:** افتُتح المصنع في المنطقة الصناعية، مما يعكس التوجّه نحو التنمية ويسهم في تعزيز الاقتصاد المحلي.
**بعد:** افتُتح المصنع في المنطقة الصناعية.

### AR4. تجنّب الجملة الاسمية البسيطة
**راقب:** يُعدّ، يُعتبر، يمثّل، يشكّل، يحظى بـ، يأتي ليكون، بمثابة
**Problem:** the Arabic twin of §8. Arabic does not need a copula at all, so these verbs are pure padding in front of a nominal sentence.
**قبل:** يُعتبر النقل العام أحد أهم الحلول، ويمثّل خياراً فعّالاً لتخفيف الازدحام.
**بعد:** النقل العام يخفّف الازدحام.

### AR5. الإفراط في "تم" و"قام بـ"
**Problem:** `تم + مصدر` hides the actor and `قام بـ + مصدر` inflates a verb that already exists (`قام بزيارة` for `زار`). Use the plain verb. Name the actor only when the source names one; otherwise keep the internal passive (`عُقد`, `نُوقشت`).
**قبل:** تم عقد الاجتماع وتمت مناقشة الخطة، ثم قام الفريق بتقديم التقرير.
**بعد:** انعقد الاجتماع ونوقشت الخطة، ثم قدّم الفريق التقرير.

### AR6. "حيث" و"الأمر الذي" كصمغ عام
**Problem:** `حيث` becomes a universal connector for place, time, cause, and relative clauses at once, often as the ungrammatical `حيث أنّ`. `الأمر الذي` and `وذلك` do the same job of gluing clauses that should be separate sentences.
**قبل:** زار الوفد المصنع حيث تم الاطلاع على الخطوط، حيث أنّ الإنتاج ارتفع، الأمر الذي أسعد الإدارة.
**بعد:** زار الوفد المصنع واطّلع على خطوط الإنتاج. الإنتاج ارتفع، وهذا أسعد الإدارة.

### AR7. الروابط المقحمة والاستطراد
**راقب:** بالإضافة إلى ذلك، علاوة على ذلك، ومن الجدير بالذكر، تجدر الإشارة إلى، وفي هذا السياق، في ظل، في إطار، ومن ناحية أخرى
**قبل:** وتجدر الإشارة إلى أنّ المشروع بدأ عام 2020، وفي هذا السياق، وفي إطار خطة التطوير، فقد استمر العمل.
**بعد:** بدأ المشروع عام 2020 ضمن خطة التطوير.

### AR8. الترادف المزدوج
**راقب:** الغني والمتنوع، الفريد والمميز، الشامل والمتكامل، الآمن والموثوق، التطور والازدهار، الدقيق والصارم
**Problem:** LLM Arabic pairs near-synonyms with `و` for rhythm. Keep one word.
**قبل:** تقدّم المنصة تجربة فريدة ومميزة ضمن بيئة آمنة وموثوقة.
**بعد:** تقدّم المنصة تجربة مختلفة ضمن بيئة آمنة.

### AR9. الخواتيم الوعظية
**راقب:** وفي الختام، وخلاصة القول، وفي نهاية المطاف، ويبقى X عنواناً لـ، ويبقى الأمل معقوداً، ولعلّ أبرز ما
**قبل:** وفي الختام، يبقى التعليم عنواناً للنهضة، ويبقى الأمل معقوداً على الأجيال القادمة.
**بعد:** (احذف الفقرة واختم بآخر معلومة فعلية.)

### AR10. الترجمة الحرفية
**راقب:** يلعب دوراً حاسماً، في نهاية اليوم، هذا هو السبب في أنّ، الأمر كله يتعلق بـ، لا يتعلق الأمر بـ... بل بـ، خذ خطوة إلى الوراء
**Problem:** English idiom and English word order dragged into Arabic. Watch for a subject opening every single sentence where a verb-first sentence is the natural Arabic shape.
**قبل:** في نهاية اليوم، الأمر لا يتعلق بالسرعة، بل يتعلق بالثقة. وهذا هو السبب في أنّ الفريق يلعب دوراً حاسماً.
**بعد:** الثقة أهم من السرعة، ولهذا يهمّ دور الفريق.

### AR11. سلاسل الإضافة والمصادر
**Problem:** stacked `مصدر` nouns (`عملية تطوير آليات تحسين مستوى جودة الأداء`) replace a verb that would say the same thing in three words.
**قبل:** تهدف عملية تطوير آليات تحسين مستوى جودة الأداء إلى تحقيق النتائج المرجوّة.
**بعد:** الهدف تحسين جودة الأداء.

### AR12. الاستهلال الخطابي والإعلان عن المحتوى
**راقب:** عزيزي القارئ، دعنا نستعرض، هيا بنا، سؤال يطرح نفسه، قبل أن نبدأ، في هذا المقال سنتناول، لنغص في التفاصيل
**قبل:** عزيزي القارئ، سؤال يطرح نفسه: ما أهمية النوم؟ في هذا المقال سنتناول الإجابة.
**بعد:** (ابدأ بالمعلومة نفسها بدل الإعلان عنها.)

### AR13. الترقيم والرسم الإملائي
**Rule:** use Arabic punctuation (`،` `؛` `؟` `«»`), not `,` `;` `?` `“”`. Keep one numeral system throughout, whichever the source uses (`١٢٣` or `123`). No tatweel (`ـــ`) for emphasis, no em or en dashes at all. Add tashkeel only where a word is genuinely ambiguous, or inside a Quranic or poetic quotation; sprinkled diacritics like `يُعَدُّ` in ordinary prose are a tell.
**قبل:** هل انتهى المشروع? نعم — تم التسليم في 2024, وبقيت مرحلة واحدة.
**بعد:** هل انتهى المشروع؟ نعم، سُلّم المشروع في 2024، وبقيت مرحلة واحدة.

### AR14. رتابة الإيقاع و"إنّ" المتكررة
**Problem:** LLM Arabic produces long sentences of near-identical length, all chained with `و`, and opens clause after clause with `إنّ`. Vary the length, break the chain into separate sentences, and drop `إنّ` unless it is doing real emphatic work.
**قبل:** إنّ المشروع يهدف إلى تحسين الخدمة، وإنّ الفريق يسعى إلى تطوير الأداء، وإنّ النتائج تبدو مشجّعة.
**بعد:** المشروع يهدف إلى تحسين الخدمة. الفريق يعمل على الأداء، والنتائج مشجّعة حتى الآن.

## ما لا يُعدّ دليلاً في العربية (false positives)

- **آيات قرآنية، أحاديث، شعر، أمثال، وأقوال منقولة.** Never rewrite quoted material, and keep its tashkeel and its original wording exactly.
- **الصيغ الدينية والدعائية** (بسم الله، إن شاء الله، صلى الله عليه وسلم، رحمه الله، حفظه الله). These are ordinary human writing, not decoration. Do not strip them.
- **السجع والجناس في نص أدبي متعمَّد.** Deliberate rhymed prose is a craft choice, not slop. Only cut it when the surrounding text is plainly informational.
- **الجمل الطويلة الموصولة بالواو.** Long coordinated sentences are native Arabic rhythm. Do not chop them into English-length staccato; that is a different tell, not a fix.
- **الألقاب والكنى** (أبو فلان، الشيخ، الدكتور، المهندس). Keep them as the source has them.
- **اختلاف الإملاء** (أ/ا، ة/ه، ى/ي، همزات). Human typing is uneven here. Do not treat it as an error to hunt, and do not introduce new errors either.

## علامات الكتابة البشرية العربية (احتفظ بها)

- **مفردة محلية أو لهجة مقحمة داخل نص فصيح**, and slang that belongs to one country or one decade.
- **تفصيل محدّد يصعب اختلاقه**: اسم حارة، سعر، موقف شخصي صغير، اسم محل.
- **السخرية والمبالغة الشخصية**, self-deprecation, and complaint. Models default to a polite civic tone.
- **رأي غير محسوم**: mixed feelings stated without resolving them.
- **الاستطراد بين قوسين وتصحيح الكاتب لنفسه** in the middle of a sentence.
