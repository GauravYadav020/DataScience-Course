# ============================================================
# M13 Lesson 3 – Comparison Charts
# ============================================================
# Comparison charts are used to compare values across different
# categories or groups. Key types: Bar Chart, Grouped Bar,
# Stacked Bar, Radar/Spider Chart, and Lollipop Chart.
# ============================================================

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

sns.set_theme(style="whitegrid")
np.random.seed(15)


# ----------------------------
# Activity 1: Grouped and Stacked Bar Charts
# ----------------------------
# Goal: Compare multiple categories side by side and as stacked proportions.
# Summary: Students will use grouped bar charts to compare quarterly
#          sales and stacked bars to show category contribution per month.

# Task:
quarters    = ["Q1", "Q2", "Q3", "Q4"]
electronics = [85000, 92000, 78000, 110000]
clothing    = [42000, 38000, 51000, 63000]
food        = [31000, 35000, 29000, 40000]
x           = np.arange(len(quarters))
width       = 0.25

# Grouped bar chart
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

axes[0].bar(x - width, electronics, width, label="Electronics", color="steelblue")
axes[0].bar(x,         clothing,    width, label="Clothing",    color="salmon")
axes[0].bar(x + width, food,        width, label="Food",        color="mediumseagreen")
axes[0].set_xticks(x)
axes[0].set_xticklabels(quarters)
axes[0].set_title("Grouped Bar – Quarterly Sales by Category")
axes[0].set_ylabel("Sales (₹)")
axes[0].legend()

# Stacked bar chart
axes[1].bar(quarters, electronics, label="Electronics", color="steelblue")
axes[1].bar(quarters, clothing,    bottom=electronics, label="Clothing", color="salmon")
axes[1].bar(quarters, food,        bottom=[e + c for e, c in zip(electronics, clothing)],
            label="Food", color="mediumseagreen")
axes[1].set_title("Stacked Bar – Category Contribution per Quarter")
axes[1].set_ylabel("Sales (₹)")
axes[1].legend()

plt.tight_layout()
plt.show()


# ----------------------------
# Activity 2: Lollipop Chart
# ----------------------------
# Goal: Use a lollipop chart as a clean alternative to bar charts.
# Summary: Students will create a lollipop chart to compare average
#          salaries across departments in a visually minimal way.

# Task:
departments = ["Engineering", "Sales", "HR", "Marketing", "Finance", "Design"]
avg_salary  = [95000, 72000, 55000, 68000, 80000, 74000]

sorted_idx  = np.argsort(avg_salary)
departments = [departments[i] for i in sorted_idx]
avg_salary  = [avg_salary[i] for i in sorted_idx]

plt.hlines(departments, xmin=0, xmax=avg_salary, colors="steelblue", linewidth=2)
plt.plot(avg_salary, departments, "o", color="steelblue", markersize=10)

for i, val in enumerate(avg_salary):
    plt.text(val + 800, i, f"₹{val:,}", va="center", fontsize=9)

plt.title("Lollipop Chart – Average Salary by Department")
plt.xlabel("Average Salary (₹)")
plt.xlim(0, 110000)
plt.tight_layout()
plt.show()


# ----------------------------
# Activity 3: Radar / Spider Chart
# ----------------------------
# Goal: Compare multiple attributes of two entities using a radar chart.
# Summary: Students will plot a radar chart to compare skill scores
#          of two candidates across five different skill areas.

# Task:
skills      = ["Python", "SQL", "ML", "Visualization", "Statistics"]
candidate_a = [8, 7, 6, 9, 7]
candidate_b = [6, 9, 8, 7, 8]

angles = np.linspace(0, 2 * np.pi, len(skills), endpoint=False).tolist()
angles += angles[:1]   # Close the loop

candidate_a += candidate_a[:1]
candidate_b += candidate_b[:1]

fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

ax.plot(angles, candidate_a, "o-", linewidth=2, label="Candidate A", color="steelblue")
ax.fill(angles, candidate_a, alpha=0.2, color="steelblue")

ax.plot(angles, candidate_b, "o-", linewidth=2, label="Candidate B", color="salmon")
ax.fill(angles, candidate_b, alpha=0.2, color="salmon")

ax.set_thetagrids(np.degrees(angles[:-1]), skills)
ax.set_ylim(0, 10)
ax.set_title("Radar Chart – Candidate Skill Comparison", pad=20)
ax.legend(loc="upper right", bbox_to_anchor=(1.3, 1.1))
plt.tight_layout()
plt.show()
