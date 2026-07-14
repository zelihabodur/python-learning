import json 

DOSYA_ADI = "students_v9.json"

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

def metin_al(mesaj):
    return input(mesaj).strip()

def tam_sayi_al(mesaj):
    while True:
        try:
            return float(input(mesaj))
        
        except ValueError:
            print("Hata: Lutfen sayisal deger gir.")

def ondalikli_sayi_al(mesaj):
    while True:
        try:
            return float(input(mesaj))
        except ValueError:
            print("Hata: Lutfen sayisal deger gir.")

def ogrenci_yazdir(ogrenci):
    print(f"Numara: {ogrenci['numara']}")
    print(f"Isim: {ogrenci['isim']}")
    print(f"Yas: {ogrenci['yas']}")
    print(f"Bolum: {ogrenci['bolum']}")
    print(f"Sinif: {ogrenci['sinif']}")
    print(f"Ortalama: {ogrenci['ortalama']}")
    
    if ogrenci['ortalama'] >= 3:
        print("Durum: Basarili")

    else:
        print("Durum: Gelistirilmeli")

def ogrenci_bul_numara(numara):
    for ogrenci in ogrenciler:
        if ogrenci["numara"] == numara:
            return ogrenci
        
    return None

def ogrenci_ekle():
    print("Yeni Ogrenci Bilgileri")

    numara = metin_al("Ogrenci Numarasi: ")

    mevcut_ogrenci = ogrenci_bul_numara(numara)

    if mevcut_ogrenci is not None:
        print("Bu numara zaten kayitli.")
        return
    
    isim = metin_al("Isim: ")
    yas = tam_sayi_al("Yas: ")
    bolum = metin_al("Bolum: ")
    sinif = tam_sayi_al("Sinif: ")
    ortalama = ondalikli_sayi_al("Ortalama: ")

    ogrenci = {
        "numara": numara,
        "isim": isim,
        "yas": yas,
        "bolum": bolum,
        "sinif": sinif,
        "ortalama": ortalama
    }

    ogrenciler.append(ogrenci)
    verileri_kaydet()

    print("Ogrenci Kaydedildi")

def ogrencileri_listele():
    print("Kayitli Ogrenciler")

    if len(ogrenciler) == 0:
        print("Henuz kayitli ogrenci yok.")
        return

    for ogrenci in ogrenciler:
        ogrenci_yazdir(ogrenci)

def ogrenci_ara():
    print("Ogrenci Arama")

    aranan_numara = metin_al("Aranacak ogrenci numarasi: ")

    ogrenci = ogrenci_bul_numara(aranan_numara)

    if ogrenci is None:
        print("Bu numarada ogrenci bulunamadi.")
    else:
        print("Ogrenci bulundu:")
        ogrenci_yazdir(ogrenci)


def ogrenci_sil():
    print("Ogrenci Silme")

    silinecek_numara = metin_al("Silinecek ogrenci numarasi: ")

    ogrenci = ogrenci_bul_numara(silinecek_numara)

    if ogrenci is None:
        print("Bu numarada ogrenci bulunamadi.")
    else:
        ogrenciler.remove(ogrenci)
        verileri_kaydet()
        print("Ogrenci silindi.")


def ogrenci_guncelle():
    print("Ogrenci Guncelleme")

    guncellenecek_numara = metin_al("Guncellenecek ogrenci numarasi: ")

    ogrenci = ogrenci_bul_numara(guncellenecek_numara)

    if ogrenci is None:
        print("Bu numarada ogrenci bulunamadi.")
        return

    print("Mevcut bilgiler:")
    ogrenci_yazdir(ogrenci)

    print("Yeni bilgileri gir:")
    print("Not: Ogrenci numarasi degistirilmeyecek.")

    yeni_isim = metin_al("Yeni isim: ")
    yeni_yas = tam_sayi_al("Yeni yas: ")
    yeni_bolum = metin_al("Yeni bolum: ")
    yeni_sinif = tam_sayi_al("Yeni sinif: ")
    yeni_ortalama = ondalikli_sayi_al("Yeni ortalama: ")

    ogrenci["isim"] = yeni_isim
    ogrenci["yas"] = yeni_yas
    ogrenci["bolum"] = yeni_bolum
    ogrenci["sinif"] = yeni_sinif
    ogrenci["ortalama"] = yeni_ortalama

    verileri_kaydet()

    print("Ogrenci bilgileri guncellendi.")


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

        if ogrenci["ortalama"] >= 3.0:
            basarili_sayisi += 1
        else:
            gelistirilmeli_sayisi += 1

    sinif_ortalamasi = toplam_ortalama / toplam_ogrenci

    print(f"Toplam ogrenci sayisi: {toplam_ogrenci}")
    print(f"Sinif ortalamasi: {sinif_ortalamasi}")
    print(f"Basarili ogrenci sayisi: {basarili_sayisi}")
    print(f"Gelistirilmeli ogrenci sayisi: {gelistirilmeli_sayisi}")


def menu_goster():
    print("1 - Ogrenci ekle")
    print("2 - Ogrencileri listele")
    print("3 - Numara ile ogrenci ara")
    print("4 - Ogrenci sil")
    print("5 - Ogrenci guncelle")
    print("6 - Istatistikleri goster")
    print("7 - Cikis")


def main():
    print("Ogrenci Kayit Sistemi v9")

    while True:
        menu_goster()

        secim = metin_al("Secimin: ")

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

main()