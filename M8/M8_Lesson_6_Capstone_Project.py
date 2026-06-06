# Lesson Name: Capstone Project
# Goal: Build a simple data analysis project.

import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Month":["Jan","Feb","Mar","Apr"],
    "Sales":[1000,1500,1200,1800]
}

df = pd.DataFrame(data)

print(df)

print("Total Sales:",df["Sales"].sum())

plt.plot(df["Month"],df["Sales"])
plt.show()

# Summary:
# Completed a mini project using analysis and visualization.
