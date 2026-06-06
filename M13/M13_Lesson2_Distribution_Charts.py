# ============================================================
# M13 Lesson 2 – Distribution Charts
# ============================================================
# Distribution charts show how data values are spread across
# a range. Key types: Histogram, KDE Plot, Box Plot,
# Violin Plot, and ECDF (Empirical Cumulative Distribution).
# ============================================================

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

sns.set_theme(style="whitegrid")
np.random.seed(7)


# ----------------------------
# Activity 1: Histogram and KDE Plot
# ----------------------------
# Goal: Visualize data distribution using histogram and KDE overlay.
# Summary: Students will plot exam scores as a histogram and add a
#          KDE (Kernel Density Estimate) curve to see the smooth shape.

# Task:
scores = np.random.normal(loc=70, scale=12, size=200)

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Histogram only
axes[0].hist(scores, bins=20, color="steelblue", edgecolor="black", alpha=0.8)
axes[0].set_title("Histogram – Exam Scores")
axes[0].set_xlabel("Score")
axes[0].set_ylabel("Frequency")

# Histogram + KDE overlay using Seaborn
sns.histplot(scores, bins=20, kde=True, color="salmon", ax=axes[1])
axes[1].set_title("Histogram + KDE – Exam Scores")
axes[1].set_xlabel("Score")

plt.tight_layout()
plt.show()

# Comparing two groups with KDE
class_a = np.random.normal(72, 10, 150)
class_b = np.random.normal(65, 14, 150)

sns.kdeplot(class_a, label="Class A", shade=True, color="steelblue")
sns.kdeplot(class_b, label="Class B", shade=True, color="salmon")
plt.title("KDE Comparison – Class A vs Class B")
plt.xlabel("Score")
plt.legend()
plt.tight_layout()
plt.show()


# ----------------------------
# Activity 2: Box Plot and Violin Plot
# ----------------------------
# Goal: Compare distributions across multiple groups visually.
# Summary: Students will use box plots to identify median and outliers,
#          and violin plots to see the full distribution shape per group.

# Task:
df = pd.DataFrame({
    "Score": list(np.random.normal(72, 10, 50)) +
             list(np.random.normal(65, 14, 50)) +
             list(np.random.normal(78, 8, 50)),
    "Class": ["A"] * 50 + ["B"] * 50 + ["C"] * 50
})

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

sns.boxplot(data=df, x="Class", y="Score", palette="Set2", ax=axes[0])
axes[0].set_title("Box Plot – Score by Class")

sns.violinplot(data=df, x="Class", y="Score", palette="Set3",
               inner="quartile", ax=axes[1])
axes[1].set_title("Violin Plot – Score by Class")

plt.tight_layout()
plt.show()


# ----------------------------
# Activity 3: ECDF and Strip Plot
# ----------------------------
# Goal: Use ECDF to understand cumulative distribution and strip plot for raw spread.
# Summary: Students will plot an ECDF to find what percentage of students
#          scored below a value, and a strip plot to see all individual points.

# Task:
sns.ecdfplot(data=df, x="Score", hue="Class", palette="Set1")
plt.title("ECDF – Cumulative Score Distribution by Class")
plt.xlabel("Score")
plt.ylabel("Proportion")
plt.axvline(x=70, color="black", linestyle="--", label="Pass Mark (70)")
plt.legend()
plt.tight_layout()
plt.show()

sns.stripplot(data=df, x="Class", y="Score", palette="Set2",
              jitter=True, alpha=0.6, size=5)
plt.title("Strip Plot – Individual Scores by Class")
plt.tight_layout()
plt.show()
