# ============================================================
# M12 Lesson 2 – Visualization with Data Science II
# ============================================================
# Bar Charts and Histograms are used to compare categories and
# understand the distribution of data. This lesson covers
# vertical/horizontal bar charts and histogram creation.
# ============================================================

import matplotlib.pyplot as plt
import numpy as np


# ----------------------------
# Activity 1: Bar Chart
# ----------------------------
# Goal: Create a vertical bar chart to compare categorical data.
# Summary: Students will build a bar chart showing sales by product
#          category and customize bar colors and labels.

# Task:
categories = ["Electronics", "Clothing", "Food", "Books", "Toys"]
revenue    = [85000, 42000, 31000, 18000, 25000]
colors     = ["steelblue", "salmon", "mediumseagreen", "gold", "mediumpurple"]

plt.bar(categories, revenue, color=colors, edgecolor="black")
plt.title("Revenue by Product Category")
plt.xlabel("Category")
plt.ylabel("Revenue (₹)")
plt.tight_layout()
plt.show()


# ----------------------------
# Activity 2: Horizontal Bar Chart and Grouped Bar Chart
# ----------------------------
# Goal: Compare data using horizontal bars and grouped bar charts.
# Summary: Students will create a horizontal bar chart for readability
#          and a grouped bar chart to compare two series side by side.

# Task:
# Horizontal Bar Chart
plt.barh(categories, revenue, color=colors)
plt.title("Revenue by Category (Horizontal)")
plt.xlabel("Revenue (₹)")
plt.tight_layout()
plt.show()

# Grouped Bar Chart
q1 = [85000, 42000, 31000, 18000, 25000]
q2 = [92000, 38000, 35000, 21000, 29000]
x  = np.arange(len(categories))

plt.bar(x - 0.2, q1, width=0.4, label="Q1", color="steelblue")
plt.bar(x + 0.2, q2, width=0.4, label="Q2", color="salmon")
plt.xticks(x, categories)
plt.title("Q1 vs Q2 Revenue by Category")
plt.xlabel("Category")
plt.ylabel("Revenue (₹)")
plt.legend()
plt.tight_layout()
plt.show()


# ----------------------------
# Activity 3: Histogram
# ----------------------------
# Goal: Visualize the frequency distribution of a dataset using a histogram.
# Summary: Students will generate sample score data and use a histogram
#          to understand how scores are distributed across ranges.

# Task:
np.random.seed(42)
scores = np.random.randint(40, 100, size=100)

plt.hist(scores, bins=10, color="steelblue", edgecolor="black")
plt.title("Distribution of Student Scores")
plt.xlabel("Score Range")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.show()

# Overlay two histograms:
class_a = np.random.randint(50, 100, size=50)
class_b = np.random.randint(40, 90,  size=50)

plt.hist(class_a, bins=10, alpha=0.6, color="blue",  label="Class A")
plt.hist(class_b, bins=10, alpha=0.6, color="orange", label="Class B")
plt.title("Score Distribution: Class A vs Class B")
plt.xlabel("Score")
plt.ylabel("Frequency")
plt.legend()
plt.tight_layout()
plt.show()
