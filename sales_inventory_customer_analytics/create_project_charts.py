import os
import pandas as pd
import matplotlib.pyplot as plt

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
REPORTS_DIR = os.path.join(PROJECT_DIR, "reports")
CHARTS_DIR = os.path.join(PROJECT_DIR, "charts")

os.makedirs(CHARTS_DIR, exist_ok=True)

for file_name in os.listdir(CHARTS_DIR):
    if file_name.endswith(".png"):
        os.remove(os.path.join(CHARTS_DIR, file_name))


def save_chart(file_name):
    path = os.path.join(CHARTS_DIR, file_name)
    plt.tight_layout()
    plt.savefig(path, dpi=150)
    plt.close()


sehir_raporu = pd.read_csv(
    os.path.join(REPORTS_DIR, "sehir_ciro_raporu.csv"),
    encoding="utf-8-sig"
)

kategori_raporu = pd.read_csv(
    os.path.join(REPORTS_DIR, "kategori_performans_raporu.csv"),
    encoding="utf-8-sig"
)

musteri_tipi_raporu = pd.read_csv(
    os.path.join(REPORTS_DIR, "musteri_tipi_raporu.csv"),
    encoding="utf-8-sig"
)

aylik_rapor = pd.read_csv(
    os.path.join(REPORTS_DIR, "aylik_ciro_raporu.csv"),
    encoding="utf-8-sig"
)

kritik_stok_raporu = pd.read_csv(
    os.path.join(REPORTS_DIR, "kritik_stok_raporu.csv"),
    encoding="utf-8-sig"
)

en_iyi_urunler_raporu = pd.read_csv(
    os.path.join(REPORTS_DIR, "en_iyi_urunler_raporu.csv"),
    encoding="utf-8-sig"
)


print("Rapor dosyalari basariyla okundu.")


plt.figure(figsize=(10, 6))
plt.bar(sehir_raporu["Şehir"], sehir_raporu["Toplam Ciro"])
plt.title("Şehirlere Göre Toplam Ciro")
plt.xlabel("Şehir")
plt.ylabel("Toplam Ciro")
plt.xticks(rotation=30)
save_chart("sehir_ciro_grafigi.png")


plt.figure(figsize=(10, 6))
plt.bar(kategori_raporu["Kategori"], kategori_raporu["Toplam Ciro"])
plt.title("Kategorilere Göre Toplam Ciro")
plt.xlabel("Kategori")
plt.ylabel("Toplam Ciro")
save_chart("kategori_ciro_grafigi.png")


plt.figure(figsize=(10, 6))
plt.plot(aylik_rapor["Ay"], aylik_rapor["Aylık Ciro"], marker="o")
plt.title("Aylara Göre Ciro Trendi")
plt.xlabel("Ay")
plt.ylabel("Aylık Ciro")
plt.xticks(rotation=30)
save_chart("aylik_ciro_trendi.png")


plt.figure(figsize=(10, 6))
plt.plot(aylik_rapor["Ay"], aylik_rapor["Kümülatif Ciro"], marker="o")
plt.title("Aylara Göre Kümülatif Ciro")
plt.xlabel("Ay")
plt.ylabel("Kümülatif Ciro")
plt.xticks(rotation=30)
save_chart("kumulatif_ciro_grafigi.png")


plt.figure(figsize=(10, 6))
plt.bar(musteri_tipi_raporu["Müşteri Tipi"], musteri_tipi_raporu["Toplam Ciro"])
plt.title("Müşteri Tipine Göre Toplam Ciro")
plt.xlabel("Müşteri Tipi")
plt.ylabel("Toplam Ciro")
save_chart("musteri_tipi_ciro_grafigi.png")


en_iyi_5_urun = en_iyi_urunler_raporu.head(5)

plt.figure(figsize=(10, 6))
plt.bar(en_iyi_5_urun["Ürün Adı"], en_iyi_5_urun["Toplam Ciro"])
plt.title("Ciroya Göre En İyi 5 Ürün")
plt.xlabel("Ürün")
plt.ylabel("Toplam Ciro")
plt.xticks(rotation=30)
save_chart("en_iyi_5_urun_grafigi.png")


plt.figure(figsize=(10, 6))
plt.bar(kritik_stok_raporu["Ürün Adı"], kritik_stok_raporu["Mevcut Stok"])
plt.title("Kritik Stoktaki Ürünlerin Mevcut Stok Seviyesi")
plt.xlabel("Ürün")
plt.ylabel("Mevcut Stok")
plt.xticks(rotation=30)
save_chart("kritik_stok_grafigi.png")


print("\nGrafikler basariyla olusturuldu:")
print("- charts/sehir_ciro_grafigi.png")
print("- charts/kategori_ciro_grafigi.png")
print("- charts/aylik_ciro_trendi.png")
print("- charts/kumulatif_ciro_grafigi.png")
print("- charts/musteri_tipi_ciro_grafigi.png")
print("- charts/en_iyi_5_urun_grafigi.png")
print("- charts/kritik_stok_grafigi.png")