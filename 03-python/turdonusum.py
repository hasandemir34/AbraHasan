
def main():
    mil=int(input("kaç mil giriniz: "))
    km=float(mil*1.62)
    print(f"{mil} yaklaşık olarak {km} yapıyor.")
    print(type(km))

if __name__=="__main__":
    main()