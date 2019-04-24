#Gökhan Kozan No:21763436
#1. soru
metin = "Açık bilim, araştırma çıktılarına ve süreçlerine herkesin serbestçe erişmesini, bunların ortak kullanımını, dağıtımını ve üretimini kolaylaştıran bilim uygulamasıdır."
print(metin[:20])

#2. soru
liste = ["Açık Bilim", "Açık Erişim", "Açık Lisans", "Açık Eğitim", "Açık Veri", "Açık Kültür"]
for i in liste:

    print(i)
#3. soru
sozluk = {"elma": "Ağaçta yetişen bir tür meyve" , "salatalık" : "Fidan üzerinde bir tür sebze"}
kelime= input("kelimeyi giriniz:")

print(sozluk == kelime.lower())
while True:

    if kelime =="elma":
       print("Aradığınız kelime var")
       print(sozluk["elma"])
       break
    elif kelime == "salatalık":
       print("aradığınız kelime var")
       print(sozluk["salatalık"])
       break
    else:
       print("Aradığınız kelime yok.")
       break