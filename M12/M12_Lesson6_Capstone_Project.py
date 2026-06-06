# ============================================================
# M12 Lesson 6 – Capstone Project
# ============================================================
# This capstone combines all M12 visualization skills to build
# a complete Data Science dashboard. You will analyze a retail
# sales dataset and present insights using multiple chart types.
# ============================================================

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

sns.set_theme(style="whitegrid")
np.random.seed(42)


# ----------------------------
# Activity 1: Build the Dataset and Explore It
# ----------------------------
# Goal: Create a structured sales dataset and perform basic exploration.
# Summary: Students will build a realistic retail DataFrame with multiple
#          columns and use .describe(), .info(), and basic plots to explore it.

# Task:
months     = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
categories = ["Electronics", "Clothing", "Food", "Books"]

data = {
    "Month":    months * 4,
    "Category": ["Electronics"] * 12 + ["Clothing"] * 12 + ["Food"] * 12 + ["Books"] * 12,
    "Sales":    list(np.random.randint(40000, 100000, 12)) +
                list(np.random.randint(20000, 60000,  12)) +
                list(np.random.randint(15000, 40000,  12)) +
                list(np.random.randint(8000,  25000,  12)),
    "Units":    list(np.random.randint(100, 500, 48)),
    "Returns":  list(np.random.randint(5, 50, 48)),
}
df = pd.DataFrame(data)
df["Month_Num"] = df["Month"].apply(lambda m: months.index(m) + 1)
df["Profit"]    = df["Sales"] * np.random.uniform(0.15, 0.35, 48)

print("Dataset Overview:")
print(df.describe())
print("\nFirst 5 rows:")
print(df.head())

# Bar chart: Total Sales per Category
category_sales = df.groupby("Category")["Sales"].sum().reset_index()
sns.barplot(data=category_sales, x="Category", y="Sales", palette="Set2")
plt.title("Total Annual Sales by Category")
plt.tight_layout()
plt.show()


# ----------------------------
# Activity 2: Trend and Distribution Analysis
# ----------------------------
# Goal: Visualize monthly sales trends and distribution of profits.
# Summary: Students will create a multi-line trend chart for all
#          categories and a histogram + box plot for profit distribution.

# Task:

# Multi-line trend chart
plt.figure(figsize=(12, 5))
for cat in categories:
    cat_df = df[df["Category"] == cat].sort_values("Month_Num")
    plt.plot(cat_df["Month"], cat_df["Sales"], marker="o", label=cat)
plt.title("Monthly Sales Trend by Category")
plt.xlabel("Month")
plt.ylabel("Sales (₹)")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Profit distribution
fig, axes = plt.subplots(1, 2, figsize=(12, 4))
axes[0].hist(df["Profit"], bins=15, color="steelblue", edgecolor="black")
axes[0].set_title("Profit Distribution (Histogram)")
axes[0].set_xlabel("Profit (₹)")

sns.boxplot(data=df, x="Category", y="Profit", palette="Set3", ax=axes[1])
axes[1].set_title("Profit by Category (Box Plot)")
plt.tight_layout()
plt.show()


# ----------------------------
# Activity 3: Final Dashboard with Insights
# ----------------------------
# Goal: Combine all charts into a single dashboard and annotate key insights.
# Summary: Students will create a 2x2 dashboard figure and add text
#          annotations to present final business insights from the data.

# Task:
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("M12 Capstone – Retail Sales Dashboard", fontsize=16, fontweight="bold")

# 1. Total Sales by Category (Bar)
sns.barplot(data=category_sales, x="Category", y="Sales", palette="Set2", ax=axes[0, 0])
axes[0, 0].set_title("Total Sales by Category")

# 2. Monthly Trend (Line)
for cat in categories:
    cat_df = df[df["Category"] == cat].sort_values("Month_Num")
    axes[0, 1].plot(cat_df["Month"], cat_df["Sales"], marker="o", label=cat)
axes[0, 1].set_title("Monthly Sales Trend")
axes[0, 1].legend(fontsize=7)
axes[0, 1].tick_params(axis="x", rotation=45)

# 3. Heatmap: Category vs Month
pivot = df.pivot_table(values="Sales", index="Category", columns="Month_Num", aggfunc="mean")
sns.heatmap(pivot, cmap="YlOrRd", annot=False, ax=axes[1, 0])
axes[1, 0].set_title("Sales Heatmap (Category vs Month)")

# 4. Pie chart: Sales share
axes[1, 1].pie(category_sales["Sales"], labels=category_sales["Category"],
               autopct="%1.1f%%", colors=sns.color_palette("Set2"))
axes[1, 1].set_title("Sales Share by Category")

plt.tight_layout()
plt.show()

# Final Insights (print as text)
best_cat = category_sales.loc[category_sales["Sales"].idxmax(), "Category"]
print("\n========== CAPSTONE INSIGHTS ==========")
print(f"Insight 1: Best performing category is '{best_cat}'")
print(f"Insight 2: Average monthly profit across all categories = ₹{df['Profit'].mean():,.0f}")
print(f"Insight 3: Highest single-month sales = ₹{df['Sales'].max():,}")
print("Recommendation: Focus marketing budget on Electronics in Q4.")
print("=========================================")
