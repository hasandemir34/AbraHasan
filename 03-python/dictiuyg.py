
ogr={  #bu iç içe {} sayesinde alt küme tarzında veri de yazabiliyorum.
    101: {"isim": "hasan bilgi", "not":(80,50)} ,
    102: {"isim": "ada bilgi", "not":(50,50)},
    103: {"isim": "kemal bilgi", "not":(80,80)}

}

no= int(input("ögr no girin: ")) 

print(f"{ogr[no]["isim"]} derse hoş geldin. not ortalaman: {sum(ogr[no]['not']) / len(ogr[no]['not'])}")