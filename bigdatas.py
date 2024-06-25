import pandas as pd

# Normall loading
df = pd.read_csv('data/modified.csv')

# Lets say you are importing big datas like 20gb
#bdf = pd.read_csv('modified.csv', chunksize=5)

new_df = pd.DataFrame(columns=df.columns) #this creates a new dataframe with these column names

for df in pd.read_csv('data/modified.csv', chunksize=5): #that means 5 rows are being passed in at the time JUST FOR NOW GETTING MESSED
    result = df.groupby(['Type 1']).count()

    new_df = pd.concat([new_df, result])
    print(new_df)



