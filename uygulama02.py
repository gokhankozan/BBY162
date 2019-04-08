#Yazar: Gökhan Kozan    Numara:21763436

sorular = ['Lionel Messi kaç kez Ballon d\'or ödülünü kazanmıştır?', \
           'İstanbul hangi yıl kültür başkenti seçilmiştir?', \
           'Türkçe hangi dil grubuna girmektedir?', \
           'Hangisi Türkiye\'nin komşusu değildir?', \
           'Depremin büyüklüğünü ölçen alete ne denir?']

cevaplar = ['C', 'D', 'A', 'B', 'C']

cevapA = ['3',\
          '2013',\
          'Ural-Altay',\
          'İran',\
          'Monograf']
cevapB = ['4',\
          '2012',\
          'Hint-Avrupa',\
          'Macaristan',\
          'Tomograf']
cevapC = ['5',\
          '2011',\
          'Hami-Sami',\
          'Gürcistan',\
          'Simograf']
cevapD = ['6',\
          '2010',\
          'Çin-Tibet',\
          'Bulgaristan',\
          'Sonografi']
puan=0
for i in range(len(sorular)):
    print("soru" +str(i+1) +":" + sorular[i])
    print("A)" + cevapA[i])
    print("B)" + cevapB[i])
    print("C)" + cevapC[i])
    print("D)" + cevapD[i])
    cevap=input("Cevabınız..? :")

    if cevaplar[i] == cevap.upper():
        print("Bravo!")
        puan +=2


    else:
        print("Malesef yanlış cevap!")
        print("Bu sorunun doğru cevabı:"+cevaplar[i])
        puan -= 1

print("Aldığınız not: "+str(puan*10))