import modul #tanımladığımız modul kodlarını bu syade main içerisinde kullanıcaz


sonuc=modul.sayi  #moduldeki sayıyı alıp geliyor buraya. 25 değerini mesela
print(sonuc)

ad=modul.urun["marka"] #direkt oradan veriyi çekiyoruz.
print(ad)

toplam=modul.topla(14,24)
print(toplam)

import modul as m  # burda da m olarak kayıt ettim ve kullandım.
sayi=m.sayi
print(sayi)


from modul import sayi,sayilar # bu şekilde yazarsam m yazmaya da gerek yok direkt kullanabiliyorum.
print(sayi)