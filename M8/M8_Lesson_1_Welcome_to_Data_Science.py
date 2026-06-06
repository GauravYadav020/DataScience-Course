# Lesson Name: Welcome to Data Science
# Goal: Understand the basics of data science and datasets.

students = ["Aman","Riya","Karan","Priya"]
print(students)

marks = [80,90,75,88]
print(sum(marks)/len(marks))

highest = max(marks)
print(highest)




# Summary: ACP
# Learned what data is and how it can be analyzed.
import pandas as pd

data = {"Name":["Aman","Riya"],"Marks":[90,85]}
df = pd.DataFrame(data)
print(df)

print(df.head())

print(df["Name"])

