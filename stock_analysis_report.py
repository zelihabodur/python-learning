import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales_data.csv")

print("Ham satis verisi:")
print(df)

print("Tablo bilgisi:")
df.info()

print("Eksik veri sayilari:")
print(df.isna().sum())

df["tarih"] = pd.to_datetime(df["tarih"])

df["ciro"] = df["satis_adedi"] * df["birim_fiyat"]

df["ay"] = df["tarih"].dt.to_period("M")

print("Ciro ve ay sutunlari eklenmis tablo:")
print(df)

df.to_csv("sales_clean_report.csv", index=False)


kategori_ozeti = df.groupby("kategori").agg({
    "satis_adedi": "sum",
    "ciro": "sum",
    "birim_fiyat": "mean"
})

kategori_ozeti = kategori_ozeti.rename(columns={
    "satis_adedi": "toplam_satis_adedi",
    "ciro": "toplam_ciro",
    "birim_fiyat": "ortalama_birim_fiyat"
})

kategori_ozeti.to_csv("sales_category_summary.csv")

print("\nKategori ozeti:")
print(kategori_ozeti)


sehir_ozeti = df.groupby("sehir").agg({
    "satis_adedi": "sum",
    "ciro": "sum"
})

sehir_ozeti = sehir_ozeti.rename(columns={
    "satis_adedi": "toplam_satis_adedi",
    "ciro": "toplam_ciro"
})

sehir_ozeti = sehir_ozeti.sort_values("toplam_ciro", ascending=False)

sehir_ozeti.to_csv("sales_city_summary.csv")

print("Sehir ozeti:")
print(sehir_ozeti)


aylik_ciro = df.groupby("ay")["ciro"].sum()
aylik_ciro.to_csv("sales_monthly_revenue.csv")

print("Aylik ciro:")
print(aylik_ciro)


en_cok_satan_urunler = df.groupby("urun_adi").agg({
    "satis_adedi": "sum",
    "ciro": "sum"
})

en_cok_satan_urunler = en_cok_satan_urunler.rename(columns={
    "satis_adedi": "toplam_satis_adedi",
    "ciro": "toplam_ciro"
})

en_cok_satan_urunler = en_cok_satan_urunler.sort_values("toplam_satis_adedi", ascending=False)

en_cok_satan_urunler.to_csv("sales_top_products.csv")

print("En cok satan urunler:")
print(en_cok_satan_urunler)


kategori_ciro = df.groupby("kategori")["ciro"].sum()
kategori_ciro = kategori_ciro.sort_values(ascending=False)

plt.figure(figsize=(8, 5))
kategori_ciro.plot(kind="bar")
plt.title("Kategoriye Gore Toplam Ciro")
plt.xlabel("Kategori")
plt.ylabel("Toplam Ciro")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("sales_category_revenue_chart.png")
plt.close()


sehir_ciro = df.groupby("sehir")["ciro"].sum()
sehir_ciro = sehir_ciro.sort_values(ascending=False)

plt.figure(figsize=(8, 5))
sehir_ciro.plot(kind="bar")
plt.title("Sehre Gore Toplam Ciro")
plt.xlabel("Sehir")
plt.ylabel("Toplam Ciro")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("sales_city_revenue_chart.png")
plt.close()


aylik_ciro = aylik_ciro.sort_index()

plt.figure(figsize=(8, 5))
aylik_ciro.plot(kind="box", marker="o")
plt.title("Aylik Ciro Trendi")
plt.xlabel("Ay")
plt.ylabel("Toplam Ciro")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("sales_monthly_revenue_chart.png")
plt.close()


top_urunler_ciro = en_cok_satan_urunler.sort_values("toplam_ciro", ascending=False).head(5)

plt.figure(figsize=(8, 5))
plt.bar(top_urunler_ciro.index, top_urunler_ciro["toplam_ciro"])
plt.title("Ciroya Gore En Degerli 5 Urun")
plt.xlabel("Urun")
plt.ylabel("Toplam Ciro")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("sales_top_products_revenue_chart.png")
plt.close()


print("Rapor dosyalari olusturuldu:")
print("sales_clean_report.csv")
print("sales_category_summary.csv")
print("sales_city_summary.csv")
print("sales_monthly_revenue.csv")
print("sales_top_products.csv")
print("sales_category_revenue_chart.png")
print("sales_city_revenue_chart.png")
print("sales_monthly_revenue_chart.png")
print("sales_top_products_revenue_chart.png")