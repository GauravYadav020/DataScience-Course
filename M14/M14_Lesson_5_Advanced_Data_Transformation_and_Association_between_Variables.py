# M14 Lesson 5 – Advanced Data Transformation and Association between Variables
# Short Description: Correlation, covariance, and advanced transformations.

# Activity 1
# Goal: Calculate correlation between variables.
# Summary: Compute Pearson correlation coefficient.
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

"""#### **Minimum and Maximum Values of Age**"""

minimum_age = data['Age'].min()
print('Minimum Age :', minimum_age)

maximum_age = data['Age'].max()
print('Maximum Age :', maximum_age)

"""#### **Creating binned age and giving it a label**"""

bins = [0, 15, 30, 45, 60, 75]

data['binned_age'] = pd.cut(data['Age'], bins)

print(data[['binned_age', 'Age']].head())

age_labels = ['Young', 'Young - Adult', 'Middle Aged', 'Middle-Older Age', 'Senior']
 
# Bin the values of the 'Age' column and specify the labels 
data['binned_age'] = pd.cut(data['Age'], bins, labels = age_labels)

"""#### **Barplot for binned age**"""

data['binned_age'].value_counts().plot(kind='bar')
 
# Label the bar graph
plt.title('Dance Class Age Distribution')
plt.xlabel('Ages')
plt.ylabel('Count')

"""**Conclusion**
 
- Features Gender and Embarked have only 2 and 3 categories respectively
- Other categorcial features have too many categories to even collapse

#### **Check distribution and skewness of all the features**
"""

labels = ['PassengerId','Survived','Pclass','Age','SibSp','Parch','Fare']
for label in labels:
  print('Distribution of', label)
  sns.distplot(data[label])
  plt.show()
  print('Skewness -', data[label].skew())

"""**Conclusion**

- Features - SibSp, Parch and Fare are skewed

#### **Log Transform Skewed Features**
"""

data['log_SibSp'] = np.log(data['SibSp'])
data['log_Parch'] = np.log(data['Parch'])
data['log_Fare'] = np.log(data['Fare'])
# Activity 2
# Goal: Understand covariance and its interpretation.
# Summary: Calculate covariance matrix for multiple variables.
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

"""#### **Check association between Embarked and Age**"""

sns.boxplot(data = data, x = 'Embarked', y = 'Age')
plt.show()

"""- **There is too much overlapping in the boxplots, which means there is no much association between Embarked and Age**

#### **Check association between Survived and Fare, SibSp, Parch**
"""

plt.scatter(x = data['Fare'], y = data['Survived'])
plt.ylabel('Survived')
plt.xlabel('Fare')
plt.show()

plt.scatter(x = data['Parch'], y = data['Survived'])
plt.ylabel('Survived')
plt.xlabel('Parch')
plt.show()

plt.scatter(x = data['SibSp'], y = data['Survived'])
plt.ylabel('Survived')
plt.xlabel('SibSp')
plt.show()

"""- **There is association of features Parch, SibSp with Survived**

#### **Check association between Gender and Embarked**
"""

association_categorical = pd.crosstab(data['Gender'], data['Embarked'])
print(association_categorical)

# ACP
# Goal: Apply log transformation and other advanced techniques.
# Summary: Handle skewed data using transformations.
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
