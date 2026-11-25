import os

kitap_listesi = []
yazar_listesi = []
def kütüphanesistemi():

    while True:
        # YAZILAR
        os.system("cls")
        print("** KÜTÜPHANE SİSTEMİ **\n")
        print(
            "1- Kitap Ekle\n"
            "2- Kitapları Listele\n"
            "3- Kitap Ara\n"
            "4- Kitap Ödünç Ver\n"
            "5- Kitap İade Et\n"
            "6- Çıkış\n"
        )

        secim = int(input("Seçim Yapınız: "))

        # DEFLER
        def kitap_ekle():
            os.system("cls")
            kitap_adı = input("Kitap Adı: ")
            yazar_adı = input("Yazar Adı: ")

            kitap_listesi.append(kitap_adı)
            yazar_listesi.append(yazar_adı)

            print("\nBaşarıyla Eklendi. Ana Ekran için Enter'a Basınız.")
            input()

        def kitap_listele():
            os.system("cls")
            if len(kitap_listesi) == 0:
                print("Kitap Listeniz Boş!!")
                print("Ana Ekran İçin Enter'a Basınız.")
                input()

            else:
                print("** Kitap Listele **\n")
                for i in range(len(kitap_listesi)):
                    print(kitap_listesi[i] ,"-", yazar_listesi[i])

                input()


        def kitap_ara():
            os.system("cls")
            istenen_kitap = input("Bulmak İstediğiniz Kitapın İsmini Giriniz: ")

            if istenen_kitap in kitap_listesi:
                print("\nKitap Listede Bulunmaktadır...")
                print("Ana Ekran İçin Enter'a Basınız.")
                input()

            else:
                print("\nKitap Listede Bulunmamaktadır...")
                print("Ana Ekran İçin Enter'a Basınız.")
                input

        
        def ödünç_ver():
            os.system("cls")
            almakistenilen_kitap = input("Almak İstediğiniz Kitap İsmini Giriniz:")

            if almakistenilen_kitap not in kitap_listesi:
                print("\nAlmak İstediğiniz Kitap Listede Bulunmamaktadır...")
                print("Ana Ekran İçin Enter'a Basınız.")
                input()

            else:
                kitap_listesi.remove(almakistenilen_kitap)
                print("Kitap Alımı Başarılı İyi Günlerde Kullanın:)")
                print("Ana Ekran İçin Enter'a Basınız.")
                input()


        def iade_et():
            os.system("cls")
            iadeedilecek_kitap = input("İade Edilecek Kitapın İsmini Giriniz: ")
            yazar_adı = input("Yazar Adını Giriniz: ")

            kitap_listesi.append(iadeedilecek_kitap)
            yazar_listesi.append(yazar_adı)

            print("Kitap Başarıyla İade Edildi.")
            print("Ana Ekran İçin Enter'a Basınız.")
            input()

        # İFLER

        if secim == 1:
            kitap_ekle()

        elif secim == 2:
            kitap_listele()

        elif secim == 3:
            kitap_ara()

        elif secim == 4:
            ödünç_ver()

        elif secim == 5:
            iade_et()

        elif secim == 6:
            os.system("cls")
            print("Çıkış Yapılıyor..")
            break

        else:
            print("Yanlış Seçim Yaptınız. Enter'a Basınız")

kütüphanesistemi()