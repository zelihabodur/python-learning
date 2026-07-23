import sqlite3

conn = sqlite3.connect("sales_intro.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS satislar")

cursor.execute("""
CREATE TABLE satislar (
    satis_id INTEGER PRIMARY KEY,
    sehir TEXT,
    kategori TEXT,
    urun_adi TEXT,
    musteri_tipi TEXT,
    satis_adedi INTEGER,
    birim_fiyat REAL
    )
""")

satislar = [
    (1, "Adana", "Elektronik", "Laptop", "Bireysel", 2, 25000),
    (2, "Mersin", "Elektronik", "Mouse", "Bireysel", 10, 500),
    (3, "Adana", "Elektronik", "Klavye", "Kurumsal", 6, 1200),
    (4, "İstanbul", "Kirtasiye", "Defter", "Bireysel", 50, 50),
    (5, "Ankara", "Kirtasiye", "Kalem", "Bireysel", 100, 10),
    (6, "Adana", "Mobilya", "Sandalye", "Kurumsal", 5, 1500),
    (7, "İstanbul", "Elektronik", "Monitor", "Kurumsal", 4, 6000),
    (8, "Mersin", "Elektronik", "Kulaklik", "Bireysel", 8, 900),
    (9, "Ankara", "Mobilya", "Masa", "Kurumsal", 3, 3500),
    (10, "Adana", "Kirtasiye", "Dosya", "Bireysel", 40, 25)
]

cursor.executemany("""
INSERT INTO satislar (
    satis_id,
    sehir,
    kategori,
    urun_adi,
    musteri_tipi,
    satis_adedi,
    birim_fiyat
)
VALUES (?, ?, ?, ?, ?, ?, ?)
 """, satislar)

conn.commit()

print("Tum Satislar:")
cursor.execute("SELECT * FROM satislar")
tum_satislar = cursor.fetchall()

for satis in tum_satislar:
    print(satis)

print("Toplam satis kaydi sayisi:")
cursor.execute("SELECT COUNT(*) FROM satislar")
toplam_kayit = cursor.fetchone()
print(toplam_kayit[0])

print("Toplam satis adedi:")
cursor.execute("SELECT SUM(satis_adedi) FROM satislar")
toplam_satis_adedi = cursor.fetchone()
print(toplam_satis_adedi[0])

print("Ortalama birim fiyat:")
cursor.execute("SELECT AVG(birim_fiyat) FROM satislar")
ortalama_fiyat = cursor.fetchone()
print(round(ortalama_fiyat[0], 2))

print("En yuksek birim fiyat:")
cursor.execute("SELECT MAX(birim_fiyat) FROM satislar")
en_yuksek_fiyat = cursor.fetchone()
print(en_yuksek_fiyat[0])

print("En dusuk fiyat:")
cursor.execute("SELECT MIN(birim_fiyat) FROM satislar")
en_dusuk_fiyat = cursor.fetchone()
print(en_dusuk_fiyat[0])

print("Kategoriye gore toplam satis adedi:")
cursor.execute("""
SELECT kategori, SUM(satis_adedi)
FROM satislar
GROUP BY kategori
""")
kategori_satislari = cursor.fetchall()

for satir in kategori_satislari:
    print(satir)

print("Sehre gore toplam satis adedi:")
cursor.execute("""
SELECT sehir, SUM(satis_adedi)
FROM satislar
GROUP BY sehir
""")
sehir_satislari = cursor.fetchall()

for satir in sehir_satislari:
    print(satir)

print("Kategoriye gore toplam ciro:")
cursor.execute("""
SELECT
    kategori,
    SUM(satis_adedi * birim_fiyat) AS toplam_ciro
FROM satislar
GROUP BY kategori
ORDER BY toplam_ciro DESC
""")
kategori_ciro = cursor.fetchall()
for satir in kategori_ciro:
    print(satir)

print("Musteri tipine gore toplam ciro:")
cursor.execute("""
SELECT 
    musteri_tipi,
    SUM(satis_adedi * birim_fiyat) AS toplam_ciro
FROM satislar
GROUP BY musteri_tipi
ORDER BY toplam_ciro DESC
""")
musteri_tipi_ciro = cursor.fetchall()

for satir in musteri_tipi_ciro:
    print(satir)


print("Toplam cirosu 10000 TL'den yuksek kategoriler:")
cursor.execute("""
SELECT 
    kategori,
    SUM(satis_adedi * birim_fiyat) AS toplam_ciro
FROM satislar
GROUP BY kategori
HAVING toplam_ciro > 10000
ORDER BY toplam_ciro DESC
""")
yuksek_ciro_kategoriler = cursor.fetchall()

for satir in yuksek_ciro_kategoriler:
    print(satir)


conn.close()