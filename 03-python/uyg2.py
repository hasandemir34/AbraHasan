ogrenciler = []

n = int(input("Kaç öğrenci ekleyeceksiniz: "))

for i in range(n):
    no = int(input("Öğrenci numarası: "))
    ad = input("Öğrenci adı: ")
    soyad = input("Öğrenci soyadı: ")

    ogrenci = {
        "ogrenciNo": no,
        "ogrenciAdi": ad,
        "ogrenciSoyadi": soyad
    }

    ogrenciler.append(ogrenci)

for ogrenci in ogrenciler:
    print(ogrenci)
