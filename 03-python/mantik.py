
yas=18
velizin=False

if(yas>=18 or velizin):
    print("gidebilirsin")
else:
    print("gidemez !!")


notlar={
   "mat": 50,
   "türk":65,
   "din": 10
}

zayif=False
for notu in notlar.values():
    if (notu <40):
        zayif=True




if ((sum(notlar.values())/3)>40 and not zayif):
    print((sum(notlar.values())/3))
    print("geçti")
else:
    print(round((sum(notlar.values())/3),2))#iç içe karışık gelebilir ama ort 2 virgülden sonrası
    #alcak şekilde yazdım sadece basit yani
    print("kaldın reis")
