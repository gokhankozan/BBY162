#Yazar: Gökhan Kozan No. 21763436

import random
import sys

kelimeListesi = [
"kule", "savaş", "ölüm", "salata", "ayakkabı", "sağlık", "futbol", "marangoz",
 "zürafa", "barış", "subjektif", "fındıkzade", "rabona", "trivela", "marjinal"
           ]

kelime_tahmin = []
gizliKelime = random.choice(kelimeListesi)
kelime_uzunluğu = len(gizliKelime)
alfabe = "abcçdefgğhıijklmnoöprsştuüvyz"
harf_boyutu = []




def giris():

    while True:
        print("Adam asmacaya hoşgeldin!")
        secim = input("Oynamak istiyor musun?\n").lower()

        if secim == "evet" or secim == "e":
            break
        elif secim == "hayır" or secim == "h":
            sys.exit("Hoşçakal!")
        else:
            print("Lütfen evet ya da hayır de!")
            continue


giris()



def tanım():

    for karakter in gizliKelime:
        kelime_tahmin.append("-")

    print("Tahmin edeceğin kelime", kelime_uzunluğu, "karakter.")

    print("A-Z arasında bir harf seçmelisin.")

    print("5 canın var ve aynı harfi seçtiğin zaman canında değişiklik olmaz.\n\n")

    print(kelime_tahmin)



def tahmin():
    tahmin_edilen = 0

    while tahmin_edilen < 5:

        print("Kalan can: ", 5-tahmin_edilen)

        tahmin = input("Bir harf yaz\n").lower()


        if not tahmin in alfabe:
            print("A ve Z arasında bir harf yaz!")
        elif tahmin in harf_boyutu:
            print("Bu harfi zaten seçtin!")
        else:

            harf_boyutu.append(tahmin)
            if tahmin in gizliKelime:
                print("Doğru!")
                for x in range(0, kelime_uzunluğu):
                    if gizliKelime[x] == tahmin:
                        kelime_tahmin[x] = tahmin
                        print(kelime_tahmin)

                if not '-' in kelime_tahmin:
                    print("Bravo!")
                    break
            else:
                print("Kelimede bu harf yok. Yeniden dene!")
                tahmin_edilen += 1
                if tahmin_edilen == 10:
                    print("Üzgünüm, kaybettin! cevap:",         gizliKelime)


tanım()
tahmin()

print("Oyun bitti!")