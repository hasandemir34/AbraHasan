
def ogrenciKayit(): #tamam

    ad=str(input("öğrenci ad: "))
    soyad=str(input("öğrenci soyad: "))
    not1=int(input("not1: "))
    not2=int(input("not2: "))
    not3=int(input("not3: "))

    with open("yeniuyg.txt","a",encoding="utf-8") as file:
        file.write(f"{ad} {soyad} : {not1},{not2},{not3} \n")



def notyazdir():  #tamam
    with open("yeniuyg.txt","r",encoding="utf-8") as file:
         for satir in file:
            print(not_hesapla(satir))


def not_hesapla(satir):
    satir = satir.strip() #Bu yöntem satırın başındaki ve sonundaki gereksiz boşlukları ve \n karakterini temizler.
    liste = satir.split(":")

    ogrenciAdi = liste[0]
    notlar = liste[1].split(",")

    not1 = int(notlar[0])
    not2 = int(notlar[1])
    not3 = int(notlar[2])

    ortalama = (not1 + not2 + not3) / 3
    if ortalama >= 90:
        harf = "AA"
    elif ortalama >= 80:
        harf = "BA"
    elif ortalama >= 75:
        harf = "BB"
    elif ortalama >= 70:
        harf = "CB"
    elif ortalama >= 65:
        harf = "CC"
    elif ortalama >= 60:
        harf = "DC"
    elif ortalama >= 50:
        harf = "DD"
    elif ortalama >= 40:
        harf = "FD"
    else:
        harf = "FF"

    return f"{ogrenciAdi} : {harf} - ({ortalama})\n"
    


def harfNotu():
    with open("yeniuyg.txt","r",encoding="utf-8") as file:
        liste = []

        for satir in file:
            liste.append(not_hesapla(satir))

        with open("sonuclar.txt","w",encoding="utf-8") as file2:
            file2.writelines(liste)

    print("Harf notları sonuclar.txt dosyasına kaydedildi!")
    


while True:

    try:
        islem=int(input("işlemi seçin \n 1)öğrenci kayit \n 2)notları oku \n 3)harf notu \n 4)çıkış \n islem:  "))
        if(islem==1):
            ogrenciKayit()
        elif(islem==2):
            notyazdir()
        elif(islem==3):
            harfNotu()
        elif(islem==4):
            print("güvenli çıkış")
            break
        else:
            print("hatalı giris: ")
    except ValueError:
        print("hatalı girdin moruk!")