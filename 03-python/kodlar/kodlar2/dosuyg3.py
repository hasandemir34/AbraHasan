
import json
from pathlib import Path  # os kullanmıştık ama bu da kullanılıyormuş.

BILGI_DOSYASI = Path(__file__).resolve().with_name("bilgi.json")

def verileriOku():
    if not BILGI_DOSYASI.exists():
        return {}

    with open(BILGI_DOSYASI, "r", encoding="utf-8") as dosya:
        icerik = dosya.read().strip()  # strip dosyadaki yazıyı okur, baştaki/sondaki boşlukları siler

    if icerik:
        return json.loads(icerik)  # icerik bir str olduğu için loads kullanıyoruz
    else:
        return {}

def maasGir():
   
        try:
            a=int(input("maaşı girin: "))
            if(a<=0):
                print("böyle bir maaş yok!")
                return
            
            veriler = verileriOku()
            veriler["maas"] = a

            with open(BILGI_DOSYASI, "w", encoding="utf-8") as bilgi: #güncel bilgileri yazıyoruz
                json.dump(veriler, bilgi, indent=4)
            print("maaş girildi")
                
        except ValueError:
            print("hatalı giris")

def gelirGir():
    a = int(input("Gelir gir: "))

    veriler = verileriOku()

    veriler["gelir"] = veriler.get("gelir", 0) + a  #bu sayede yeni gelir eklenirse toplanıp yazılacak, üstüne yazma biter.

    with open(BILGI_DOSYASI, "w", encoding="utf-8") as bilgi:
        json.dump(veriler, bilgi, indent=4)

    print("Gelir kaydedildi!")


def harcamaekle():
    a = int(input("Harcama gir: "))

    if a <= 0:
        print("Geçersiz harcama!")
        return

    veriler = verileriOku()

    veriler["harcama"] = veriler.get("harcama", 0) + a

    with open(BILGI_DOSYASI, "w", encoding="utf-8") as bilgi:
        json.dump(veriler, bilgi, indent=4)

    print("Harcama kaydedildi!")

    
def bakiye():

    veriler = verileriOku()

    maas = veriler.get("maas", 0)  #get ile olmayan değer 0 kabul edilir.
    gelir = veriler.get("gelir", 0)
    harcama = veriler.get("harcama", 0)

    toplam = maas + gelir - harcama

    print(f"Üstad senin bakiyen: {toplam} TL")
    



while True:
    try:
        a=int((input("işlem seçin: \n 1)Maaşını Gir \n 2)Gelir Ekle \n 3)Harcama Ekle \n 4)Bakiye Sorgu \n 5)ÇIKIŞ \n İşlem: ")))
        if(a==1):
            maasGir()
        elif(a==2):
            gelirGir()
        elif(a==3):
            harcamaekle()
        elif(a==4):
            bakiye()
        elif(a==5):
            break
        else:
            print("1 il 5 arasında girin!")
    except ValueError:
        print("geçersiz işlem. \n")
