import pandas as pd

df = pd.read_csv('data/modified.csv')

print(df.loc[df['Type 1'] == 'Grass'])

# we can pass in multiple
# and python pandas filtering doesn'y work on and or conditions, it works on & | singns
print(df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] > 70)])

# or we can do something like saving filtered data to another data
new_df = df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] > 80)]
print(new_df)
#save it
new_df.to_csv('data/filtered.csv')
# but index doesn't change, to reset index
new_df = new_df.reset_index(drop=True)  #we also have some options like drop 
new_df.to_csv('data/filtered2.csv')
print(new_df)

# or if you don't want to reset you data you can inplace it
new_df = new_df.reset_index(drop=True, inplace=True)