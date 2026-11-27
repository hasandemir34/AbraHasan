kurs="btk akademide python eğitimi"

print(len(kurs)) #karakter sayısı
print(id(kurs)) #pythonda pointer mantığı yok ama nesne yuva mantığı var ve id ile onu görebiliyom. //1801438280624 gibi

print(kurs[0:4]) #ilk karakter ve nereye kadar olacağı. 
print(kurs[4:14:2]) 
print(kurs[::]) #tamamını almayı gösterir

#FORMAT DENİLEN KISIM


ad = "hasan"
soyad = "Turan"
yas = 40

# msj = "My name is " + ad + " " + soyad + "." + "I'm " + str(yas) + " ye

#msj = "My name {} {}. I'm {} years old.".format(ad, soyad, yas) # kısa yolmuş yersen

#msj=f"my name {ad} I'm {yas} years old." #bildiğim ve en kısa yol.
# f-string


#print(msj)




#UYGULAMA
print("--------------------------------------------------------------------------------------------------------")
title="abra akademide python eğitimi"
print(len(title))
print(title[:5])
print(title[-5:len(title):])
print(title[::-1])