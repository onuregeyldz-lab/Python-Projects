# ================================
#        HASTANE OTOMASYONU
# ================================

# 1 - Hasta Kaydet
# 2 - Hastaları Listele
# 3 - Hasta Ara
# 4 - Çıkış


import os

Hasta_Adı = []
Hasta_Yas = []
Hasta_No = []

def hastatakip():
    while True:
        os.system("cls")

        # YAZILAR
        print("**** HASTANE OTOMASYONU ****\n")
        print(
            "1 - Hasta Kaydet\n"
            "2 - Hastaları Listele\n"
            "3 - Hasta Ara\n"
            "4 - Çıkış\n"
        )

        secim = input("Seçiminiz: ")

        # DEFLER

        def HastaKaydet():
            os.system("cls")
            print("--- Hasta Kaydetme Ekranı ---\n")

            ad = input("Hastanın Adını Giriniz: ")
            yas = int(input("Hastanın Yaşı: "))
            no = int(input("Hastanın Numarası:"))

            Hasta_Adı.append(ad)
            Hasta_Yas.append(yas)
            Hasta_No.append(no)

            print("\nBaşarıyla Eklendi.")
            input()


        def HastaListele():
            os.system("cls")

            Hasta_sayısı = len(Hasta_Adı)

            if Hasta_sayısı == 0 :
                print("Listede Hasta Bulunmamaktadır...")
                input()

            else:
                print("--- HASTA LİSTESİ ---\n")

                for i in range(len(Hasta_Adı)):
                    print("Hasta Adı :",Hasta_Adı[i],"||","Hasta Yaşı :",Hasta_Yas[i],"||","Hasta Numarası :",Hasta_No[i])
                input()


        def HastaAra():
            os.system("cls")

            Hasta_sayısı = len(Hasta_Adı)

            if Hasta_sayısı == 0:
                print("Listede Hasta Bulunmamaktadır...")
                input()

            else:
                print("--- HASTA ARAMA EKRANI")

                numara = int(input("Hastanın Numarasını Giriniz: "))

                if numara not in Hasta_No:
                    print("\nHASTA BULUNMAMAKTADIR...") 
                    input()

                else:
                    print("\nHASTA BULUNMAKTADIR...")
                    input()

            
        # İFLER

        if secim == "1":
            HastaKaydet()

        elif secim == "2":
            HastaListele()

        elif secim == "3":
            HastaAra()

        elif secim == "4":
            os.system("cls")
            print("Çıkış Yapılıyor.")
            break

        else:
            os.system("cls")
            print("Yanlış Seçim Yaptınız.")
            input()

hastatakip()