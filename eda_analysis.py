# 23/CS/193
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load preprocessed merged data
data_path = "C:/Users/JHUGAN KARTIKEY/PROJECTS/DPIO/data/"
products = pd.read_csv(data_path + "products.csv")
inventory = pd.read_csv(data_path + "inventory.csv")
sales = pd.read_csv(data_path + "sales.csv")

# Merge
sales["date"] = pd.to_datetime(sales["date"])
merged = sales.merge(products, on="product_id", how="left") \
              .merge(inventory, on="product_id", how="left")

# Total revenue per transaction
merged["revenue"] = merged["units_sold"] * merged["price_sold"]

# ---------- EDA 1: Total revenue over time ----------
plt.figure(figsize=(10,5))
daily_revenue = merged.groupby("date")["revenue"].sum().reset_index()
sns.lineplot(data=daily_revenue, x="date", y="revenue")
plt.title("Total Revenue Over Time")
plt.xlabel("Date")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ---------- EDA 2: Category-wise total revenue ----------
category_revenue = merged.groupby("category")["revenue"].sum().sort_values(ascending=False)
plt.figure(figsize=(10,5))
sns.barplot(x=category_revenue.index, y=category_revenue.values)
plt.title("Revenue by Product Category")
plt.ylabel("Revenue")
plt.xlabel("Category")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ---------- EDA 3: Units sold vs price ----------
plt.figure(figsize=(10,6))
sns.scatterplot(data=merged, x="price_sold", y="units_sold", alpha=0.6)
plt.title("Price vs Units Sold")
plt.xlabel("Selling Price")
plt.ylabel("Units Sold")
plt.tight_layout()
plt.show()

# ---------- EDA 4: Inventory vs Sales ----------
avg_sales = merged.groupby("product_id")["units_sold"].mean()
stock_levels = inventory.set_index("product_id")["stock_available"]
compare = pd.DataFrame({"avg_units_sold": avg_sales, "stock_available": stock_levels})
compare.dropna(inplace=True)

plt.figure(figsize=(10,6))
sns.scatterplot(data=compare, x="stock_available", y="avg_units_sold")
plt.title("Inventory vs Average Demand")
plt.xlabel("Stock Available")
plt.ylabel("Average Units Sold per Day")
plt.tight_layout()
plt.show()
