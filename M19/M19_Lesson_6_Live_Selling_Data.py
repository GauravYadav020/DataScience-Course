# M19 Lesson 6 – Live Selling Data
# Short Description: Apply unsupervised learning techniques on live selling / e-commerce dataset.

# Activity 1
# Goal: Perform customer segmentation using K-Means on sales data.
# Summary: Group customers based on purchase behavior.

# Import libraries
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt # for data visualization
import seaborn as sns # for statistical data visualization
%matplotlib inline

# Input data files are available in the "../input/" directory.
import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# Ignore warnings
import warnings
warnings.filterwarnings('ignore')

# Import dataset
data = '/kaggle/input/facebook-live-sellers-in-thailand-uci-ml-repo/live.csv'
df = pd.read_csv(data)

# Exploratory data analysis
df.shape

df.head()

df.info()

df.isnull().sum()

df.drop(['column1', 'column2', 'column3', 'column4'], axis=1, inplace=True)

df.info()

df.describe()

df['status_id'].unique()

len(df['status_id'].unique())

df['status_published'].unique()

len(df['status_published'].unique())

df['status_type'].unique()

len(df['status_type'].unique())

df.drop(['status_id', 'status_published'], axis=1, inplace=True)

df.info()

df.head()

# Declare feature vector and target variable
X = df
y = df['status_type']

# Convert categorical variable into integers
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
X['status_type'] = le.fit_transform(X['status_type'])
y = le.transform(y)

# View the summary of X
X.info()

# Preview the dataset X
X.head()

# Feature Scaling
cols = X.columns
from sklearn.preprocessing import MinMaxScaler
ms = MinMaxScaler()
X = ms.fit_transform(X)
X = pd.DataFrame(X, columns=[cols])

X.head()

# K-Means model with two clusters
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=2, random_state=0)
kmeans.fit(X)

kmeans.cluster_centers_

# Check quality of weak classification by the model
labels = kmeans.labels_
correct_labels = sum(y == labels)
print("Result: %d out of %d samples were correctly labeled." % (correct_labels, y.size))
print('Accuracy score: {0:0.2f}'. format(correct_labels/float(y.size)))

# Use elbow method to find optimal number of clusters
from sklearn.cluster import KMeans
cs = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', max_iter = 300, n_init = 10, random_state = 0)
    kmeans.fit(X)
    cs.append(kmeans.inertia_)
plt.plot(range(1, 11), cs)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('')
plt.show()

from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=7, random_state=0) #with 2 clusters
kmeans.fit(X)
labels = kmeans.labels_