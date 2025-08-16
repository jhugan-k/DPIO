# 23/CS/193
import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
data_path = "C:/Users/JHUGAN KARTIKEY/PROJECTS/DPIO/data/"
df = pd.read_csv(data_path + "optimal_prices.csv")
products = pd.read_csv(data_path + "products.csv")

# Merge category info
df = df.merge(products[["product_id", "category"]], on="product_id", how="left")

# ----------------- Streamlit UI -----------------
st.set_page_config(page_title="DPIO Dashboard", layout="wide")
st.title("📈 Dynamic Pricing & Inventory Optimisation Dashboard")

# Sidebar filters
category_filter = st.sidebar.selectbox("Select Category", ["All"] + sorted(df["category"].unique().tolist()))
search = st.sidebar.text_input("Search Product")

# Apply filters
filtered_df = df.copy()
if category_filter != "All":
    filtered_df = filtered_df[filtered_df["category"] == category_filter]
if search:
    filtered_df = filtered_df[filtered_df["product_name"].str.contains(search, case=False)]

# Show table
st.subheader("🛒 Product Pricing Suggestions")
st.dataframe(filtered_df[[
    "product_name", "category", "base_price", "optimal_price",
    "predicted_units", "expected_revenue"
]].sort_values(by="expected_revenue", ascending=False))

# Revenue comparison plot
st.subheader("💰 Revenue Comparison (Base vs Optimal Pricing)")
filtered_df["base_revenue"] = filtered_df["base_price"] * filtered_df["predicted_units"]
revenue_plot = px.bar(
    filtered_df.sort_values("expected_revenue", ascending=False).head(20),
    x="product_name",
    y=["base_revenue", "expected_revenue"],
    barmode="group",
    labels={"value": "Revenue", "product_name": "Product"},
    title="Top 20 Products by Revenue Potential"
)
st.plotly_chart(revenue_plot, use_container_width=True)
