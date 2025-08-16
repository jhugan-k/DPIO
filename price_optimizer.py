# 23/CS/193
import pandas as pd
import numpy as np
import joblib

# Load data and model
data_path = "C:/Users/JHUGAN KARTIKEY/PROJECTS/DPIO/data/"
products = pd.read_csv(data_path + "products.csv")
inventory = pd.read_csv(data_path + "inventory.csv")
model = joblib.load(data_path + "demand_model.pkl")

# Set today's context for features
from datetime import datetime
today = datetime.now()
day_of_week = today.weekday()
is_weekend = 1 if day_of_week >= 5 else 0

# Output list
optimal_prices = []

# For each product
for _, row in products.iterrows():
    pid = row["product_id"]
    base_price = row["base_price"]
    category = row["category"]
    
    # Get current stock
    stock = inventory[inventory["product_id"] == pid]["stock_available"].values[0]

    # Try prices from -20% to +20% of base price (step ₹50)
    price_range = np.arange(base_price * 0.8, base_price * 1.2 + 1, 50)
    best_price = base_price
    best_revenue = 0
    best_predicted_demand = 0

    for price in price_range:
        price = round(price, 2)
        price_deviation = (price - base_price) / base_price

        # Example values for simplicity
        sales_velocity = 5
        category_encoded = pd.Series([category]).astype("category").cat.codes[0]
        stock_to_sales_ratio = stock / (sales_velocity + 1)

        features = [[
            price, price_deviation, stock,
            stock_to_sales_ratio, sales_velocity,
            day_of_week, is_weekend, category_encoded
        ]]

        predicted_units = model.predict(features)[0]
        revenue = predicted_units * price

        if revenue > best_revenue:
            best_revenue = revenue
            best_price = price
            best_predicted_demand = predicted_units

    optimal_prices.append({
        "product_id": pid,
        "product_name": row["product_name"],
        "base_price": base_price,
        "optimal_price": best_price,
        "predicted_units": round(best_predicted_demand, 2),
        "expected_revenue": round(best_revenue, 2)
    })

# Save output
df_optimal = pd.DataFrame(optimal_prices)
df_optimal.to_csv(data_path + "optimal_prices.csv", index=False)

print("✅ Price optimisation complete. Saved as optimal_prices.csv")
