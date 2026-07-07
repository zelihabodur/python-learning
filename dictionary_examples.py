ogrenci = {
    "isim": "Zeliha",
    "yas": 20,
    "bolum": "Endustri Muhendisligi"
}

print(ogrenci)
print(ogrenci["isim"])
print(ogrenci["yas"])
print(ogrenci["bolum"])

ogrenci["sinif"] = 3
print(ogrenci)

ogrenci["yas"] = 21
print(ogrenci)

for anahtar, deger in ogrenci.items():
    print(anahtar, ":", deger)