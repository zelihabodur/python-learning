import os
import pandas as pd

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(PROJECT_DIR, "data")
REPORTS_DIR = os.path.join(PROJECT_DIR, "reports")

os.makedirs(REPORTS_DIR, exist_ok=True)

for file_name in os.listdir(REPORTS_DIR):
    if file_name.endswith(".csv"):
        os.remove(os.path.join(REPORTS_DIR, file_name))

customers_path = os.path.join(DATA_DIR, "customers.csv")
products_path = os.path.join(DATA_DIR, "products.csv")
orders_path = os.path.join(DATA_DIR, "orders.csv")
order_items_path = os.path.join(DATA_DIR, "order_items.csv")
inventory_path = os.path.join(DATA_DIR, "inventory.csv")

customers = pd.read_csv(customers_path)
products = pd.read_csv(products_path)
orders = pd.read_csv(orders_path)
order_items = pd.read_csv(order_items_path)
inventory = pd.read_csv(inventory_path)

print("Veri dosyalari basariyla okundu.")
print("Musteriler:", customers.shape)
print("Urunler:", products.shape)
print("Siparisler:", orders.shape)
print("Siparis urunleri:", order_items.shape)
print("Stok:", inventory.shape)

sales_data = order_items.merge(
    orders,
    on="order_id",
    how="left"
)

sales_data = sales_data.merge(
    customers,
    on="customer_id",
    how="left"
)

sales_data = sales_data.merge(
    products,
    on="product_id",
    how="left"
)

sales_data = sales_data.merge(
    inventory,
    on="product_id",
    how="left"
)

city_map = {
    "Istanbul": "İstanbul",
    "Izmir": "İzmir",
    "Adana": "Adana",
    "Mersin": "Mersin",
    "Ankara": "Ankara",
    "Bursa": "Bursa"
}

category_map = {
    "Electronics": "Elektronik",
    "Stationery": "Kırtasiye",
    "Furniture": "Mobilya"
}

product_map = {
    "Laptop": "Laptop",
    "Mouse": "Mouse",
    "Keyboard": "Klavye",
    "Monitor": "Monitör",
    "Phone": "Telefon",
    "Headphones": "Kulaklık",
    "Notebook": "Defter",
    "Pen": "Kalem",
    "Folder": "Dosya",
    "Chair": "Sandalye",
    "Desk": "Masa",
    "Sofa": "Koltuk"
}

customer_type_map = {
    "Individual": "Bireysel",
    "Corporate": "Kurumsal"
}

sales_channel_map = {
    "Online": "Online",
    "Store": "Mağaza",
    "Corporate": "Kurumsal"
}

sales_data["city"] = sales_data["city"].replace(city_map)
sales_data["category"] = sales_data["category"].replace(category_map)
sales_data["product_name"] = sales_data["product_name"].replace(product_map)
sales_data["customer_type"] = sales_data["customer_type"].replace(customer_type_map)
sales_data["sales_channel"] = sales_data["sales_channel"].replace(sales_channel_map)

sales_data["order_date"] = pd.to_datetime(sales_data["order_date"])
sales_data["month"] = sales_data["order_date"].dt.to_period("M").astype(str)

sales_data["revenue"] = sales_data["quantity"] * sales_data["unit_price"]
sales_data["total_cost"] = sales_data["quantity"] * sales_data["unit_cost"]
sales_data["profit"] = sales_data["revenue"] - sales_data["total_cost"]
sales_data["profit_margin_pct"] = ((sales_data["profit"] / sales_data["revenue"]) * 100).round(2)

sales_data["stock_status"] = sales_data.apply(
    lambda row: "Kritik Stok" if row["current_stock"] <= row["reorder_level"] else "Sağlıklı Stok",
    axis=1
)

def save_report(dataframe, file_name):
    path = os.path.join(REPORTS_DIR, file_name)
    dataframe.to_csv(path, index=False, encoding="utf-8-sig")


master_report = sales_data.rename(columns={
    "order_item_id": "Sipariş Ürün ID",
    "order_id": "Sipariş ID",
    "product_id": "Ürün ID",
    "quantity": "Adet",
    "customer_id": "Müşteri ID",
    "order_date": "Sipariş Tarihi",
    "sales_channel": "Satış Kanalı",
    "customer_name": "Müşteri Adı",
    "city": "Şehir",
    "customer_type": "Müşteri Tipi",
    "product_name": "Ürün Adı",
    "category": "Kategori",
    "unit_cost": "Birim Maliyet",
    "unit_price": "Birim Satış Fiyatı",
    "current_stock": "Mevcut Stok",
    "reorder_level": "Yeniden Sipariş Seviyesi",
    "month": "Ay",
    "revenue": "Ciro",
    "total_cost": "Toplam Maliyet",
    "profit": "Kâr",
    "profit_margin_pct": "Kâr Marjı (%)",
    "stock_status": "Stok Durumu"
})

save_report(master_report, "ana_satis_verisi.csv")

city_report = sales_data.groupby("city").agg(
    total_revenue=("revenue", "sum"),
    total_profit=("profit", "sum"),
    total_quantity=("quantity", "sum"),
    order_count=("order_id", "nunique")
).reset_index()

city_report = city_report.sort_values("total_revenue", ascending=False)

