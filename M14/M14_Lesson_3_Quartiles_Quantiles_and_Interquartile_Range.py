# M14 Lesson 3 – Quartiles, Quantiles and Interquartile Range
# Short Description: Understanding position-based statistics and outliers detection.

# Activity 1
# Goal: Calculate quartiles and IQR.
# Summary: Compute Q1, Q2, Q3 and IQR for a dataset.
####**Import Libraries**

# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

"""####**Import Dataset**"""

from google.colab import files
uploaded = files.upload()

# Import dataset
data = pd.read_csv('Titanic Dataset.csv')

data.head(5)

"""####**Check Null Values**"""

data.isnull().sum()

"""**Null values present in Cabin -**

#### **Quartiles of Feature Age**
"""

age_q1 = np.quantile(data['Age'], 0.25)
age_q2 = np.quantile(data['Age'], 0.50)
age_q3 = np.quantile(data['Age'], 0.75)

print("Age Quartiles -")
print("Q1 -", age_q1)
print("Q2 -", age_q2)
print("Q3 -", age_q3)

"""#### **Interquartile Range of Feature Age**"""

IQR_age = age_q3 - age_q1
print("Interquartile Range :", IQR_age)

"""#### **Plot Histogram for feature Age**"""

plt.hist(data['Age'])
plt.ylabel("Count of Passengers")
plt.xlabel("Age")

"""#### **Quartiles for feature Fare**"""

fare_q1 = np.quantile(data['Fare'], 0.25)
fare_q2 = np.quantile(data['Fare'], 0.50)
fare_q3 = np.quantile(data['Fare'], 0.75)

print("Fare Quartiles -")
print("Q1 -", fare_q1)
print("Q2 -", fare_q2)
print("Q3 -", fare_q3)

"""#### **Interquartile Range of Feature Fare**"""

IQR_fare = fare_q3 - fare_q1
print("Interquartile Range :", IQR_fare)

"""#### **Plot histogram for feature Fare**"""

bins =np.arange(0,250,20)
plt.hist(data['Fare'], bins=np.arange(1,250, 20))
plt.ylabel("Count of Passengers")
plt.xlabel("Fare")
plt.xticks(bins)
# Activity 2
# Goal: Detect outliers using IQR method.
# Summary: Identify and handle outliers in the given data.
####**Import Libraries**

# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

"""####**Import Dataset**"""

from google.colab import files
uploaded = files.upload()

# Import dataset
data = pd.read_csv('Titanic Dataset.csv')

data.head(5)

"""####**Check Null Values**"""

data.isnull().sum()

"""**Null values present in Cabin -**

#### **Boxplot of Feature Age and Pclass**
"""

plt.boxplot(data['Age'])
plt.title('Age distribution')
plt.show()

plt.boxplot(data['Pclass'])
plt.title('Passenger Class distribution')
plt.show()


# ACP 
# Goal: Visualize quartiles using box plots.
# import libraries
import pandas as pd
import numpy as np
import seaborn as sns

# import dataset
data = sns.load_dataset('iris')

# calculate quartiles
data_ten_percent = np.quantile(data['petal_length'], 0.10)
data_thirty_three_percent = np.quantile(data['petal_length'], 0.33)

print("The value that splits 10% of the data is   -", data_ten_percent)
print("The value that splits 33% of the data is   -", data_thirty_three_percent)