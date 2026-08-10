import os
import pandas as pd

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(PROJECT_DIR, "data")

os.makedirs(DATA_DIR, exist_ok=True)

customers = [
    {"customer_id": 1, "customer_name": "Ahmet Yilmaz", "city": "Adana", "customer_type": "Individual"},
    {"customer_id": 2, "customer_name": "Zeynep Kaya", "city": "Mersin", "customer_type": "Individual"},
    {"customer_id": 3, "customer_name": "ABC Ltd.", "city": "Istanbul", "customer_type": "Corporate"},
    {"customer_id": 4, "customer_name": "Nova A.S.", "city": "Ankara", "customer_type": "Corporate"},
    {"customer_id": 5, "customer_name": "Deniz Demir", "city": "Adana", "customer_type": "Individual"},
    {"customer_id": 6, "customer_name": "Kuzey Market", "city": "Izmir", "customer_type": "Corporate"},
    {"customer_id": 7, "customer_name": "Murat Celik", "city": "Bursa", "customer_type": "Individual"},
    {"customer_id": 8, "customer_name": "Beta Teknoloji", "city": "Istanbul", "customer_type": "Corporate"},
    {"customer_id": 9, "customer_name": "Elif Arslan", "city": "Ankara", "customer_type": "Individual"},
    {"customer_id": 10, "customer_name": "Akdeniz Ofis", "city": "Mersin", "customer_type": "Corporate"},
]

products = [
    {"product_id": 1, "product_name": "Laptop", "category": "Electronics", "unit_cost": 18000, "unit_price": 25000},
    {"product_id": 2, "product_name": "Mouse", "category": "Electronics", "unit_cost": 250, "unit_price": 500},
    {"product_id": 3, "product_name": "Keyboard", "category": "Electronics", "unit_cost": 700, "unit_price": 1200},
    {"product_id": 4, "product_name": "Monitor", "category": "Electronics", "unit_cost": 4200, "unit_price": 6000},
    {"product_id": 5, "product_name": "Phone", "category": "Electronics", "unit_cost": 13000, "unit_price": 18000},
    {"product_id": 6, "product_name": "Headphones", "category": "Electronics", "unit_cost": 450, "unit_price": 900},
    {"product_id": 7, "product_name": "Notebook", "category": "Stationery", "unit_cost": 20, "unit_price": 50},
    {"product_id": 8, "product_name": "Pen", "category": "Stationery", "unit_cost": 4, "unit_price": 10},
    {"product_id": 9, "product_name": "Folder", "category": "Stationery", "unit_cost": 10, "unit_price": 25},
    {"product_id": 10, "product_name": "Chair", "category": "Furniture", "unit_cost": 900, "unit_price": 1500},
    {"product_id": 11, "product_name": "Desk", "category": "Furniture", "unit_cost": 2400, "unit_price": 3500},
    {"product_id": 12, "product_name": "Sofa", "category": "Furniture", "unit_cost": 8500, "unit_price": 12000},
]

orders = [
    {"order_id": 1, "customer_id": 1, "order_date": "2026-01-05", "sales_channel": "Online"},
    {"order_id": 2, "customer_id": 2, "order_date": "2026-01-08", "sales_channel": "Store"},
    {"order_id": 3, "customer_id": 3, "order_date": "2026-01-15", "sales_channel": "Corporate"},
    {"order_id": 4, "customer_id": 4, "order_date": "2026-02-02", "sales_channel": "Corporate"},
    {"order_id": 5, "customer_id": 5, "order_date": "2026-02-12", "sales_channel": "Online"},
    {"order_id": 6, "customer_id": 6, "order_date": "2026-02-20", "sales_channel": "Corporate"},
    {"order_id": 7, "customer_id": 7, "order_date": "2026-03-03", "sales_channel": "Store"},
    {"order_id": 8, "customer_id": 8, "order_date": "2026-03-10", "sales_channel": "Corporate"},
    {"order_id": 9, "customer_id": 9, "order_date": "2026-03-22", "sales_channel": "Online"},
    {"order_id": 10, "customer_id": 10, "order_date": "2026-04-01", "sales_channel": "Corporate"},
    {"order_id": 11, "customer_id": 1, "order_date": "2026-04-08", "sales_channel": "Online"},
    {"order_id": 12, "customer_id": 3, "order_date": "2026-04-16", "sales_channel": "Corporate"},
    {"order_id": 13, "customer_id": 4, "order_date": "2026-05-04", "sales_channel": "Corporate"},
    {"order_id": 14, "customer_id": 6, "order_date": "2026-05-14", "sales_channel": "Corporate"},
    {"order_id": 15, "customer_id": 8, "order_date": "2026-05-25", "sales_channel": "Corporate"},
    {"order_id": 16, "customer_id": 2, "order_date": "2026-06-06", "sales_channel": "Store"},
    {"order_id": 17, "customer_id": 5, "order_date": "2026-06-11", "sales_channel": "Online"},
    {"order_id": 18, "customer_id": 7, "order_date": "2026-06-19", "sales_channel": "Store"},
    {"order_id": 19, "customer_id": 9, "order_date": "2026-06-24", "sales_channel": "Online"},
    {"order_id": 20, "customer_id": 10, "order_date": "2026-06-28", "sales_channel": "Corporate"},
]

