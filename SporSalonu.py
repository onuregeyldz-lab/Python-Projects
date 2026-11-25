import os

uye_adlari = []
uye_numaralari = []
uyelik_sureleri = []

def sporsalonu():
    while True:
        os.system("cls")
        print("===== SPOR SALONU =====\n")
        print("1 - Üye Ekle")
        print("2 - Üyeleri Listele")
        print("3 - Üye Ara")
        print("4 - Üye Sil")
        print("5 - Üyelik Ücreti Hesapla")
        print("6 - Çıkış\n")

        secim = input("Seçiminiz: ")


        def üyeekle():
            os.system("cls")
            print("*** ÜYE EKLEME EKRANI ***\n")
            ad = input("Üye Adınızı Giriniz: ")
            numara = int(input("Üyelik Numaranızı Giriniz: "))
            sure = int(input("Üyelik Sürenizi Giriniz: "))

            uye_adlari.append(ad)
            uye_numaralari.append(numara)
            uyelik_sureleri.append(sure)

            print("\nBaşarıyla Üye Olundu... Ana Ekran İçin Enter'a Bas.")
            input()


        def üyeleriListele():
            os.system("cls")
            üye_sayısı = len(uye_adlari)

            if (üye_sayısı == 0):
                os.system("cls")
                print("LİSTEDE ÜYE BULUNMAMAKTADIR...")
                input()

            else:               
                print("*** ÜYE LİSTESİ ***\n")

                for i in range(len(uye_adlari)):
                    print("Üye Ad:",uye_adlari[i], "||","Üye Numara:",uye_numaralari[i],"||","Üyelik Süresi:",uyelik_sureleri[i],"Ay")

                input()

        def üyeleriaAra():
            os.system("cls")
            

            üye_sayısı = len(uye_adlari)

            if (üye_sayısı == 0):
                os.system("cls")
                print("LİSTEDE ÜYE BULUNMAMAKTADIR...")
                input()

            else:
                print("*** ÜYE BULMA ***\n")
                
                bulmak_ad = input("Bulmak İstediğiniz Üye Adı: ")

                if bulmak_ad not in uye_adlari:
                    print("\nÖğrenci Listede Bulunmamaktadır.")
                    input()

                else:
                    bulmak_numara = int(input("Bulmak İstediğiniz Üye Numarası: "))

                    if bulmak_numara not in uye_numaralari:
                        print("\nÖğrenci Listede Bulunmamaktadır.")
                        input()

                    else:
                        bulmak_not = int(input("Bulmak İstediğiniz Üyenin Süresini Giriniz: "))

                        if bulmak_not not in uyelik_sureleri:
                            print("\nÖğrenci Listede Bulunmamaktadır.")
                            input()

                        else:
                            print("\nÖğrenci Listede Bulunmaktadır.")
                            input()


        def üyeSil():
            os.system("cls")
                              
            üye_sayısı = len(uye_adlari)

            if (üye_sayısı == 0):
                os.system("cls")
                print("LİSTEDE ÜYE BULUNMAMAKTADIR...")
                input()

            else:
                print("*** ÜYE SİLME ***\n")
                
                bulmak_ad = input("Silmek İstediğiniz Üye Adı: ")

                if bulmak_ad not in uye_adlari:
                    print("\nÜye Listede Bulunmamaktadır.")
                    input()

                else:
                    bulmak_numara = int(input("Silmek İstediğiniz Üye Numarası: "))

                    if bulmak_numara not in uye_numaralari:
                        print("\nÖğrenci Listede Bulunmamaktadır.")
                        input()

                    else:
                        bulmak_not = int(input("Silmek İstediğiniz Üyenin Süresini Giriniz: "))

                        if bulmak_not not in uyelik_sureleri:
                            print("\nÖğrenci Listede Bulunmamaktadır.")
                            input()

                        else:

                            uye_adlari.remove(bulmak_ad)
                            uyelik_sureleri.remove(bulmak_not)
                            uye_numaralari.remove(bulmak_numara)

                            print("\nÜye Başarıyla Silindi.")
                            input()

        def ücretHesapla():
            os.system("cls")
            sure = int(input("Üyelik Sürenizi Giriniz: "))

            a1 = 500
            a3 = 1350
            a6 = 2400
            a9 = 3500
            a12 = 4200

            if sure == 1:
                print("\nÜcretiniz :",a1,"TL")
                input()

            elif sure == 3:
                print("\nÜcretiniz :",a3,"TL")
                input()

            elif sure == 6:
                print("\nÜcretiniz :",a6,"TL")
                input()

            elif sure == 9:
                print("\nÜcretiniz :",a9,"TL")
                input()

            elif sure == 12:
                print("\nÜcretiniz :",a12,"TL")
                input()

            else:
                print("Yanlış Seçim Yaptınınız...")
                input()
                
                
                
        if secim == "1":
            üyeekle()

        elif secim == "2":
            üyeleriListele()

        elif secim == "3":
            üyeleriaAra()

        elif secim == "4":
            üyeSil()

        elif secim == "5":
            ücretHesapla()

        elif secim == "6":
            os.system("cls")
            print("Çıkış Yapılıyor...")
            break

        else:
            os.system("cls")
            print("Yanlış seçim!")
            input()

sporsalonu()