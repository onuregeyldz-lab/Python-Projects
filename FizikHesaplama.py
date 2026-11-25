import os

def fizikhes():
    while True:
        os.system("cls")
    # Yazılar

        print("** FİZİK HESAPLAMA UYGULAMASI **\n")
        print(
            "1- Hız Hesaplama\n"
            "2- Yol Hesaplama\n"
            "3- Zaman Hesaplama\n"
            "4- Sürat Hesaplama\n"
            "5- Çıkış\n"
        )
        secim = int(input("Seçiminiz: "))

        # Defler

        def hız_hesaplama():
            os.system("cls")
            yer_değiştirme = int(input("Yer Değiştirmeyi Giriniz: "))
            zaman = int(input("Zamanı Saniye Cinsinden Giriniz: "))

            hız = yer_değiştirme // zaman

            print("\nHız =",hız,"m/s")
            input()

        def yol_hesaplama():
            os.system("cls")
            hız = int(input("Hızınızı Giriniz: "))
            zaman = int(input("Zamanı Süre Cinsinden Giriniz: "))

            yol = hız * zaman

            print("\nToplam Yolunuz =",yol,"Metre")
            input()

        def zaman_hesaplama():
            os.system("cls")
            yol = int(input("Toplam Yolunuzu Giriniz: "))
            hız = int(input("Hızınızı Giriniz: "))

            zaman = yol // hız

            print("\nToplam Zamanınız =",zaman,"Saniye")
            input()


        def sürat_hesaplama():
            os.system("cls")
            yol = int(input("Toplam Alınan Yolu Giriniz: "))
            zaman = int(input("Zamanı Saniye Cinsinde Giriniz: "))

            sürat = yol // zaman

            print("\nSüratiniz =",sürat,"M/S")
            input()


        #  İfler

        if secim == 1:
            hız_hesaplama()

        elif secim == 2:
            yol_hesaplama()

        elif secim == 3:
            zaman_hesaplama()

        elif secim == 4:
            sürat_hesaplama()

        elif secim == 5:
            os.system("cls")
            print("Çıkış Yapılıyor...")
            break

        else:
            os.system("cls")
            print("Yanlış Seçim Yaptınız..")
            print("Ana Ekrana Dönmek İçin Enter'a Basınız...")
            input()        
fizikhes()