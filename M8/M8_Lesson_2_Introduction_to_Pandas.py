# Lesson Name: Introduction to Pandas
# Goal: Learn basic DataFrame operations.

import pandas as pd

data = {"Name":["Aman","Riya"],"Marks":[90,85]}
df = pd.DataFrame(data)
print(df)

print(df.head())

print(df["Name"])

# Summary:
# Practiced creating and viewing DataFrames.
