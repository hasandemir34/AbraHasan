import json



def verileriGetir():
  with open("urunler.json", "r", encoding="utf-8") as file:
    return json.load(file)


def verileriYaz(veri):
    with open("urunler.json","w",encoding="utf-8") as file:
        json.dump(veri,file,ensure_ascii=False,indent=4)


def urunEkle(ad:str,stok:int):
    güncel=verileriGetir()
    yeniId=len(güncel["urunler"])+1
    yeniurun={"id":yeniId,"ad":ad,"stok":stok}
    güncel["urunler"].append(yeniurun)
    verileriYaz(güncel)
    print("yeni ürün eklendi")



def listele():
    veri=verileriGetir()
    print("\n--- ÜRÜN LİSTESİ ---")
    for urun in veri["urunler"]:
        print(f"ID: {urun['id']} | Ürün: {urun['ad']} | Stok: {urun['stok']}")
    print("---------------------\n")


def guncelle(a:int,stok:int):
    veriler=verileriGetir()
    for urun in veriler["urunler"]:
        if urun["id"] == a:
            urun["stok"]=stok
            verileriYaz(veriler)
            print(f"'{urun['ad']}' ürününün stoğu {stok} olarak güncellendi!")
            return
    print("Hata: Bu ID'ye sahip bir ürün bulunamadı!")


def main():
    while True:
        
        try:
             a=int(input("İşlem seçin\n1) Ürünleri listele\n2) Ürün ekle\n3) Stok güncelle\n0) Çıkış\n SEÇİM: "))
        except ValueError:
            print("geçerli sayı girin!")
        else:
            if (a==0):
                break
            elif(a==1):
                listele()
            elif(a==2):
                a=input("ürün adı girin: ").strip()
                b=int(input("stok miktarı girin: "))
                urunEkle(a,b)
            elif(a==3):
                listele()
                a=int(input("geçerli bir id girin: "))
                stok = int(input("Yeni stok miktarını girin: "))
                guncelle(a,stok)
            else:
                print("GEÇERLİ SAYI GİR MORUK")



if __name__ == "__main__":
    main()