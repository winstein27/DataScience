import pandas as pd

df = pd.read_csv('ebola_dataset.csv')

df = pd.melt(df, id_vars=['Date', 'Day'], value_name='Counts')

df['Type'] = df.variable.apply(lambda x: x.split('_')[0])
df['Country'] = df.variable.apply(lambda x: x.split('_')[1])

df = df.drop('variable', axis=1)

df = df.reindex(['Date', 'Day', 'Country', 'Type', 'Counts'], axis=1, copy=False)

df.to_csv('tidy_ebola_dataset.csv', index=False)
