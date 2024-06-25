import pandas as pd

# Load the dataset
df = pd.read_csv('data/modified.csv')

# Print the dataframe to check the data
print(df)

# Perform groupby operation only on numeric columns
numeric_cols = df.select_dtypes(include='number').columns
result = df.groupby(['Type 1'])[numeric_cols].mean().sort_values('Attack', ascending=False)  # It takes the avarage of all the type 1 things and shows it at rows, here we are sorting it by defence, powerfull to powerless

# Print the result
result

## By sum we get the sum of all the types
summy = df.groupby(['Type 1'])[numeric_cols].sum()
summy

##To know how many type 1s' are dark or dragon we have a method called count
coun = df.groupby(['Type 1'])[numeric_cols].count()
coun #example we have 69 of bug ...
# OR some easier way
df['count'] = 1
ecoun = df.groupby(['Type 1'])[numeric_cols].count()['count']
print(ecoun) #this way we get only one column

# I can also group by multiple parameters
coun = df.groupby(['Type 1', 'Type 2'])[numeric_cols].count()

