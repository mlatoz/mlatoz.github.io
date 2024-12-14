# Install mlxtend if not already installed
# pip install mlxtend

# Import necessary libraries
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

# Example transaction data (replace this with your own dataset)
transactions = [
    ['bread', 'milk', 'eggs'],
    ['bread', 'butter', 'jam'],
    ['milk', 'coffee'],
    ['bread', 'milk', 'butter'],
    ['eggs', 'jam']
]

# Convert the transaction data to a one-hot encoded format
te = TransactionEncoder()
te_ary = te.fit(transactions).transform(transactions)
df = pd.DataFrame(te_ary, columns=te.columns_)

# Apply Apriori algorithm to find frequent itemsets
frequent_itemsets = apriori(df, min_support=0.2, use_colnames=True)

# Generate association rules from frequent itemsets
association_rules_df = association_rules(frequent_itemsets, metric='confidence', min_threshold=0.7)

# Display the frequent itemsets and association rules
print("Frequent Itemsets:")
print(frequent_itemsets)

print("\nAssociation Rules:")
print(association_rules_df)