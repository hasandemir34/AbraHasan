

class kisiler():
    def __init__(self,name,bakiye:int=0): #bakiye default olarak sıfır
        self.name=name
        self.bakiye=bakiye #tür kontrolü
        if type(bakiye) is not int:  #hata fırlatıyoruz.
            raise TypeError("Bakiye tam sayı olmalıdır!")


    def paraYatir(self,para:int):
        self.bakiye+=para
        return self.bakiye

    def paraCek(self,para:int):
        self.bakiye-=para
        return self.bakiye



k1=kisiler("hasan",1000)
k1.paraYatir(500)
k1.paraCek(200)
print(k1.bakiye)