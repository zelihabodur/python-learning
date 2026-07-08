ogrenciler = []

def ogrenci_ekle():
    print("Yeni Ogrenci Bilgileri")

    try:
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
        
        print("Ogrenci Kaydedildi")

    except ValueError:
        print("Hata: Yas ve Sinif tam sayi, Ortalama sayisal deger olmalidir")

def ogrencileri_listele():
    print("Kayitli Ogrenciler")

    if len(ogrenciler) == 0:
        print("Henuz kayitli ogrenci yok")
        return
    
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

print("Ogrenci Kayit Sistemi v2")

while True:
    print("1 - Ogrenci ekle")
    print("2 - Ogrencileri listele")
    print("3 - Cikis")

    secim = input("Secimin: ")

    if secim == "1":
        ogrenci_ekle()

    elif secim == "2":
        ogrencileri_listele()

    elif secim == "3":
        print("Program Kapatiliyor..")
        break

    else:
        print("Gecersiz secim yaptin.")

