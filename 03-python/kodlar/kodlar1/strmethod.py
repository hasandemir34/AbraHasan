#tüm bu metodlar orjinal nesne üzerinde bir farklılık yapmaz kopya üzerinde işlemler yaparlar.

mesaj="abrababsb  absb ali  dbasbbda"
sonuc=mesaj.upper()
print(sonuc)

sonuc2=mesaj.capitalize() #ilk harf büyüt
print(sonuc2)
sonuc3=mesaj.title() #her kelimenin ilk harfini büyük harfe çevirir.
print(sonuc3)
print(sonuc3.isupper())

mes="AASASFA"
print(mes.isupper()) #bütün harfler büyük ise true döner. bütün ona dikkat et.

sonuc4=mesaj.split('a') #metni boşluklarından böler ve bir liste olarak döner. ['abrababsb', 'absb', 'dbasbbda']
                        #içine yazdığın değişkene bakıp onunla bölüyor. mesela her a geldiğinde listeye yeni eleman ekler.
print(sonuc4)

sonuc5=mesaj.replace("alis","veli") #ali kelimesini bulur ve veli yapar bulamaz ise hata vermez
print(sonuc5)
print("----------------------------uygulama--------------------------------------")
kurs="hsan ile proje geliştirme kursu"
hsn=kurs.replace(" ", "-")
print(hsn)
hsn1=kurs.rstrip()
print(hsn1)
hsn2=kurs.find("ile") #bulur ve indeksini verir.
print(type(hsn2))
print(kurs.index("ile"))
print(kurs[hsn2::])
hsn3=kurs.split()
print(hsn3)
a=hsn3[2]
print(a)