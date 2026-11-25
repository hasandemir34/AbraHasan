import modul1 as m1
import modul2 as m2


while True:
    try:
        a=int(input("işlem seçiniz \n1)fiyat gir: \n 2)ürün ekle\n işlem: "))

        if a==1:
            a=int(input("fiyat giriniz: "))
            if type(a) is not int:
                print("geçerli fiyat gir")
            else:
                m2.fiyatEkle(a)
                print(m1.urunler)
                continue
        elif a==2:
            a=str(input("ürün giriniz"))
            m2.ekleUrun(a)
            print(m1.urunler)
            continue
        elif a==3:
            break

    except:
        print("geçerli sayı girin")
        




