
'''
f= open("log.txt","r",encoding="utf-8") #utf ile türkçe karakterleri de okumayı sağlıyorum.
print(f.read())
f.close()
'''


try:  #hata kontrolü içine yazıp çalıştırmak daha sağlıklı olur.
    with open("log3.txt","r",encoding="utf-8") as file:  #with oto olarak kapama yapıyormuş
        print(file.read())
except FileNotFoundError as e:
    print("dosya bulunamadı hatası: ")
    print("Hata detayı:", e)