#key value işlemleri oluyor burada.
#önce zor olan sözlğksğn ksımına örnek yapalım.

sehirler=["ist","ankra"]
plakalar=[34,6]

print(plakalar[sehirler.index("ist")])
print(sehirler[plakalar.index(6)])

#şimdi sözlük ile key value yapcaz.

plakas={    #direkt veriye erişmiş oldum.
    "ankara":6,
    "istanbul":34,
    "erzurum": 25
}
plakas["antalya"]=7  #bu şekilde eleman ekleme yapıyoz.
print(plakas["erzurum"])