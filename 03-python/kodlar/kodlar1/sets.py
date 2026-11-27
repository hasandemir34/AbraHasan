#bunlar indekslemez, sıralanamaz,güncellenemez,tekrarlanamaz,elemanı siler ya da ekleriz.
meyveler={"kiraz","elma","armut","portakal","kiraz"}
#kiraz 2 tane de olsa sadece 1 kere yazıcak ve yazma sırası karışık çünkü indeksleme yok


sonuc=meyveler
print(sonuc) 

for x in meyveler:  #elemanları gezip ekrana yazdırma
    print(x)


varmi= "elma" in meyveler   #true döner eğer listede elma değeri varsa

meyveler.add("karpuz") #eleman ekleme olayı basitçe
print(sonuc)