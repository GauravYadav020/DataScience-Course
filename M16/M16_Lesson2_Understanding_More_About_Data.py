# ============================================================
# M16 Lesson 2 – Understanding More About Data
# ============================================================
# Good ML models start with good data. This lesson covers:
# types of data (numerical/categorical), features vs labels,
# data preprocessing — handling missing values, encoding,
# scaling — and train/test splitting.
# ============================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, MinMaxScaler, StandardScaler


# ----------------------------
# Activity 1: Features, Labels, and Data Types
# ----------------------------
# Goal: Identify features (inputs) and labels (outputs) in a dataset.
# Summary: Students will build a sample student dataset and correctly
#          identify numerical vs categorical columns, features vs labels.

# Task:
df = pd.DataFrame({
    "Name":       ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace", "Hank"],
    "Age":        [14, 15, 14, 16, 15, 14, 16, 15],
    "StudyHours": [5, 3, 7, 2, 6, 4, 8, 1],
    "Attendance": [90, 70, 95, 60, 88, 75, 98, 55],
    "Grade":      ["A", "C", "A", "F", "B", "B", "A", "F"],
    "Passed":     [1, 1, 1, 0, 1, 1, 1, 0],
})

print("Sample Dataset:")
print(df.to_string(index=False))

print("\n--- Data Types ---")
print(df.dtypes)

print("\n--- Features (Inputs) ---")
print("Numerical : Age, StudyHours, Attendance")
print("Categorical: Name, Grade")

print("\n--- Label (Output / Target) ---")
print("'Passed' column → 1 = Passed, 0 = Failed")

print("\n--- Basic Statistics ---")
print(df.describe())


# ----------------------------
# Activity 2: Data Cleaning – Missing Values and Encoding
# ----------------------------
# Goal: Handle missing values and encode categorical data for ML use.
# Summary: Students will introduce missing values in the dataset, use
#          fillna() to handle them, and encode Grade using LabelEncoder.

# Task:
df_messy = df.copy()
df_messy.loc[2, "StudyHours"] = np.nan
df_messy.loc[5, "Attendance"] = np.nan

print("\nDataset with Missing Values:")
print(df_messy[["Name", "StudyHours", "Attendance"]].to_string(index=False))
print(f"\nMissing values:\n{df_messy.isnull().sum()}")

# Fill missing values with column mean
df_messy["StudyHours"].fillna(df_messy["StudyHours"].mean(), inplace=True)
df_messy["Attendance"].fillna(df_messy["Attendance"].mean(), inplace=True)

print("\nAfter filling missing values:")
print(f"Missing values:\n{df_messy.isnull().sum()}")

# Encode categorical Grade column
le = LabelEncoder()
df["Grade_Encoded"] = le.fit_transform(df["Grade"])
print("\nGrade Encoding:")
for original, encoded in zip(le.classes_, range(len(le.classes_))):
    print(f"   {original} → {encoded}")
print(df[["Grade", "Grade_Encoded"]])


# ----------------------------
# Activity 3: Feature Scaling and Train/Test Split
# ----------------------------
# Goal: Scale features to a common range and split data for training/testing.
# Summary: Students will apply MinMaxScaler and StandardScaler to features,
#          then split the dataset into 80% training and 20% testing sets.

# Task:
features = df[["StudyHours", "Attendance"]].values
label    = df["Passed"].values

# MinMax Scaling (0 to 1)
scaler_mm = MinMaxScaler()
features_minmax = scaler_mm.fit_transform(features)

# Standard Scaling (mean=0, std=1)
scaler_std = StandardScaler()
features_std = scaler_std.fit_transform(features)

print("\n--- Feature Scaling Comparison ---")
print(f"{'Original':<20} {'MinMax':<20} {'Standard'}")
for orig, mm, std in zip(features, features_minmax, features_std):
    print(f"{str(orig):<20} {str(mm.round(2)):<20} {str(std.round(2))}")

# Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(
    features_minmax, label, test_size=0.2, random_state=42
)
print(f"\nTotal samples   : {len(features)}")
print(f"Training samples: {len(X_train)}  (80%)")
print(f"Testing samples : {len(X_test)}   (20%)")
