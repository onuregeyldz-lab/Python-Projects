import os

os.system("cls")

print("** Not Hesaplama Uygulaması **\n")

x = input("Öğrenci Adı: ")

s1 = int(input("1. Sınavınızı Giriniz: "))

s2 = int(input("2. Sınavınızı Giriniz: "))

ortalama = (s1 + s2) / 2

print("\nÖğrenci Adı:", x)

print("Ortalama:", ortalama)

if ortalama >= 50:
    print("Durum: Başarılı")

else:
    print("Durum: Başarısız")

