import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("messy_products.csv")

print("Ham veri:")
print(df)

print("Ham veri bilgisi:")
df.info()

print("Eksik veri sayilari:")
print(df.isna().sum())

print("Tekrar eden satir sayisi:")
print(df.duplicated().sum())

df["fiyat"] = pd.to_numeric(df["fiyat"], errors="coerce")
df["stok"] = pd.to_numeric(df["stok"], errors="coerce")

print("Sayiya cevirme sonrasi veri:")
print(df)

print("Sayiya cevirme sonrasi eksik veri sayilari:")
print(df.isna().sum())

df["kategori"] = df["kategori"].fillna("Bilinmiyor")
df["fiyat"] = df["fiyat"].fillna(0)
df["stok"] = df["stok"].fillna(0)

df = df.drop_duplicates()

df["stok_degeri"] = df["fiyat"] * df["stok"]

print("Temizlenmis veri:")
print(df)

df.to_csv("stock_clean_report.csv", index=False)

kategori_ozeti = df.groupby("kategori").agg({
    "urun_adi": "count",
    "stok": "sum",
    "stok_degeri": "sum",
    "fiyat": "mean"
})

kategori_ozeti = kategori_ozeti.rename(columns={
    "urun_adi": "urun_sayisi",
    "stok": "toplam_stok",
    "stok_degeri": "topam_stok_degeri",
    "fiyat": "ortalama_fiyat"
})

kategori_ozeti.to_csv("stock_category_summary_report.csv")

print("Kategori Ozeti:")
print(kategori_ozeti)

kritik_stok = df[df["stok"] <= 5]
kritik_stok.to_csv("stock_critical_items_report.csv", index=False)

print("Kritik Stok Urunleri:")
print(kritik_stok)

en_degerli_urunler = df.sort_values("stok_degeri", ascending=False).head(5)
en_degerli_urunler.to_csv("stock_top_value_items_report.csv", index=False)

print("En degerli 5 urun:")
print(en_degerli_urunler)

kategori_stok_degeri = df.groupby("kategori")["stok_degeri"].sum()
kategori_stok_degeri = kategori_stok_degeri.sort_values(ascending=False)

plt.figure(figsize=(8, 5))
kategori_stok_degeri.plot(kind="bar")
plt.title("Kategoriye Gore Toplam Stok Degeri")
plt.xlabel("Kategori")
plt.ylabel("Toplam Stok Degeri")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("stock_category_value_chart.png")
plt.close()


kategori_urun_sayisi = df.groupby("kategori")["urun_adi"].count()
kategori_urun_sayisi = kategori_urun_sayisi.sort_values(ascending=False)

plt.figure(figsize=(8, 5))
kategori_urun_sayisi.plot(kind="bar")
plt.title("Kategoriye Gore Urun Sayisi")
plt.xlabel("Kategori")
plt.ylabel("Urun Sayisi")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("stock_category_count_chart.png")
plt.close()


plt.figure(figsize=(8, 5))
plt.bar(en_degerli_urunler["urun_adi"], en_degerli_urunler["stok_degeri"])
plt.title("En Degerli 5 Urun")
plt.xlabel("Urun Adi")
plt.ylabel("Stok Degeri")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("stock_top_value_items_chart.png")
plt.close()


print("Rapor dosyalari olusturuldu:")
print("stock_clean_report.csv")
print("stock_category_summary_report.csv")
print("stock_critical_items_report.csv")
print("stock_top_value_items_report.csv")
print("stock_category_value_chart.png")
print("stock_category_count_chart.png")
print("stock_top_value_items_chart.png")