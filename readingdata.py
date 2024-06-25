import pandas as pd

# Load data
df = pd.read_csv('data/pokemon_data.csv')

## Reading headrs
print(df.columns)

## Read each column
print(df['Name']) # df['column name'] or more columns
print(df[['Name', 'Type 1', 'HP']])
#for specifying
print(df['Name'][0:5]) #0 to 5 columns
#OR
print(df.Name)


## Read each Row
print(df.head(4))
print(df.iloc[1]) # that will give me evrything at second row 0-1 1-2 
print(df.iloc[1:4]) # It giver me 1-3 items
for index, row in df.iterrows():
    print(index, row)



## Read specific location (R, C)
print(df.iloc[1])
#with positions
print(df.iloc[2, 1]) #second row first position [row, position]

# SUPER RARE METHOD for specific row
print(df.loc[df['Type 1'] == 'Fire']) # it only showes the rows that type 1 colun is Fire | Jusr Fire Pokemons