import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("advanced_clean_products.csv")

print("Temiz urun tablosu:")
print(df)

if "stok_degeri" not in df.columns:
    df["stok_degeri"] = df["fiyat"] * df["stok"]


kategori_stok_degeri = df.groupby("kategori")["stok_degeri"].sum()
kategori_stok_degeri = kategori_stok_degeri.sort_values(ascending=False)

plt.figure(figsize=(8, 5))
kategori_stok_degeri.plot(kind="bar")
plt.title("Kategoriye Gore Toplam Stok Degeri")
plt.xlabel("Kategori")
plt.ylabel("Toplam Stok Degeri")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("kategori_stok_degeri_rapor.png")
plt.close()

print("\nkategori_stok_degeri_rapor.png olusturuldu.")


en_degerli_urunler = df.sort_values("stok_degeri", ascending=False).head(5)

plt.figure(figsize=(8, 5))
plt.bar(en_degerli_urunler["urun_adi"], en_degerli_urunler["stok_degeri"])
plt.title("En Degerli 5 Urun")
plt.xlabel("Urun Adi")
plt.ylabel("Stok Degeri")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("en_degerli_urunler_rapor.png")
plt.close()

print("en_degerli_urunler_rapor.png olusturuldu.")


kategori_urun_sayisi = df.groupby("kategori")["urun_adi"].count()
kategori_urun_sayisi = kategori_urun_sayisi.sort_values(ascending=False)

plt.figure(figsize=(8, 5))
kategori_urun_sayisi.plot(kind="bar")
plt.title("Kategoriye Gore Urun Sayisi")
plt.xlabel("Kategori")
plt.ylabel("Urun Sayisi")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("kategori_urun_sayisi_rapor.png")
plt.close()

print("kategori_urun_sayisi_rapor.png olusturuldu.")


print("Tum grafik raporlari basariyla olusturuldu.")