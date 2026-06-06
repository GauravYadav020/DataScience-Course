# M14 Lesson 4 – Statistics for Categorical Variables and Data Transformation
# Short Description: Frequency analysis and basic data preprocessing techniques.

# Activity 1
# Goal: Analyze categorical data using frequency counts.
# Summary: Compute mode, counts, and percentages for categorical variables.
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

data.dtypes

"""#### **Nominal and Ordinal Categorical Features -**


"""

# Nominal Categorical Variables
nominal_cat = ['Name','Ticket','Cabin']

# Ordinal Categorical Variables
ordinal_cat = ['Embarked','Gender']

"""#### **Median value of feature Gender and Embarked**"""

data['Gender'].value_counts()

gender_categories = ['Female','Male']

data['Gender'] = pd.Categorical(data['Gender'], gender_categories, ordered=True)

median_index = np.median(data['Gender'].cat.codes)
median_gender = gender_categories[int(median_index)]
print(median_gender)

data['Embarked'].value_counts()

embarked_categories = ['S','C','Q']

data['Embarked'] = pd.Categorical(data['Embarked'], embarked_categories, ordered=True)

median_index = np.median(data['Embarked'].cat.codes)
median_embarked = embarked_categories[int(median_index)]
print(median_embarked)
# Activity 2
# Goal: Perform data transformation (normalization, scaling).
# Summary: Apply min-max scaling and standardization on numerical features.
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


# Activity 3
# Goal: Encode categorical variables.
# Summary: Use one-hot encoding and label encoding techniques.
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

"""#### **Create new dataset with only Numerical Features**"""

num_data = data.drop(['Name', 'Ticket', 'Cabin', 'Embarked', 'Gender'], axis=1)

labels = ['PassengerId','Survived','Pclass','Age','SibSp','Parch','Fare']

"""#### **Creating boxplot for all the features**"""

for label in labels:
  plt.boxplot(num_data[label])
  print('Distribution of', label)
  plt.show()

"""**Conclusion -**

- since there are outliers present in many features, so we should standardize the features

#### **Scaling Dataset**
"""

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
num_data = scaler.fit_transform(num_data)