import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales_data.csv")

df["tarih"] = pd.to_datetime(df["tarih"])
df["ciro"] = df["satis_adedi"] * df["birim_fiyat"]
df["ay"] = df["tarih"].dt.to_period("M")

print("Satis verisi:")
print(df)

kategori_sehir_pivot = pd.pivot_table(
    df,
    values="ciro",
    index="kategori",
    columns="sehir",
    aggfunc="sum",
    fill_value=0
)

print("Kategori ve sehre gore ciro pivot tablosu:")
print(kategori_sehir_pivot)

kategori_sehir_pivot.to_csv("sales_category_city_pivot.csv")

aylik_kategori_pivot = pd.pivot_table(
    df,
    values="ciro",
    index="ay",
    columns="kategori",
    aggfunc="sum",
    fill_value=0
)

print("Aylik kategori ciro pivot tablosu:")
print(aylik_kategori_pivot)

aylik_kategori_pivot.to_csv("sales_mothly_category_pivot.csv")

musteri_kategori_pivot = pd.pivot_table(
    df,
    values="satis_adedi",
    index="musteri_tipi",
    columns="kategori",
    aggfunc="sum",
    fill_value=0
)

print("Musteri tipi ve kategoriye gore satis adedi pivot tablosu:")
print(musteri_kategori_pivot)

musteri_kategori_pivot.to_csv("sales_customer_category_pivot.csv")

kategori_sehir_pivot.plot(kind="bar", figsize=(9, 5))
plt.title("Kategori ve Şehre Göre Ciro")
plt.xlabel("Kategori")
plt.ylabel("Toplam Ciro")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("sales_category_city_pivot_chart.png")
plt.close()

aylik_kategori_pivot.plot(kind="line", marker="o", figsize=(9, 5))
plt.title("Aylik Kategori Ciro Trendi")
plt.xlabel("Ay")
plt.ylabel("Toplam Ciro")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("sales_monthly_category_pivot_chart.png")
plt.close()


musteri_kategori_pivot.plot(kind="bar", figsize=(9, 5))
plt.title("Musteri Tipi ve Kategoriye Gore Satis Adedi")
plt.xlabel("Musteri Tipi")
plt.ylabel("Toplam Satis Adedi")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("sales_customer_category_pivot_chart.png")
plt.close()


print("\nPivot raporlari olusturuldu:")
print("sales_category_city_pivot.csv")
print("sales_monthly_category_pivot.csv")
print("sales_customer_category_pivot.csv")
print("sales_category_city_pivot_chart.png")
print("sales_monthly_category_pivot_chart.png")
print("sales_customer_category_pivot_chart.png")