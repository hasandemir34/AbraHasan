#kişinin sattığı üründen kar marjını çıkarıp daha sonra kdv oranını hesaplicam
kdv = 0.18
kar_marj = 0.40  # %40 kar marjı

a,b,c=10,20,30 #alt alta yazmak zorunda değilim
e,d,f=25  #direkt hepsine atama yapabilirim

def hesapla(satis_fiyati):
    kalan = satis_fiyati - ((satis_fiyati - (satis_fiyati * kar_marj)) * kdv)
    return kalan

def main():
    satis = float(input("Satış fiyatını gir: "))
    kalan_tutar = hesapla(satis)
    print("Kalan Tutar:", kalan_tutar)

if __name__ == "__main__":
    main()