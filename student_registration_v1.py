ogrenciler = []

print("Ogrenci Kayit Sistemi v1")

while True:
    print("Yeni Ogrenci Bilgileri")

    isim = input("Isim: ")
    yas = int(input("Yas: "))
    bolum = input("Bolum: ")
    sinif = int(input("Sinif: "))
    ortalama = float(input("Ortalama: "))

    ogrenci = {
        "isim": isim,
        "yas": yas,
        "bolum": bolum,
        "sinif": sinif,
        "ortalama": ortalama
    }

    ogrenciler.append(ogrenci)

    print("Ogrenci Kaydedildi.")

    devam = input("Yeni ogrenci eklemek istiyor musun? evet/hayir: ").lower()

    if devam == "hayir":
        break

print("Kayitli Ogrenciler")

for ogrenci in ogrenciler:
    print(f"Isim: {ogrenci['isim']}")
    print(f"Yas: {ogrenci['yas']}")
    print(f"Bolum: {ogrenci['bolum']}")
    print(f"Sinif: {ogrenci['sinif']}")
    print(f"Ortalama: {ogrenci['ortalama']}")

    if ogrenci["ortalama"] >= 3:
        print("Durum: Basarili")

    else:
        print("Durum: Gelistirilmeli")