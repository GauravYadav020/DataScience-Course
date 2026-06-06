# ============================================================
# M16 Lesson 4 – Study of Regression
# ============================================================
# Regression is studied in depth here — covering Simple Linear
# Regression, Multiple Linear Regression, Polynomial Regression,
# and key regression concepts: slope, intercept, residuals, R².
# ============================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score, mean_squared_error


# ----------------------------
# Activity 1: Simple Linear Regression – Deep Dive
# ----------------------------
# Goal: Understand slope, intercept, residuals, and R² score in detail.
# Summary: Students will manually calculate and visualize residuals
#          (prediction errors) and compute the R² score to evaluate fit.

# Task:
np.random.seed(42)
X = np.array([1,2,3,4,5,6,7,8,9,10], dtype=float).reshape(-1,1)
y = np.array([2.5, 4.1, 5.8, 7.2, 9.5, 10.8, 13.1, 14.9, 16.2, 18.5])

model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)

r2  = r2_score(y, y_pred)
mse = mean_squared_error(y, y_pred)

print("=" * 50)
print("  SIMPLE LINEAR REGRESSION – DEEP DIVE")
print("=" * 50)
print(f"Equation  : y = {model.coef_[0]:.4f}x + {model.intercept_:.4f}")
print(f"Slope (m) : {model.coef_[0]:.4f}  → for each +1 in X, y increases by {model.coef_[0]:.2f}")
print(f"Intercept : {model.intercept_:.4f} → value of y when X = 0")
print(f"R² Score  : {r2:.4f}  → model explains {r2*100:.1f}% of variance")
print(f"MSE       : {mse:.4f}")
print(f"RMSE      : {np.sqrt(mse):.4f}")

print(f"\n{'X':>5} {'Actual y':>10} {'Predicted':>10} {'Residual':>10}")
print("-" * 40)
for xi, yi, yp in zip(X.flatten(), y, y_pred):
    print(f"{xi:>5.0f} {yi:>10.2f} {yp:>10.2f} {yi-yp:>10.2f}")

# Visualize residuals
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.scatter(X, y, color="steelblue", s=70, zorder=3, label="Actual")
plt.plot(X, y_pred, color="red", linewidth=2, label="Fit Line")
for xi, yi, yp in zip(X, y, y_pred):
    plt.vlines(xi, min(yi, yp), max(yi, yp), colors="gray", linestyles="dotted")
plt.title("Regression Line with Residuals")
plt.legend(); plt.grid(True, alpha=0.3)

plt.subplot(1, 2, 2)
residuals = y - y_pred
plt.bar(X.flatten(), residuals, color=["green" if r > 0 else "red" for r in residuals])
plt.axhline(0, color="black", linewidth=1)
plt.title("Residuals (Actual − Predicted)")
plt.xlabel("X"); plt.ylabel("Residual")
plt.tight_layout()
plt.show()


# ----------------------------
# Activity 2: Multiple Linear Regression
# ----------------------------
# Goal: Extend regression to use multiple input features.
# Summary: Students will predict house prices using area, rooms, and
#          age as inputs, train a Multiple Linear Regression model.

# Task:
np.random.seed(5)
n = 50
area     = np.random.randint(600, 2500, n)
rooms    = np.random.randint(1, 6, n)
age      = np.random.randint(1, 30, n)
price    = (area * 45) + (rooms * 80000) - (age * 5000) + np.random.randn(n) * 30000

house_df = pd.DataFrame({"Area_sqft": area, "Rooms": rooms, "Age_years": age, "Price": price})

X_house = house_df[["Area_sqft", "Rooms", "Age_years"]]
y_house = house_df["Price"]

model_multi = LinearRegression()
model_multi.fit(X_house, y_house)

print("\n--- Multiple Linear Regression: House Price Prediction ---")
print(f"Coefficients:")
for feat, coef in zip(X_house.columns, model_multi.coef_):
    print(f"   {feat:<15}: ₹{coef:,.0f}")
print(f"Intercept: ₹{model_multi.intercept_:,.0f}")
print(f"R² Score : {r2_score(y_house, model_multi.predict(X_house)):.4f}")

# Predict a new house
new_house = pd.DataFrame({"Area_sqft": [1200], "Rooms": [3], "Age_years": [10]})
predicted_price = model_multi.predict(new_house)[0]
print(f"\nPrediction for 1200 sqft, 3 rooms, 10 years old: ₹{predicted_price:,.0f}")


# ----------------------------
# Activity 3: Polynomial Regression
# ----------------------------
# Goal: Fit curved (non-linear) data using Polynomial Regression.
# Summary: Students will compare degree-1 (linear) vs degree-2 (polynomial)
#          fits on curved data and see how R² improves with the right degree.

# Task:
np.random.seed(99)
X_poly = np.linspace(-3, 3, 40).reshape(-1, 1)
y_poly = 2 * X_poly.flatten()**2 - 3 * X_poly.flatten() + 5 + np.random.randn(40) * 2

# Degree 1 (linear)
m1 = LinearRegression().fit(X_poly, y_poly)
y1 = m1.predict(X_poly)

# Degree 2 (polynomial)
poly = PolynomialFeatures(degree=2)
X_p2 = poly.fit_transform(X_poly)
m2 = LinearRegression().fit(X_p2, y_poly)
y2 = m2.predict(X_p2)

plt.figure(figsize=(10, 4))
plt.scatter(X_poly, y_poly, color="steelblue", s=50, label="Data", zorder=3)
plt.plot(X_poly, y1, color="orange",  linewidth=2, label=f"Degree 1 – R²={r2_score(y_poly,y1):.3f}")
plt.plot(X_poly, y2, color="red",     linewidth=2, label=f"Degree 2 – R²={r2_score(y_poly,y2):.3f}")
plt.title("Linear vs Polynomial Regression on Curved Data")
plt.xlabel("X"); plt.ylabel("y")
plt.legend(); plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

print(f"\nDegree 1 R²: {r2_score(y_poly,y1):.4f} (poor fit for curved data)")
print(f"Degree 2 R²: {r2_score(y_poly,y2):.4f} (much better fit!)")
