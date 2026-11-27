urunler = [  #bu bir dictinary ve bunun üstündeyiz.
    {"urunAdi": "Hp Victus", "fiyat": 32999},
    {"urunAdi": "Lenovo ThinkPad", "fiyat": 25499},
    {"urunAdi": "Apple Macbook", "fiyat": 49999},
    {"urunAdi": "Huawei Matebook", "fiyat": 26999},
    {"urunAdi": "Casper Nirvana", "fiyat": 20000}
]

for x in urunler:
    print(f"{x["urunAdi"]} markalı pcnin fiyati: {x["fiyat"]}") #sözlükteki bir değerin valuelarına bu şekilde erişiyorum.

toplam=0


for a in urunler: #tüm fiyatlar toplamı
    toplam+=a["fiyat"]
print(toplam)


for b in urunler:  #2 fiyat aralığındaki ürünler
    if (b["fiyat"]>25000) and (b["fiyat"]<40000):
        print(f"{b["urunAdi"]} markalı pcnin fiyati: {b["fiyat"]}")


kelime=input("aradığın ürünü gir: ")

for urun in urunler:
    if(urun["urunAdi"].lower().find(kelime.lower()) > -1): #bu da bulmaya yarıyor find methodu
        print(f"{urun['urunAdi']}")