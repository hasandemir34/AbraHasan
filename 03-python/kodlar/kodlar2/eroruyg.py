liste = ["1","3","5","20b","abc","10a","60"]

sayilar=[]


for a in liste:
    try:
        b=int(a)
    except:
        continue  #break olmicak. devam edip diğer kısma geçicek kod.
    else:
        sayilar.append(b)
print(f"sayı olanlar {sayilar}")




def get(sozluk, key):
    if key in sozluk:
        return sozluk[key]
    return "Stokta yok"

# Kullanımı:
fiyatlar = {
    "ekmek": 10,
    "sut": 30,
    "yumurta": 90
}

print(f"sütün fiyatı {get(fiyatlar, "sut")}")      # Çıktı: 30
print(get(fiyatlar, "cikolata")) # Çıktı: Stokta yok