yas = int(input("yasiniz: "))

if yas <= 12:
    print("cocuk indirimi")

elif yas <= 24:
    print("ogrenci indirimi")

elif yas >= 65:
    print("emekli indirimi")

else:
    print("indirim yok")