# ============================================================
# M16 Lesson 6 – Implementation of Linear Regression
# ============================================================
# This lesson brings it all together — a complete end-to-end
# Linear Regression implementation using a real-style dataset.
# Steps: Load data → EDA → Preprocess → Train → Evaluate → Predict.
# ============================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

sns.set_theme(style="whitegrid")
np.random.seed(42)


# ----------------------------
# Activity 1: Load and Explore the Dataset (EDA)
# ----------------------------
# Goal: Build a realistic dataset and perform EDA before modeling.
# Summary: Students will create a house price dataset, explore it with
#          .describe(), .corr(), and visualize feature relationships.

# Task:
n = 100
area      = np.random.randint(500, 3000, n)
bedrooms  = np.random.randint(1, 6, n)
bathrooms = np.random.randint(1, 4, n)
age       = np.random.randint(1, 40, n)
distance  = np.random.randint(2, 30, n)     # km from city center
price     = (area * 50 + bedrooms * 75000
             + bathrooms * 50000 - age * 3000
             - distance * 8000
             + np.random.randn(n) * 40000)

df = pd.DataFrame({
    "Area_sqft":  area,
    "Bedrooms":   bedrooms,
    "Bathrooms":  bathrooms,
    "Age_years":  age,
    "Distance_km": distance,
    "Price":      price.astype(int)
})

print("=" * 60)
print("  M16 CAPSTONE – HOUSE PRICE LINEAR REGRESSION")
print("=" * 60)
print(f"\nDataset Shape: {df.shape}")
print(f"\nFirst 5 rows:\n{df.head().to_string(index=False)}")
print(f"\nStatistics:\n{df.describe().to_string()}")
print(f"\nMissing Values:\n{df.isnull().sum().to_string()}")

# EDA: Correlation heatmap
plt.figure(figsize=(8, 5))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Correlation Heatmap – House Features vs Price")
plt.tight_layout()
plt.show()

# EDA: Feature vs Price scatter plots
fig, axes = plt.subplots(2, 3, figsize=(14, 8))
features_plot = ["Area_sqft", "Bedrooms", "Bathrooms", "Age_years", "Distance_km"]
for i, feat in enumerate(features_plot):
    ax = axes[i // 3][i % 3]
    ax.scatter(df[feat], df["Price"], alpha=0.5, color="steelblue", s=30)
    ax.set_xlabel(feat)
    ax.set_ylabel("Price (₹)")
    ax.set_title(f"{feat} vs Price")
axes[1][2].axis("off")
plt.suptitle("Feature vs Price – EDA Scatter Plots", fontsize=13)
plt.tight_layout()
plt.show()


# ----------------------------
# Activity 2: Preprocess and Train the Model
# ----------------------------
# Goal: Prepare features, split data, scale, and train Linear Regression.
# Summary: Students will separate features from labels, apply StandardScaler,
#          perform train/test split, and fit the LinearRegression model.

# Task:
X = df.drop("Price", axis=1)
y = df["Price"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
print(f"\nTrain size : {len(X_train)} samples")
print(f"Test size  : {len(X_test)} samples")

scaler  = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled  = scaler.transform(X_test)

model = LinearRegression()
model.fit(X_train_scaled, y_train)

print("\n--- Trained Model Coefficients ---")
for feat, coef in zip(X.columns, model.coef_):
    direction = "↑ increases" if coef > 0 else "↓ decreases"
    print(f"   {feat:<15}: ₹{coef:>10,.0f}  → {direction} price")
print(f"   {'Intercept':<15}: ₹{model.intercept_:>10,.0f}")


# ----------------------------
# Activity 3: Evaluate, Visualize, and Predict
# ----------------------------
# Goal: Evaluate the model on test data and make new predictions.
# Summary: Students will compute all regression metrics, plot actual vs
#          predicted prices, and use the model to predict custom houses.

# Task:
y_pred = model.predict(X_test_scaled)

mae  = mean_absolute_error(y_test, y_pred)
mse  = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2   = r2_score(y_test, y_pred)

print("\n--- MODEL EVALUATION (on Test Set) ---")
print(f"MAE  : ₹{mae:,.0f}   → avg prediction off by ₹{mae:,.0f}")
print(f"RMSE : ₹{rmse:,.0f}")
print(f"R²   : {r2:.4f}  → model explains {r2*100:.1f}% of price variance")

# Actual vs Predicted plot
plt.figure(figsize=(7, 5))
plt.scatter(y_test, y_pred, alpha=0.6, color="steelblue", s=60, edgecolors="black")
min_val = min(y_test.min(), y_pred.min())
max_val = max(y_test.max(), y_pred.max())
plt.plot([min_val, max_val], [min_val, max_val], "r--", linewidth=2, label="Perfect Prediction")
plt.xlabel("Actual Price (₹)")
plt.ylabel("Predicted Price (₹)")
plt.title(f"Actual vs Predicted House Prices (R² = {r2:.3f})")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# Predict on new custom houses
new_houses = pd.DataFrame({
    "Area_sqft":   [1200, 2000, 800],
    "Bedrooms":    [3,    4,    2],
    "Bathrooms":   [2,    3,    1],
    "Age_years":   [5,    10,   20],
    "Distance_km": [8,    5,    15],
})

new_scaled   = scaler.transform(new_houses)
new_prices   = model.predict(new_scaled)

print("\n--- PREDICTING NEW HOUSE PRICES ---")
print(f"{'Area':>6} {'Beds':>5} {'Bath':>5} {'Age':>5} {'Dist':>6}  →  Predicted Price")
print("-" * 55)
for i, row in new_houses.iterrows():
    print(f"{row['Area_sqft']:>6} sqft | {row['Bedrooms']:>2} beds | "
          f"{row['Bathrooms']:>2} bath | {row['Age_years']:>3} yr | "
          f"{row['Distance_km']:>3} km  →  ₹{new_prices[i]:>10,.0f}")
