# ============================================================
# M12 Lesson 5 – Visualization with Data Science V
# ============================================================
# This lesson covers advanced visualizations: pair plots, joint plots,
# time series line charts, and annotating charts with text and arrows
# to communicate insights directly on the visualization.
# ============================================================

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# ----------------------------
# Activity 1: Pair Plot and Joint Plot
# ----------------------------
# Goal: Explore relationships across multiple variables simultaneously.
# Summary: Students will use sns.pairplot() to see all variable pairs
#          and sns.jointplot() for a detailed view of two variables.

# Task:
np.random.seed(7)
df = pd.DataFrame({
    "StudyHours":  np.random.randint(1, 10, 80),
    "Attendance":  np.random.randint(60, 100, 80),
    "ExamScore":   np.random.randint(40, 100, 80),
    "Class":       np.random.choice(["A", "B"], 80)
})

sns.pairplot(df, hue="Class", palette="Set1")
plt.suptitle("Pair Plot – Student Performance", y=1.02)
plt.tight_layout()
plt.show()

sns.jointplot(data=df, x="StudyHours", y="ExamScore", kind="scatter",
              marginal_kws=dict(bins=10), color="steelblue")
plt.suptitle("Study Hours vs Exam Score", y=1.02)
plt.tight_layout()
plt.show()


# ----------------------------
# Activity 2: Time Series Visualization
# ----------------------------
# Goal: Plot and analyze a time series dataset using line charts.
# Summary: Students will create a date-indexed DataFrame and visualize
#          trends over time with rolling averages for smoothing.

# Task:
dates  = pd.date_range(start="2024-01-01", periods=90, freq="D")
values = np.cumsum(np.random.randn(90)) + 100    # Simulated stock price

ts_df = pd.DataFrame({"Date": dates, "Price": values})
ts_df["7-Day MA"] = ts_df["Price"].rolling(window=7).mean()

plt.figure(figsize=(12, 5))
plt.plot(ts_df["Date"], ts_df["Price"],    alpha=0.5, label="Daily Price", color="steelblue")
plt.plot(ts_df["Date"], ts_df["7-Day MA"], linewidth=2, label="7-Day Moving Avg", color="red")
plt.title("Simulated Stock Price – Jan to Mar 2024")
plt.xlabel("Date")
plt.ylabel("Price (₹)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()


# ----------------------------
# Activity 3: Annotating Charts
# ----------------------------
# Goal: Add text annotations and arrows to highlight key data points.
# Summary: Students will use plt.annotate() and plt.text() to mark
#          important events or peaks directly on a visualization.

# Task:
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales  = [1200, 1500, 1100, 2500, 2000, 1700]

plt.plot(months, sales, marker="o", color="steelblue", linewidth=2)
plt.title("Monthly Sales with Annotations")
plt.xlabel("Month")
plt.ylabel("Sales (₹)")

# Annotate the peak
max_idx = sales.index(max(sales))
plt.annotate(
    f"Peak: ₹{max(sales)}",
    xy=(months[max_idx], max(sales)),
    xytext=(months[max_idx - 1], max(sales) - 300),
    arrowprops=dict(arrowstyle="->", color="red"),
    fontsize=10, color="red"
)

# Annotate the dip
min_idx = sales.index(min(sales))
plt.annotate(
    f"Dip: ₹{min(sales)}",
    xy=(months[min_idx], min(sales)),
    xytext=(months[min_idx + 1], min(sales) + 200),
    arrowprops=dict(arrowstyle="->", color="orange"),
    fontsize=10, color="orange"
)

plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
