import pandas as pd
import re

df = pd.read_csv('data/modified.csv')

# lets say some names that I don't want to see, example flame
df.loc[df['Type 1'] == 'Fire', 'Type 1'] = 'Fire' # it replaces the Fire element with Flamer, puts Flamer instead if Fire
df

## Or more something like, we want to set all Fire pokemons Legendary
df.loc[df['Type 1'] == 'Fire', 'Legendary'] = True
df #now we got all the fire pokemons are legendary

#multiple conditions
df.loc[df['Total'] > 500, ['Generation', 'Legendary']] = 'TEST VALUE'
df

#we can modify them individually
df.loc[df['Total'] > 500, ['Generation', 'Legendary']] = ['Test1', 'Test2']
print(df)