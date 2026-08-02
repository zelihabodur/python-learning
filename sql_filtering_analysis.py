import sqlite3

conn = sqlite3.connect("sales_intro.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS urun_fitlreleme")

cursor.execute("""
CREATE TABLE urun_filtreleme (
    urun_id INTEGER PRIMARY KEY,
    urun_adi TEXT,
    kategori TEXT,
    marka TEXT,
    sehir TEXT,
    fiyat REAL,
    stok INTEGER
)
""")

urunler = [
    (1, "Laptop", "Elektronik", "Lenovo", "Adana", 25000, 5),
    (2, "Mouse", "Elektronik", "Logitech", "Adana", 500, 20),
    (3, "Klavye", "Elektronik", "Logitech", "Mersin", 1200, 10),
    (4, "Monitor", "Elektronik", "Samsung", "Istanbul", 6000, 4),
    (5, "Telefon", "Elektronik", "Samsung", "Ankara", 18000, 6),
    (6, "Kulaklik", "Elektronik", "JBL", "Mersin", 900, 15),
    (7, "Defter", "Kirtasiye", "Mopak", "Ankara", 50, 100),
    (8, "Kalem", "Kirtasiye", "Faber", "Adana", 10, 200),
    (9, "Dosya", "Kirtasiye", "Mopak", "Adana", 25, 80),
    (10, "Sandalye", "Mobilya", "Ikea", "Istanbul", 1500, 8),
    (11, "Masa", "Mobilya", "Ikea", "Ankara", 3500, 3),
    (12, "Koltuk", "Mobilya", "Bellona", "Mersin", 12000, 2)
]

cursor.executemany("""
INSERT INTO urun_filtreleme (
    urun_id,
    urun_adi,
    kategori,
    marka,
    sehir,
    fiyat,
    stok
)
VALUES (?, ?, ?, ?, ?, ?, ?)
""", urunler)

conn.commit()


print("Tum urunler:")
cursor.execute("SELECT * FROM urun_filtreleme")
for satir in cursor.fetchall():
    print(satir)


print("Tekrarsiz kategoriler:")
cursor.execute("SELECT DISTINCT kategori FROM urun_filtreleme")
for satir in cursor.fetchall():
    print(satir)


print("Fiyati 1000 ile 10000 arasinda olan urunler:")
cursor.execute("""
SELECT urun_adi, kategori, fiyat
FROM urun_filtreleme
WHERE fiyat BETWEEN 1000 AND 10000
ORDER BY fiyat DESC
""")
for satir in cursor.fetchall():
    print(satir)


print("Elektronik veya Mobilya kategorisindeki urunler:")
cursor.execute("""
SELECT urun_adi, kategori, fiyat
FROM urun_filtreleme
WHERE kategori IN ('Elektronik', 'Mobilya')
ORDER BY kategori, fiyat DESC
""")
for satir in cursor.fetchall():
    print(satir)


print("\nAdinda 'la' gecen urunler:")
cursor.execute("""
SELECT urun_adi, kategori, fiyat
FROM urun_filtreleme
WHERE urun_adi LIKE '%la%'
""")
for satir in cursor.fetchall():
    print(satir)


print("Stogu kritik ve fiyati yuksek urunler:")
cursor.execute("""
SELECT urun_adi, kategori, fiyat, stok
FROM urun_filtreleme
WHERE stok <= 5 AND fiyat >= 5000
ORDER BY fiyat DESC
""")
for satir in cursor.fetchall():
    print(satir)


print("Adana veya Mersin'deki urunler:")
cursor.execute("""
SELECT urun_adi, sehir, kategori, fiyat
FROM urun_filtreleme
WHERE sehir = 'Adana' OR sehir = 'Mersin'
ORDER BY sehir
""")
for satir in cursor.fetchall():
    print(satir)


print("En pahali 3 urun:")
cursor.execute("""
SELECT urun_adi, kategori, fiyat
FROM urun_filtreleme
ORDER BY fiyat DESC
LIMIT 3
""")
for satir in cursor.fetchall():
    print(satir)


print("Markaya gore urun sayisi:")
cursor.execute("""
SELECT marka, COUNT(*) AS urun_sayisi
FROM urun_filtreleme
GROUP BY marka
ORDER BY urun_sayisi DESC
""")
for satir in cursor.fetchall():
    print(satir)


conn.close()