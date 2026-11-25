import random
import os

def randomsayı():
    os.system("cls")
    sayi = random.randint(1, 100)
    while True:
        sayi = random.randint(1, 100)
        os.system("cls")
        x = int(input("1-100 Arasında Sayı Tahmin Ediniz: "))

        if sayi == x:
            print("\nDoğru Bildiniz Tebrikler:)\n")
            input()
            

        elif sayi > x:
            print("\nLütfen Daha Büyük Sayı Giriniz...\n")
            input()
            

        elif sayi < x:
            print("\nLütfen Daha Küçük Bir Sayı Giriniz\n")
            input()

        else:
            print("Yanlış Seçim Yaptınız...")
            input()

randomsayı()