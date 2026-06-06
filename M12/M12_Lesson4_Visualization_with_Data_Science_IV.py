# ============================================================
# M12 Lesson 4 – Visualization with Data Science IV
# ============================================================
# Seaborn is built on top of Matplotlib and provides beautiful
# statistical visualizations with less code. This lesson covers
# Seaborn's heatmaps, box plots, and pair plots.
# ============================================================

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# ----------------------------
# Activity 1: Seaborn Bar Plot and Count Plot
# ----------------------------
# Goal: Use Seaborn to create styled bar and count plots easily.
# Summary: Students will load a sample DataFrame and use sns.barplot()
#          and sns.countplot() to visualize categorical data beautifully.

# Task:
data = pd.DataFrame({
    "Department": ["HR", "IT", "IT", "Sales", "HR", "IT", "Sales", "HR", "Sales", "IT"],
    "Salary":     [50000, 90000, 85000, 62000, 52000, 95000, 68000, 48000, 71000, 88000],
    "Gender":     ["F", "M", "F", "M", "F", "M", "F", "M", "M", "F"]
})

sns.set_theme(style="whitegrid")

sns.barplot(data=data, x="Department", y="Salary", hue="Gender", palette="Set2")
plt.title("Avg Salary by Department and Gender")
plt.tight_layout()
plt.show()

sns.countplot(data=data, x="Department", palette="pastel")
plt.title("Employee Count by Department")
plt.tight_layout()
plt.show()


# ----------------------------
# Activity 2: Box Plot and Violin Plot
# ----------------------------
# Goal: Use box and violin plots to visualize data spread and distribution.
# Summary: Students will create box plots to see median, quartiles, and
#          outliers, and violin plots to view full distribution shape.

# Task:
np.random.seed(10)
scores_data = pd.DataFrame({
    "Class":  ["A"] * 30 + ["B"] * 30 + ["C"] * 30,
    "Scores": list(np.random.randint(50, 100, 30)) +
              list(np.random.randint(40, 90, 30))  +
              list(np.random.randint(60, 100, 30))
})

sns.boxplot(data=scores_data, x="Class", y="Scores", palette="Set3")
plt.title("Score Distribution per Class (Box Plot)")
plt.tight_layout()
plt.show()

sns.violinplot(data=scores_data, x="Class", y="Scores", palette="muted")
plt.title("Score Distribution per Class (Violin Plot)")
plt.tight_layout()
plt.show()


# ----------------------------
# Activity 3: Heatmap
# ----------------------------
# Goal: Use a heatmap to visualize correlation between numeric variables.
# Summary: Students will compute a correlation matrix from a DataFrame
#          and display it as a color-coded heatmap using sns.heatmap().

# Task:
np.random.seed(42)
df = pd.DataFrame({
    "StudyHours":  np.random.randint(1, 10, 50),
    "Attendance":  np.random.randint(60, 100, 50),
    "Assignments": np.random.randint(5, 20, 50),
    "ExamScore":   np.random.randint(40, 100, 50),
    "FinalGrade":  np.random.randint(50, 100, 50),
})

correlation = df.corr()

sns.heatmap(correlation, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Correlation Heatmap – Student Performance")
plt.tight_layout()
plt.show()
