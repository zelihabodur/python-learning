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
        
        print("Ogrenci Kaydedildi.")

    except ValueError:
        print("Hata: Yas ve Sinif tam sayi, ortalama sayisal deger olmali.")


def ogrencileri_listele():
    print("Kayitli Ogrenciler")

    if len(ogrenciler) == 0:
        print("Henuz Kayitli Ogrenci Yok")
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

def ogrenci_ara():
    print("Ogrenci Arama")

    aranan_isim = input("Aranacak Isim: ").lower()

    bulundu = False

    for ogrenci in ogrenciler:
        if ogrenci['isim'].lower() == aranan_isim:
            print("Ogrenci Bulundu: ")
            print(f"Isim: {ogrenci['isim']}")
            print(f"Yas: {ogrenci['yas']}")
            print(f"Bolum: {ogrenci['bolum']}")
            print(f"Sinif: {ogrenci['sinif']}")
            print(f"Ortalama: {ogrenci['ortalama']}")

            if ogrenci["ortalama"] >= 3:
                print("Durum: Basarili")

            else:
                print("Durum: Gelistirilmeli")

            bulundu = True
            break
    
    if bulundu == False:
        print("Bu isimde ogrenci bulunamadi.")

print("Ogrenci Kayit sistemi v3")

while True:
    print("1 - Ogrenci Ekle")
    print("2 - Ogrencileri Listele")
    print("3 - Isimle Ogrenci Ara")
    print("4 - Cikis")
    
    secim = input("Secimin: ") 

    if secim == "1":
        ogrenci_ekle()

    elif secim == "2":
        ogrencileri_listele()

    elif secim == "3":
        ogrenci_ara()
    
    elif secim == "4":
        print("Program Kapatiliyor..")
        break

    else:
        print("Gecersiz Secim Yaptin.")