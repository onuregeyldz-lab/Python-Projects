# ===== ÖĞRENCİ YÖNETİM SİSTEMİ =====

# 1 - Öğrenci Ekle
# 2 - Öğrencileri Listele
# 3 - Öğrenci Ara
# 4 - Öğrenci Sil
# 5 - Not Güncelle
# 6 - Sınıf Ortalamasını Hesapla
# 7 - En Yüksek Notu Bul
# 8 - Çıkış

# Seçiminiz:

import os

adListesi = []
OgrenciNo = []
ogrenciNot = []

def ogrenciyonetim():
    while True:
        os.system("cls")

        # Yazılar
        print("*** ÖĞRENCİ YÖNETİM SİSTEMİ ***\n")
        print(
            "1-Öğrenci Ekle\n"
            "2-Öğrencileri Listele\n"
            "3-Öğrenci Ara\n"
            "4-Öğrenci Sil\n"
            "5-Sınıf Ortalamasını Hesapla\n"
            "6-En Yüksek Notu Bul\n"
            "7-Çıkış\n"
        )

        secim = int(input("Seçiminiz: "))      

        # Defler

        def ogrenciekle():
            os.system("cls")
            print("** ÖĞRENCİ EKLE **\n")
            ad = input("Eklemek İstediğiniz Öğrenci Adı Giriniz: ")
            numara = int(input("Öğrencinin Numarasını Giriniz: "))
            notu = int(input("Öğrencinin Notunu Giriniz: "))

            adListesi.append(ad)
            OgrenciNo.append(numara)
            ogrenciNot.append(notu)

            print("\nÖğrenci Başarıyla Eklendi.")
            input()



        def ogrencilistele():
            os.system("cls")
            ads = len(adListesi)

            if (ads == 0):
                print("Liste Boştur.")
                input()

            else:
                print("** ÖĞRENCİ LİSTESİ **\n")

                for i in range(len(adListesi)):
                    print("Öğrenci Adı:",adListesi[i],"||","Öğrenci No:",OgrenciNo[i],"||","Öğrenci Not:",ogrenciNot[i])
                    input()



        def ogrenciAra():
            os.system("cls")
            ads = len(adListesi)

            if(ads == 0):
                print("Liste Boştur.")
                input()

            else:
                print("** ÖĞRENCİ BULMA **\n")

                bulmak_ad = input("Bulmak İstediğiniz Öğrenci Adı: ")

                if bulmak_ad not in adListesi:
                    print("Öğrenci Listede Bulunmamaktadır.")
                    input()

                else:
                    bulmak_numara = int(input("Bulmak İstediğiniz Öğrenci Numarası: "))

                    if bulmak_numara not in OgrenciNo:
                        print("Öğrenci Listede Bulunmamaktadır.")
                        input()

                    else:
                        bulmak_not = int(input("Bulmak İstediğiniz Öğrenci Notunu Giriniz: "))

                        if bulmak_not not in ogrenciNot:
                            print("Öğrenci Listede Bulunmamaktadır.")
                            input()

                        else:
                            print("Öğrenci Listede Bulunmaktadır.")
                            input()




        def ogrenciSil():
            os.system("cls")
            ads = len(adListesi)

            if(ads == 0):
                print("Listede Öğrenci Bulunmamaktadır.")
                input()

            else:
                bulmak_ad = input("Silmek İstediğiniz Öğrencinin Adını Giriniz: ")

                if bulmak_ad not in adListesi:
                    print("Öğrenci Listede Bulunmamaktadır.")
                    input()

                else:
                    bulmak_no = int(input("Silmek İstediğiniz Öğrencinin Numarasını Giriniz: "))

                    if bulmak_no not in OgrenciNo:
                        print("Öğrenci Listede Bulunmamaktadır.")
                        input()

                    else:
                        bulmak_not = int(input("Silmek İstediğiniz Öğrencinin Notunu Giriniz: "))

                        if bulmak_not not in ogrenciNot:
                            print("Öğremci Listede Bulunmamaktadır.")
                            input()

                        else:
                            adListesi.remove(bulmak_ad)
                            OgrenciNo.remove(bulmak_no)
                            ogrenciNot.remove(bulmak_not)

                            print("\nBaşarıyla Silindi.")
                            input()

        def sınıfOrt():
            os.system("cls")
            ads = len(adListesi)

            if(ads == 0):
                print("Listede Öğrenci Bulunmamaktadır.")
                input()

            else:
                toplam = 0
                for i in range(len(ogrenciNot)):
                    toplam += ogrenciNot[i]

                    nots = ogrenciNot.count

                    ort = toplam // len(ogrenciNot)

                    print("Sınıf Ortalaması =",ort)


        def enYuksekNot():
            os.system("cls")
            ads = len(adListesi)

            if(ads == 0):
                print("Listede Öğrenci Bulunmamaktadır.")
                input()

            else:
                max = max(ogrenciNot)

                print("En Yüksek Not =",max)
            
        # İfler

        if secim == 1:
            ogrenciekle()

        elif secim == 2:
            ogrencilistele()

        elif secim == 3:
            ogrenciAra()

        elif secim == 4:
            ogrenciSil()

        elif secim == 5:
            sınıfOrt()

        elif secim == 6:
            enYuksekNot()

        elif secim == 7:
            os.system("cls")
            print("Çıkış Yapılıyor...")
            break

        else:
            os.system("cls")
            print("Yanlış Seçim Yaptınız..")
            input()

ogrenciyonetim()