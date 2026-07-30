import sqlite3

conn = sqlite3.connect("sales_intro.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS siparis_analizi")

cursor.execute("""
CREATE TABLE siparis_analizi (
    satis_id INTEGER PRIMARY KEY,
    sehir TEXT,
    kategori TEXT,
    urun_adi TEXT,
    musteri_tipi TEXT,
    adet INTEGER,
    birim_fiyat REAL
)
""")

siparisler = [
    (1, "Adana", "Elektronik", "Laptop", "Bireysel", 1, 25000),
    (2, "Adana", "Elektronik", "Mouse", "Bireysel", 2, 500),
    (3, "Mersin", "Elektronik", "Klavye", "Bireysel", 1, 1200),
    (4, "Istanbul", "Elektronik", "Monitor", "Kurumsal", 4, 6000),
    (5, "Istanbul", "Mobilya", "Sandalye", "Kurumsal", 10, 1500),
    (6, "Ankara", "Mobilya", "Masa", "Kurumsal", 3, 3500),
    (7, "Ankara", "Kirtasiye", "Defter", "Bireysel", 50, 50),
    (8, "Adana", "Kirtasiye", "Kalem", "Bireysel", 100, 10),
    (9, "Mersin", "Elektronik", "Kulaklik", "Bireysel", 8, 900),
    (10, "Istanbul", "Elektronik", "Telefon", "Kurumsal", 2, 18000)
]

cursor.executemany("""
INSERT INTO siparis_analizi (
    satis_id,
    sehir,
    kategori,
    urun_adi,
    musteri_tipi,
    adet,
    birim_fiyat
)
VALUES (?, ?, ?, ?, ?, ?, ?)
""", siparisler)

conn.commit()


print("Tum siparisler:")
cursor.execute("SELECT * FROM siparis_analizi")
for satir in cursor.fetchall():
    print(satir)


print("Ciro hesaplanmis siparisler:")
cursor.execute("""
SELECT
    satis_id,
    urun_adi,
    kategori,
    adet,
    birim_fiyat,
    adet * birim_fiyat AS ciro
FROM siparis_analizi
""")
for satir in cursor.fetchall():
    print(satir)


print("Fiyat grubuna gore siniflandirma:")
cursor.execute("""
SELECT
    urun_adi,
    kategori,
    birim_fiyat,
    CASE
        WHEN birim_fiyat >= 10000 THEN 'Yuksek fiyatli'
        WHEN birim_fiyat >= 1000 THEN 'Orta fiyatli'
        ELSE 'Dusuk fiyatli'
    END AS fiyat_grubu
FROM siparis_analizi
""")
for satir in cursor.fetchall():
    print(satir)


print("Ciro grubuna gore siniflandirma:")
cursor.execute("""
SELECT
    urun_adi,
    adet,
    birim_fiyat,
    adet * birim_fiyat AS ciro,
    CASE
        WHEN adet * birim_fiyat >= 20000 THEN 'Yuksek ciro'
        WHEN adet * birim_fiyat >= 5000 THEN 'Orta ciro'
        ELSE 'Dusuk ciro'
    END AS ciro_grubu
FROM siparis_analizi
ORDER BY ciro DESC
""")
for satir in cursor.fetchall():
    print(satir)


print("Musteri tipine gore satis segmenti:")
cursor.execute("""
SELECT
    urun_adi,
    musteri_tipi,
    adet * birim_fiyat AS ciro,
    CASE
        WHEN musteri_tipi = 'Kurumsal' AND adet * birim_fiyat >= 20000 THEN 'Onemli kurumsal satis'
        WHEN musteri_tipi = 'Kurumsal' THEN 'Standart kurumsal satis'
        WHEN musteri_tipi = 'Bireysel' AND adet * birim_fiyat >= 10000 THEN 'Yuksek bireysel satis'
        ELSE 'Standart bireysel satis'
    END AS satis_segmenti
FROM siparis_analizi
ORDER BY ciro DESC
""")
for satir in cursor.fetchall():
    print(satir)


print("Ciro grubuna gore ozet:")
cursor.execute("""
SELECT
    CASE
        WHEN adet * birim_fiyat >= 20000 THEN 'Yuksek ciro'
        WHEN adet * birim_fiyat >= 5000 THEN 'Orta ciro'
        ELSE 'Dusuk ciro'
    END AS ciro_grubu,
    COUNT(*) AS siparis_sayisi,
    SUM(adet * birim_fiyat) AS toplam_ciro
FROM siparis_analizi
GROUP BY ciro_grubu
ORDER BY toplam_ciro DESC
""")
for satir in cursor.fetchall():
    print(satir)


conn.close()