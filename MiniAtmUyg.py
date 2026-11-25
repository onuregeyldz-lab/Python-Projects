import os

def miniatm():
    bakiye = 0

    while True:
        os.system("cls")

        print("===== MINI ATM =====\n")
        print("1 - Bakiye Görüntüle")
        print("2 - Para Yatır")
        print("3 - Para Çek")
        print("4 - Çıkış")

        secim = input("Seçiminiz: ")

        if secim == "4":
            os.system("cls")
            print("Çıkış Yapılıyor...")
            break

        elif secim == "2":
            os.system("cls")

            eklenecek_para = int(input("Yatırmak istediğiniz para miktarını giriniz: "))

            if eklenecek_para > 0:
                bakiye += eklenecek_para
                print("Paranız başarıyla eklendi.")
                print("Yeni bakiyeniz:", bakiye, "TL")

            else:
                print("Lütfen sıfırdan büyük bir miktar giriniz.")

            input("Ana ekrana dönmek için Enter'a basınız.")

        elif secim == "1":
            os.system("cls")

            print("Mevcut bakiyeniz:", bakiye, "TL")

            input("Ana ekrana dönmek için Enter'a basınız.")

        elif secim == "3":
            os.system("cls")

            alınacak_para = int(input("Çekmek istediğiniz para miktarını giriniz: "))

            if alınacak_para <= 0:
                print("Lütfen sıfırdan büyük bir miktar giriniz.")
                
            elif bakiye >= alınacak_para:
                bakiye -= alınacak_para

                print("Paranız başarıyla çekildi.")
                print("Yeni bakiyeniz:", bakiye, "TL")

            else:
                print("Bakiyeniz bu işlem için yetersiz.")

            input("Ana ekrana dönmek için Enter'a basınız.")

        else:
            print("Geçersiz seçim yaptınız.")
            input("Devam etmek için Enter'a basınız.")

miniatm()

