
try:
    x = int(input("x: "))
    y = int(input("y: "))
    print(x / y)
except ZeroDivisionError as e:
    print("y sıfır olamaz")   
    print(e) 
except ValueError:
    print("x ve y sayı olmalıdır")
except Exception as e :     #yukardaki 2 türden hata gelmez ise alttaki hata mesajı fırlatılır.
    print("bilinmeyen bir hata oluştu")
    print(e)