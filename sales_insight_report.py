import pandas as pd

df = pd.read_csv("sales_data.csv")

df["tarih"] = pd.to_datetime(df["tarih"])
df["ciro"] = df["satis_adedi"] * df["birim_fiyat"]
df["ay"] = df["tarih"].dt.to_period("M")

toplam_ciro = df["ciro"].sum()
toplam_satis_adedi = df["satis_adedi"].sum()
ortalama_siparis_cirosu = df["ciro"].mean()

kategori_ciro = df.groupby("kategori")["ciro"].sum()
en_yuksek_kategori = kategori_ciro.idxmax()
en_yuksek_kategori_ciro = kategori_ciro.max()

sehir_ciro = df.groupby("sehir")["ciro"].sum()
en_yuksek_sehir = sehir_ciro.idxmax()
en_yuksek_sehir_ciro = sehir_ciro.max()

aylik_ciro = df.groupby("ay")["ciro"].sum()
en_yuksek_ay = aylik_ciro.idxmax()
en_yuksek_ay_ciro = aylik_ciro.max()

urun_ciro = df.groupby("urun_adi")["ciro"].sum()
en_yuksek_urun = urun_ciro.idxmax()
en_yuksek_urun_ciro = urun_ciro.max()

urun_satis_adedi = df.groupby("urun_adi")["satis_adedi"].sum()
en_cok_satan_urun = urun_satis_adedi.idxmax()
en_cok_satan_urun_adedi = urun_satis_adedi.max()

rapor = f"""
SATIŞ ANALİZİ METİN RAPORU

GENEL ÖZET
Toplam ciro: {toplam_ciro} TL
Toplam satis adedi: {toplam_satis_adedi}
Ortalama siparis cirosu: {round(ortalama_siparis_cirosu, 2)} TL

KATEGORI ANALIZI
En yuksek ciro getiren kategori: {en_yuksek_kategori}
Bu kategorinin toplam cirosu: {en_yuksek_kategori_ciro} TL

SEHIR ANALIZI
En yuksek ciro getiren sehirler: {en_yuksek_sehir}
Bu sehrin toplam cirosu: {en_yuksek_sehir_ciro} TL

AYLIK ANALIZ
En yuksek ciro yapilan ay: {en_yuksek_ay}
Bu ayin toplam cirosu: {en_yuksek_ay_ciro} TL

URUN ANALIZI
En yuksek ciro getiren urun: {en_yuksek_urun}
Bu urunun toplam cirosu: {en_yuksek_urun_ciro} TL

En cok satan urun: {en_cok_satan_urun}
Bu urunun toplam satis adedi: {en_cok_satan_urun_adedi}

GENEL YORUM
Bu satis verisine gore en guclu performans {en_yuksek_kategori} kategorisinde gorulmektedir.
Ciro acisindan en onemli sehir {en_yuksek_sehir} olarak one cikmaktadir.
Aylik performansta en yuksek ciro {en_yuksek_ay} doneminde elde edilmistir.
Urun bazinda {en_yuksek_urun}, toplam ciroya en fazla katkida bulunan urundur.
"""
print(rapor)

with open("sales_insight_report.txt", "w", encoding="utf-8") as dosya:
    dosya.write(rapor)

print("sales_insight_report.txt dosyasi olusturuldu.")