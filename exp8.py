import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

# Sample transaction data (same as before)
data = {
    'TransactionID': [1, 2, 3, 4, 5, 6, 7, 8],
    'Items': [
        ['Milk', 'Bread', 'Diaper'],
        ['Milk', 'Bread'],
        ['Bread', 'Diaper', 'Eggs'],
        ['Milk', 'Diaper', 'Eggs'],
        ['Bread', 'Diaper'],
        ['Milk', 'Bread', 'Diaper', 'Eggs'],
        ['Bread'],
        ['Milk', 'Bread', 'Diaper', 'Eggs', 'Cola']
    ]
}

# Create a DataFrame
transactions = pd.DataFrame(data)

# Transform transactions into a one-hot encoded DataFrame
te = TransactionEncoder()
te_ary = te.fit(transactions['Items']).transform(transactions['Items'])
df = pd.DataFrame(te_ary, columns=te.columns_)

# Apply Apriori algorithm with mlxtend
frequent_itemsets = apriori(df, min_support=0.3, use_colnames=True)

# Generate association rules
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.6)

# Print frequent itemsets and association rules
print("Frequent Itemsets:")
print(frequent_itemsets)
print("\nAssociation Rules:")
print(rules)
