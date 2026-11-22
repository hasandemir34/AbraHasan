

def topla( a, b):
    toplam=a+b
    return toplam



def main():

    # 1. Sayıyı Al
    while True:
        try:
            alinan = int(input("int değer gir: "))
            break
        except ValueError:
            print("Geçerli bir 1. int girin!")

    # 2. Sayıyı Al
    while True:
        try:
            ikinci = int(input("2. int gir: "))
            break
        except ValueError:
            print("Geçerli bir 2. int girin!")

    toplam=topla(alinan,ikinci)
    print(f"topladık ssayıları: {toplam}")



if __name__ == "__main__":
    main()