import sqlite3

conn = sqlite3.connect("sales_intro.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS urunler")

cursor.execute("""
CREATE TABLE urunler (
    urun_id INTEGER PRIMARY KEY,
    urun_adi TEXT,
    kategori TEXT,
    fiyat REAL,
    stok INTEGER
)
""")

urunler = [
    (1, "Laptop", "Elektronik", 25000, 5),
    (2, "Mouse", "Elektronik", 500, 20),
    (3, "Klavye", "Elektronik", 1200, 10),
    (4, "Defter", "Kirtasiye", 50, 100),
    (5, "Kalem", "Kirtasiye", 10, 200),
    (6, "Sandalye", "Mobilya", 1500, 8)
]

cursor.executemany("""
INSERT INTO urunler (urun_id, urun_adi, kategori, fiyat, stok)
VALUES (?, ?, ?, ?, ?)
""", urunler)

conn.commit()

print("Tum urunler:")
cursor.execute("SELECT * FROM urunler")
tum_urunler = cursor.fetchall()

for urun in tum_urunler:
    print(urun)


print("Sadece urun adi ve fiyat:")
cursor.execute("SELECT urun_adi, fiyat FROM urunler")
urun_fiyatlari = cursor.fetchall()

for urun in urun_fiyatlari:
    print(urun)


print("Elektronik kategorisindeki urunler:")
cursor.execute("SELECT * FROM urunler WHERE kategori = 'Elektronik'")
elektronik_urunler = cursor.fetchall()

for urun in elektronik_urunler:
    print(urun)


print("Fiyati 1000 TL'den yuksek urunler:")
cursor.execute("SELECT * FROM urunler WHERE fiyat > 1000")
pahali_urunler = cursor.fetchall()

for urun in pahali_urunler:
    print(urun)


print("Stogu 10'dan az veya esit olan urunler:")
cursor.execute("SELECT * FROM urunler WHERE stok <= 10")
kritik_stok_urunler = cursor.fetchall()

for urun in kritik_stok_urunler:
    print(urun)


print("Fiyata gore buyukten kucuge siralama:")
cursor.execute("SELECT * FROM urunler ORDER BY fiyat DESC")
fiyata_gore_sirali = cursor.fetchall()

for urun in fiyata_gore_sirali:
    print(urun)


conn.close()