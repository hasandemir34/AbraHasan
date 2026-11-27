#there is some product and some people. write a code in type this metarial after that people can buy that. 
#finally you can calculate the total price


telNo="05364578885"
mail="hsahs@gmail.com"

kablosusMouse=500
telefon=1500
telefonKilif=460

def main():
    print("Aldıklarını ve ismini söyle")
    name = input("Adınız: ")
    sepet = input("Sepet: ")

    toplam = 0

    if sepet == "kablosusMouse":
        toplam = kablosusMouse
        print(f"{name} beyin aldıkları toplam: {toplam} TL")
    elif sepet == "telefonKilif":
        toplam = telefonKilif
        print(f"{name} beyin aldıkları toplam: {toplam} TL")
    elif sepet == "telefon":
        toplam = telefon
        print(f"{name} beyin aldıkları {toplam} TL ")
    else:
        print("Geçersiz ürün girdiniz!")

if __name__ == "__main__":
    main()