# 23/CS/193
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="📊 DPIO Optimiser", layout="wide")

# ---------------- STYLING ----------------
st.markdown("""
    <style>
    body, .main, .block-container {
        background-color: #493628;
        color: #E4E0E1;
        font-family: 'Segoe UI', sans-serif;
    }

    h1, h2 {
        color: #AB886D;
        font-weight: 800;
    }

    h3, .stMarkdown h3 {
        color: #B99470;
    }

    .stSidebar {
        background-color: #D6C0B3 !important;
        color: #493628;
    }

    .stSidebar label, .stSidebar .stTextInput > label, .stSidebar .stSelectbox > label {
        color: #9A7C5D !important;
        font-weight: 600;
    }

    .stSelectbox div, .stTextInput input {
        background-color: #F4EBD3 !important;
        color: #493628 !important;
        border-radius: 8px;
        box-shadow: none !important;
    }

    thead tr th {
        background-color: #D6C0B3 !important;
        color: #493628 !important;
        font-weight: bold;
    }

    tbody tr td {
        background-color: #D6C0B3 !important;
        color: #493628 !important;
    }

    tbody tr:hover td {
        background-color: #B99470 !important;
        color: #fff !important;
    }

    .stDataFrame {
        border-radius: 10px;
        overflow: hidden;
    }

    .stButton > button {
        background-color: #AB886D;
        color: white;
        border-radius: 8px;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------- LOAD DATA ----------------
data_path = 'data/' # Or even just use 'data/optimal_prices.csv' directly
df = pd.read_csv(data_path + "optimal_prices.csv")

df = pd.read_csv(data_path + "optimal_prices.csv")
products = pd.read_csv(data_path + "products.csv")
df = df.merge(products[["product_id", "category"]], on="product_id", how="left")

# ---------------- HEADER ----------------
st.title("📊 Dynamic Pricing & Inventory Optimisation")
st.markdown("Use ML-driven demand prediction to maximise e-commerce revenue.")

# ---------------- SIDEBAR ----------------
st.sidebar.header("🔎 Filter")
category_filter = st.sidebar.selectbox("Product Category", ["All"] + sorted(df["category"].unique()))
search = st.sidebar.text_input("Search Product")

# ---------------- ABOUT SECTION ----------------
st.sidebar.markdown("---")
st.sidebar.subheader("ℹ️ About This Project")
st.sidebar.markdown(
    """
    **DPIO** is a data-driven tool that uses Machine Learning to:
    - Predict product demand
    - Suggest optimal prices
    - Maximize revenue
    - Support inventory planning

    Built with ❤️ using Streamlit, Pandas & Plotly.
    """
)

# ---------------- FILTER DATA ----------------
filtered_df = df.copy()
if category_filter != "All":
    filtered_df = filtered_df[filtered_df["category"] == category_filter]
if search:
    filtered_df = filtered_df[filtered_df["product_name"].str.contains(search, case=False)]

# ---------------- SUMMARY CARDS ----------------
st.markdown("### 📌 Summary")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Products", len(filtered_df))

with col2:
    st.metric("Total Expected Revenue", f"${filtered_df['expected_revenue'].sum():,.0f}")

with col3:
    uplift = (filtered_df["optimal_price"].mean() - filtered_df["base_price"].mean()) / filtered_df["base_price"].mean() * 100
    st.metric("Avg Price Uplift", f"{uplift:.2f}%")

# ---------------- MAIN TABLE ----------------
st.markdown("### 🧾 Product Pricing Suggestions")
st.dataframe(
    filtered_df[["product_name", "category", "base_price", "optimal_price", "predicted_units", "expected_revenue"]]
    .sort_values(by="expected_revenue", ascending=False)
    .reset_index(drop=True),
    use_container_width=True,
)

# ---------------- DOWNLOAD ----------------
csv_download = filtered_df.to_csv(index=False).encode('utf-8')
st.download_button("📥 Download Filtered Data", csv_download, file_name="filtered_results.csv", mime='text/csv')

# ---------------- CHART ----------------
st.markdown("### 📈 Revenue at Base vs Optimal Price")

top_20 = df.sort_values(by="expected_revenue", ascending=False).head(20)

fig = px.bar(top_20,
             x="product_name",
             y=["base_price", "optimal_price"],
             barmode="group",
             title="Top 20 Products by Revenue Potential",
             labels={"value": "Price", "product_name": "Product"},
             height=500,
             color_discrete_sequence=["#F4EBD3", "#B99470"]
)

fig.update_layout(
    plot_bgcolor="#493628",
    paper_bgcolor="#493628",
    font=dict(color="#E4E0E1"),
    title_font=dict(color="#AB886D"),
    legend=dict(font=dict(color="#E4E0E1")),
    xaxis=dict(tickfont=dict(color="#E4E0E1")),
    yaxis=dict(tickfont=dict(color="#E4E0E1")),
)

st.plotly_chart(fig, use_container_width=True)
