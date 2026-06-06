# M19 Lesson 4 – Association Rule Base Learning
# Short Description: Learn association rule mining like Apriori algorithm for market basket analysis.

# Activity 1
# Goal: Generate frequent itemsets from transaction data.
# Summary: Apply Apriori algorithm manually on small dataset.

frequent_itemsets = apriori(dataset, min_support=0.01, use_colnames=True)
frequent_itemsets['length'] = frequent_itemsets['itemsets'].apply(lambda x: len(x))
frequent_itemsets

frequent_itemsets[(frequent_itemsets['length'] == 2) & (frequent_itemsets['support'] >= 0.05)]

frequent_itemsets[(frequent_itemsets['length'] == 3)].head()