city_report = city_report.rename(columns={
    "city": "Şehir",
    "total_revenue": "Toplam Ciro",
    "total_profit": "Toplam Kâr",
    "total_quantity": "Toplam Satış Adedi",
    "order_count": "Sipariş Sayısı"
})

save_report(city_report, "sehir_ciro_raporu.csv")

category_report = sales_data.groupby("category").agg(
    total_revenue=("revenue", "sum"),
    total_profit=("profit", "sum"),
    total_quantity=("quantity", "sum"),
    average_profit_margin_pct=("profit_margin_pct", "mean")
).reset_index()

category_report["average_profit_margin_pct"] = category_report["average_profit_margin_pct"].round(2)
category_report = category_report.sort_values("total_revenue", ascending=False)

category_report = category_report.rename(columns={
    "category": "Kategori",
    "total_revenue": "Toplam Ciro",
    "total_profit": "Toplam Kâr",
    "total_quantity": "Toplam Satış Adedi",
    "average_profit_margin_pct": "Ortalama Kâr Marjı (%)"
})

save_report(category_report, "kategori_performans_raporu.csv")

customer_type_report = sales_data.groupby("customer_type").agg(
    total_revenue=("revenue", "sum"),
    total_profit=("profit", "sum"),
    total_quantity=("quantity", "sum"),
    order_count=("order_id", "nunique")
).reset_index()

customer_type_report = customer_type_report.sort_values("total_revenue", ascending=False)

customer_type_report = customer_type_report.rename(columns={
    "customer_type": "Müşteri Tipi",
    "total_revenue": "Toplam Ciro",
    "total_profit": "Toplam Kâr",
    "total_quantity": "Toplam Satış Adedi",
    "order_count": "Sipariş Sayısı"
})

save_report(customer_type_report, "musteri_tipi_raporu.csv")

monthly_report = sales_data.groupby("month").agg(
    monthly_revenue=("revenue", "sum"),
    monthly_profit=("profit", "sum"),
    monthly_quantity=("quantity", "sum"),
    order_count=("order_id", "nunique")
).reset_index()

monthly_report = monthly_report.sort_values("month")
monthly_report["cumulative_revenue"] = monthly_report["monthly_revenue"].cumsum()

monthly_report = monthly_report.rename(columns={
    "month": "Ay",
    "monthly_revenue": "Aylık Ciro",
    "monthly_profit": "Aylık Kâr",
    "monthly_quantity": "Aylık Satış Adedi",
    "order_count": "Sipariş Sayısı",
    "cumulative_revenue": "Kümülatif Ciro"
})

save_report(monthly_report, "aylik_ciro_raporu.csv")

product_inventory = products.merge(
    inventory,
    on="product_id",
    how="left"
)

product_inventory["category"] = product_inventory["category"].replace(category_map)
product_inventory["product_name"] = product_inventory["product_name"].replace(product_map)

product_inventory["stock_status"] = product_inventory.apply(
    lambda row: "Kritik Stok" if row["current_stock"] <= row["reorder_level"] else "Sağlıklı Stok",
    axis=1
)

critical_stock_report = product_inventory[product_inventory["stock_status"] == "Kritik Stok"]
critical_stock_report = critical_stock_report.sort_values("current_stock")

critical_stock_report = critical_stock_report.rename(columns={
    "product_id": "Ürün ID",
    "product_name": "Ürün Adı",
    "category": "Kategori",
    "unit_cost": "Birim Maliyet",
    "unit_price": "Birim Satış Fiyatı",
    "current_stock": "Mevcut Stok",
    "reorder_level": "Yeniden Sipariş Seviyesi",
    "stock_status": "Stok Durumu"
})

save_report(critical_stock_report, "kritik_stok_raporu.csv")

top_products_report = sales_data.groupby(["product_id", "product_name", "category"]).agg(
    total_revenue=("revenue", "sum"),
    total_profit=("profit", "sum"),
    total_quantity=("quantity", "sum")
).reset_index()

top_products_report = top_products_report.sort_values("total_revenue", ascending=False)

top_products_report = top_products_report.rename(columns={
    "product_id": "Ürün ID",
    "product_name": "Ürün Adı",
    "category": "Kategori",
    "total_revenue": "Toplam Ciro",
    "total_profit": "Toplam Kâr",
    "total_quantity": "Toplam Satış Adedi"
})

save_report(top_products_report, "en_iyi_urunler_raporu.csv")

print("\nRaporlar basariyla olusturuldu:")
print("- reports/ana_satis_verisi.csv")
print("- reports/sehir_ciro_raporu.csv")
print("- reports/kategori_performans_raporu.csv")
print("- reports/musteri_tipi_raporu.csv")
print("- reports/aylik_ciro_raporu.csv")
print("- reports/kritik_stok_raporu.csv")
print("- reports/en_iyi_urunler_raporu.csv")

print("Ana satis verisinin ilk 5 satiri:")
print(master_report.head())

print("Sehir ciro raporu:")
print(city_report)

print("Kategori performans raporu:")
print(category_report)

print("Kritik stok raporu:")
print(critical_stock_report[["Ürün Adı", "Kategori", "Mevcut Stok", "Yeniden Sipariş Seviyesi", "Stok Durumu"]])