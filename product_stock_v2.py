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
                    "fiyat": satir["fiyat"],
                    "stok": satir["stok"]
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

def urun_yazdir(urun):
    print(f"Urun Kodu: {urun['urun_kodu']}")
    print(f"Urun Adi: {urun['urun_adi']}")
    print(f"Kategori: {urun['kategori']}")
    print(f"Fiyat: {urun['fiyat']}")
    print(f"Stok: {urun['stok']}")

def urun_bul_kod(urun_kodu):
    for urun in urunler:
        if urun['urun_kodu'].lower() == urun_kodu.lower():
            return urun
        
    return None

def urun_ekle():
    print("Yeni Urun Bilgileri")

    urun_kodu = input("Urun Kodu: ").strip()

    mevcut_urun = urun_bul_kod(urun_kodu)

    if mevcut_urun is not None:
        print("Bu urun kodu zaten kayitli.")
        return
    
    try:
        urun_adi = input("Urun Adi: ")
        kategori = input("Kategori:")
        fiyat = float(input("Fiyat: "))
        stok = int(input("Stok: "))
        
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

    except ValueError:
        print("Hata: Fiyat sayisal deger, stok tam sayi olmali.")

def urunleri_listele():
    print("Kayitli Urunler")
    
    if len(urunler) == 0:
        print("Henuz kayitli urun yok.")
        return

    for urun in urunler:
        urun_yazdir(urun)

def urun_ara():
    print("Urun Arama")

    aranan_kod = input("Aranan Urun Kodu: ").strip()

    urun = urun_bul_kod(aranan_kod)

    if urun is None:
        print("Bu kodda urun bulunamadi.")

    else:
        print("Urun bulundu:")
        urun_yazdir(urun)


print("Urun Stok Sistemi v2")

while True:
    print("1 - Urun Ekle")
    print("2 - Urun Listele")
    print("3 - Urun Ara")
    print("4 - Cikis")

    secim = input("Secimin: ")

    if secim == "1":
        urun_ekle()

    elif secim == "2":
        urunleri_listele()

    elif secim == "3":
        urun_ara()

    elif secim == "4":
        print("Program Kapatiliyor..")
        break

    else:
        print("Gecersiz secim yaptiniz.")
    