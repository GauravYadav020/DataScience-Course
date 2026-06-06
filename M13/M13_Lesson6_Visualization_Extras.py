# ============================================================
# M13 Lesson 6 – Visualization Extras
# ============================================================
# This lesson covers advanced and interactive visualizations:
# Word Cloud, Plotly interactive charts, Pair Grid, FacetGrid,
# and combining everything into a polished multi-chart figure.
# ============================================================

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

sns.set_theme(style="whitegrid")
np.random.seed(55)


# ----------------------------
# Activity 1: Seaborn FacetGrid and PairGrid
# ----------------------------
# Goal: Create small-multiple charts for each category using FacetGrid.
# Summary: Students will use FacetGrid to plot separate histograms for
#          each department, and PairGrid to show custom pair-wise plots.

# Task:
df = pd.DataFrame({
    "Score":      list(np.random.normal(72, 10, 50)) +
                  list(np.random.normal(65, 12, 50)) +
                  list(np.random.normal(80, 8,  50)),
    "StudyHours": list(np.random.randint(2, 9, 50)) +
                  list(np.random.randint(1, 7, 50)) +
                  list(np.random.randint(4, 10, 50)),
    "Class":      ["A"] * 50 + ["B"] * 50 + ["C"] * 50
})

# FacetGrid – separate histogram per class
g = sns.FacetGrid(df, col="Class", palette="Set2", height=4)
g.map(sns.histplot, "Score", bins=12, kde=True)
g.set_titles("Class {col_name}")
g.figure.suptitle("Score Distribution per Class – FacetGrid", y=1.03)
plt.tight_layout()
plt.show()

# PairGrid
g2 = sns.PairGrid(df, hue="Class", palette="Set1")
g2.map_upper(sns.scatterplot, alpha=0.5)
g2.map_lower(sns.kdeplot)
g2.map_diag(sns.histplot, kde=True)
g2.add_legend()
g2.figure.suptitle("PairGrid – Score vs StudyHours by Class", y=1.02)
plt.tight_layout()
plt.show()


# ----------------------------
# Activity 2: Annotated Heatmap and Diverging Color Map
# ----------------------------
# Goal: Build a richly annotated heatmap with diverging colors for contrast.
# Summary: Students will create a monthly performance heatmap using a
#          pivot table and apply a diverging colormap to highlight highs and lows.

# Task:
months  = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
regions = ["North", "South", "East", "West"]

sales_data = pd.DataFrame(
    np.random.randint(40, 100, (4, 12)),
    index=regions,
    columns=months
)

fig, ax = plt.subplots(figsize=(14, 4))
sns.heatmap(
    sales_data, annot=True, fmt="d",
    cmap="RdYlGn",           # Diverging: Red = low, Green = high
    linewidths=0.5,
    linecolor="white",
    cbar_kws={"label": "Sales Score"},
    ax=ax
)
ax.set_title("Monthly Sales Performance by Region – Annotated Heatmap", fontsize=14)
ax.set_xlabel("Month")
ax.set_ylabel("Region")
plt.tight_layout()
plt.show()


# ----------------------------
# Activity 3: Final Polished Multi-Chart Dashboard
# ----------------------------
# Goal: Combine multiple chart types into a single publication-ready figure.
# Summary: Students will arrange 4 different chart types in a grid using
#          GridSpec for flexible layout, creating a complete analytics dashboard.

# Task:
import matplotlib.gridspec as gridspec

fig = plt.figure(figsize=(16, 10))
fig.suptitle("M13 Final Dashboard – Data Science Visualization",
             fontsize=16, fontweight="bold", y=1.01)

gs = gridspec.GridSpec(2, 3, figure=fig, hspace=0.45, wspace=0.35)

ax1 = fig.add_subplot(gs[0, :2])   # Wide top-left
ax2 = fig.add_subplot(gs[0, 2])    # Top-right
ax3 = fig.add_subplot(gs[1, 0])    # Bottom-left
ax4 = fig.add_subplot(gs[1, 1])    # Bottom-middle
ax5 = fig.add_subplot(gs[1, 2])    # Bottom-right

# 1. Time series (wide)
dates  = pd.date_range("2024-01-01", periods=90, freq="D")
values = np.cumsum(np.random.randn(90)) + 50
ax1.plot(dates, values, color="steelblue", linewidth=1.5)
ax1.fill_between(dates, values, alpha=0.15, color="steelblue")
ax1.set_title("90-Day Sales Trend")
ax1.tick_params(axis="x", rotation=30)

# 2. Pie chart
ax2.pie([35, 25, 20, 20], labels=regions,
        autopct="%1.0f%%", colors=sns.color_palette("Set2"))
ax2.set_title("Regional Share")

# 3. Bar chart
ax3.bar(["Q1","Q2","Q3","Q4"], [82000,91000,78000,105000],
        color=sns.color_palette("Set1", 4))
ax3.set_title("Quarterly Revenue")
ax3.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"₹{x/1000:.0f}K"))

# 4. Box plot
sns.boxplot(data=df, x="Class", y="Score", palette="Set3", ax=ax4)
ax4.set_title("Score Distribution")

# 5. Scatter plot
ax5.scatter(df["StudyHours"], df["Score"],
            c=df["Class"].map({"A": "steelblue", "B": "salmon", "C": "green"}),
            alpha=0.5, s=40)
ax5.set_title("Hours vs Score")
ax5.set_xlabel("Study Hours")
ax5.set_ylabel("Score")

plt.tight_layout()
plt.show()
