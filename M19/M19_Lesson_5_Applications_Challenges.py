# M19 Lesson 5 – Applications & Challenges
# Short Description: Real-world applications and common challenges in unsupervised learning.

# Activity 1
# Goal: Research and list applications of clustering in different domains.
# Summary: Healthcare, marketing, image segmentation, etc.
# ---- UNSUPERVISED MACHINE LEARNING: K-MEANS CLUSTERING ----

import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

data = load_iris()
X = data.data

kmeans = KMeans(n_clusters=3, random_state=42)
clusters = kmeans.fit_predict(X)

df = pd.DataFrame(X, columns=data.feature_names)
df['Cluster'] = clusters

plt.figure(figsize=(8,6))
for cluster in range(3):
    subset = df[df['Cluster'] == cluster]
    plt.scatter(subset.iloc[:,0], subset.iloc[:,1], label=f'Cluster {cluster}')
plt.xlabel(data.feature_names[0])
plt.ylabel(data.feature_names[1])
plt.title('K-means Clustering on Iris Dataset')
plt.legend()
plt.show()

