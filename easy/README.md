# encapsulation_abstruction

8-dars. OOP(Object Oriented Programming). Encapsulation and Abstraction.

—------------------------------------------------------------------------------------------------------------------------

Oson 

1- masla  
 "Xodim ma’lumotlari" klassini yaratish
Shart: Xodim nomli klass yarating. Bu klassda xodimning ism-familiyasi, yoshi, va lavozimi haqida ma’lumot saqlansin.
Qoidalangan: Ma’lumotlarni o‘zgartirish uchun maxsus metodlar (getter va setter) yozing. Lavozimni o‘zgartirganda, yangi lavozim bo‘sh emasligini tekshiring.





2  - masala
"Telefon" klassi
Shart: 
Telefon klassini yarating, unda ism va telefon raqami juftligini saqlang.
Qoidalangan: Faqatgina metodlar orqali yangi kontakt qo‘shish va mavjud kontaktni olish imkoniyatini bering.



3 -  masala  
"Hayvonot bog‘i boshqaruvi"
Shart:
 Hayvon bazaviy klassini yarating, unda umumiy atributlar bo‘lsin (turi, yoshi). Yirtqich va O‘txo‘r klasslarini voris qilib, o‘ziga xos atributlar va metodlar qo‘shing.
4-masala
 Avtomobil Classi
Elementlar:
Nom (private)
Marka (private)
Narx (private)
Shart: Getter va Setter yordamida narxni o‘zgartiring. Agar narx manfiy bo‘lsa, xato xabar chiqaring.




5  -  masala
Transport Yaratish Factory
OTA_Class: Transport
Method: harakat qilish (abstrakt)
BOLA_Classlar: Avtobus, Poezd
Avtobus: avtobus uchun maxsus harakat rejasi
Poezd: faqat relsda harakatlanadi
Shart: Transport obyektini yaratish uchun factory methoddan foydalaning.


—------------------------------------------------------------------------------------------------------------------------


O’rta

1 -  masala
Avtomobil Classi:
Public: Model, Rang
Private: Narx, Marka, Ishlab chiqarilgan yil
Shartlar: 
Getter bilan narx va ishlab chiqarilgan yilni ko‘rsating.
Setter yordamida narxni yangilang (agar yangi narx manfiy bo‘lsa, xato xabar chiqaring).
Rangni bevosita o‘zgartirish mumkin bo‘lsin.


2  -  masala
Hayvonot Classlari
OTA_Class: Hayvon
Xususiyatlar: turi, vazni
Method: ovoz chiqarish (abstrakt)
BOLA_Classlar: It, Mushuk
It: ovoz sifatida "vov-vov"
Mushuk: ovoz sifatida "miyov-miyov"
Shart: Turli hayvonlarning ovoz chiqarishini model qiling.

3  -  masala  
O‘quv Markazi Classlari
OTA_Class: O‘quvMarkazi
Method: dars o‘tkazish (abstrakt)
BOLA_Classlar: ITMarkazi, TilMarkazi
ITMarkazi: dasturlash darslari o‘tkazadi
TilMarkazi: xorijiy til darslari o‘tkazadi
Shart: Har bir markazda turli xil darslar o‘tkaziladi.


4-masala
Kitobdo‘kon Classi
Elementlar:
Do‘kon nomi
Joylashuvi
Kitoblar ro‘yxati
Xizmatlar
Shart:
Kitoblar ro‘yxatida ilmiy kitoblar bo‘lgan do‘konlar haqida ma'lumot chiqaring.

5 -  masala  

Book nomli class yarating.
Unda quyidagi property (xususiyatlar) bo‘lsin:
Name: Kitob nomi
Page_count: Kitobning sahifalar soni
Price: Kitobning narxi
Ushbu classdan 5 ta obyekt yarating.
Har bir obyekt uchun foydalanuvchi nom, sahifalar soni va narxni kiritishi kerak.
Quyidagi amallarni bajaradigan methodlar yozing:
Sahifa sonini oshirish: Har bir kitobning sahifa sonini 10 taga oshiradigan method yozing.
Narxni kamaytirish: Agar sahifa soni 100 dan ko‘p bo‘lsa (oshirilganidan keyin), ushbu kitobning narxini 2 baravar kamaytiradigan method yozing.
Natijada barcha obyektlarning yangi ma’lumotlarini ekranga chiqaring.



—------------------------------------------------------------------------------------------------------------------------

Qiyin
1 -  masala  
 Robot Classi
Elementlar:
Public: Model raqami, Ishlovchi hududi
Private: Zaryad darajasi, Maksimal ish vaqti, Status (Ishlayapti / Kutmoqda)
Shartlar:
Getter orqali zaryad darajasini ko‘rsating, lekin agar daraja 20% dan past bo‘lsa, "Zaryadlash kerak" xabari chiqsin.
Maksimal ish vaqtini setter orqali yangilang, lekin bu 12 soatdan oshmasligi kerak.
Statusni faqat getter orqali ko‘ring, "Kutmoqda" bo‘lsa, zaryadni avtomatik 100% ga o‘rnatish amalga oshsin.

2- masala
Taksi Classi
Elementlar:
Public: Haydovchi ismi, Mashina nomi
Private: Narx, Yo‘nalish, Bo‘sh joylar soni
Shartlar:
Getter yordamida narxni oling.
Setter yordamida bo‘sh joylarni yangilang (agar 0 dan kam bo‘lsa, xato xabar chiqaring).
Haydovchi va mashina nomini bevosita oling va o‘zgartiring.


3 -  masala
Mashina Classi
Elementlar:
Public: Model, Rangi
Private: Tezlik, Narx, Yoqilg‘i turi
Shartlar:
Getter orqali tezlikni ko‘rsating.
Yoqilg‘i turini setter orqali o‘zgartiring.
Model va rangni bevosita oling va o‘zgartiring.

4 -  masala
Laptop Class:
Laptop classini yarating, atributlari:
brand,
price,
battery_life (batareya vaqti, soatlarda).
Quyidagi metodlarni yozing:
apply_discount(percent) — narxini percent ga pasaytirsin.
Agar batareya vaqti 5 soatdan kam bo‘lsa, narxini 10% pasaytiruvchi metod qo‘shing.

5  -  masla 

Developer Klassini Yaratish
1. Developer nomli klassni yarating. U quyidagi atributlarga ega bo‘lsin:
Surname (Familiyasi): Xodimning familiyasi.
Position (Lavozimi): Xodimning lavozimi (Junior, Middle, Senior).
Salary (Oyligi): Xodimning asosiy oyligi.

2. SoftwareEngineer Klassini Yaratish
SoftwareEngineer nomli klassni yarating, u Developer klassidan voris bo‘lsin. Qo‘shimcha atributlar:
Bonus (Ustama haqi): Oylikka qo‘shiladigan ustama.
Department (Bo‘lim): Xodim qaysi bo‘limda ishlaydi (1-bo‘lim, 2-bo‘lim, yoki 3-bo‘lim).

3. Masala Sharti
SoftwareEngineer klassidan 5 ta obyekt yarating va har birining quyidagi ma’lumotlarini foydalanuvchi kiritishi kerak:
Familiyasi, lavozimi, asosiy oyligi, ustama haqi, va bo‘limi.
Har bir bo‘lim uchun umumiy to‘langan maoshni hisoblang. Bu quyidagicha bo‘ladi:
Umumiy maosh = asosiy oylik + ustama haqi.
Natijada har bir bo‘lim uchun jami maosh summasini chiqaring.
