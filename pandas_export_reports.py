import pandas as pd
df = pd.read_csv("stock_products.csv")

df["stok_degeri"] = df["fiyat"] * df["stok"]

print("Ana Stok Tablosu:")
print(df)

kritik_stok = df[df["stok"] <= 5]

kritik_stok.to_csv("kritik_stok_urunleri.csv", index=False)
print("Kritik stok urunleri csv dosyasina kaydedildi.")

en_pahali_urunler = df.sort_values("fiyat", ascending=False).head(3)

en_pahali_urunler.to_csv("en_pahali_urunler.csv", index=False)

print("En pahali 3 urun csv dosyasina kaydedildi.")

kategori_ozeti = df.groupby("kategori").agg({
    "urun_adi": "count",
    "stok": "sum",
    "stok_degeri": "sum",
    "fiyat": "mean"
})

kategori_ozeti = kategori_ozeti.rename(columns={
    "urun_adi": "urun_sayisi",
    "stok": "toplam_stok",
    "stok_degeri": "toplam_stok_degeri",
    "fiyat": "ortalama_fiyat"
})

kategori_ozeti.to_csv("kategori_ozeti.csv")

print("Kategori Ozeti csv dosyasina kaydedildi.")

print("Kategori Ozeti:")
print(kategori_ozeti)