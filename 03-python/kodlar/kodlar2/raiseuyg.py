

b=str(input("parola girin: "))



while True:
    for a in b:
        if a=="ü" or a=="ç" or a=="ğ":
            raise Exception ("türkçe karakter kullanamazsın.")
    else:
        print("parola alındı")
        break
    