import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

df = pd.read_excel('ready4cats.xlsx')

# Split the 'Genres/Sentiments' column into multiple columns
genreSenti = df['Genres/Sentiments'].str.get_dummies(sep=',')
transactions = pd.concat([df[['ID']], genreSenti], axis=1)
# Don't need ID
transactions = transactions.drop(columns=['ID'])

# Apply the Apriori algorithm
frequent_itemsets = apriori(transactions, min_support=0.1, use_colnames=True)

# Generate the association rules
rules = association_rules(frequent_itemsets, num_itemsets=len(transactions), metric="lift", min_threshold=1)

frequent_itemsets.to_csv('frequent_cats.csv', index=False)
print("End frequency")
rules.to_csv('association_cats.csv', index=False)
print("End association")
