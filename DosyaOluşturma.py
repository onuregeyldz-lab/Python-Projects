
import os

klasor = "OgrenciKayitlari"
dosya = os.path.join(klasor, "ogrenciler.txt")


# Klasör oluşturma
def klasor_olustur():
    if not os.path.exists(klasor):
        os.mkdir(klasor)
        print("Klasör oluşturuldu.")
        print(os.getcwd())
    else:
        print("Klasör zaten mevcut.")


# Öğrenci ekleme
def ogrenci_ekle():
    os.system("cls")

    ad = input("Öğrencinin adını giriniz: ")

    try:
        puan = float(input("Öğrencinin puanını giriniz: "))

        if puan < 0 or puan > 100:
            print("Puan 0 ile 100 arasında olmalıdır.")
            input("Devam etmek için Enter'a basınız...")
            return

    except ValueError:
        print("Lütfen geçerli bir sayısal puan giriniz.")
        input("Devam etmek için Enter'a basınız...")
        return

    with open(dosya, "a", encoding="utf-8") as f:
        f.write(ad + "," + str(puan) + "\n")

    print("Öğrenci başarıyla kaydedildi.")
    input("Devam etmek için Enter'a basınız...")


# Öğrencileri listeleme
def ogrencileri_listele():
    os.system("cls")

    if not os.path.exists(dosya):
        print("Henüz öğrenci kaydı bulunmuyor.")

    else:
        with open(dosya, "r", encoding="utf-8") as f:
            kayitlar = f.readlines()

        if len(kayitlar) == 0:
            print("Öğrenci listesi boş.")

        else:
            print("** ÖĞRENCİ LİSTESİ **\n")

            for kayit in kayitlar:
                ad, puan = kayit.strip().split(",")
                print("Öğrenci:", ad, "| Puan:", puan)

    input("\nAna menüye dönmek için Enter'a basınız...")


# Öğrenci arama
def ogrenci_ara():
    os.system("cls")

    if not os.path.exists(dosya):
        print("Henüz öğrenci kaydı bulunmuyor.")
        input("Devam etmek için Enter'a basınız...")
        return

    aranan = input("Aranacak öğrencinin adını giriniz: ")
    bulundu = False

    with open(dosya, "r", encoding="utf-8") as f:
        for kayit in f:
            ad, puan = kayit.strip().split(",")

            if ad.lower() == aranan.lower():
                print("Öğrenci:", ad)
                print("Puan:", puan)
                bulundu = True

    if not bulundu:
        print("Öğrenci bulunamadı.")

    input("Devam etmek için Enter'a basınız...")


# Not analizi
def not_analizi():
    os.system("cls")

    if not os.path.exists(dosya):
        print("Analiz edilecek öğrenci kaydı bulunmuyor.")
        input("Devam etmek için Enter'a basınız...")
        return

    puanlar = []

    with open(dosya, "r", encoding="utf-8") as f:
        for kayit in f:
            ad, puan = kayit.strip().split(",")
            puanlar.append(float(puan))

    if len(puanlar) == 0:
        print("Öğrenci listesi boş.")

    else:
        ortalama = sum(puanlar) / len(puanlar)
        en_yuksek = max(puanlar)
        basarili = 0

        for puan in puanlar:
            if puan >= 50:
                basarili += 1

        print("Öğrenci sayısı:", len(puanlar))
        print("Not ortalaması:", round(ortalama, 2))
        print("En yüksek puan:", en_yuksek)
        print("Başarılı öğrenci sayısı:", basarili)
        print("Başarısız öğrenci sayısı:", len(puanlar) - basarili)

    input("Ana menüye dönmek için Enter'a basınız...")


# Ana program
klasor_olustur()

while True:
    os.system("cls")

    print("===== ÖĞRENCİ KAYIT SİSTEMİ =====\n")
    print("1- Öğrenci Ekle")
    print("2- Öğrencileri Listele")
    print("3- Öğrenci Ara")
    print("4- Not Analizi")
    print("5- Çıkış")

    secim = input("\nSeçiminiz: ")

    if secim == "1":
        ogrenci_ekle()

    elif secim == "2":
        ogrencileri_listele()

    elif secim == "3":
        ogrenci_ara()

    elif secim == "4":
        not_analizi()

    elif secim == "5":
        print("Programdan çıkılıyor...")
        break

    else:
        print("Geçersiz seçim!")
        input("Devam etmek için Enter'a basınız...")

