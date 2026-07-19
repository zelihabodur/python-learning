import pandas as pd

df = pd.read_csv("dirty_products.csv")

print("Kirli Veri Tablosu:")
print(df)

print("Eksik veri sayilari:")
print(df.isna().sum())

print("Eksik kategori olan sayilar:")
eksik_kategori = df[df["kategori"].isna()]
print(eksik_kategori)

print("Eksik fiyat olan satirlar:")
eksik_fiyat = df[df["fiyat"].isna()]
print(eksik_fiyat)

print("Eksik stok olan satirlar:")
eksik_stok = df[df["stok"].isna()]
print(eksik_stok)

df["kategori"] = df["kategori"].fillna("Bilinmiyor")
df["fiyat"] = df["fiyat"].fillna(0)
df["stok"] = df["stok"].fillna(0)

print("Temizlenmis Tablo:")
print(df)

print("Temizlik sonrasi eksik veri sayilari:")
print(df.isna().sum())

df["stok_degeri"] = df["fiyat"] * df["stok"]

print("Stok Degeri eklenmis temiz tablo:")
print(df)

df.to_csv("clean_products.csv", index=False)

print("Temizlenmis veri clean_products.csv dosyasina kaydedildi.")