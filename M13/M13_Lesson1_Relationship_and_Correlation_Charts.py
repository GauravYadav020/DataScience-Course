# ============================================================
# M13 Lesson 1 – Relationship and Correlation Charts
# ============================================================
# Relationship charts help us understand how two or more variables
# are connected. Key chart types: Scatter Plot, Bubble Chart,
# and Correlation Heatmap using Matplotlib and Seaborn.
# ============================================================

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

sns.set_theme(style="whitegrid")
np.random.seed(42)


# ----------------------------
# Activity 1: Scatter Plot with Trend Line
# ----------------------------
# Goal: Visualize the relationship between two variables and add a trend line.
# Summary: Students will plot advertising spend vs sales revenue as a
#          scatter plot and overlay a linear trend line using np.polyfit().

# Task:
ad_spend = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
revenue  = np.array([15, 28, 35, 50, 58, 72, 80, 88, 95, 110]) + np.random.randn(10) * 3

plt.scatter(ad_spend, revenue, color="steelblue", s=100, edgecolors="black", label="Data Points")

# Trend line
m, b = np.polyfit(ad_spend, revenue, 1)
plt.plot(ad_spend, m * ad_spend + b, color="red", linestyle="--", label=f"Trend (y={m:.2f}x+{b:.2f})")

plt.title("Advertising Spend vs Revenue")
plt.xlabel("Ad Spend (₹ thousands)")
plt.ylabel("Revenue (₹ thousands)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()


# ----------------------------
# Activity 2: Bubble Chart
# ----------------------------
# Goal: Add a third dimension to a scatter plot using bubble size.
# Summary: Students will create a bubble chart where x = hours studied,
#          y = exam score, and bubble size = number of assignments done.

# Task:
students     = ["A", "B", "C", "D", "E", "F", "G", "H"]
hours        = [2, 4, 6, 3, 8, 5, 7, 1]
exam_score   = [45, 60, 80, 55, 92, 70, 85, 40]
assignments  = [5, 10, 18, 7, 20, 13, 17, 3]
bubble_size  = [a * 30 for a in assignments]

plt.scatter(hours, exam_score, s=bubble_size, alpha=0.6, color="darkorange", edgecolors="black")

for i, name in enumerate(students):
    plt.annotate(name, (hours[i], exam_score[i]), ha="center", va="center", fontsize=8, fontweight="bold")

plt.title("Bubble Chart – Study Hours vs Exam Score\n(Bubble size = Assignments Done)")
plt.xlabel("Study Hours per Day")
plt.ylabel("Exam Score")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()


# ----------------------------
# Activity 3: Correlation Heatmap
# ----------------------------
# Goal: Compute and visualize correlation between multiple numeric variables.
# Summary: Students will build a DataFrame with several features, compute
#          a correlation matrix, and display it as an annotated heatmap.

# Task:
df = pd.DataFrame({
    "StudyHours":   np.random.randint(1, 10, 60),
    "Attendance":   np.random.randint(55, 100, 60),
    "Assignments":  np.random.randint(5, 20, 60),
    "SleepHours":   np.random.randint(4, 9, 60),
    "ExamScore":    np.random.randint(40, 100, 60),
})

corr = df.corr()
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f",
            linewidths=0.5, square=True, cbar_kws={"shrink": 0.8})
plt.title("Correlation Heatmap – Student Performance Factors")
plt.tight_layout()
plt.show()
