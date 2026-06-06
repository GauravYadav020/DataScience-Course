# Lesson Name: Introduction to Matplotlib
# Goal: Create basic charts using matplotlib.

import matplotlib.pyplot as plt

x=[1,2,3,4]
y=[10,20,15,25]
plt.plot(x,y)
plt.show()

subjects=["Math","Science","English"]
marks=[90,85,88]
plt.bar(subjects,marks)
plt.show()

sizes=[40,35,25]
plt.pie(sizes)
plt.show()

# Summary:
# Created line, bar and pie charts.
