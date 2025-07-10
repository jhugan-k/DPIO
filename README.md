# DPIO – Dynamic Pricing & Inventory Optimisation Dashboard

A data-driven dashboard that uses Machine Learning to optimize product pricing and predict demand. Designed for e-commerce companies to maximize revenue by adjusting prices intelligently based on demand and stock levels.

---

## Features

>  Upload product, sales, and inventory data  

>  Predict product demand using ML  

>  Suggest optimal prices to maximize revenue  

>  Visual dashboard with filters, graphs, and tables  

>  Download filtered results as CSV  

>  Summary stats: revenue, uplift, product count


---

## Working

1. **Data Inputs**: `products.csv`, `sales.csv`, `inventory.csv`
2. **Model**: Trained using `RandomForestRegressor` on historical sales patterns
3. **Predictions**: For each product, estimate demand at multiple price points
4. **Optimisation**: Choose the price with the highest expected revenue
5. **Output**: Display in an interactive Streamlit dashboard

---

##  Tech Stack Used

- **Frontend**: Streamlit, Plotly
- **Backend**: Python, Pandas
- **ML Model**: Random Forest (scikit-learn)
- **Deployment**: Streamlit Cloud

---


##  Future Work
>Add time-based price suggestions


>Add user data integration features

>Include category-wise comparison graphs


>Integrate with live e-commerce APIs (like Shopify or Flipkart Seller API)
