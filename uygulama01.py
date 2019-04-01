
cevaplar = ['a', 'c', 'b', 'b', 'a']
puan = 0
#soru1
soru1 = "Türkiye\'nin başkent" \
        "i aşağıdaki illerimiziden hangisidir? \nA)Ankara B)Bursa C)Trabzon"

cevap = input(soru1 + "\n Lütfen cevabınızı giriniz: ")
if cevaplar[0] == cevap.lower():
    print("Tebrikler")
    puan += 1
else:
    print("Üzgünüm! Cevabınız yanlış")
    puan -= 1
#soru2
soru2 = "İstanbul\'un fethi kaç yılında gerçekleşmiştir? \nA)1563 B)1722 C)1453"

cevap = input(soru2 + "\n Lütfen cevabınızı giriniz: ")
if cevaplar[1] == cevap.lower():
    print("Tebrikler")
    puan += 1
else:
    print("Üzgünüm! Cevabınız yanlış")
    puan -= 1
    #soru3
soru3 = "Futbolun kralı olarak bilinen Allah ayağına zeval vermesin dediğimiz eski futbolcu kimdir? \n A)Gheorge Hagi B)Alex de souza C)Tuncay Şanlı"
cevap = input(soru3 + "\n Lütfen cevabınızı giriniz: ")
if cevaplar[2] == cevap.lower():
    print("Tebrikler")
    puan += 1
else:
    print("Üzgünüm! Cevabınız yanlış")
    puan -= 1
#soru4
soru4 ="\"Gönüldağı\" şarkışı hangi sanatçımıza aittir? \n A)Yıldız Tilbe B)Neşet Ertaş C)Müslüm Gürses"
cevap = input(soru4 + "\n Lütfen cevabınızı giriniz: ")
if cevaplar[3] == cevap.lower():
    print("Tebrikler")
    puan += 1
else:
    print("Üzgünüm!Yanlış cevap")
    puan -= 1
#soru5
soru5 = "Edebiyatımızdaki ilk psikolojik roman aşağıdakilerden hangisidir? \n A)Eylül B)Araba Sevdası C)Makber"
cevap = input(soru5  + "\n Lütfen cevabınızı giriniz: ")
if cevaplar[4] == cevap.lower():
    print("Tebrikler")
    puan += 1
else:

    print("Üzgünüm! Cevabınız yanlış")
    puan -= 1
print ("Testi bitirdiniz,bu testen aldığınız puan: "+str(puan*20))



