# M14 Lesson 6 – Exploratory Data Analysis
# Short Description: Comprehensive EDA techniques using Python libraries.

# Activity 1
# Goal: Perform univariate analysis.
# Summary: Generate summary statistics and histograms.
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

"""#### **Set Plot Style**"""

sns.set_style('whitegrid')

"""#### **Countplot for feature 'Survived'**"""

sns.countplot(x='Survived', data=data)

"""#### **Barchart for showing passengers belonging to different gender who survived or not**

"""

sns.countplot(x='Gender', hue='Survived', data=data)

"""#### **Customize Plots**"""

sns.countplot(x='Survived', data=data, palette='winter')

sns.countplot(x='Gender', hue='Survived', data=data, palette='winter')

"""#### **Countplot for Embarked**"""

sns.countplot(x='Embarked', data=data)

"""#### **Rotate the value labels and modify their font size**

"""

sns.countplot(x='Embarked', data=data)
plt.xticks(rotation=30, fontsize=20)
plt.show()

# Activity 2
# Goal: Conduct bivariate and multivariate analysis.
# Summary: Create scatter plots, correlation heatmaps.
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

