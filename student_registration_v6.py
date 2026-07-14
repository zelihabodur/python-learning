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
        print("Henuz kayitli ogrenci yok.")

    for ogrenci in ogrenciler:
        ogrenci_yazdir(ogrenci)

def ogrenci_ara():
    print("Ogrenci Arama")
     
    aranan_isim = input("Aranacak Isim: ")

    ogrenci = ogrenci_bul(aranan_isim)

    if ogrenci is None:
        print("Bu isimde ogrenci bulunamadi.")

    else:
        print("Ogrenci Bulundu: ")
        ogrenci_yazdir(ogrenci)

def ogrenci_sil():
    print("Ogrenci Silme")

    silinecek_isim = input("Silinecek ogrenci ismi: ").lower()

    ogrenci = ogrenci_bul(silinecek_isim)

    if ogrenci is None:
        print("Bu isimde ogrenci bulunamadi.")

    else:
        ogrenciler.remove(ogrenci)
        print("Ogrenci silindi.")

def ogrenci_guncelle():
    print("Ogrenci Guncelleme")

    guncellenecek_isim = input("Guncellenecek ogrenci ismi: ")
    
    ogrenci = ogrenci_bul(guncellenecek_isim)

    if ogrenci is None:
        print("Bu isimde ogrenci bulunamadi.")
        return
   
    print("Mevcut Bilgiler: ")
    ogrenci_yazdir(ogrenci)

    print("Yeni bilgileri gir: ")

    try:
            yeni_isim = input("Yeni isim: ")
            yeni_yas = int(input("Yeni yas: "))
            yeni_bolum = input("Yeni bolum: ")
            yeni_sinif = int(input("Yeni sinif: "))
            yeni_ortalama = float(input("Yeni ortalama: "))

            ogrenci["isim"] = yeni_isim
            ogrenci["yas"] = yeni_yas
            ogrenci["bolum"] = yeni_bolum
            ogrenci["sinif"] = yeni_sinif
            ogrenci["ortalama"] = yeni_ortalama

            print("Ogrenci bilgileri guncellendi.")

    except ValueError:
        print("Hata: Yas ve sinif tam sayi, ortalama sayisal deger olmali.")

def istatistikleri_goster():
    print("Ogrenci Istatistikleri")

    if len(ogrenciler) == 0:
        print("Henuz kayitli ogrenci yok.")
        return
    
    toplam_ogrenci = len(ogrenciler)
    toplam_ortalama = 0
    basarili_sayisi = 0
    gelistirilmeli_sayisi = 0

    for ogrenci in ogrenciler:
        toplam_ortalama += ogrenci["ortalama"]

        if ogrenci['ortalama'] >= 3.0:
            basarili_sayisi += 1

        else:
            gelistirilmeli_sayisi += 1

    sinif_ortalamasi = toplam_ortalama / toplam_ogrenci

    print(f"Toplam ogrenci sayisi: {toplam_ogrenci}")
    print(f"Sinif ortalamasi: {sinif_ortalamasi}")
    print(f"Basarili ogrenci sayisi: {basarili_sayisi}")
    print(f"Gelistirilmeli ogrenci sayisi: {gelistirilmeli_sayisi}")

print("Ogrenci Kayit Sistemi v6")

while True:
    print("1 - Ogrenci Ekle")
    print("2 - Ogrencileri Listele")
    print("3 - Isimle Ogrenci Ara")
    print("4 - Ogrenci Sil") 
    print("5 - Ogrenci Guncelle")
    print("6 - Istatistikleri Goster")
    print("7 - Cikis")

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
        istatistikleri_goster()

    elif secim == "7":
        print("Program Kapatiliyor..")
        break

    else:
        print("Gecersiz secim yaptin.")