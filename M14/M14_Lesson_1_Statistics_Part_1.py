# M14 Lesson 1 – Statistics – Part 1
# Short Description: Introduction to basic statistical concepts including mean, median, and mode.

# Activity 1
# Goal: Understand and calculate measures of central tendency.
# Summary: Students will compute mean, median, and mode for a given dataset using Python.
# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from google.colab import files
uploaded = files.upload()

# Import dataset
data = pd.read_csv('Titanic Dataset.csv')
data.head(5)

# Check the datatype
data.dtypes

# Check Null Values
data.isnull().sum()
# Activity 2
# Goal: Learn about measures of dispersion like range and variance.
# Summary: Calculate range, variance, and standard deviation for sample data.
# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

"""####**Import Dataset**"""

from google.colab import files
uploaded = files.upload()

data = pd.read_csv('Titanic Dataset.csv')

data.head()

"""####**Mean Value of Age and Fare**"""

# Mean Value of age
mean_age = np.mean(data['Age'])
print("Mean Age of Passengers is - ",mean_age)

# Mean Value of Fare
mean_fare = np.mean(data['Fare'])
print("Mean Fare is - ",mean_fare)

# Activity 3
# Goal: Apply statistical concepts to real-world data.
# Summary: Analyze a small dataset and interpret the results.
# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

"""####**Import Dataset**"""

from google.colab import files
uploaded = files.upload()

data = pd.read_csv('Titanic Dataset.csv')

data.head()

"""####**Mean Value of Age and Fare**"""

# Mean Value of age
mean_age = np.mean(data['Age'])
print("Mean Age of Passengers is - ",mean_age)

# Mean Value of Fare
mean_fare = np.mean(data['Fare'])
print("Mean Fare is - ",mean_fare)

# acp

####**Import Libraries**

# Import Libraries
import pandas as pd
import numpy as np
import statistics as stats
import matplotlib.pyplot as plt
import seaborn as sns

"""####**Import Dataset**"""

from google.colab import files
uploaded = files.upload()

data = pd.read_csv('Titanic Dataset.csv')

data.head()

"""####**Median Value of Age and Fare**"""

median_age = np.median(data['Age'])
print("Median value of Age -", median_age)

median_fare = np.median(data['Fare'])
print("Median value of Fare -", median_fare)

"""####**Mode Value of Age and PClass**"""

mode_age = stats.mode(data['Age'])
print("Mode value of Age -", mode_age)

mode_class = stats.mode(data['Pclass'])
print("Mode value of PClass -", mode_class)

"""####**Mode Value of Categorical Feature - Gender**"""

mode_gender = data['Gender'].value_counts().index[0]
print("Mode of Feature Gender -", mode_gender)