

a=10

# if a>5:
#     raise Exception ("a 5 den büyük olamaz")  #kendi kuralımızı koyup hata fırlatıyoruz.


while True:

    a = input("Faktöriyel için sayı gir (Çıkış: q): ")

    if a == "q":
        break

    try:
        a = int(a)

    except ValueError:
        print("Sadece sayı girin.")

    else:
        sonuc = 1
        for b in range(1, a + 1):
            sonuc *= b

        print(f"Girdiğin {a} sayısının faktöriyeli: {sonuc}")
    