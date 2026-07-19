import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("advanced_clean_products.csv")

print("Temiz urun tablosu:")
print(df)

kategori_stok_degeri = df.groupby("kategori")["stok_degeri"].sum()

print("Kategoriye gore toplam stok degeri:")
print(kategori_stok_degeri)

plt.figure(figsize=(8, 5))

kategori_stok_degeri.plot(kind="bar")

plt.title("Kategoriye Gore Toplam Stok Degeri")
plt.xlabel("Kategori")
plt.ylabel("Toplam Stok Degeri")

plt.tight_layout()

plt.savefig("kategori_stok_degeri.png")

plt.show()

print("Grafik kategori_stok_degeri.png dosyasina kaydedildi.")

