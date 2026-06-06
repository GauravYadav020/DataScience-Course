# ============================================================
# M12 Lesson 1 – Visualization with Data Science I
# ============================================================
# Data Visualization turns raw data into visual graphics like
# charts and graphs. We use Matplotlib — Python's most popular
# plotting library — to create and customize basic plots.
# ============================================================

import matplotlib.pyplot as plt


# ----------------------------
# Activity 1: Your First Line Plot
# ----------------------------
# Goal: Learn how to create a basic line plot using Matplotlib.
# Summary: Students will plot a simple dataset on a line chart,
#          add a title, axis labels, and display the chart.

# Task:
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales  = [1200, 1500, 1100, 1800, 2000, 1700]

plt.plot(months, sales)
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales (₹)")
plt.show()


# ----------------------------
# Activity 2: Customize the Line Plot
# ----------------------------
# Goal: Improve the line plot with colors, markers, and line styles.
# Summary: Students will customize their line chart by changing the
#          color, adding markers at data points, and adjusting line style.

# Task:
plt.plot(months, sales, color="blue", marker="o", linestyle="--", linewidth=2, markersize=8)
plt.title("Monthly Sales (Styled)")
plt.xlabel("Month")
plt.ylabel("Sales (₹)")
plt.grid(True)
plt.tight_layout()
plt.show()


# ----------------------------
# Activity 3: Plot Multiple Lines
# ----------------------------
# Goal: Display two data series on the same chart using a legend.
# Summary: Students will add a second data series (Target Sales) to the
#          chart and use plt.legend() to label both lines clearly.

# Task:
target = [1400, 1400, 1400, 1600, 1600, 1800]

plt.plot(months, sales,  color="blue",  marker="o", label="Actual Sales")
plt.plot(months, target, color="green", marker="s", linestyle="--", label="Target Sales")
plt.title("Actual vs Target Sales")
plt.xlabel("Month")
plt.ylabel("Sales (₹)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
