import pandas as pd

df = pd.read_csv("stock_products.csv")

print("Stok Urunleri Tablosu")
print(df)

print("Ilk 5 satir:")
print(df.head())

print("Tablo Bilgisi:")
df.info()

print("Sayisal Ozet:")
print(df.describe())

print("Sadece urun adi ve stok:")
print(df[["urun_adi", "stok"]])

kritik_stok = df[df["stok"] <= 5]

print("Kritik Stoktaki Urunler:")
print(kritik_stok)

df["stok_degeri"] = df["fiyat"] * df["stok"]

print("Stok Degeri Eklenmis Tablo:")
print(df)

toplam_stok = df["stok"].sum()
toplam_stok_degeri = df["stok_degeri"].sum()
ortalama_fiyat = df["fiyat"].mean()
en_yuksek_fiyat = df["fiyat"].max()
en_dusuk_fiyat = df["fiyat"].min()

print("Genel Stok Analizi:")
print("Toplam Stok Adedi", toplam_stok)
print("Toplam Stok Degeri", toplam_stok_degeri)
print("Ortalama Fiyat", ortalama_fiyat)
print("En Yuksek Fiyat", en_yuksek_fiyat)
print("En Dusuk Fiyat", en_dusuk_fiyat)
