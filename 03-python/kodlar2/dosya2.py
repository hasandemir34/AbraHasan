

with open("dosya.txt","w",encoding="utf-8") as dosya: #bu sadece yazma old. için okuyamıyom
    dosya.write("hasan babuş \n")

with open("dosya.txt", "a", encoding="utf-8") as dosya:
    dosya.write("alemin kralı abra\n")
    
   
with open("dosya.txt", "r", encoding="utf-8") as dosya:
    print(dosya.read())