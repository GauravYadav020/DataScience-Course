# M14 Lesson 2 – Statistics – Part 2
# Short Description: Advanced concepts in descriptive statistics and probability basics.

# Activity 1
# Goal: Explore probability distributions.
# Summary: Implement and visualize normal distribution using Python.
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
data = pd.read_csv('Weather Dataset.csv')

data.head(5)

data.info()

"""####**Check Null Values**"""

data.isnull().sum()

"""**No feature has any null values**

#### **Mean, Variance and Standard Deviation of Temperature (C)**
"""

mean_temp = np.mean(data['Temperature (C)'])
print("Mean Temperature is :", mean_temp)

var_temp = np.var(data['Temperature (C)'])
print("Variation of Temperature is :", var_temp)

standard_deviation_temp = np.std(data['Temperature (C)'])
print("Standard Deviation of Temperature is :", standard_deviation_temp)

"""#### **Mean, Variance and Standard Deviation of Temperature (C) for every month**"""

for i in range(1, 13):
  month = data.loc[data["month"] == i]["Temperature (C)"]
  print("For month "+str(i))
  print("Mean temperature is "+ str(np.mean(month)))
  print("Standard deviation is "+ str(np.std(month))+"\n")
# Activity 2
# Goal: Understand skewness and kurtosis.
# Summary: Calculate skewness and kurtosis for different datasets.
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
data = pd.read_csv('IMDB Dataset.csv')

data.head(5)

"""####**Check Null Values**"""

data.isnull().sum()

"""**No null values present -**

#### **Plot Histogram for feature Runtime**
"""

plt.hist(data['Runtime'])
plt.ylabel("Count of movies")
plt.xlabel("Runtime")

"""#### **Plot Histogram for feature IMDB_Rating**"""

plt.hist(data['IMDB_Rating'])
plt.ylabel("Count of movies")
plt.xlabel("IMDB Rating")

"""#### **Define parameter bins_runtime for feature Runtime and plot histogram for it**"""

data['Runtime'].unique()

bins_time = np.arange(80, 230, 10)
plt.hist(data['Runtime'], edgecolor="black", bins=bins_time, color='g')
plt.ylabel("Count of movies")
plt.xlabel("Runtime")

"""#### **Define parameter bins_rating for feature IMDB_Rating and plot histogram for it**"""

data['IMDB_Rating'].unique()

bins_rating = np.arange(8, 10, 0.20)
plt.hist(data['IMDB_Rating'], edgecolor="black", bins=bins_rating, color='g')
plt.ylabel("Count of movies")
plt.xlabel("IMDB Rating")
plt.xticks(bins_rating)

# ACP 
# Goal: Perform hypothesis testing basics.
# Summary: Conduct a simple hypothesis test on sample data.
# import libraries
import pandas as pd
import numpy as np
import seaborn as sns

data = sns.load_dataset('iris')

pet_len_deviation = np.std(data['petal_length'])
print("Standard Deviation of Petal Length -", pet_len_deviation)