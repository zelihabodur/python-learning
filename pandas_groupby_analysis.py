import pandas as pd

df = pd.read_csv("stock_products.csv")

print("Stok Tablosu:")
print(df)

df["stok_degeri"] = df["fiyat"] * df["stok"]

print("Stok Degeri Eklenmis Tablo:")
print(df)

print("Kategoriye Urun Sayisi:")
kategori_urun_sayisi = df.groupby("kategori")["urun_adi"].count()
print(kategori_urun_sayisi)

print("Kategoriye Gore Toplam Stok:")
kategori_toplam_stok = df.groupby("kategori")["stok"].sum()
print(kategori_toplam_stok)

print("Kategoriye Gore Toplam Stok Degeri:")
kategori_toplam_stok_degeri = df.groupby("kategori")["stok_degeri"].sum()
print(kategori_toplam_stok_degeri)

print("Kategoriye Gore Ortalama Fiyat:")
kategori_ortalama_fiyat = df.groupby("kategori")["fiyat"].mean()
print(kategori_ortalama_fiyat)

print("Kategoriye Gore En Yuksek Fiyat:")
kategori_en_yuksek_fiyat = df.groupby("kategori")["fiyat"].max()
print(kategori_en_yuksek_fiyat)