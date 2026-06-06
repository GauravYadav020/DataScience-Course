# ============================================================
# M12 Lesson 3 – Visualization with Data Science III
# ============================================================
# Scatter Plots reveal relationships between two variables.
# Pie Charts show proportional distribution of a whole.
# This lesson also introduces subplots for multiple charts.
# ============================================================

import matplotlib.pyplot as plt
import numpy as np


# ----------------------------
# Activity 1: Scatter Plot
# ----------------------------
# Goal: Use a scatter plot to explore the relationship between two variables.
# Summary: Students will plot study hours vs exam scores to visually
#          identify if more study time leads to better scores.

# Task:
study_hours = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
exam_scores = [45, 50, 55, 62, 70, 75, 80, 85, 90, 95]

plt.scatter(study_hours, exam_scores, color="darkorange", s=100, edgecolors="black")
plt.title("Study Hours vs Exam Scores")
plt.xlabel("Study Hours per Day")
plt.ylabel("Exam Score")
plt.grid(True)
plt.tight_layout()
plt.show()


# ----------------------------
# Activity 2: Pie Chart
# ----------------------------
# Goal: Create a pie chart to show the proportional share of categories.
# Summary: Students will visualize market share data as a pie chart,
#          adding percentage labels, explode effect, and a legend.

# Task:
brands  = ["Samsung", "Apple", "Xiaomi", "OnePlus", "Others"]
shares  = [28, 25, 20, 12, 15]
explode = (0.05, 0.1, 0.05, 0.05, 0.05)   # Highlight Apple
colors  = ["steelblue", "silver", "tomato", "mediumseagreen", "gold"]

plt.pie(shares, labels=brands, explode=explode, colors=colors,
        autopct="%1.1f%%", startangle=140, shadow=True)
plt.title("Smartphone Market Share")
plt.tight_layout()
plt.show()


# ----------------------------
# Activity 3: Subplots – Multiple Charts in One Figure
# ----------------------------
# Goal: Display multiple charts together using plt.subplot().
# Summary: Students will combine a line chart, bar chart, scatter plot,
#          and pie chart into one figure using a 2x2 subplot grid.

# Task:
fig, axes = plt.subplots(2, 2, figsize=(10, 8))
fig.suptitle("M12 Dashboard – Multiple Charts", fontsize=14)

months  = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales   = [1200, 1500, 1100, 1800, 2000, 1700]
scores  = [45, 50, 55, 62, 70, 75]
hours   = [1, 2, 3, 4, 5, 6]

# Line chart
axes[0, 0].plot(months, sales, marker="o", color="steelblue")
axes[0, 0].set_title("Monthly Sales")

# Bar chart
axes[0, 1].bar(months, sales, color="salmon")
axes[0, 1].set_title("Sales Bar Chart")

# Scatter plot
axes[1, 0].scatter(hours, scores, color="darkorange", s=80)
axes[1, 0].set_title("Hours vs Scores")

# Pie chart
axes[1, 1].pie([28, 25, 20, 15, 12], labels=brands[:5], autopct="%1.0f%%")
axes[1, 1].set_title("Market Share")

plt.tight_layout()
plt.show()
