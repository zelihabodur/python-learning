def toplama(a, b):
    return a + b

def cikarma(a, b):
    return a - b

def carpma(a, b):
    return a * b

def bolme(a, b):
    return a / b

print("Hesap Makinesi v4")

while True:
    print("1 - Toplama")
    print("2 - Cikarma")
    print("3 - Carpma")
    print("4 - Bolme")
    print("5 - Cikis")

    secim = input("Islem sec: ")

    if secim == "5":
        print("Program Kapatiliyor..")
        break

    if secim not in("1","2","3","4"):
        print("Gecersiz islem secimi.")
        continue

    try:
        sayi1 = float(input("Birinci sayi: "))
        sayi2 = float(input("Ikinci sayi: "))

        if secim == "1":
            print("Sonuc:", toplama(sayi1, sayi2))

        elif secim == "2":
            print("Sonuc:", cikarma(sayi1, sayi2))

        elif secim == "3":
            print("Sonuc:", carpma(sayi1, sayi2))

        else:
            print("Somnuc:", bolme(sayi1, sayi2))

    except ValueError:
        print("Lutfen sayi gir.")
    
    except ZeroDivisionError:
        print("Bir sayi 0'a bolunemez")