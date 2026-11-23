

class Product():
                #init demek her bu nesneden oluşturulduğunda çalışacak yer demek.
    def __init__(self,isim):   #bu class içinde old. için method diyorum. dışarda olsaydı fonk. olurdu.
        # print("nesne oluşturuldu")
        self.name=isim



p1=Product("alii")  #burda isim değişkenini dışardan bekliyo. onsuz nesne oluşturursak kod patlar.
print(p1.name)
sonuc=p1.name
print(sonuc)