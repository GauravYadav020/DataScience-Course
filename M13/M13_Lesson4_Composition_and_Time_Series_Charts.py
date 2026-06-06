# ============================================================
# M13 Lesson 4 – Composition and Time Series Charts
# ============================================================
# Composition charts show how a whole is divided into parts.
# Time Series charts track how data changes over time.
# Key types: Pie, Donut, Area Chart, Stacked Area, and Time Series.
# ============================================================

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

sns.set_theme(style="whitegrid")
np.random.seed(21)


# ----------------------------
# Activity 1: Pie Chart and Donut Chart
# ----------------------------
# Goal: Show part-to-whole composition using pie and donut charts.
# Summary: Students will create a standard pie chart and a donut chart
#          displaying budget allocation across departments.

# Task:
departments = ["Engineering", "Marketing", "HR", "Sales", "Operations"]
budget      = [35, 25, 15, 15, 10]
colors      = ["steelblue", "salmon", "mediumseagreen", "gold", "mediumpurple"]

fig, axes = plt.subplots(1, 2, figsize=(13, 5))

# Pie chart
axes[0].pie(budget, labels=departments, colors=colors,
            autopct="%1.1f%%", startangle=140, shadow=True)
axes[0].set_title("Budget Allocation – Pie Chart")

# Donut chart
wedges, texts, autotexts = axes[1].pie(
    budget, labels=departments, colors=colors,
    autopct="%1.1f%%", startangle=140,
    wedgeprops=dict(width=0.5)    # This creates the donut hole
)
axes[1].set_title("Budget Allocation – Donut Chart")

plt.tight_layout()
plt.show()


# ----------------------------
# Activity 2: Area Chart and Stacked Area Chart
# ----------------------------
# Goal: Show how values and their cumulative composition change over time.
# Summary: Students will create a filled area chart for a single series
#          and a stacked area chart comparing multiple categories over months.

# Task:
months      = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
electronics = np.random.randint(60, 110, 12) * 1000
clothing    = np.random.randint(30, 60, 12)  * 1000
food        = np.random.randint(20, 40, 12)  * 1000

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Single area chart
axes[0].fill_between(months, electronics, alpha=0.5, color="steelblue")
axes[0].plot(months, electronics, color="steelblue", linewidth=2)
axes[0].set_title("Electronics Sales – Area Chart")
axes[0].set_xlabel("Month")
axes[0].set_ylabel("Sales (₹)")
axes[0].tick_params(axis="x", rotation=45)

# Stacked area chart
axes[1].stackplot(months, electronics, clothing, food,
                  labels=["Electronics", "Clothing", "Food"],
                  colors=["steelblue", "salmon", "mediumseagreen"], alpha=0.7)
axes[1].set_title("Stacked Area – Monthly Revenue by Category")
axes[1].set_xlabel("Month")
axes[1].set_ylabel("Revenue (₹)")
axes[1].legend(loc="upper left")
axes[1].tick_params(axis="x", rotation=45)

plt.tight_layout()
plt.show()


# ----------------------------
# Activity 3: Time Series Analysis
# ----------------------------
# Goal: Plot and analyze a time series with trend and moving averages.
# Summary: Students will generate a 365-day sales time series, plot it,
#          and overlay 7-day and 30-day rolling averages to spot trends.

# Task:
dates  = pd.date_range(start="2024-01-01", periods=365, freq="D")
sales  = (np.sin(np.linspace(0, 3 * np.pi, 365)) * 3000
          + np.random.randn(365) * 800 + 10000)

ts = pd.DataFrame({"Date": dates, "Sales": sales})
ts["7D_MA"]  = ts["Sales"].rolling(7).mean()
ts["30D_MA"] = ts["Sales"].rolling(30).mean()

plt.figure(figsize=(14, 5))
plt.plot(ts["Date"], ts["Sales"],   alpha=0.3, color="steelblue", label="Daily Sales")
plt.plot(ts["Date"], ts["7D_MA"],   color="orange",  linewidth=1.5, label="7-Day MA")
plt.plot(ts["Date"], ts["30D_MA"],  color="red",     linewidth=2.5, label="30-Day MA")
plt.title("Daily Sales with Moving Averages – 2024")
plt.xlabel("Date")
plt.ylabel("Sales (₹)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
