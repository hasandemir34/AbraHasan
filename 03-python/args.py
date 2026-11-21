

def display_user(**kwargs):  #pointer mantığı ile ne kadar veri girersen gir içine alıyor.
    

    for key, value in kwargs.items():
        print(f"{key}: {value}")
    print("\n")


display_user(username="sadikturan")
display_user(username="sadikturan", email="info@sadikturan.com")



def sayilar(*args): #bu da isim verilmeden veri gönderme çeşiti 
    print(args)         #mantık tamamen pointer ile aynı.

sayilar(10, 20, 30)