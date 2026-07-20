import pandas as pd

df = pd.read_csv("sales_data.csv")

df["tarih"] = pd.to_datetime(df["tarih"])
df["ciro"] = df["satis_adedi"] * df["birim_fiyat"]
df["ay"] = df["tarih"].dt.to_period("M").astype(str)

print("Satis verisi:")
print(df)


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


sehir_ozeti = df.groupby("sehir").agg({
    "satis_adedi": "sum",
    "ciro": "sum"
})

sehir_ozeti = sehir_ozeti.rename(columns={
    "satis_adedi": "toplam_satis_adedi",
    "ciro": "toplam_ciro"
})

sehir_ozeti = sehir_ozeti.sort_values("toplam_ciro", ascending=False)


aylik_ciro = df.groupby("ay")["ciro"].sum()
aylik_ciro = aylik_ciro.reset_index()
aylik_ciro = aylik_ciro.rename(columns={
    "ciro": "toplam_ciro"
})


urun_ozeti = df.groupby("urun_adi").agg({
    "satis_adedi": "sum",
    "ciro": "sum"
})

urun_ozeti = urun_ozeti.rename(columns={
    "satis_adedi": "toplam_satis_adedi",
    "ciro": "toplam_ciro"
})

urun_ozeti = urun_ozeti.sort_values("toplam_ciro", ascending=False)


with pd.ExcelWriter("sales_excel_report.xlsx", engine="openpyxl") as writer:
    df.to_excel(writer, sheet_name="Temiz Satis Verisi", index=False)
    kategori_ozeti.to_excel(writer, sheet_name="Kategori Ozeti")
    sehir_ozeti.to_excel(writer, sheet_name="Sehir Ozeti")
    aylik_ciro.to_excel(writer, sheet_name="Aylik Ciro", index=False)
    urun_ozeti.to_excel(writer, sheet_name="Urun Ozeti")


print("sales_excel_report.xlsx dosyasi olusturuldu.")


excel_df = pd.read_excel("sales_excel_report.xlsx", sheet_name="Temiz Satis Verisi")

print("Excel dosyasindan okunan veri:")
print(excel_df.head())

print("Excel dosyasi basariyla okundu.")