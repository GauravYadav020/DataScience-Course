# M19 Lesson 3 – Density-Based Clustering
# Short Description: Introduction to DBSCAN and other density-based clustering methods.

# Activity 1
# Goal: Understand how DBSCAN identifies core points, border points, and noise.
# Summary: Manually label points based on density parameters.
frequent_itemsets = apriori(dataset, min_support=0.01, use_colnames=True)
frequent_itemsets['length'] = frequent_itemsets['itemsets'].apply(lambda x: len(x))
frequent_itemsets

frequent_itemsets[(frequent_itemsets['length'] == 2) & (frequent_itemsets['support'] >= 0.05)]

frequent_itemsets[(frequent_itemsets['length'] == 3)].head()