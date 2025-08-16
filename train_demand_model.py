# 23/CS/193
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from math import sqrt
import joblib

# ---------- Load Feature Data ----------
data_path = "C:/Users/JHUGAN KARTIKEY/PROJECTS/DPIO/data/"
df = pd.read_csv(data_path + "features.csv")

# ---------- Define Input Features ----------
features = [
    "price_sold", "price_deviation", "stock_available",
    "stock_to_sales_ratio", "sales_velocity",
    "day_of_week", "is_weekend", "category_encoded"
]

X = df[features]
y = df["units_sold"]

# ---------- Train/Test Split ----------
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ---------- Train Model ----------
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# ---------- Predict and Evaluate ----------
y_pred = model.predict(X_test)
rmse = sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print("✅ Model Performance:")
print(f"RMSE: {rmse:.2f}")
print(f"R2 Score: {r2:.2f}")

# ---------- Save Model ----------
joblib.dump(model, data_path + "demand_model.pkl")
print("📦 Model saved as demand_model.pkl")
