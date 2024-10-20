import pandas as pd 
# Load CSV File 
csv_path = "/content/Countries.csv" 
df = pd.read_csv(csv_path) 
# Create A Frequency Table USing Crosstab 
frequency_table = pd.crosstab(df['Countries'], df['Outcomes']) 
print(frequency_table) 
print() 
# Calculate Prior Probabilities P(A) And P(B) 
P_A = df['Countries'].value_counts(normalize = True) 
P_B = df['Outcomes'].value_counts(normalize = True) 
print (P_A) 
print (P_B) 
print() 
#Calculate The Likehood P(A|B) 
P_A_given_B = frequency_table.div(frequency_table.sum(axis=0), axis=1) 
# Assume We Are Given A Specific Weather Condition 'Sunny' And Outcome 'YES' 
A = 'India' 
B = 'Yes' 
#Apply Naive Bayes Theroem: P(B|A) = (P(A|B) * P(B)) / P(A) 
P_B_given_A = (P_A_given_B[B][A] * P_B[B]) / P_A[A] 
# Display Result 
print(f"P(A) - Probability of Countries '{A}': {P_A[A]:.4f}") 
print(f"P(B) - Probability of Outcome '{B}': {P_B[B]:.4f}") 
print(f"P(A|B) - Probability of Countries '{A}' given Outcome '{B}': 
{P_A_given_B[B][A]:.4f}") 
print(f"P(B|A) - Probability of Outcome '{B}' given Countries '{A}': {P_B_given_A:.4f}")