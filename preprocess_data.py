# 23/CS/193
import pandas as pd

# Set your data path
data_path = 'data/'

# Load datasets
products = pd.read_csv(data_path + "products.csv")
inventory = pd.read_csv(data_path + "inventory.csv")
sales = pd.read_csv(data_path + "sales.csv")

# Convert date columns to datetime
sales["date"] = pd.to_datetime(sales["date"])
inventory["last_updated"] = pd.to_datetime(inventory["last_updated"])

# Check for missing values
print("\n🔍 Missing Values Check:")
print("Products:\n", products.isnull().sum())
print("Inventory:\n", inventory.isnull().sum())
print("Sales:\n", sales.isnull().sum())

# Fill or handle missing values (if any)
# Example:
# products["base_price"].fillna(products["base_price"].median(), inplace=True)

# Check data types
print("\n📋 Data Types:")
print(products.dtypes)
print(inventory.dtypes)
print(sales.dtypes)

# Ensure 'product_id' is int in all files
products["product_id"] = products["product_id"].astype(int)
inventory["product_id"] = inventory["product_id"].astype(int)
sales["product_id"] = sales["product_id"].astype(int)

# Check for duplicates
print("\n📦 Duplicate Rows:")
print("Products:", products.duplicated().sum())
print("Inventory:", inventory.duplicated().sum())
print("Sales:", sales.duplicated().sum())

# Optional: Merge all datasets for preview
merged_df = sales.merge(products, on="product_id", how="left") \
                 .merge(inventory, on="product_id", how="left")

# Preview merged data
print("\n✅ Merged Dataset Preview:")
print(merged_df.head())
