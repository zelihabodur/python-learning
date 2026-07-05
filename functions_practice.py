def kare_al (sayi):
    return sayi * sayi

sonuc = kare_al(5)
print(sonuc)

def yas_kontrol(yas):
    if yas >= 18:
        return "Resit"
    
    else:
        return "Resit Degil"

print(yas_kontrol(20))
print(yas_kontrol(15))

def cift_mi(sayi):
    if sayi % 2 == 0:
        return True
    
    else:
        return False
    
print(cift_mi(10))
print(cift_mi(17))

def ortalama_hesapla(not1, not2, not3):
    return (not1 + not2 + not3) / 3

ortalama = ortalama_hesapla(80, 90, 100)
print("Ortalama:", ortalama)

sayi = int(input("Bir sayi gir: "))
print("Sayinin karesi:", kare_al(sayi))
