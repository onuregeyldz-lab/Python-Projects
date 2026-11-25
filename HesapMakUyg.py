import os

def hesapmakinesi():
    while True:
        os.system("cls")
        print("** Hesap Makinesi **\n")
        print("1-Toplama\n"
              "2-Çıkarma\n"
              "3-Çarpma\n"
              "4-Bölme\n"
              "5-Çıkış\n"            
              )
        secim = int(input("Seçiminiz: "))

        def toplama():
            os.system("cls")
            s1 = int(input("1.Sayıyı Giriniz: "))
            s2 = int(input("2.Sayıyı Giriniz: "))
            top = s1 + s2

            print("\nToplam :",top)
            print("Ana Ekran İçin Enter'a Basınız.")
            input()


        def cıkarma():
            os.system("cls") 
            s1 = int(input("1.Sayıyı Giriniz: "))
            s2 = int(input("2.Sayıyı Giriniz: "))
            top = s1 - s2

            print("\nToplam :",top)
            print("Ana Ekran İçin Enter'a Basınız.")
            input()

        def carpma():
            os.system("cls")
            s1 = int(input("1.Sayıyı Giriniz: "))
            s2 = int(input("2.Sayıyı Giriniz: "))
            top = s1 * s2
            
            print("\nToplam :",top)
            print("Ana Ekran İçin Enter'a Basınız.")
            input()

        def bolme():
            os.system("cls")
            s1 = int(input("1.Sayıyı Giriniz: "))
            s2 = int(input("2.Sayıyı Giriniz: "))
            top = s1 // s2
                        
            print("\nToplam :",top)
            print("Ana Ekran İçin Enter'a Basınız.")
            input()



        if secim == 1:
            toplama()

        elif secim == 2:
            cıkarma()

        elif secim == 3:
            carpma()

        elif secim == 4:
            bolme()

        elif secim == 5:
            os.system("cls")
            print("Çıkış Yapılıyor...")
            break

hesapmakinesi()