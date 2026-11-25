import os

araclar = ["Toyota Corolla", "Renault Clio", "BMW 320i"]

fiyatlar = [1500, 1200, 3500]

durumlar = ["Müsait", "Müsait", "Müsait"]

def araçkiralama():
    while True:
        os.system("cls")
        # YAZILAR
        print("** Araç Kiralama Sistemi **\n")
        print(
            "1 - Araçları Listele\n"
            "2 - Araç Kirala\n"
            "3 - Araç İade Et\n"
            "4 - Müsait Araçları Göster\n"
            "5 - Çıkış\n"
        )

        secim = int(input("Seçiminiz: "))
        # DEFLER

        def araçlarılistele():
            os.system("cls")
            print("** Araç Listele **\n")

            for i in range(len(araclar)):
                print(araclar[i],"|","Fiyat:",fiyatlar[i],"|","Durum:",durumlar[i])

            input()


        def araçkirala():
            print("\n===== ARAÇ KİRALAMA =====\n")

            # Araçları listele
            for i in range(len(araclar)):
                print(i + 1, "-", araclar[i],
                    "| Günlük Ücret:", fiyatlar[i], "TL",
                    "| Durum:", durumlar[i])

            # Kullanıcıdan araç adı al
            secilen_arac = input("\nKiralamak istediğiniz araç: ")

            # Araç listede var mı?
            if secilen_arac in araclar:

                # Aracın listedeki indeksini bul
                index = araclar.index(secilen_arac)

                # Araç müsait mi?
                if durumlar[index] == "Müsait":

                    gun = int(input("Kaç gün kiralamak istiyorsunuz?: "))

                    if gun > 0:
                        toplam = fiyatlar[index] * gun

                        print("\nAraç başarıyla kiralandı!")
                        print("Araç:", araclar[index])
                        print("Günlük ücret:", fiyatlar[index], "TL")
                        print("Kiralama süresi:", gun, "gün")
                        print("Toplam ücret:", toplam, "TL")

                        # Aracın durumunu değiştir
                        durumlar[index] = "Kiralandı"

                    else:
                        print("Gün sayısı 0'dan büyük olmalıdır!")

                else:
                    print("Bu araç şu anda müsait değil!")

            else:
                print("Böyle bir araç bulunamadı!")



        def araçiadeet():
            os.system("cls")
            print("===== ARAÇ İADE ET =====\n")

            # Araçları listele
            for i in range(len(araclar)):
                print(i + 1, "-", araclar[i],
                    "| Durum:", durumlar[i])

            # İade edilecek aracı sor
            iade_arac = input("\nİade edilecek aracın adı: ")

            # Araç listede var mı?
            if iade_arac in araclar:

                # Aracın indeksini bul
                index = araclar.index(iade_arac)

                # Araç kiralanmış mı?
                if durumlar[index] == "Kiralandı":

                    durumlar[index] = "Müsait"

                    print("\nAraç başarıyla iade edildi!")
                    print("Araç:", araclar[index])
                    print("Yeni durum:", durumlar[index])

                else:
                    print("\nBu araç zaten müsait!")

            else:
                print("\nBöyle bir araç bulunamadı!")



        def müsaitaraç():
            os.system("cls")
            print("\n===== MÜSAİT ARAÇLAR =====\n")

            musait_var = False

            for i in range(len(araclar)):
                if durumlar[i] == "Müsait":
                    print(
                        i + 1, "-", araclar[i],
                        "| Günlük Ücret:", fiyatlar[i], "TL"
                    )
                    musait_var = True

            if musait_var == False:
                print("Şu anda müsait araç bulunmuyor!")


        # İFLER

        if secim == 1:
            araçlarılistele()

        elif secim == 2:
            araçkirala()

        elif secim == 3:
            araçiadeet()

        elif secim == 4:
            müsaitaraç()

        elif secim == 5:
            os.system("cls")
            print("Çıkış Yapılıyor...")
            break

        else:
            os.system("cls")
            print("Yanlış Seçim Yaptınız.")
            print("Ana Ekrana Dönmek İçin Enter'a Basınız.")
            input()

araçkiralama()