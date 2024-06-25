import pandas as pd

df = pd.read_csv('data/pokemon_data.csv')

# Adding a column
df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']
print(df.head(5))

# Removing Column
df = df.drop(columns=['Total'])
print(df.head(5))

# Adding a column in a different way
df['Total'] = df.iloc[:, 4:10].sum(axis=1)
print(df.head(5))

## Fully making changes
# For preautions we get the columns
cols = list(df.columns.values)
#make changes
df = df[cols[0:4] + [cols[-1]] + cols[4:12]]
print(df) #here totals moves to center



########################## ONLY HERE BUT NOWHERE ###############################
########################## SAVING OUR DATA ##################################### it's saving data changes

# saving it as csv file
df.to_csv('data/modified.csv', index=False) #there are more options like index=False or anything else like this

#saving as excel
#df.to_excel('data/modifiedexcel.xlxs')

#another way
df.to_csv('data/modifiedtxt.txt', index=False, sep='\t')  #there is no delimiter, but we have seperate function
# sep='\t' just seperates with tabs