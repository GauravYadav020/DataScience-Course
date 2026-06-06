# ============================================================
# M16 Lesson 5 – Gradient Descent and Accuracy Metrics
# ============================================================
# Gradient Descent is the optimization algorithm that trains ML
# models by minimizing error step by step. Accuracy Metrics
# tell us how well the model is performing on unseen data.
# ============================================================

import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import (mean_squared_error, mean_absolute_error,
                              r2_score, accuracy_score, confusion_matrix,
                              classification_report)


# ----------------------------
# Activity 1: Gradient Descent – Step by Step
# ----------------------------
# Goal: Understand how gradient descent minimizes error to find best parameters.
# Summary: Students will implement gradient descent from scratch on a
#          simple dataset and visualize how the cost decreases each iteration.

# Task:
np.random.seed(42)
X = np.array([1,2,3,4,5,6,7,8,9,10], dtype=float)
y = np.array([2.5, 4.1, 5.8, 7.2, 9.5, 10.8, 13.1, 14.9, 16.2, 18.5])

# Gradient Descent from scratch
m, b         = 0.0, 0.0      # Start: slope = 0, intercept = 0
learning_rate = 0.01
n_iterations  = 500
n             = len(X)
cost_history  = []

for i in range(n_iterations):
    y_pred  = m * X + b
    error   = y_pred - y
    cost    = np.mean(error ** 2)          # MSE cost
    dm      = (2 / n) * np.dot(error, X)  # Gradient w.r.t. m
    db      = (2 / n) * np.sum(error)     # Gradient w.r.t. b
    m      -= learning_rate * dm          # Update slope
    b      -= learning_rate * db          # Update intercept
    cost_history.append(cost)

print("=" * 55)
print("  GRADIENT DESCENT – FROM SCRATCH")
print("=" * 55)
print(f"Final Slope (m)    : {m:.4f}")
print(f"Final Intercept (b): {b:.4f}")
print(f"Final Cost (MSE)   : {cost_history[-1]:.4f}")
print(f"Cost reduced from {cost_history[0]:.2f} → {cost_history[-1]:.4f} in {n_iterations} steps")

# Visualize cost curve
fig, axes = plt.subplots(1, 2, figsize=(12, 4))
axes[0].plot(cost_history, color="red", linewidth=2)
axes[0].set_title("Gradient Descent – Cost vs Iterations")
axes[0].set_xlabel("Iteration")
axes[0].set_ylabel("MSE Cost")
axes[0].grid(True, alpha=0.3)

axes[1].scatter(X, y, color="steelblue", s=70, zorder=3, label="Data")
axes[1].plot(X, m*X+b, color="red", linewidth=2, label=f"Learned: y={m:.2f}x+{b:.2f}")
axes[1].set_title("Data + Learned Regression Line")
axes[1].set_xlabel("X"); axes[1].set_ylabel("y")
axes[1].legend(); axes[1].grid(True, alpha=0.3)
plt.tight_layout()
plt.show()


# ----------------------------
# Activity 2: Regression Accuracy Metrics
# ----------------------------
# Goal: Compute and interpret MAE, MSE, RMSE, and R² for regression models.
# Summary: Students will use sklearn metrics on actual vs predicted values
#          and understand what each metric tells about the model quality.

# Task:
y_actual    = np.array([50, 62, 78, 45, 90, 55, 83, 70, 61, 88])
y_predicted = np.array([48, 65, 75, 50, 88, 58, 80, 72, 63, 85])

mae  = mean_absolute_error(y_actual, y_predicted)
mse  = mean_squared_error(y_actual, y_predicted)
rmse = np.sqrt(mse)
r2   = r2_score(y_actual, y_predicted)

print("\n--- REGRESSION METRICS ---")
print(f"MAE  (Mean Absolute Error)  : {mae:.4f}")
print(f"     → On average, prediction is off by {mae:.2f} units")
print(f"MSE  (Mean Squared Error)   : {mse:.4f}")
print(f"     → Penalizes large errors more heavily")
print(f"RMSE (Root MSE)             : {rmse:.4f}")
print(f"     → Same unit as target variable; avg error = {rmse:.2f}")
print(f"R²   (R-Squared Score)      : {r2:.4f}")
print(f"     → Model explains {r2*100:.1f}% of the variance in data")
print(f"     → R²=1.0 is perfect; R²=0 means model predicts mean only")


# ----------------------------
# Activity 3: Classification Metrics
# ----------------------------
# Goal: Evaluate classification models using accuracy, confusion matrix, and F1.
# Summary: Students will examine a confusion matrix, understand True/False
#          Positives and Negatives, and compute Precision, Recall, and F1-Score.

# Task:
y_true = np.array([1,0,1,1,0,1,0,0,1,1,0,1,0,0,1])
y_pred = np.array([1,0,1,0,0,1,1,0,1,1,0,0,0,1,1])

acc = accuracy_score(y_true, y_pred)
cm  = confusion_matrix(y_true, y_pred)

print("\n--- CLASSIFICATION METRICS ---")
print(f"Accuracy : {acc * 100:.1f}%")
print(f"\nConfusion Matrix:")
print(f"                 Predicted 0   Predicted 1")
print(f"Actual 0  (TN/FP):   {cm[0,0]}             {cm[0,1]}")
print(f"Actual 1  (FN/TP):   {cm[1,0]}             {cm[1,1]}")
print(f"\nTP={cm[1,1]} TN={cm[0,0]} FP={cm[0,1]} FN={cm[1,0]}")
print(f"\nClassification Report:")
print(classification_report(y_true, y_pred, target_names=["Fail","Pass"]))

# Visualize confusion matrix
fig, ax = plt.subplots(figsize=(5, 4))
im = ax.imshow(cm, cmap="Blues")
ax.set_xticks([0,1]); ax.set_yticks([0,1])
ax.set_xticklabels(["Predicted Fail","Predicted Pass"])
ax.set_yticklabels(["Actual Fail","Actual Pass"])
for i in range(2):
    for j in range(2):
        ax.text(j, i, cm[i,j], ha="center", va="center", fontsize=16, fontweight="bold",
                color="white" if cm[i,j] > cm.max()/2 else "black")
ax.set_title("Confusion Matrix")
plt.colorbar(im)
plt.tight_layout()
plt.show()
