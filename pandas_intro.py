import pandas as pd

veriler = {
    "urun_adi": ["Laptop", "Mouse", "Klavye"],
    "fiyat": [25000, 500, 1200],
    "stok": [5, 20, 10]
}

df = pd.DataFrame(veriler)

print(df)

print("Ilk 5 satir:")
print(df.head())

print("Tablo Bilgisi")
df.info()

print("Sayisal Ozet:")
print(df.describe())

print("Sadece urun adlari:")
print(df["urun_adi"])

print("Urun adi ve stok:")
print(df[["urun_adi", "stok"]])

kritik_stok = df[df["stok"] <= 5]

print("Kritik Stoktaki Urunler:")
print(kritik_stok)

df["stok_degeri"] = df["fiyat"] * df["stok"]

print("Stok degeri eklnemis tablo:")
print(df)

toplam_stok_degeri = df["stok_degeri"].sum()
print("Toplam stok degeri:", toplam_stok_degeri)