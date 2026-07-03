print("Hata vermeyen hesap makinesi v2")

try:
    sayi1 = float(input("Birinci sayi: "))
    sayi2 = float(input("Ikinci sayi: "))

    print("1 - Toplama")
    print("2 - Cikarma")
    print("3 - Carpma")
    print("4 - Bolme")

    secim = input("Islem sec: ")

    if secim == "1":
        print("Sonuc:", sayi1 + sayi2)

    elif secim == "2":
        print("Sonuc:", sayi1 - sayi2)

    elif secim == "3":
        print("Sonuc:", sayi1 * sayi2)

    elif secim == "4":
        print("Sonuc:", sayi1 / sayi2)

    else:
        print("Gecersiz islem secimi.")

except ValueError:
    print("Lutfen sadece sayi gir.")

except ZeroDivisionError:
    print("Bir sayi sifira bolunemez")