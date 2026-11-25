
# with open("dosya.txt","a",encoding="utf-8") as b:
#     b.write("\n 6-togg")


# with open("dosya.txt","r+",encoding="utf-8") as b:  direkt en başa yazma işlemi için.
#     markalar= b.read()
#     markalar="1) tesla \n" + markalar
#     b.seek(0) #bununla en başa imleci alıyorum üstad.
#     b.write(markalar)

with open("dosya.txt", "r+", encoding="utf-8") as file:  #istediğin satıra yazmak için
    markalar = file.readlines()
    markalar.insert(2, "3-Renault\n")
    file.seek(0)
    # for marka in markalar:
    #     file.write(marka)
    file.writelines(markalar)

    
with open("dosya.txt","r",encoding="utf-8") as b:
    print(b.read())