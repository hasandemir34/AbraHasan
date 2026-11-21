

def selamla(isim="isimsiz",mesaj="selamlar"): #fonksiyonlarda son karakter default olabilir sadece
    return f"{isim} kişisi {mesaj}"


sonuc=selamla("hasan","merhaba")
sonuc2=selamla("cabbar")
sonuc=selamla()
print(sonuc)
print(sonuc2)


def toplam(a, b):
    return a + b

def cikarma(a, b):
    return a - b

def islem(a, b, fn=toplam): #hangi fonk seçeceğimizi de ayarladık. default olarak toplama yapacak.
    return fn(a, b)  


sonuc = islem(10, 20, cikarma) #fn olarak çıkarma yapmasını istedik mesela. 
sonuc = islem(10, 20)
sonuc = islem(10, 20, toplam)