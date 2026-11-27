#enumarate konusu da burada buluyor.
#zip konusu da burada bulunuyor
#basit bir konu zaten bildiğim bir muhabbet sadece kullanırken son eleman almama olayına dikkat et.
#öyle kullan gerisi easy 
for a in range(10):
    print(a)

print("--------------------------------------------------------------")
for b in range(10,32,7):
    print(b)

print("--------------------------------------------------------------")

for a in range(10,280,5):
    if a%8==0:
        print(a)   

markalar=["bmw","togg","toyota"]
obj=enumerate(markalar,1)#ilk değere ne vereceğini seçiyorum önden.
print(list(obj))  #bir liste içine alıp ekrana basıyorum. 


for ali,marka in enumerate(markalar,1):
    print(f"{ali}-{marka}")


isim=["ali","ahemy","bilo","reis"]
no=[10,25,44]
print(list(zip(isim,no))) #2 tane listeyi direkt birleştirdik.