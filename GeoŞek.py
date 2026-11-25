import os

def geoşek():
    while True:
        os.system("cls")

        # Yazılar

        print("*** GEOMETRİK ŞEKİLLER HESAPLAMA ***\n")
        print(
            "1-Kare\n"
            "2-Dikdörtgen\n"
            "3-Üçgen\n"
            "4-Eşkenar Üçgen\n"
            "5-Düzgün Beşgen\n"
            "6-Düzgün Altıgen\n"
            "7-Çıkış\n"
        )

        secim = int(input("Seçiminiz: "))

        # Defler

        def kare():
            os.system("cls")
            print("** KARE HESAPLAMA **\n")
            karekenar = int(input("Karenin Bir Kenar Uzunluğunu Girin: "))

            alan = karekenar * karekenar
            çevre = karekenar * 4

            print("\nAlan:",alan)
            print("Çevre:",çevre)
            input()

        def dikdörtgen():
            os.system("cls")
            print("** DİKDÖRTGEN HESAPLAMA **\n")
            uzunkenar = int(input("Dikdörtgenin Uzun Kenar Uzunluğu Girin: "))
            kısakenar = int(input("Dikdörtgenin Kısa Kenar Uzunluğu Girin: "))

            alan = uzunkenar * kısakenar
            çevre = 2* (uzunkenar + kısakenar)

            print("\nAlan:",alan)
            print("Çevre:",çevre)
            input()


        def üçgen():
            os.system("cls")
            print("** ÜÇGEN HESAPLAMA **\n")

            print(
                "1-Alan\n"
                "2-Çevre\n"
            )

            secim1 = int(input("Seçiminiz: "))

            if secim1 == 1:
                os.system("cls")
                taban = int(input("Üçgenin Taban Uzunluğu: "))
                yüksekli = int(input("Üçgenin Yükseklik Uzunluğu: "))

                alan = (taban * yüksekli) // 2

                print("\nAlan:",alan)
                input()

            elif secim1 == 2:
                os.system("cls")
                k1 = int(input("1.Kenar: "))
                k2 = int(input("2.Kenar: "))
                k3 = int(input("3.Kenar: "))

                cevre = k1 + k2 + k3

                print("\nÇevre:",cevre)

        def eşkenarüçgen():
            import math
            os.system("cls")
            print("** EŞKENAR ÜÇGEN HESAPLA\n")
            kenar = int(input("Eşkenar Üçgenin Bir Kenarını Girin: "))

            cevre = 3 * kenar
            alan = (kenar ** 2 * math.sqrt(3)) // 4

            print("Üçgenin çevresi:", cevre) 
            print("Üçgenin alanı:", alan)
            input()


        def beşgenüçgen():
            os.system("cls")
            print("** EŞKENAR BEŞGEN HESAPLA **\n")

            kenar = float(input("Beşgenin bir kenar uzunluğunu girin: "))
            apotem = float(input("Beşgenin apotem uzunluğunu girin: "))

            cevre = 5 * kenar
            alan = (cevre * apotem) / 2

            print("Beşgenin çevresi:", cevre)
            print("Beşgenin alanı:", alan)
            input()

        def altıgen():
            os.system("cls")
            import math
            print("** EŞKENAR ALTIGEN HESAPLA **\n")

            kenar = int(input("Düzgün Altıgenin Kenar Uzunluğunu Girin: "))

            alan = (3 * math.sqrt(3) * kenar ** 2) / 2
            çevre = 6 * kenar

            print("\nAlan:",alan)
            print("Çevre:",çevre)
            input()

        # İfler

        if secim == 1:
            kare()

        elif secim == 2:
            dikdörtgen()

        elif secim == 3:
            üçgen()

        elif secim == 4:
            eşkenarüçgen()

        elif secim == 5:
            beşgenüçgen()

        elif secim == 6:
            altıgen()

        elif secim == 7:
            os.system("cls")
            print("Çıkış Yapılıyor...")
            break

        else:
            os.system("cls")
            print("Yanlış Seçim Yaptınız...")
            input()

geoşek()