satislar=[100,200,300,400,500]
kiisler=["hasan","ali","mamo","bilo","merve"]
satislar.append(999)
print(satislar)
satislar.pop()
print(satislar)


for kisi, satis in zip(kiisler, satislar):
    print(f"{kisi} kişisinin harcaması: {satis + 1}")

kiisler.sort()
print(kiisler)

sonuc=min(satislar)
print(sonuc)