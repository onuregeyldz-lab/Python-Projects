import os

ürünler = []
Fiyat = []
Stok = []

def stoksistemi():
    while True:
        os.system("cls")
        # Yazılar
        print("===== STOK TAKİP SİSTEMİ =====\n") 
        print("1 - Ürün Ekle") 
        print("2 - Ürünleri Listele") 
        print("3 - Ürün Ara") 
        print("4 - Ürün Sil") 
        print("5 - Ürün Güncelle") 
        print("6 - Çıkış")

        secim = int(input("\nSeçiminiz: "))

        # Defler

        def ürün_ekle():
            os.system("cls")
            ad = input("Ürün Adını Giriniz: ")
            fiyat = int(input("Ürün Fiyatını Giriniz: "))
            miktar = int(input("Ürün Stoğunu Giriniz: "))

            ürünler.append(ad)
            Fiyat.append(fiyat)
            Stok.append(miktar)

            print(ad,", Başarıyla Eklendi.")
            print("Ana Ekrana Dönmek İçin Enter'a Basınız.")
            input()

        def ürün_listele():
            os.system("cls")
            sayı = len(ürünler)

            if sayı == 0:
                print("Listenizde Ürün Bulunmamaktadır.")
                input()

            else:
                print("** Kitap Listesi **\n")

                for i in range(len(ürünler)):
                    print(ürünler[i], "|","Fiyat :",Fiyat[i],"TL","|","Stok :",Stok[i])
                input()

        def ürün_ara():
            os.system("cls")
            bulmak_ürün = input("Bulmak İstediğiniz Ürün Adı: ")

            if bulmak_ürün not in ürünler:
                print("Ürün Listede Bulunmamaktadır.")
                print("Ana Ekrana Dönmek İçin Enter'a Basınız.")
                input()

            else:
                fiyatürün = int(input("Bulmak İstediğiniz Ürünün Fiyatını Giriniz: "))

                if fiyatürün not in Fiyat:
                    print("Ürün Listede Bulunmamaktadır.")
                    print("Ana Ekrana Dönmek İçin Enter'a Basınız.")
                    input()

                else:
                    stokürün = int(input("Bulmak İstediğiniz Ürünün Stoğunu Giriniz: "))

                    if stokürün not in Stok:
                        print("Ürün Listede Bulunmamaktadır.")
                        print("Ana Ekrana Dönmek İçin Enter'a Basınız.")
                        input()

                    else:
                        print("Ürün Listede Bulunmaktadır.")
                        print("Ana Ekrana Dönmek İçin Enter'a Basınız.")
                        input()

        def ürünsil():

            os.system("cls")
            bulmak_ürün = input("Bulmak İstediğiniz Ürün Adı: ")

            if bulmak_ürün not in ürünler:
                print("Ürün Listede Bulunmamaktadır.")
                print("Ana Ekrana Dönmek İçin Enter'a Basınız.")
                input()

            else:
                fiyatürün = int(input("Bulmak İstediğiniz Ürünün Fiyatını Giriniz: "))
                ürünler.remove(bulmak_ürün)

                if fiyatürün not in Fiyat:
                    print("Ürün Listede Bulunmamaktadır.")
                    print("Ana Ekrana Dönmek İçin Enter'a Basınız.")
                    input()

                else:
                    stokürün = int(input("Bulmak İstediğiniz Ürünün Stoğunu Giriniz: "))
                    Fiyat.remove(fiyatürün)

                    if stokürün not in Stok:
                        print("Ürün Listede Bulunmamaktadır.")
                        print("Ana Ekrana Dönmek İçin Enter'a Basınız.")
                        input()

                    else:
                        Stok.remove(stokürün)
                        print("Ürün Başarıyla Silindi.")
                        input()



        def ürün_güncelle():
            os.system("cls")

            güncellemekürün = input("Güncellemek İstediğiniz Ürünün Adı: ")

            if güncellemekürün not in ürünler:
                print("Ürün Listede Bulunamamaktadır.")
                input("Devam etmek için Enter'a basınız.")
                return

            index = ürünler.index(güncellemekürün)

            print("\n** Güncelleme Ekranı **\n")
            print("1 - Fiyat Güncelle")
            print("2 - Stok Güncelle")

            seciminiz = input("Seçiminiz: ")

            if seciminiz == "1":
                os.system("cls")

                print("Ürünün Eski Fiyatı:", Fiyat[index], "TL")
                yeni_fiyat = int(input("Yeni Fiyatı Giriniz: "))

                Fiyat[index] = yeni_fiyat

                print("Fiyat Başarıyla Güncellendi!")
                print("Yeni Fiyat:", Fiyat[index], "TL")
                input("Devam etmek için Enter'a basınız.")

            elif seciminiz == "2":
                os.system("cls")

                print("Ürünün Eski Stoğu:", Stok[index])
                yeni_stok = int(input("Yeni Stok Miktarını Giriniz: "))

                Stok[index] = yeni_stok

                print("Stok Başarıyla Güncellendi!")
                print("Yeni Stok:", Stok[index])
                input("Devam etmek için Enter'a basınız.")

            else:
                print("Geçersiz Seçim!")
                input("Devam etmek için Enter'a basınız.")


        # İfler

        if secim == 1:
            ürün_ekle()

        elif secim == 2:
            ürün_listele()

        elif secim == 3:
            ürün_ara()

        elif secim== 4:
            ürünsil()

        elif secim== 5:
            ürün_güncelle()

        elif secim == 6:
            os.system("cls")
            print("Çıkış Yapılıyor...")
            break

        else:
            os.system("cls")
            print("Yanlış Seçim Yaptınız...")

stoksistemi()