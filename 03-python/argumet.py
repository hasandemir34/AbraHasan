

def hitap(firstname:str,lastname:str) ->str:  #girilmesi gereken veririn türünü belirledik ancak pythonda bu 
    return f"hoş geldin {firstname} {lastname}"  #direkt engelleme olmuyor bu yazım şeklinde. 10 da yazsa direkt
                                                #str e çevirip ekrana basıyor.
sonuc=hitap("hasan","demir")
sonuc=hitap(10,"demir")
print(sonuc)