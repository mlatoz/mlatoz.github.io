# Install mlxtend if not already installed
# pip install mlxtend

# Import necessary libraries
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import eclat

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

# Apply Eclat algorithm to find frequent itemsets
frequent_itemsets = eclat(df, min_support=0.2, max_length=3)

# Display the frequent itemsets
print("Frequent Itemsets:")
print(frequent_itemsets)