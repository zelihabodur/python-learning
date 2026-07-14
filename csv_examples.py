import csv

dosya_adi = "products.csv"

urunler = [
    {"urun_adi": "Laptop", "fiyat": 25000, "stok": 5},
    {"urun_adi": "Mouse", "fiyat": 500, "stok": 20},
    {"urun_adi": "Klavye", "fiyat": 1200, "stok": 10}
]

with open(dosya_adi, "w", newline="", encoding="utf-8") as dosya:
    alanlar = ["urun_adi", "fiyat", "stok"]

    yazici = csv.DictWriter(dosya, fieldnames=alanlar)

    yazici.writeheader()

    for urun in urunler:
        yazici.writerow(urun)

print("CSV dosyasi olusturuldu.")

with open(dosya_adi, "r", encoding="utf-8") as dosya:
    okuyucu = csv.DictReader(dosya)

    print("CSV dosyasindaki urunler:")

    for satir in okuyucu:
        print("Urun adi:", satir["urun_adi"])
        print("Fiyat:", satir["fiyat"])
        print("Stok:", satir["stok"])
