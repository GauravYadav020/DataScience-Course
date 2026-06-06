# ============================================================
# M13 Lesson 5 – Customizing Visualizations
# ============================================================
# Customization makes charts more professional and readable.
# This lesson covers: themes, color palettes, figure size,
# annotations, legends, tick formatting, and saving figures.
# ============================================================

import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
import pandas as pd
import numpy as np

np.random.seed(33)


# ----------------------------
# Activity 1: Themes, Styles, and Color Palettes
# ----------------------------
# Goal: Apply different visual themes and color palettes to charts.
# Summary: Students will compare Matplotlib styles and Seaborn themes,
#          and use custom color palettes to improve chart aesthetics.

# Task:
categories = ["Electronics", "Clothing", "Food", "Books", "Toys"]
values     = [85000, 42000, 31000, 18000, 25000]

# Compare three different Matplotlib styles
styles = ["default", "seaborn-v0_8-darkgrid", "ggplot"]
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

for ax, style in zip(axes, styles):
    with plt.style.context(style):
        ax.bar(categories, values, color=sns.color_palette("Set2", 5))
        ax.set_title(f"Style: {style}", fontsize=9)
        ax.tick_params(axis="x", rotation=30)

plt.suptitle("Same Data – Three Different Styles", fontsize=13)
plt.tight_layout()
plt.show()

# Seaborn color palette showcase
palettes = ["Set1", "pastel", "coolwarm", "husl"]
fig, axes = plt.subplots(1, 4, figsize=(16, 4))

for ax, pal in zip(axes, palettes):
    colors = sns.color_palette(pal, 5)
    sns.barplot(x=categories, y=values, palette=pal, ax=ax)
    ax.set_title(f"Palette: {pal}", fontsize=9)
    ax.tick_params(axis="x", rotation=30)

plt.suptitle("Seaborn Color Palettes", fontsize=13)
plt.tight_layout()
plt.show()


# ----------------------------
# Activity 2: Annotations, Tick Formatting, and Legends
# ----------------------------
# Goal: Add data labels, custom tick formatting, and a styled legend.
# Summary: Students will annotate bars with values, format Y-axis as
#          currency, and customize the legend position and style.

# Task:
months  = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
revenue = [45000, 62000, 53000, 78000, 91000, 84000]
target  = [60000, 60000, 65000, 70000, 75000, 80000]

fig, ax = plt.subplots(figsize=(10, 5))

bars = ax.bar(months, revenue, color="steelblue", label="Actual Revenue", alpha=0.85)
ax.plot(months, target, "r--o", linewidth=2, label="Target", markersize=7)

# Add value labels on each bar
for bar in bars:
    height = bar.get_height()
    ax.annotate(f"₹{height/1000:.0f}K",
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 5), textcoords="offset points",
                ha="center", fontsize=9, fontweight="bold")

# Format Y-axis as currency
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"₹{x/1000:.0f}K"))

# Styled legend
ax.legend(loc="upper left", frameon=True, shadow=True,
          fancybox=True, framealpha=0.9, fontsize=10)

ax.set_title("Monthly Revenue vs Target", fontsize=14, fontweight="bold")
ax.set_xlabel("Month")
ax.set_ylabel("Revenue")
ax.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.show()


# ----------------------------
# Activity 3: Figure Size, Fonts, and Saving the Chart
# ----------------------------
# Goal: Control figure dimensions, font sizes, and export charts as files.
# Summary: Students will set custom figure sizes, use rcParams to change
#          global font settings, and save the final chart as a PNG and PDF.

# Task:
plt.rcParams.update({
    "figure.figsize":   (10, 5),
    "font.size":        12,
    "axes.titlesize":   15,
    "axes.labelsize":   12,
    "xtick.labelsize":  10,
    "ytick.labelsize":  10,
    "font.family":      "sans-serif",
})

fig, ax = plt.subplots()
ax.plot(months, revenue, marker="o", color="steelblue", linewidth=2.5, markersize=9)
ax.fill_between(months, revenue, alpha=0.15, color="steelblue")
ax.set_title("Monthly Revenue – Custom Font & Style")
ax.set_xlabel("Month")
ax.set_ylabel("Revenue (₹)")
ax.grid(True, alpha=0.3)
plt.tight_layout()

# Save chart
plt.savefig("revenue_chart.png", dpi=150, bbox_inches="tight")
plt.savefig("revenue_chart.pdf", bbox_inches="tight")
print("Charts saved as revenue_chart.png and revenue_chart.pdf")
plt.show()

# Reset rcParams to default after done
plt.rcParams.update(plt.rcParamsDefault)