order_items = [
    {"order_item_id": 1, "order_id": 1, "product_id": 1, "quantity": 1},
    {"order_item_id": 2, "order_id": 1, "product_id": 2, "quantity": 2},
    {"order_item_id": 3, "order_id": 2, "product_id": 3, "quantity": 1},
    {"order_item_id": 4, "order_id": 2, "product_id": 6, "quantity": 2},
    {"order_item_id": 5, "order_id": 3, "product_id": 4, "quantity": 5},
    {"order_item_id": 6, "order_id": 3, "product_id": 10, "quantity": 8},
    {"order_item_id": 7, "order_id": 4, "product_id": 11, "quantity": 4},
    {"order_item_id": 8, "order_id": 4, "product_id": 7, "quantity": 60},
    {"order_item_id": 9, "order_id": 5, "product_id": 8, "quantity": 100},
    {"order_item_id": 10, "order_id": 5, "product_id": 9, "quantity": 40},
    {"order_item_id": 11, "order_id": 6, "product_id": 5, "quantity": 3},
    {"order_item_id": 12, "order_id": 6, "product_id": 4, "quantity": 2},
    {"order_item_id": 13, "order_id": 7, "product_id": 10, "quantity": 2},
    {"order_item_id": 14, "order_id": 7, "product_id": 8, "quantity": 50},
    {"order_item_id": 15, "order_id": 8, "product_id": 1, "quantity": 2},
    {"order_item_id": 16, "order_id": 8, "product_id": 12, "quantity": 1},
    {"order_item_id": 17, "order_id": 9, "product_id": 6, "quantity": 5},
    {"order_item_id": 18, "order_id": 9, "product_id": 3, "quantity": 2},
    {"order_item_id": 19, "order_id": 10, "product_id": 11, "quantity": 6},
    {"order_item_id": 20, "order_id": 10, "product_id": 10, "quantity": 12},
    {"order_item_id": 21, "order_id": 11, "product_id": 2, "quantity": 4},
    {"order_item_id": 22, "order_id": 11, "product_id": 7, "quantity": 30},
    {"order_item_id": 23, "order_id": 12, "product_id": 5, "quantity": 4},
    {"order_item_id": 24, "order_id": 12, "product_id": 4, "quantity": 3},
    {"order_item_id": 25, "order_id": 13, "product_id": 12, "quantity": 2},
    {"order_item_id": 26, "order_id": 13, "product_id": 11, "quantity": 5},
    {"order_item_id": 27, "order_id": 14, "product_id": 1, "quantity": 3},
    {"order_item_id": 28, "order_id": 14, "product_id": 6, "quantity": 10},
    {"order_item_id": 29, "order_id": 15, "product_id": 4, "quantity": 6},
    {"order_item_id": 30, "order_id": 15, "product_id": 10, "quantity": 15},
    {"order_item_id": 31, "order_id": 16, "product_id": 3, "quantity": 3},
    {"order_item_id": 32, "order_id": 17, "product_id": 8, "quantity": 120},
    {"order_item_id": 33, "order_id": 18, "product_id": 7, "quantity": 80},
    {"order_item_id": 34, "order_id": 19, "product_id": 2, "quantity": 5},
    {"order_item_id": 35, "order_id": 20, "product_id": 5, "quantity": 2},
    {"order_item_id": 36, "order_id": 20, "product_id": 12, "quantity": 1},
]

inventory = [
    {"product_id": 1, "current_stock": 6, "reorder_level": 5},
    {"product_id": 2, "current_stock": 18, "reorder_level": 10},
    {"product_id": 3, "current_stock": 8, "reorder_level": 10},
    {"product_id": 4, "current_stock": 4, "reorder_level": 5},
    {"product_id": 5, "current_stock": 3, "reorder_level": 4},
    {"product_id": 6, "current_stock": 12, "reorder_level": 8},
    {"product_id": 7, "current_stock": 120, "reorder_level": 50},
    {"product_id": 8, "current_stock": 200, "reorder_level": 100},
    {"product_id": 9, "current_stock": 35, "reorder_level": 40},
    {"product_id": 10, "current_stock": 7, "reorder_level": 6},
    {"product_id": 11, "current_stock": 2, "reorder_level": 4},
    {"product_id": 12, "current_stock": 1, "reorder_level": 3},
]

pd.DataFrame(customers).to_csv(os.path.join(DATA_DIR, "customers.csv"), index=False)
pd.DataFrame(products).to_csv(os.path.join(DATA_DIR, "products.csv"), index=False)
pd.DataFrame(orders).to_csv(os.path.join(DATA_DIR, "orders.csv"), index=False)
pd.DataFrame(order_items).to_csv(os.path.join(DATA_DIR, "order_items.csv"), index=False)
pd.DataFrame(inventory).to_csv(os.path.join(DATA_DIR, "inventory.csv"), index=False)

print("Project data files created successfully.")
print("Created files:")
print("- data/customers.csv")
print("- data/products.csv")
print("- data/orders.csv")
print("- data/order_items.csv")
print("- data/inventory.csv")