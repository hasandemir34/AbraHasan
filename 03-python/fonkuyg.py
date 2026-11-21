ekHesap = 999


def paracek(a):
    global bakiye, ekHesap

    if a <= 0:
        print("Geçerli bir tutar gir!")
        return

    if a <= bakiye:
        bakiye -= a
        print(f"Para çekildi. Yeni bakiyen: {bakiye} TL")

    else:
        print("Hesapta yeterli para yok. Ek hesap kullanmak ister misin?")
        cevap = input("Evet(e) Hayır(h): ").lower()

        if cevap == "e":
            if a <= bakiye + ekHesap:
                ekHesap -= (a - bakiye)
                bakiye = 0
                print("Para çekme işlemi başarılı!")
                print(f"Yeni bakiye: {bakiye} TL")
                print(f"Kalan ek hesap: {ekHesap} TL")
            else:
                print("Ek hesap dahil yeterli paranız yok!")

        elif cevap == "h":
            print("İşlem iptal edildi.")

        else:
            print("Geçersiz seçim!")


def parayatir(a):
    global bakiye

    if a > 0:
        bakiye += a
        print(f"Paranız yatırıldı. Yeni bakiye: {bakiye} TL")
    else:
        print("Geçerli bir tutar gir!")


def bakiyeSorgu():
    global bakiye,ekHesap
    print(f"Bakiyeniz: {bakiye} TL")
    print(f"Ek hesap miktarı: {ekHesap} TL")


def hesapBilgileri(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


# Kullanıcı bilgileri
hesapAdi = input("Hesap adı girin: ")

while True:
    try:
        bakiye = int(input("Başlangıç bakiyenizi girin: "))
        if bakiye < 0:
            print("Bakiye negatif olamaz!")
            continue
        break
    except ValueError:
        print("Lütfen geçerli bir sayı girin!")

hesapBilgileri(hesap=hesapAdi, bakiye=bakiye)


# Ana menü
while True:
    try:
        islem = int(input("""
========== BANKA UYGULAMASI ==========

1) Para Çek
2) Para Yatır
3) Bakiye Sorgula
4) Çıkış

İşlem seçin: """))

        if islem == 1:
            w = int(input("Ne kadar çekeceksiniz: "))
            paracek(w)

        elif islem == 2:
            w = int(input("Ne kadar yatıracaksınız: "))
            parayatir(w)

        elif islem == 3:
            bakiyeSorgu()

        elif islem == 4:
            print("Çıkış yapılıyor...")
            break

        else:
            print("Geçerli bir işlem seçin!")

    except ValueError:
        print("Lütfen sadece tam sayı girin!")