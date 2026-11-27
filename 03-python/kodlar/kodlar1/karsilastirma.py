sonuc=int(True)
print(sonuc)

a=int(input("first number: "))
b=int(input("second number: "))

if (a<b):
    print(f"ilk girilen {a} sayısı küçüktür {b} den")
elif(a==b):
    print(f"ilk girilen {a} sayısı eşittir {b}")
else:
    print(f"ilk girilen {a} sayısı büyüktür {b} den")


c=int(input("sayi gir cano: "))
if ((c %2) ==0):
    print("bu sayi çift")
else:
    print("bu sayi tek")