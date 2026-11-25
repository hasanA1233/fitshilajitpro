موقع FitShilajitPro — HTML / CSS / JavaScript
=============================================

شنو كاين فالملف:
- index.html ............ اللاندينغ بيج (الصفحة الرئيسية)
- blog/ ................. صفحة المدونة + 12 مقال (كل مقال فدوسي بوحدو)
- affiliate-disclosure/, privacy-policy/, terms/ ... الصفحات القانونية
- 404.html .............. صفحة "الصفحة غير موجودة"
- assets/style.css ...... التصميم
- assets/main.js ........ القائمة فالموبايل، نسخ الكود، تتبع subid
- assets/og-image.png ... الصورة اللي كتبان ملي تبارطاجي الرابط
- sitemap.xml, robots.txt ... للسيو (Google)
- _redirects ............ الرابط القصير fitshilajitpro.com/go/shilajit كيدي للإحالة ديالك (Cloudflare)
- _headers .............. الكاش ديال الملفات (Cloudflare)

رابط الإحالة (Pure Himalayan Shilajit):
https://www.purehimalayanshilajit.com/?ref=4878

جميع الأزرار كيمشيو لـ /go/shilajit. إلا بدلتي رابط الإحالة، بدلو غير فـ _redirects
(سطر واحد لكل قاعدة) — ما تحتاجش تبدل حتى صفحة.

مكون CTA (assets/style.css): .aff-box (صندوق صغير بعد المقدمة) و .aff-box--lg (صندوق كبير فالأخير).
الصورة: assets/pure-himalayan-shilajit-cta.webp (المصدر SVG حداها).

النشر على Cloudflare Pages مع GitHub:
1) صاوب repo جديد فـ GitHub، وطلع فيه هاد الملفات كاملين (المحتوى ديال هاد الدوسي، ماشي الدوسي براسو).
2) Cloudflare ← Workers & Pages ← Create ← Pages ← Connect to Git ← اختار الـ repo.
3) Framework preset: None
   Build command: (خليها خاوية)
   Build output directory: /
4) Save and Deploy ← من بعد زيد الدومين فـ Custom domains.

من بعد النشر:
- Google Search Console ← زيد الموقع ← Sitemaps ← صيفط: sitemap.xml

الصور:
المنتجات معروضين برسمة ديال بوطة (SVG). إلا بغيتي صور حقيقية، حطهم فـ assets/
ومن بعد بدل الرسمة بـ <img src="/assets/اسم-الصورة.jpg" alt="...">.

تتبع الإعلانات (Native Ads):
مطفي دابا. إلا أكد ليك البرنامج ديال Pure Himalayan Shilajit أنه كيقبل subid،
بدل AFFILIATE_SUBID_PARAM فـ assets/main.js من null لـ 'subid'.
