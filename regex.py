import pandas as pd
import re #powerful filtering data library

df = pd.read_csv('data/pokemon_data.csv')

# print(df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] > 70)])

#regex filtering like let's say you have BruhMegaPokeman, you want all Mega pokemons, and it's regex filtering

df.loc[df['Name'].str.contains('Mega')] #only ad ~ and you drop all these Mega words

df.loc[~df['Name'].str.contains('Mega')]

df.loc[df['Type 1'].str.contains('fire|grass', flags=re.I, regex=True)]  # flags=re.I is like whatever the type capitalized or not it shows you results


## Anothre example let's say we wanna get all the pokemon names that has Pi
df.loc[df['Name'].str.contains('pi[a-z]*', flags=re.I, regex=True)] #it returns names that has pi and contious with a-z charecters, 

##names that starts with pi
print(df.loc[df['Name'].str.contains('^pi[a-z]*', flags=re.I, regex=True)]) # ^ charecter says to the programm that show me names starts with pi