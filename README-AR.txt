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
- _redirects ............ الرابط القصير fitshilajitpro.com/go كيدي للإحالة ديالك (Cloudflare)
- _headers .............. الكاش ديال الملفات (Cloudflare)

رابط الإحالة المستعمل فكل الأزرار:
https://naturalshilajit.com/?rfsn=9125072.26616e

إلا بدلتي رابط الإحالة: فـ VS Code دير Ctrl+Shift+H (بحث واستبدال فجميع الملفات)
وبدل الرابط القديم بالجديد.

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
زيد ?clickid={click_id} فرابط الإعلان (مثلاً فـ MGID)، والموقع غادي يزيدو أوتوماتيكياً
لرابط الإحالة كـ subid. تأكد من Refersion واش كيقبل subid.
