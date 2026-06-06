# Lesson Name: Seaborn Library in Python
# Goal: Create attractive visualizations.

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
sns.scatterplot(data=tips,x="total_bill",y="tip")
plt.show()

sns.histplot(tips["total_bill"])
plt.show()

sns.boxplot(data=tips,y="total_bill")
plt.show()

# Summary:
# Learned basic plotting with seaborn.
