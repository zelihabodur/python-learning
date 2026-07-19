import pandas as pd

df = pd.read_csv("messy_products.csv")

print("Kirli tablo:")
print(df)

print("Ilk tablo bilgisi:")
df.info()


print("Tekrar eden satir sayisi:")
print(df.duplicated().sum())


print("Tekrar eden satirlar:")
tekrar_edenler = df[df.duplicated()]
print(tekrar_edenler)


df["fiyat"] = pd.to_numeric(df["fiyat"], errors="coerce")
df["stok"] = pd.to_numeric(df["stok"], errors="coerce")

print("Sayiya cevirme sonrasi tablo:")
print(df)

print("Sayiya cevirme sonrasi eksik veri sayilari:")
print(df.isna().sum())


df["fiyat"] = df["fiyat"].fillna(0)
df["stok"] = df["stok"].fillna(0)

df = df.drop_duplicates()

df["stok_degeri"] = df["fiyat"] * df["stok"]

print("Temizlenmis tablo:")
print(df)

print("Temizlenmis tablo bilgisi:")
df.info()

df.to_csv("advanced_clean_products.csv", index=False)

print("Temizlenmis veri advanced_clean_products.csv dosyasina kaydedildi.")