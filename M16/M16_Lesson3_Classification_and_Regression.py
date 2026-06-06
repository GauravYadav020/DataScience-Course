# ============================================================
# M16 Lesson 3 – Classification and Regression
# ============================================================
# Supervised Learning has two main types:
# → Classification: predicts a CATEGORY  (e.g., Pass/Fail, Spam/Not Spam)
# → Regression:     predicts a NUMBER    (e.g., price, temperature, score)
# ============================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, mean_squared_error


# ----------------------------
# Activity 1: Classification vs Regression – Side by Side
# ----------------------------
# Goal: Clearly distinguish classification from regression with examples.
# Summary: Students will compare both problem types by examining datasets,
#          outputs, and algorithms suitable for each type.

# Task:
print("=" * 60)
print("   CLASSIFICATION vs REGRESSION – Key Differences")
print("=" * 60)

comparison = {
    "Output Type":    ("Category / Class",          "Continuous Number"),
    "Output Example": ("Spam / Not Spam",            "House Price = ₹45,00,000"),
    "Question asked": ("Which category does it fit?","How much / How many?"),
    "Algorithms":     ("Logistic Reg, Decision Tree","Linear Reg, Ridge, Lasso"),
    "Error Metric":   ("Accuracy, F1-Score",         "MSE, RMSE, R² Score"),
}

print(f"\n{'Aspect':<20} {'Classification':<30} {'Regression'}")
print("-" * 75)
for aspect, (cls_val, reg_val) in comparison.items():
    print(f"{aspect:<20} {cls_val:<30} {reg_val}")

print("\nReal-world examples:")
examples = [
    ("Email",         "Spam or Not Spam?",     "How many emails per day?"),
    ("Student",       "Pass or Fail?",          "What score will they get?"),
    ("House",         "Luxury or Budget?",      "What is the price?"),
    ("Weather",       "Rain or No Rain?",       "How many mm of rainfall?"),
    ("Medical",       "Diabetic or Healthy?",   "What is blood sugar level?"),
]
print(f"\n{'Domain':<15} {'Classification':<30} {'Regression'}")
print("-" * 70)
for domain, cls_ex, reg_ex in examples:
    print(f"{domain:<15} {cls_ex:<30} {reg_ex}")


# ----------------------------
# Activity 2: Simple Regression Model
# ----------------------------
# Goal: Build and visualize a basic Linear Regression model.
# Summary: Students will predict exam scores from study hours using
#          LinearRegression, visualize the fit, and make predictions.

# Task:
np.random.seed(10)
study_hours = np.array([1,2,3,4,5,6,7,8,9,10]).reshape(-1, 1)
exam_scores = np.array([40,50,55,65,70,75,82,88,92,97]) + np.random.randn(10) * 2

model_reg = LinearRegression()
model_reg.fit(study_hours, exam_scores)

y_pred_reg = model_reg.predict(study_hours)
predict_7h = model_reg.predict([[7]])[0]

print(f"\n--- Linear Regression Results ---")
print(f"Slope (m)     : {model_reg.coef_[0]:.2f}")
print(f"Intercept (b) : {model_reg.intercept_:.2f}")
print(f"Equation      : Score = {model_reg.coef_[0]:.2f} × Hours + {model_reg.intercept_:.2f}")
print(f"Prediction    : 7 hours of study → Score = {predict_7h:.1f}")

plt.figure(figsize=(7, 4))
plt.scatter(study_hours, exam_scores, color="steelblue", s=80, label="Actual Data", zorder=3)
plt.plot(study_hours, y_pred_reg, color="red", linewidth=2, label="Regression Line")
plt.title("Linear Regression – Study Hours vs Exam Score")
plt.xlabel("Study Hours")
plt.ylabel("Exam Score")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()


# ----------------------------
# Activity 3: Simple Classification Model
# ----------------------------
# Goal: Build a Logistic Regression model to classify Pass or Fail.
# Summary: Students will train a Logistic Regression on study hours
#          and attendance, predict outcomes, and check accuracy.

# Task:
np.random.seed(7)
data = pd.DataFrame({
    "StudyHours": [1,2,2,3,4,5,5,6,7,8,8,9,3,4,6],
    "Attendance": [50,55,60,65,70,75,80,85,88,90,92,95,58,72,78],
    "Passed":     [0,0,0,0,1,1,1,1,1,1,1,1,0,1,1],
})

X = data[["StudyHours", "Attendance"]]
y = data["Passed"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model_cls = LogisticRegression()
model_cls.fit(X_train, y_train)

y_pred_cls = model_cls.predict(X_test)
acc = accuracy_score(y_test, y_pred_cls)

print(f"\n--- Logistic Regression (Classification) Results ---")
print(f"Accuracy: {acc * 100:.1f}%")
print(f"\nPredictions vs Actual:")
for pred, actual in zip(y_pred_cls, y_test):
    status = "✓" if pred == actual else "✗"
    print(f"  Predicted: {'Pass' if pred==1 else 'Fail'}  |  Actual: {'Pass' if actual==1 else 'Fail'}  {status}")

# New prediction
new_student = [[5, 76]]
result = model_cls.predict(new_student)[0]
print(f"\nNew Student (5 hrs, 76% attendance): {'PASS ✓' if result == 1 else 'FAIL ✗'}")
