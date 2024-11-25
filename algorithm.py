# Part 2: takes transaction list and computes Apriori algorithm
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

df = pd.read_excel('ready4cats.xlsx')

# Create a binary matrix for the Genres/Sentiments
# Split the 'Genres/Sentiments' column into multiple columns
genreSenti = df['Genres/Sentiments'].str.get_dummies(sep=',')

# Concatenate the 'ID' column with the binary matrix
transactions = pd.concat([df[['ID']], genreSenti], axis=1)

# Drop the 'ID' column as it's not needed for the Apriori algorithm
transactions = transactions.drop(columns=['ID'])

# Apply the Apriori algorithm
    # Set the minimum support threshold
frequent_itemsets = apriori(transactions, min_support=0.1, use_colnames=True)

# Generate the association rules
rules = association_rules(frequent_itemsets, num_itemsets=len(transactions), metric="lift", min_threshold=1)

# Display the results
print(frequent_itemsets)
print(rules)

frequent_itemsets.to_csv('frequent_cats.csv', index=False)
rules.to_csv('association_cats.csv', index=False)
