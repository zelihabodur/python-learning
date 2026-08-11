import os
import pandas as pd

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
REPORTS_DIR = os.path.join(PROJECT_DIR, "reports")

city_report = pd.read_csv(
    os.path.join(REPORTS_DIR, "sehir_ciro_raporu.csv"),
    encoding="utf-8-sig"
)

category_report = pd.read_csv(
    os.path.join(REPORTS_DIR, "kategori_performans_raporu.csv"),
    encoding="utf-8-sig"
)

customer_type_report = pd.read_csv(
    os.path.join(REPORTS_DIR, "musteri_tipi_raporu.csv"),
    encoding="utf-8-sig"
)

monthly_report = pd.read_csv(
    os.path.join(REPORTS_DIR, "aylik_ciro_raporu.csv"),
    encoding="utf-8-sig"
)

critical_stock_report = pd.read_csv(
    os.path.join(REPORTS_DIR, "kritik_stok_raporu.csv"),
    encoding="utf-8-sig"
)

top_products_report = pd.read_csv(
    os.path.join(REPORTS_DIR, "en_iyi_urunler_raporu.csv"),
    encoding="utf-8-sig"
)


def format_currency(value):
    return f"{value:,.0f} TL".replace(",", ".")


def format_number(value):
    return f"{value:,.0f}".replace(",", ".")


total_revenue = city_report["Toplam Ciro"].sum()
total_profit = city_report["Toplam Kâr"].sum()
total_quantity = city_report["Toplam Satış Adedi"].sum()
total_orders = city_report["Sipariş Sayısı"].sum()
profit_margin = round((total_profit / total_revenue) * 100, 2)

top_city = city_report.loc[city_report["Toplam Ciro"].idxmax()]
top_category = category_report.loc[category_report["Toplam Ciro"].idxmax()]
top_customer_type = customer_type_report.loc[customer_type_report["Toplam Ciro"].idxmax()]
top_month = monthly_report.loc[monthly_report["Aylık Ciro"].idxmax()]
top_product = top_products_report.loc[top_products_report["Toplam Ciro"].idxmax()]

critical_stock_count = len(critical_stock_report)
critical_stock_products = ", ".join(critical_stock_report["Ürün Adı"].tolist())

