from random import choice, randint
import pandas as pd

data = pd.read_csv("sehirler.csv", encoding="UTF-8")

sehir_isimleri = data["BASLIK"]
rastgele_sehir = choice(sehir_isimleri)
harf_sayisi = len(rastgele_sehir)
print("""       TAHMİN OYUNUNA HOŞ GELDİNİZ
Her doğru tahmin şehrin harf sayısı kadar puan kazandırır.
Her ipucu kazanacağınız puanı 1 eksiltir.
İpucu almak için için ipucu yazınız.
Her şehir için 3 adet ipucu hakkınız vardır.
İpucu, şehrin içinde geçen bir harfi göstermektedir.
""")

print(f"Şehir {harf_sayisi} harflidir.")
print(f"Kelimenin ilk harfi => {rastgele_sehir[0]}")

deneme_hakki = 3
puan = 0
ipucu = 0
while True:
    cevap = input("Tahmininiz: ")
    if cevap == "ipucu" and ipucu <= 3:
        ipucu += 1
        sayi = randint(1, harf_sayisi-1)
        print(rastgele_sehir[sayi])
    elif cevap == "ipucu" and ipucu > 3:
        print("3 adet ipucu alabilirsiniz.")
        continue
    else:
        if cevap.upper() == rastgele_sehir.upper():
            print("Doğru bildiniz")
            puan += len(rastgele_sehir) - ipucu
            ipucu = 0
            print(f"Puanınız {puan}")
            karar = input("Oyuna Devam Etmek İster misiniz? Hayır için 0 / Evet için 1 ==> ")
            if karar == "0":
                print("Güle güle")
                break
            elif karar == "1":
                deneme_hakki = 3
                rastgele_sehir = choice(sehir_isimleri)
                harf_sayisi = len(rastgele_sehir)
                print(f"Şehir {harf_sayisi} harflidir.")
                print(f"Kelimenin ilk harfi => {rastgele_sehir[0]}")
                continue
            else:
                rastgele_sehir = choice(sehir_isimleri)
                harf_sayisi = len(rastgele_sehir)
                print(f"Şehir {harf_sayisi} harflidir.")
                print(f"Kelimenin ilk harfi => {rastgele_sehir[0]}")
                continue
        else:
            print("Yanlış tahmin")
            deneme_hakki -= 1
            if deneme_hakki < 1:
                print("Hakkınız bitti.")
                points -= harf_sayisi - ipucu
                ipucu = 0
                print(f"Doğru tahmin: {rastgele_sehir}")
                print(f"Puanınız {puan}")
                karar = input("Oyuna Devam Etmek İster misiniz? Hayır için 0 / Evet için 1 ==> ")
                if karar == "0":
                    print("Güle güle")
                    break
                elif karar == "1":
                    deneme_hakki = 3
                    rastgele_sehir = choice(sehir_isimleri)
                    harf_sayisi = len(rastgele_sehir)
                    print(f"Şehir {harf_sayisi} harflidir.")
                    print(f"Kelimenin ilk harfi => {rastgele_sehir[0]}")
                    continue
                else:
                    print("Yeniden oyna")
                    rastgele_sehir = choice(sehir_isimleri)
                    harf_sayisi = len(rastgele_sehir)
                    print(f"Şehir {harf_sayisi} harflidir.")
                    print(f"Kelimenin ilk harfi => {rastgele_sehir[0]}")
                    continue
            else:
                print(f"{deneme_hakki} hakkınız kaldı.")

