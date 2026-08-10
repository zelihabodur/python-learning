import sqlite3

conn = sqlite3.connect("sales_intro.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS window_satislar")

cursor.execute("""
CREATE TABLE window_satislar (
    satis_id INTEGER PRIMARY KEY,
    ay TEXT,
    sehir TEXT,
    kategori TEXT,
    urun_adi TEXT,
    musteri_tipi TEXT,
    adet INTEGER,
    birim_fiyat REAL
)
""")

satislar = [
    (1, "2026-01", "Adana", "Elektronik", "Laptop", "Bireysel", 1, 25000),
    (2, "2026-01", "Adana", "Elektronik", "Mouse", "Bireysel", 2, 500),
    (3, "2026-01", "Mersin", "Elektronik", "Klavye", "Bireysel", 1, 1200),
    (4, "2026-02", "Istanbul", "Elektronik", "Monitor", "Kurumsal", 4, 6000),
    (5, "2026-02", "Istanbul", "Mobilya", "Sandalye", "Kurumsal", 10, 1500),
    (6, "2026-02", "Ankara", "Mobilya", "Masa", "Kurumsal", 3, 3500),
    (7, "2026-03", "Ankara", "Kirtasiye", "Defter", "Bireysel", 50, 50),
    (8, "2026-03", "Adana", "Kirtasiye", "Kalem", "Bireysel", 100, 10),
    (9, "2026-03", "Mersin", "Elektronik", "Kulaklik", "Bireysel", 8, 900),
    (10, "2026-04", "Istanbul", "Elektronik", "Telefon", "Kurumsal", 2, 18000),
    (11, "2026-04", "Mersin", "Mobilya", "Koltuk", "Kurumsal", 2, 12000),
    (12, "2026-04", "Adana", "Kirtasiye", "Dosya", "Bireysel", 40, 25)
]

cursor.executemany("""
INSERT INTO window_satislar (
    satis_id,
    ay,
    sehir,
    kategori,
    urun_adi,
    musteri_tipi,
    adet,
    birim_fiyat
)
VALUES (?, ?, ?, ?, ?, ?, ?, ?)
""", satislar)

conn.commit()


print("Tum satislar:")
cursor.execute("""
SELECT 
    satis_id,
    ay,
    sehir,
    kategori,
    urun_adi,
    musteri_tipi,
    adet,
    birim_fiyat,
    adet * birim_fiyat AS ciro
FROM window_satislar
""")
for satir in cursor.fetchall():
    print(satir)


print("Genel ciro siralamasi:")
cursor.execute("""
SELECT
    urun_adi,
    kategori,
    sehir,
    adet * birim_fiyat AS ciro,
    ROW_NUMBER() OVER (
        ORDER BY adet * birim_fiyat DESC
    ) AS genel_sira
FROM window_satislar
ORDER BY genel_sira
""")
for satir in cursor.fetchall():
    print(satir)


print("Kategori icinde ciro siralamasi:")
cursor.execute("""
SELECT
    urun_adi,
    kategori,
    sehir,
    adet * birim_fiyat AS ciro,
    RANK() OVER (
        PARTITION BY kategori
        ORDER BY adet * birim_fiyat DESC
    ) AS kategori_sirasi
FROM window_satislar
ORDER BY kategori, kategori_sirasi
""")
for satir in cursor.fetchall():
    print(satir)


print("Her satisin toplam ciro icindeki payi:")
cursor.execute("""
SELECT
    urun_adi,
    kategori,
    adet * birim_fiyat AS ciro,
    SUM(adet * birim_fiyat) OVER () AS toplam_ciro,
    ROUND(
        100.0 * (adet * birim_fiyat) / SUM(adet * birim_fiyat) OVER (),
        2
    ) AS ciro_payi_yuzde
FROM window_satislar
ORDER BY ciro DESC
""")
for satir in cursor.fetchall():
    print(satir)


print("Kategori toplam cirosu ve satisin kategori icindeki payi:")
cursor.execute("""
SELECT
    urun_adi,
    kategori,
    adet * birim_fiyat AS ciro,
    SUM(adet * birim_fiyat) OVER (
        PARTITION BY kategori
    ) AS kategori_toplam_ciro,
    ROUND(
        100.0 * (adet * birim_fiyat) / SUM(adet * birim_fiyat) OVER (
            PARTITION BY kategori
        ),
        2
    ) AS kategori_ici_pay_yuzde
FROM window_satislar
ORDER BY kategori, ciro DESC
""")
for satir in cursor.fetchall():
    print(satir)


print("Aylik ciro ve kümülatif ciro:")
cursor.execute("""
SELECT
    ay,
    aylik_ciro,
    SUM(aylik_ciro) OVER (
        ORDER BY ay
    ) AS kumulatif_ciro
FROM (
    SELECT
        ay,
        SUM(adet * birim_fiyat) AS aylik_ciro
    FROM window_satislar
    GROUP BY ay
) AS aylik_ozet
ORDER BY ay
""")
for satir in cursor.fetchall():
    print(satir)


print("Sehir bazli ciro siralamasi:")
cursor.execute("""
SELECT
    sehir,
    toplam_ciro,
    RANK() OVER (
        ORDER BY toplam_ciro DESC
    ) AS sehir_sirasi
FROM (
    SELECT
        sehir,
        SUM(adet * birim_fiyat) AS toplam_ciro
    FROM window_satislar
    GROUP BY sehir
) AS sehir_ozeti
ORDER BY sehir_sirasi
""")
for satir in cursor.fetchall():
    print(satir)


conn.close()