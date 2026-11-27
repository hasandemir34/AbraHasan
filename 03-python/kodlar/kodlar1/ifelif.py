

print("araç türünüzü seçiniz. \n 1) benzin  \n 2) dizel \n 3) lpg")


while(True):
    try:
        a=int(input("seç:"))
        b=int(input("kaç km yol yaptın: "))
        break

    except ValueError:
        print("geçerli sayı giriniz")

if (a==1):
    print("araç benzinli \n")
    yakit=(b/50)*90
    print(yakit)
elif(a==2):
    print("araç dizel dayı")
    yakit=(b/50)*85
    print(yakit)
elif(a==3):
    print("araç lpg dayı")
    yakit=(b/50)*35
    print(yakit)



