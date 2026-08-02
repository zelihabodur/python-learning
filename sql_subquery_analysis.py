import sqlite3

conn = sqlite3.connect("sales_intro.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS subquery_satislar")

cursor.execute(""" 
CREATE TABLE subquery_satislar (
    satis_id INTEGER PRIMARY KEY,
    sehir TEXT,
    kategori TEXT,
    urun_adi TEXT,
    musteri_tipi TEXT,
    adet INTEGER,
    birim_fiyat REAL
)
""")

satislar = [
    (1, "Adana", "Elektronik", "Laptop", "Bireysel", 1, 25000),
    (2, "Adana", "Elektronik", "Mouse", "Bireysel", 2, 500),
    (3, "Mersin", "Elektronik", "Klavye", "Bireysel", 1, 1200),
    (4, "Istanbul", "Elektronik", "Monitor", "Kurumsal", 4, 6000),
    (5, "Istanbul", "Mobilya", "Sandalye", "Kurumsal", 10, 1500),
    (6, "Ankara", "Mobilya", "Masa", "Kurumsal", 3, 3500),
    (7, "Ankara", "Kirtasiye", "Defter", "Bireysel", 50, 50),
    (8, "Adana", "Kirtasiye", "Kalem", "Bireysel", 100, 10),
    (9, "Mersin", "Elektronik", "Kulaklik", "Bireysel", 8, 900),
    (10, "Istanbul", "Elektronik", "Telefon", "Kurumsal", 2, 18000),
    (11, "Mersin", "Mobilya", "Koltuk", "Kurumsal", 2, 12000),
    (12, "Adana", "Kirtasiye", "Dosya", "Bireysel", 40, 25)
]

cursor.executemany(""" 
INSERT INTO subquery_satislar (
    satis_id,
    sehir,
    kategori,
    urun_adi,
    musteri_tipi,
    adet,
    birim_fiyat
)
VALUES (?, ?, ?, ?, ?, ?, ?)
""", satislar)

conn.commit()

print("Tum satislar:")
cursor.execute("SELECT * FROM subquery_satislar")
for satir in cursor.fetchall():
    print(satir)

print("Ortalama birim fiyat:")
cursor.execute("""
SELECT AVG(birim_fiyat)
FROM subquery_satislar
""")
ortalama_fiyat = cursor.fetchone()[0]
print(round(ortalama_fiyat, 2))

print("Ortalama fiyatin ustundeki urunler:")
cursor.execute(""" 
SELECT
    urun_adi,
    kategori,
    birim_fiyat
FROM subquery_satislar
WHERE birim_fiyat > (
    SELECT AVG(birim_fiyat)
    FROM subquery_satislar
)
ORDER BY birim_fiyat DESC
""")
for satir in cursor.fetchall():
    print(satir)

    print("Ortalama cironun ustundeki satislar:")
cursor.execute("""
SELECT 
    urun_adi,
    kategori,
    adet,
    birim_fiyat,
    adet * birim_fiyat AS ciro
FROM subquery_satislar
WHERE adet * birim_fiyat > (
    SELECT AVG(adet * birim_fiyat)
    FROM subquery_satislar
)
ORDER BY ciro DESC
""")
for satir in cursor.fetchall():
    print(satir)


print("En yuksek cirolu kategori:")
cursor.execute("""
SELECT 
    kategori,
    SUM(adet * birim_fiyat) AS toplam_ciro
FROM subquery_satislar
GROUP BY kategori
ORDER BY toplam_ciro DESC
LIMIT 1
""")
for satir in cursor.fetchall():
    print(satir)


print("En yuksek cirolu kategorideki satislar:")
cursor.execute("""
SELECT 
    urun_adi,
    kategori,
    adet,
    birim_fiyat,
    adet * birim_fiyat AS ciro
FROM subquery_satislar
WHERE kategori = (
    SELECT kategori
    FROM subquery_satislar
    GROUP BY kategori
    ORDER BY SUM(adet * birim_fiyat) DESC
    LIMIT 1
)
ORDER BY ciro DESC
""")
for satir in cursor.fetchall():
    print(satir)


print("En yuksek cirolu sehirdeki satislar:")
cursor.execute("""
SELECT 
    sehir,
    urun_adi,
    kategori,
    adet * birim_fiyat AS ciro
FROM subquery_satislar
WHERE sehir = (
    SELECT sehir
    FROM subquery_satislar
    GROUP BY sehir
    ORDER BY SUM(adet * birim_fiyat) DESC
    LIMIT 1
)
ORDER BY ciro DESC
""")
for satir in cursor.fetchall():
    print(satir)


print("Kategori ciro ozeti:")
cursor.execute("""
SELECT 
    kategori,
    SUM(adet * birim_fiyat) AS toplam_ciro
FROM subquery_satislar
GROUP BY kategori
ORDER BY toplam_ciro DESC
""")
for satir in cursor.fetchall():
    print(satir)


print("Kategori ortalamasinin ustundeki kategoriler:")
cursor.execute("""
SELECT 
    kategori,
    toplam_ciro
FROM (
    SELECT 
        kategori,
        SUM(adet * birim_fiyat) AS toplam_ciro
    FROM subquery_satislar
    GROUP BY kategori
) AS kategori_ozeti
WHERE toplam_ciro > (
    SELECT AVG(toplam_ciro)
    FROM (
        SELECT 
            kategori,
            SUM(adet * birim_fiyat) AS toplam_ciro
        FROM subquery_satislar
        GROUP BY kategori
    ) AS alt_kategori_ozeti
)
ORDER BY toplam_ciro DESC
""")
for satir in cursor.fetchall():
    print(satir)


conn.close()