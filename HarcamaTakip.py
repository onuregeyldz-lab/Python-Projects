import os

harcama = []
fiyat = []

def harcamatakip():
    while True:
        # Yazılar
        os.system("cls")
        print("** HARCAMA TAKİP SİSTEMİ **\n")
        print(
            "1- Harcama Ekle\n"
            "2- Harcamaları Listele\n"
            "3- Toplam Harcama\n"
            "4- En Yüksek Harcama\n"
            "5- Harcama Sil\n"
            "6- Çıkış\n"
        )

        secim = input("Seçiminiz: ")

        # Defler

        def harcama_ekle():
            os.system("cls")
            harcama_adi = input("Harcama Adını Giriniz: ")
            para = int(input("Fiyatını Giriniz: "))

            harcama.append(harcama_adi)
            fiyat.append(para)

            print("\nBaşarıyla Eklendi...")
            print("Ana Ekrana Dönmek İçin Enter'a Basınız...")
            input()

        def harcama_listele():
            os.system("cls")

            if len(fiyat) == 0:
                print("HARCAMA LİSTENİZ BOŞTUR")
                print("Ana Ekrana Dönmek İçin Enter'a Basınız...")
                input()

            else:
                print("** Harcama Listesi **\n")

                for i in range(len(harcama)):
                    print(harcama[i] , "-" , fiyat[i] , "TL")
                    input()

        def toplam_harcama():
            os.system("cls")

            toplam = 0

            if len(harcama) == 0:
                print("Hiçbir Harcamanız Yoktur")
                print("Ana Ekrana Dönmek İçin Enter'a Basınız...")
                input()

            else:
                for tutar in fiyat:
                    toplam += tutar

                print("Toplam Harcamanız:",toplam,"TL")
                print("Ana Ekrana Dönmek İçin Enter'a Basınız...")
                input()


        def enyüksek_harcama():
            os.system("cls")
            if len(harcama) == 0:
                print("Hiçbir Harcamanız Yoktur")
                print("Ana Ekrana Dönmek İçin Enter'a Basınız...")
                input()

            else:
                enyuksek = max(fiyat)

                print("En Yüksek Harcama =",enyuksek,"TL")
                print("Ana Ekrana Dönmek İçin Enter'a Basınız...")
                input()

            


        def harcama_sil():
            os.system("cls")

            harcamaadi = input("Silmek İstediğiniz Harcama İsmini Giriniz: ")

            if harcamaadi not in harcama:
                print("Bu Harcama Listede Bulunmamaktadır.")
                print("Ana Ekrana Dönmek İçin Enter'a Basınız...")
                input()

            else:
                y = int(input("Harcacamınızın Fiyatını Giriniz: "))

                if y not in fiyat:
                    print("Bu Harcama Listede Bulunmamaktadır.")
                    print("Ana Ekrana Dönmek İçin Enter'a Basınız...")
                    input()

                else:

                    harcama.remove(harcamaadi)
                    fiyat.remove(y)

                    print("Silme İşlemi Tamamlandı İyi Günler Dileriz <3")
                    print("Ana Ekrana Dönmek İçin Enter'a Basınız...")
                    input()

        # İfler

        if secim == "1":
            harcama_ekle()

        elif secim == "2":
            harcama_listele()

        elif secim == "3":
            toplam_harcama()

        elif secim == "4":
            enyüksek_harcama()

        elif secim == "5":
            harcama_sil()

        elif secim == "6":
            os.system("cls")
            print("Çıkış Yapılıyor...")
            break

        else:
            os.system("cls")
            print("Yanlış Seçim Yaptınız...")
            input("Ana Ekran İçin Enter'a Basınız...")

harcamatakip()