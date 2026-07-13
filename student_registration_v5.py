ogrenciler = []

def ogrenci_yazdir(ogrenci):
    print(f"Isim: {ogrenci['isim']}")
    print(f"Yas: {ogrenci['yas']}")
    print(f"Bolum: {ogrenci['bolum']}")
    print(f"Sinif: {ogrenci['sinif']}")
    print(f"Ortalama: {ogrenci['ortalama']}")

    if ogrenci['ortalama'] >= 3:
        print("Durum: Basarili")

    else:
        print("Durum: Gelistirilmeli")

def ogrenci_bul(isim):
    for ogrenci in ogrenciler:
        if ogrenci["isim"].lower() == isim.lower():
            return ogrenci
        
    return None

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
        print("Hata: Yas ve Sinif tam sayi, Ortalama sayisal deger olmalidir.")

def ogrencileri_listele():
    print("Kayitli Ogrenciler")

    if len(ogrenciler) == 0:
        print("Henuz Kayitli Ogrenci Yok")
        return
    
    for ogrenci in ogrenciler:
        ogrenci_yazdir(ogrenci)

def ogrenci_ara():
    print("Ogrenci Arama")

    aranan_isim = input("Aranacak Isim: ")

    ogrenci = ogrenci_bul(aranan_isim)

    if ogrenci is None:
        print("Bu isimde ogrenci bulunamadi.")

    else:
        print("Ogrenci bulundu: ")
        ogrenci_yazdir(ogrenci)

def ogrenci_sil():
    print("Ogrenci Silme")

    silinecek_isim = input("Silinecek Ogrencinin Ismi: ").lower()

    ogrenci = ogrenci_bul(silinecek_isim)

    if ogrenci is None:
        print("Bu isimde ogrenci bulunamadi.")

    else:
        ogrenciler.remove(ogrenci)
        print("Ogrenci silindi.")

def ogrenci_guncelle():
    print("Ogrenci Guncelleme")

    guncellenecek_isim = input("Guncellenecek Ogrenci Ismi: ")

    ogrenci = ogrenci_bul(guncellenecek_isim)

    if ogrenci is None:
        print("Bu isimde ogrenci bulunamadi.")
        return

    print("Mevcut Bilgiler: ")
    ogrenci_yazdir(ogrenci)

    print("Yeni bilgileri gir")

    try:
        yeni_isim = input("Yeni Isim: ")
        yeni_yas = int(input("Yeni Yas: "))
        yeni_bolum = input("Yeni Bolum: ")
        yeni_sinif = int(input("Yeni Sinif: "))
        yeni_ortalama = float(input("Yeni Ortalama: "))

        ogrenci["isim"] = yeni_isim
        ogrenci["yas"] = yeni_yas
        ogrenci["bolum"] = yeni_bolum
        ogrenci["sinif"] = yeni_sinif
        ogrenci["ortalama"] = yeni_ortalama

        print("Ogrenci bilgileri guncellendi.")

    except ValueError:
        print("Hata: Yas ve Sinif tam sayi, ortalama sayisal deger olmalidir.")

print("Ogrenci Kayit Sistemi v5")

while True:
    print("1 - Ogrenci Ekle")
    print("2 - Ogrencileri Listele")
    print("3 - Isimle Ogrenci Ara")
    print("4 - Ogrenci Sil")
    print("5 - Ogrenci Guncelle")
    print("6 - Cikis")

    secim = input("Secimin: ")

    if secim == "1":
        ogrenci_ekle()

    elif secim == "2":
        ogrencileri_listele()

    elif secim == "3":
        ogrenci_ara()

    elif secim == "4":
        ogrenci_sil()

    elif secim == "5":
        ogrenci_guncelle()

    elif secim == "6":
        print("Program Kapatiliyor..")
        break

    else:
        print("Gecersiz secim yaptin.")