summary_text = f"""
SATIŞ, STOK VE MÜŞTERİ ANALİZİ YÖNETİCİ ÖZETİ

1. GENEL PERFORMANS

Toplam ciro: {format_currency(total_revenue)}
Toplam kâr: {format_currency(total_profit)}
Toplam satış adedi: {format_number(total_quantity)}
Toplam sipariş sayısı: {format_number(total_orders)}
Genel kâr marjı: %{profit_margin}

Bu sonuçlara göre işletme, analiz döneminde toplam {format_currency(total_revenue)} ciro ve {format_currency(total_profit)} kâr elde etmiştir.

2. ŞEHİR BAZLI PERFORMANS

En yüksek ciro getiren şehir: {top_city["Şehir"]}
Bu şehrin toplam cirosu: {format_currency(top_city["Toplam Ciro"])}
Bu şehrin toplam kârı: {format_currency(top_city["Toplam Kâr"])}

Yorum:
{top_city["Şehir"]}, satış performansı açısından en güçlü şehir olarak öne çıkmaktadır. Bu şehirdeki satış kanalları ve müşteri davranışları daha detaylı incelenerek diğer şehirler için örnek strateji geliştirilebilir.

3. KATEGORİ BAZLI PERFORMANS

En yüksek ciro getiren kategori: {top_category["Kategori"]}
Kategori toplam cirosu: {format_currency(top_category["Toplam Ciro"])}
Kategori toplam kârı: {format_currency(top_category["Toplam Kâr"])}
Ortalama kâr marjı: %{top_category["Ortalama Kâr Marjı (%)"]}

Yorum:
{top_category["Kategori"]} kategorisi ciro açısından en güçlü ürün grubudur. Bu kategoride stok sürekliliği, kampanya planlaması ve ürün çeşitliliği öncelikli olarak takip edilmelidir.

4. MÜŞTERİ TİPİ ANALİZİ

En yüksek ciro getiren müşteri tipi: {top_customer_type["Müşteri Tipi"]}
Bu müşteri tipinin toplam cirosu: {format_currency(top_customer_type["Toplam Ciro"])}
Bu müşteri tipinin toplam kârı: {format_currency(top_customer_type["Toplam Kâr"])}

Yorum:
{top_customer_type["Müşteri Tipi"]} müşteri grubu işletme gelirinde daha güçlü rol oynamaktadır. Satış stratejileri bu müşteri tipine göre ayrı kampanya, fiyatlandırma ve sadakat çalışmalarıyla desteklenebilir.

5. AYLIK SATIŞ TRENDİ

En yüksek ciro elde edilen ay: {top_month["Ay"]}
Bu ayın cirosu: {format_currency(top_month["Aylık Ciro"])}
Bu ayın kârı: {format_currency(top_month["Aylık Kâr"])}
Dönem sonu kümülatif ciro: {format_currency(monthly_report["Kümülatif Ciro"].iloc[-1])}

Yorum:
{top_month["Ay"]} dönemi satış performansının en güçlü olduğu ay olmuştur. Bu ayda yapılan satışların hangi şehir, kategori ve müşteri tipi üzerinden geldiği ayrıca incelenmelidir.

6. ÜRÜN PERFORMANSI

En yüksek ciro getiren ürün: {top_product["Ürün Adı"]}
Ürün kategorisi: {top_product["Kategori"]}
Ürün toplam cirosu: {format_currency(top_product["Toplam Ciro"])}
Ürün toplam kârı: {format_currency(top_product["Toplam Kâr"])}
Ürün toplam satış adedi: {format_number(top_product["Toplam Satış Adedi"])}

Yorum:
{top_product["Ürün Adı"]}, ürün bazlı performansta en güçlü kalemdir. Bu ürünün stok seviyesi, tedarik süresi ve satış kanalı performansı yakından takip edilmelidir.

7. STOK RİSKİ

Kritik stokta olan ürün sayısı: {critical_stock_count}
Kritik stoktaki ürünler: {critical_stock_products}

Yorum:
Kritik stoktaki ürünler satış kaybı riski oluşturabilir. Özellikle yüksek ciro getiren veya stratejik öneme sahip ürünlerde stok yenileme öncelikli aksiyon olmalıdır.

8. YÖNETİM İÇİN ÖNERİLER

1. En yüksek ciro getiren şehir olan {top_city["Şehir"]} için satış başarısının nedenleri detaylı incelenmelidir.
2. {top_category["Kategori"]} kategorisi için stok ve kampanya planlaması öncelikli yapılmalıdır.
3. {top_customer_type["Müşteri Tipi"]} müşteri grubuna özel satış stratejileri geliştirilmelidir.
4. Kritik stoktaki ürünler için yeniden sipariş süreci hızlandırılmalıdır.
5. Aylık ciro trendi düzenli takip edilerek düşük performanslı aylar için kampanya planlanmalıdır.
6. En yüksek ciro getiren ürünlerin stok durumu ve kâr marjı düzenli izlenmelidir.

SONUÇ

Bu proje, satış, stok ve müşteri verilerini birleştirerek yönetime karar desteği sağlayan bir analiz yapısı oluşturmuştur. Elde edilen raporlar; şehir performansı, kategori performansı, müşteri tipi, aylık trend, ürün performansı ve kritik stok risklerini birlikte değerlendirmeyi mümkün hale getirmiştir.
"""

summary_path = os.path.join(REPORTS_DIR, "yonetici_ozeti.txt")

with open(summary_path, "w", encoding="utf-8") as file:
    file.write(summary_text)


kpi_summary = pd.DataFrame([
    {"Metrik": "Toplam Ciro", "Değer": total_revenue},
    {"Metrik": "Toplam Kâr", "Değer": total_profit},
    {"Metrik": "Toplam Satış Adedi", "Değer": total_quantity},
    {"Metrik": "Toplam Sipariş Sayısı", "Değer": total_orders},
    {"Metrik": "Genel Kâr Marjı (%)", "Değer": profit_margin},
    {"Metrik": "En Güçlü Şehir", "Değer": top_city["Şehir"]},
    {"Metrik": "En Güçlü Kategori", "Değer": top_category["Kategori"]},
    {"Metrik": "En Güçlü Müşteri Tipi", "Değer": top_customer_type["Müşteri Tipi"]},
    {"Metrik": "En Güçlü Ay", "Değer": top_month["Ay"]},
    {"Metrik": "En Güçlü Ürün", "Değer": top_product["Ürün Adı"]},
    {"Metrik": "Kritik Stok Ürün Sayısı", "Değer": critical_stock_count},
])

kpi_summary.to_csv(
    os.path.join(REPORTS_DIR, "yonetici_kpi_ozeti.csv"),
    index=False,
    encoding="utf-8-sig"
)

print("Yonetici ozeti basariyla olusturuldu.")
print("- reports/yonetici_ozeti.txt")
print("- reports/yonetici_kpi_ozeti.csv")

print("Kisa KPI ozeti:")
print(kpi_summary)