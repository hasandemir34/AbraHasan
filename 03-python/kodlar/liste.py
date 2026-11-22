kurum="sakarya üniversitesi"

print(type(kurum))
new=kurum.split()
print(type(new))
print(new[0])
print(new[1])
print(new)


print("----------------------------------UYGULAMA------------------------")

markas=["toyota","mercedes","bmw","audi","renault"]
print(len(markas))
print(markas[0],markas[-1])
markas[4]="TOGG"
print(markas)
sonuc="TOGG" in markas
print(sonuc)
print(markas[:2])
markas=markas+["citroen","ford"]
print(markas)
del markas[-1]
print(markas)

print("--------------------------2. UYGULAMA---------------------------")
ogrenci1 = ["Yiğit", "Bilgi", 2010, [70, 80, 90]]
ogrenci2 = ["Ada", "Bilgi", 2012, [70, 70, 80]]
ogrenci3 = ["Çınar", "Turan", 2017, [60, 60, 90]]
listem=[]
listem=[ogrenci3,ogrenci2]
listem.append(ogrenci1)
print(listem)
print(listem[0][2])
yas=(2026-listem[0][2])+(2026-listem[1][2])+(2026-listem[2][2])
ort=yas/3
print(yas)
print(ort)