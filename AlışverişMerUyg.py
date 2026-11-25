import os

ürünler = []
fiyatlar = []

def alısverismerkezi():
    while True:
        # Yazılar
        os.system("cls")
        print("** Alışveriş Merkezi **\n")
        print(
            "1- Ürün Ekle\n"
            "2- Sepeti Görüntüle\n"
            "3- Toplam Tutarı Göster\n"
            "4- Ürün Sil\n"
            "5- Çıkış Yap\n"
        )

        secim = int(input("Seçiminiz: "))

        

        # Defler
        def ürünekle():
            os.system("cls")
            urun = input("Ürün adını giriniz: ")
            fiyat = float(input("Ürün fiyatını giriniz: "))

            ürünler.append(urun)
            fiyatlar.append(fiyat)

            print("Ürün sepete eklendi!")
            print("Ana Menü İçin Enter'a Basınız..")

        def sepet():
            os.system("cls")
            if len(ürünler) == 0:
                print("Sepetiniz Boş!")
                print("Ana Menü İçin Enter'a Basınız..")
                input()
            else:
                print("--- Alışveriş Sepetiniz ---\n")
                

            for i in range(len(ürünler)):
                print(ürünler[i], "-", fiyatlar[i], "TL")
                
            input()
                



        def toplam():
            os.system("cls")
            toplam = 0

            for fiyat in fiyatlar:
                toplam += fiyat

            print("Toplam tutar:", toplam, "TL")
            input()


        def ürünsil():
            os.system("cls")
            silinecek_urun = input("Silmek istediğiniz ürünün adını girin: ")

            if silinecek_urun in ürünler:
                indeks = ürünler.index(silinecek_urun)

                ürünler.pop(indeks)
                fiyatlar.pop(indeks)

                print("Ürün sepetten silindi!")
            else:
                print("Bu ürün sepette bulunamadı!")

            input("Devam etmek için Enter'a basın...")



        # İfler

        if secim == 1:
            ürünekle()

        if secim == 2:
            sepet()

        elif secim == 3:
            toplam()

        elif secim == 4:
            ürünsil()

        elif secim == 5:
            os.system("cls")
            print("Çıkış yapılıyor...")
            break

alısverismerkezi()

