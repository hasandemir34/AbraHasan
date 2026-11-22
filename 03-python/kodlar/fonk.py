import random


def yazdir(yazi,b):
    for i in range(b):
        print(yazi)
    

'''
yazi=input("ne yazalım: ")
b=int(input("kaç kere yazalım: "))
yazdir(yazi,b)

def alan(a,b):
    return a*b
def cevre(a,b):
    return 2*(a+b)

kısa=int(input("kısa kenar: "))
uzun=int(input("uzun kenar: "))

print(f"dikdörtgen alanı {alan(kısa,uzun)} , çevresi {cevre(kısa,uzun)}")

'''

def yaziTura():
    sayi=random.randint(1,2)
    if(sayi==1):
        print("tura")
    else:
        print("yazi")


yaziTura()

'''

def asalMi(a):  #girilen 2 aralıktaki asal sayıları ekrana yazdırıyor.
    if a < 2:
        return False

    for b in range(2, a):
        if a % b == 0:
            return False

    return True


sayi1 = int(input("İlk sayıyı gir: "))
sayi2 = int(input("İkinci sayıyı gir: "))

for i in range(min(sayi1, sayi2), max(sayi1, sayi2) + 1):
    if asalMi(i):
        print(i)

'''
def tamBolenler(b):
    liste = []

    for i in range(1, b + 1):
        if b % i == 0:
            liste.append(i)

    print(liste)


tamBolenler(32)