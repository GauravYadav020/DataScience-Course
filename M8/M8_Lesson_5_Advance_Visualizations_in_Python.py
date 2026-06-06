# Lesson Name: Advance Visualizations in Python
# Goal: Explore advanced charts.

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.heatmap(tips.corr(numeric_only=True))
plt.show()

sns.pairplot(tips)
plt.show()

sns.violinplot(data=tips,x="day",y="total_bill")
plt.show()

# Summary:
# Practiced advanced data visualizations.
