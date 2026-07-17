import csv

DOSYA_ADI = "stock_products.csv"

ALANLAR = ["urun_kodu", "urun_adi", "kategori", "fiyat", "stok"]

def urunleri_yukle():
    urunler = []

    try:
        with open(DOSYA_ADI, "r", encoding="utf-8") as dosya:
            okuyucu = csv.DictReader(dosya)

            for satir in okuyucu:
                urun = {
                    "urun_kodu": satir["urun_kodu"],
                    "urun_adi": satir["urun_adi"],
                    "kategori": satir["kategori"],
                    "fiyat": float(satir["fiyat"]), 
                    "stok": int(satir["stok"])
                }

                urunler.append(urun)

    except FileNotFoundError:
        return []
    
    return urunler

urunler = urunleri_yukle()

def urunleri_kaydet():
    with open(DOSYA_ADI, "w", newline="", encoding="utf-8") as dosya:
        yazici = csv.DictWriter(dosya, fieldnames=ALANLAR)

        yazici.writeheader()

        for urun in urunler:
            yazici.writerow(urun)

def metin_al(mesaj):
    return input(mesaj).strip()

def tam_sayi_al(mesaj):
    while True:
        try:
            return int(input(mesaj))
        
        except ValueError:
            print("Hata: Lutfen tam sayi girin.")

def ondalikli_sayi_al(mesaj):
    while True:
        try:
            return float(input(mesaj))
        
        except ValueError:
            print("Hata: Lutfen sayisal deger gir")

def urun_yazdir(urun):
    print(f"Urun Kodu: {urun['urun_kodu']}")
    print(f"Urun Adi: {urun['urun_adi']}")
    print(f"Kategori: {urun['kategori']}")
    print(f"Fiyat: {urun['fiyat']}")
    print(f"Stok: {urun['stok']}")

def urun_bul_kod(urun_kodu):
    for urun in urunler:
        if urun["urun_kodu"].lower() == urun_kodu.lower():
            return urun
        
    return None

def urun_ekle():
    print("Yeni Urun Bilgileri")

    urun_kodu = metin_al("Urun Kodu: ")

    mevcut_urun = urun_bul_kod(urun_kodu) 

    if mevcut_urun is not None:
        print("Bu urun kodu zaten kayitli.")   
        return

    urun_adi = metin_al("Urun adi: ")
    kategori = metin_al("Kategori: ")
    fiyat = ondalikli_sayi_al("Fiyat: ")
    stok = tam_sayi_al("Stok: ")

    urun = {
        "urun_kodu": urun_kodu,
        "urun_adi": urun_adi,
        "kategori": kategori,
        "fiyat": fiyat,
        "stok": stok
    }

    urunler.append(urun)
    urunleri_kaydet()

    print("Urun kaydedildi.")

def urunleri_listele():
    print("Kayitli Urunler")

    if len(urunler) == 0:
        print("Henuz kayitli urun yok.")
        return
    
    for urun in urunler:
        urun_yazdir(urun)

def urun_ara():
    print("Urun Arama")

    aranan_kod = metin_al("Aranacak urun kodu: ")

    urun = urun_bul_kod(aranan_kod)

    if urun is None:
        print("Bu kodda urun bulunamadi.")

    else:
        print("Urun bulundu: ")
        urun_yazdir(urun)

def urun_sil():
    print("Urun Silme")

    silinecek_kod = metin_al("Silinecek urun kodu: ")

    urun = urun_bul_kod(silinecek_kod)

    if urun is None:
        print("Bu kodda urun bulunamadi.")

    else:
        urunler.remove(urun)
        urunleri_kaydet()
        print("Urun silindi.")

def urun_guncelle():
    print("Urun Guncelleme")

    guncellenecek_kod = metin_al("Guncellenecek urun kodu: ")

    urun = urun_bul_kod(guncellenecek_kod)

    if urun is None:
        print("Bu kodda urun bulunamadi.")
        return
    
    print("Mevcut Urun Bilgileri:")
    urun_yazdir(urun)

    print("Yeni bilgileri gir:")
    print("Not: Urun kodu degistirilmeyecek.")

    yeni_ad = metin_al("Yeni urun adi: ")
    yeni_kategori = metin_al("Yeni kategori: ")
    yeni_fiyat = ondalikli_sayi_al("Yeni fiyat: ")
    yeni_stok = tam_sayi_al("Yeni stok: ")

    urun["urun_adi"] = yeni_ad
    urun["kategori"] = yeni_kategori
    urun["fiyat"] = yeni_fiyat
    urun["stok"] = yeni_stok

    urunleri_kaydet()

    print("Urun bilgileri guncellendi.")

def stok_ozeti_goster():
    print("Stok Ozeti")

    if len(urunler) == 0:
        print("Henuz kayitli urun yok.")
        return
    
    toplam_urun_sayisi = len(urunler)
    toplam_stok = 0
    toplam_stok_degeri = 0
    kritik_stok_sayisi = 0
    
    for urun in urunler:
        toplam_stok += urun["stok"]
        toplam_stok_degeri += urun["fiyat"] * urun["stok"]

        if urun["stok"] <= 5:
            kritik_stok_sayisi += 1

    print(f"Toplam urun cesidi: {toplam_urun_sayisi}")
    print(f"Toplam stok adedi: {toplam_stok}")
    print(f"Toplam stok degeri: {toplam_stok_degeri}")
    print(f"Kritik stoktaki urun sayisi: {kritik_stok_sayisi}")

print("Urun Stok Sistemi v3")

while True:
    print("1 - Urun Ekle")
    print("2 - Urunleri Listele")
    print("3 - Urun Ara")
    print("4 - Urun Sil")
    print("5 - Urun Guncelle")
    print("6 - Stok Ozeti Goster")
    print("7 - Cikis")

    secim = metin_al("Secimin: ")

    if secim == "1":
        urun_ekle()

    elif secim == "2":
        urunleri_listele()
    
    elif secim == "3":
        urun_ara()

    elif secim == "4":
        urun_sil()

    elif secim == "5":
        urun_guncelle()
    
    elif secim == "6":
        stok_ozeti_goster()

    elif secim == "7":
        print("Program kapatiliyor..")
        break

    else:
        print("Gecersiz secim yaptiniz.")