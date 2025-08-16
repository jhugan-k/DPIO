# 23/CS/193
import pandas as pd
import numpy as np

# Load data
data_path = "C:/Users/JHUGAN KARTIKEY/PROJECTS/DPIO/data/"
products = pd.read_csv(data_path + "products.csv")
inventory = pd.read_csv(data_path + "inventory.csv")
sales = pd.read_csv(data_path + "sales.csv")

# Convert date
sales["date"] = pd.to_datetime(sales["date"])
inventory["last_updated"] = pd.to_datetime(inventory["last_updated"])

# Merge all
df = sales.merge(products, on="product_id").merge(inventory, on="product_id")

# ------------------------ Feature Engineering ------------------------

# 1. Day of week (0 = Monday, 6 = Sunday)
df["day_of_week"] = df["date"].dt.dayofweek

# 2. Is weekend (Saturday=5 or Sunday=6)
df["is_weekend"] = df["day_of_week"].apply(lambda x: 1 if x >= 5 else 0)

# 3. Price deviation from base price
df["price_deviation"] = (df["price_sold"] - df["base_price"]) / df["base_price"]

# 4. Days since last inventory update
df["days_since_stock_update"] = (df["date"] - df["last_updated"]).dt.days

# 5. Category encoding (optional - label encode)
df["category_encoded"] = df["category"].astype("category").cat.codes

# 6. Sales velocity (rolling mean of units sold per product)
df.sort_values(by=["product_id", "date"], inplace=True)
df["sales_velocity"] = df.groupby("product_id")["units_sold"].transform(lambda x: x.rolling(window=3, min_periods=1).mean())

# 7. Stock to sales ratio
df["stock_to_sales_ratio"] = df["stock_available"] / (df["units_sold"] + 1)  # +1 to avoid divide by zero

# Preview
print(df[[
    "date", "product_id", "units_sold", "price_sold", "base_price", "price_deviation",
    "sales_velocity", "day_of_week", "is_weekend", "stock_available", "stock_to_sales_ratio"
]].head())

# Optional: Save to file
df.to_csv(data_path + "features.csv", index=False)
