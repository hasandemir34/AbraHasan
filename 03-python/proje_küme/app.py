import json


with open("giris.json","r") as first:
    veriler=json.load(first)


aKümesi=set(veriler["liste1"])
bKümesi=set(veriler["liste2"])




#birleşim
cKümesi = aKümesi | bKümesi #direkt küme döndürüyormuş. tekrar sete gerek yok

sonuclar = {
    "birlesim": sorted(cKümesi)
}

with open("sonuc.json", "w", encoding="utf-8") as sonuc:
    json.dump(sonuclar, sonuc)


#süre eklenecek son kısma onu biraz araştır.


#kesişim


#fark




