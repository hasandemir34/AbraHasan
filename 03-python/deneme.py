
MIN_KREDI_NOTU = 50


def onay(x,y):
    sonuc=((-2)*x)+((1.5)*y)
    return sonuc

def main():

    while(True):

        try: 
            b=int(input("borç değer gir: "))
            g=int(input("gelir bilgisi gir: "))
            break  #eğer sonuçlar doğru girilirse while bitirir. sonuc kısmına geçer

        except ValueError:
            print("Hatalı değer girildi düzeltin.")
                          


    sonuc=onay(b,g) #üst  fonksiyona paslama ve hesaplatma. 

    if (sonuc>=MIN_KREDI_NOTU):
        print(f"kredi notunuz: {sonuc}")
        print("onay verildi kredi alabilir.")
    else:
        print(f"kredi notunuz: {sonuc}")
        print("onay verilmedi kredi alamaz.")

if __name__ == "__main__":
    main()