

def kayitEkle():
    
    a=str(input("öğrenci isim girin: "))
    while True:
        try:

            b=int(input("öğrenci notunu girin: "))

            if(b<0) or (b>100):
                print("Not 0 ile 100 arasında olmalı!")
                continue
            else:
                break
        except ValueError:
            print("hatalı veri girdin")

    with open("uyg.txt", "a", encoding="utf-8") as files:
        files.write(f"{a},{b}\n")

    

def listele():
    with open("uyg.txt","r",encoding="utf-8") as files:
        print(files.read())


def ortGoster ():
    
    with open("uyg.txt", "r", encoding="utf-8") as files:

        for satir in files:
            isim, notu = satir.strip().split(",")
            notu = int(notu)

            if notu >= 90:
                harf = "AA"
            elif notu >= 80:
                harf = "BA"
            elif notu >= 70:
                harf = "BB"
            elif notu >= 60:
                harf = "CB"
            elif notu >= 50:
                harf = "CC"
            else:
                harf = "FF"

            print(f"{isim}: {notu} -> {harf}")
    

while True:
    try:
        a=int(input("menuden seçim yap\n 1)kayıt et \n 2)Listele \n 3)Harf notları \n 4)Çıkış \n"))
        if (a==1):
            kayitEkle()
        elif(a==2):
            listele()
        elif (a==3):
            ortGoster()
        elif (a==4):
            print("güvenli çıkış yapıldı.")
            break
        else:
            print("Geçersiz seçim!")
    except ValueError as e:
        print("hatalı girdin!")
        print(e)
   
    