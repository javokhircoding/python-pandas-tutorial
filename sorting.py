import pandas as pd

df = pd.read_csv('data/pokemon_data.csv')

# describe method giver us like all the high level or lowes, highest
print(df.describe())

# And stupidly another usefull method is just
print(df) # becouse it's very very accurate so we can differ various datas,  ...

# Sorting by alphabet or anything
print(df.sort_values('Name')) #it sorts by alphabet letters
print(df.sort_values('Name', ascending=False)) # it's kinda reverse alphabet ascending=False
print(df.sort_values(['Type 1', 'HP'])) # ascending=[1, 0]