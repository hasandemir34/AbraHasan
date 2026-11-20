

sayilar=[2,3,5,6,7,9,15,48,68,69,72]
ücler=[]

for x in sayilar:
    if ((x%3)==0):
        ücler.append(x)
    else:
        continue

print(ücler)

toplam=0
for a in sayilar:
    toplam+=a
print(toplam)


urunler = ["samsung s24", "samsung s22", "iphone 15", "iphone 14"]


for t in urunler:
    if "iphone" in t:
        print(f"aradığın ürün: {t} indexi ise: {urunler.index(t)}  ") #bu sayede hem ürünü hem de kaçıncı sırada olduğunu buluyorum.