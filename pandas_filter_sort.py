import pandas as pd

df = pd.read_csv("stock_products.csv")

print("Stok Tablosu:")
print(df)

df["stok_degeri"] = df["fiyat"] * df["stok"]

print("Stok Degeri Eklenmis Tablo:")
print(df)

print("Sadece elektronik kategorisindeki urunler:")
elektronik_urunler = df[df["kategori"] == "Elektronik"]
print(elektronik_urunler)

print("Stogu 10'dan az olan urunler:")
az_stok = df[df["stok"] < 10]
print(az_stok)

print("Fiyati 1000 TL'den yuksek urunler:")
pahali_urunler = df[df["fiyat"] > 1000]
print(pahali_urunler)

print("Stok degeri 1000 TL'den yuksek urunler:")
yuksek_stok_degeri = df[df["stok_degeri"] > 1000]
print(yuksek_stok_degeri)

print("Fiyata gore artan siralama:")
fiyata_gore_artan = df.sort_values("fiyat")
print(fiyata_gore_artan)

print("Fiyata gore azalan siralama:")
fiyata_gore_azalan = df.sort_values("fiyat", ascending=False)
print(fiyata_gore_azalan)

print("Stoga gore azalan siralama:")
stoga_gore_azalan = df.sort_values("stok", ascending=False)
print(stoga_gore_azalan)

print("Stok Degerine gore azalan siralama:")
stok_degerine_gore_azalan = df.sort_values("stok_degeri", ascending=False)
print(stok_degerine_gore_azalan)

print("En Pahali 3 Urun:")
en_pahali_3 = df.sort_values("fiyat", ascending=False).head(3)
print(en_pahali_3)

print("Stogu en az olan 3 urun:")
stogu_en_az_3 = df.sort_values("stok", ascending=False).head(3)
print(stogu_en_az_3)
