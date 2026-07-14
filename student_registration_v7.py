import json

DOSYA_ADI = "student.json"

def verileri_yukle():
    try:
        with open(DOSYA_ADI, "r", encoding="utf-8") as dosya:
            return json.load(dosya)
        
    except FileNotFoundError:
        return []
    
    except json.JSONDecodeError:
        return []

ogrenciler = verileri_yukle()

def verileri_kaydet():
    with open(DOSYA_ADI, "w", encoding="utf-8") as dosya:
        json.dump(ogrenciler, dosya, ensure_ascii=False, indent=4)

def ogrenci_yazdir(ogrenci):
    print(f"Isim: {ogrenci['isim']}")
    print(f"Yas: {ogrenci['yas']}")
    print(f"Bolum: {ogrenci['bolum']}")
    print(f"Sinif: {ogrenci['sinif']}")
    print(f"Ortalama: {ogrenci['ortalama']}")

    if ogrenci["ortalama"] >= 3.0:
        print("Durum: Basarili")
    else:
        print("Durum: Gelistirilmeli")


def ogrenci_bul(isim):
    for ogrenci in ogrenciler:
        if ogrenci["isim"].lower() == isim.lower():
            return ogrenci

    return None


def ogrenci_ekle():
    print("\nYeni Ogrenci Bilgileri")

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
        verileri_kaydet()

        print("Ogrenci kaydedildi.")

    except ValueError:
        print("Hata: Yas ve sinif tam sayi, ortalama sayisal deger olmali.")


def ogrencileri_listele():
    print("Kayitli Ogrenciler")
    print("------------------")

    if len(ogrenciler) == 0:
        print("Henuz kayitli ogrenci yok.")
        return

    for ogrenci in ogrenciler:
        ogrenci_yazdir(ogrenci)
        print("------------------")


def ogrenci_ara():
    print("Ogrenci Arama")

    aranan_isim = input("Aranacak isim: ")

    ogrenci = ogrenci_bul(aranan_isim)

    if ogrenci is None:
        print("Bu isimde ogrenci bulunamadi.")
    else:
        print("Ogrenci bulundu:")
        ogrenci_yazdir(ogrenci)


def ogrenci_sil():
    print("Ogrenci Silme")

    silinecek_isim = input("Silinecek ogrenci ismi: ")

    ogrenci = ogrenci_bul(silinecek_isim)

    if ogrenci is None:
        print("Bu isimde ogrenci bulunamadi.")
    else:
        ogrenciler.remove(ogrenci)
        verileri_kaydet()
        print("Ogrenci silindi.")


def ogrenci_guncelle():
    print("Ogrenci Guncelleme")

    guncellenecek_isim = input("Guncellenecek ogrenci ismi: ")

    ogrenci = ogrenci_bul(guncellenecek_isim)

    if ogrenci is None:
        print("Bu isimde ogrenci bulunamadi.")
        return

    print("Mevcut bilgiler:")
    ogrenci_yazdir(ogrenci)

    print("Yeni bilgileri gir:")

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

        verileri_kaydet()

        print("Ogrenci bilgileri guncellendi.")

    except ValueError:
        print("Hata: Yas ve sinif tam sayi, ortalama sayisal deger olmali.")


def istatistikleri_goster():
    print("Ogrenci Istatistikleri")
    print("----------------------")

    if len(ogrenciler) == 0:
        print("Henuz kayitli ogrenci yok.")
        return

    toplam_ogrenci = len(ogrenciler)
    toplam_ortalama = 0
    basarili_sayisi = 0
    gelistirilmeli_sayisi = 0

    for ogrenci in ogrenciler:
        toplam_ortalama += ogrenci["ortalama"]

        if ogrenci["ortalama"] >= 3.0:
            basarili_sayisi += 1
        else:
            gelistirilmeli_sayisi += 1

    sinif_ortalamasi = toplam_ortalama / toplam_ogrenci

    print(f"Toplam ogrenci sayisi: {toplam_ogrenci}")
    print(f"Sinif ortalamasi: {sinif_ortalamasi}")
    print(f"Basarili ogrenci sayisi: {basarili_sayisi}")
    print(f"Gelistirilmeli ogrenci sayisi: {gelistirilmeli_sayisi}")


print("Ogrenci Kayit Sistemi v7")

while True:
    print("1 - Ogrenci ekle")
    print("2 - Ogrencileri listele")
    print("3 - Isimle ogrenci ara")
    print("4 - Ogrenci sil")
    print("5 - Ogrenci guncelle")
    print("6 - Istatistikleri goster")
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
        print("Program kapatiliyor...")
        break

    else:
        print("Gecersiz secim yaptin.")