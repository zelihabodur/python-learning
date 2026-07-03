try:
    sayi = int(input("Bir sayi gir: "))
    print("Girdigin sayi:", sayi)

except:
    print("Hatali giris yaptin. Lutfen sayi gir.")

try:
    yas = int(input("Yasini gir: "))

    if yas >= 18:
        print("Resitsin.")
    
    else:
        print("Resit degilsin.")

except ValueError:
    print("Yas sayi olarak girilmelidir.")
