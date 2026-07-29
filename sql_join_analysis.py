import sqlite3

conn = sqlite3.connect("sales_intro.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS siparisler")
cursor.execute("DROP TABLE IF EXISTS musteriler")

cursor.execute("""
CREATE TABLE musteriler (
    musteri_id INTEGER PRIMARY KEY,
    musteri_adi TEXT,
    sehir TEXT,
    musteri_tipi TEXt
)
""")

cursor.execute("""
CREATE TABLE siparisler (
    siparis_id INTEGER PRIMARY KEY,
    musteri_id INTEGER,
    urun_adi TEXT,
    kategori TEXT,
    adet INTEGER,
    birim_fiyat REAL
)
""")

musteriler = [
    (1, "Ahmet Yilmaz", "Adana", "Bireysel"),
    (2, "Zeynep Kaya", "Mersin", "Bireysel"),
    (3, "ABC Ltd.", "Istanbul", "Kurumsal"),
    (4, "Nova A.S.", "Ankara", "Kurumsal"),
    (5, "Deniz Demir", "Adana", "Bireysel")
]

siparisler = [
    (1, 1, "Laptop", "Elektronik", 1, 25000),
    (2, 1, "Mouse", "Elektronik", 2, 500),
    (3, 2, "Klavye", "Elektronik", 1, 1200),
    (4, 3, "Monitor", "Elektronik", 4, 6000),
    (5, 3, "Sandalye", "Mobilya", 10, 1500),
    (6, 4, "Masa", "Mobilya", 3, 3500),
    (7, 4, "Defter", "Kirtasiye", 50, 50)
]

cursor.executemany("""
INSERT INTO musteriler (musteri_id, musteri_adi, sehir, musteri_tipi)
VALUES (?, ?, ?, ?)
""", musteriler)

cursor.executemany("""
INSERT INTO siparisler (siparis_id, musteri_id, urun_adi, kategori, adet, birim_fiyat)
VALUES (?, ?, ?, ?, ?, ?)
""", siparisler)

conn.commit()


print("Musteriler tablosu:")
cursor.execute("SELECT * FROM musteriler")
for satir in cursor.fetchall():
    print(satir)


print("Siparisler tablosu:")
cursor.execute("SELECT * FROM siparisler")
for satir in cursor.fetchall():
    print(satir)

print("INNER JOIN ile musteri ve siparis bilgileri:")
cursor.execute("""
SELECT 
    siparisler.siparis_id,
    musteriler.musteri_adi,
    musteriler.sehir,
    musteriler.musteri_tipi,
    siparisler.urun_adi,
    siparisler.kategori,
    siparisler.adet,
    siparisler.birim_fiyat
FROM siparisler
INNER JOIN musteriler
ON siparisler.musteri_id = musteriler.musteri_id
""")
join_sonuclari = cursor.fetchall()

for satir in join_sonuclari:
    print(satir)

print("Alias kullanarak JOIN:")
cursor.execute("""
SELECT 
    s.siparis_id,
    m.musteri_adi,
    m.sehir,
    s.urun_adi,
    s.adet,
    s.birim_fiyat
FROM siparisler AS s
INNER JOIN musteriler AS m
ON s.musteri_id = m.musteri_id
""")
alias_join_sonuclari = cursor.fetchall()

for satir in alias_join_sonuclari:
    print(satir)

print("Adana'daki musterilerin siparisleri:")
cursor.execute("""
SELECT 
    m.musteri_adi,
    m.sehir,
    s.urun_adi,
    s.adet,
    s.birim_fiyat
FROM siparisler AS s
INNER JOIN musteriler AS m
ON s.musteri_id = m.musteri_id
WHERE m.sehir = 'Adana'
""")
adana_siparisleri = cursor.fetchall()

for satir in adana_siparisleri:
    print(satir)

print("Musteri tipine gore toplam ciro:")
cursor.execute("""
SELECT 
    m.musteri_tipi,
    SUM(s.adet * s.birim_fiyat) AS toplam_ciro
FROM siparisler AS s
INNER JOIN musteriler AS m
ON s.musteri_id = m.musteri_id
GROUP BY m.musteri_tipi
ORDER BY toplam_ciro DESC
""")
musteri_tipi_ciro = cursor.fetchall()

for satir in musteri_tipi_ciro:
    print(satir)

print("Sehre gore toplam ciro:")
cursor.execute("""
SELECT 
    m.sehir,
    SUM(s.adet * s.birim_fiyat) AS toplam_ciro
FROM siparisler AS s
INNER JOIN musteriler AS m
ON s.musteri_id = m.musteri_id
GROUP BY m.sehir
ORDER BY toplam_ciro DESC
""")
sehir_ciro = cursor.fetchall()

for satir in sehir_ciro:
    print(satir)

print("LEFT JOIN ile tum musteriler ve varsa siparisleri:")
cursor.execute("""
SELECT 
    m.musteri_id,
    m.musteri_adi,
    m.sehir,
    s.urun_adi,
    s.adet
FROM musteriler AS m
LEFT JOIN siparisler AS s
ON m.musteri_id = s.musteri_id
""")
left_join_sonuclari = cursor.fetchall()

for satir in left_join_sonuclari:
    print(satir)

print("Hic siparisi olmayan musteriler:")
cursor.execute("""
SELECT 
    m.musteri_id,
    m.musteri_adi,
    m.sehir
FROM musteriler AS m
LEFT JOIN siparisler AS s
ON m.musteri_id = s.musteri_id
WHERE s.siparis_id IS NULL
""")
siparissiz_musteriler = cursor.fetchall()

for satir in siparissiz_musteriler:
    print(satir)


conn.close()