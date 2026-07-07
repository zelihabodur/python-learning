ogrenci = {
    "isim": input("Isim: "),
    "yas": int(input("Yas: ")),
    "bolum": input("Bolum: "),
    "sinif": int(input("Sinif: ")),
    "ortalama": float(input("Ortalama: "))
}

print("Ogrenci Karti")

for anahtar, deger in ogrenci.items():
    print(anahtar, ":", deger)

if ogrenci["ortalama"] >= 3.0:
    print("Durum Basaril")

else:
    print("Durum Gelistirilmeli")