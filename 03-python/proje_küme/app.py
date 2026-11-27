import json
import time


with open("giris.json", "r", encoding="utf-8") as first:
  veriler = json.load(first)


basla = time.perf_counter()

aKumesi = set(veriler["liste1"])
bKumesi = set(veriler["liste2"])


birlesim = aKumesi | bKumesi
kesisim = aKumesi & bKumesi
fark = aKumesi - bKumesi  # aKumesi'nde olup bKumesi'nde olmayanlar


bitir = time.perf_counter()
sure = bitir - basla

print(f"Geçen süre: {sure:.6f} saniye")

# 4. Tüm sonuçları ve süreyi tek bir sözlükte topla
sonuclar = {
    "birlesim": sorted(birlesim),
    "kesisim": sorted(kesisim),
    "fark": sorted(fark),
    "time": f"{sure:.6f} saniyedir.",  # JSON içinde en sona bu şekilde eklenir
}

# Tek seferde w moduyla dosyaya yazdır
with open("sonuc.json", "w", encoding="utf-8") as sonuc:
  json.dump(sonuclar, sonuc, ensure_ascii=False)  #false kısmı ile türkçe karakterleri kolaylıkla ekliyoruz.
