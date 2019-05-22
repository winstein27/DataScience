import pandas as pd

df = pd.read_csv('tb_dataset.csv')

df = pd.melt(df, id_vars=['country', 'year'], value_name='cases')

df['sex'] = df.variable.str[0]
df['age'] = df.variable.str[1:]

df = df.drop('variable', axis=1)
df = df.reindex(['country', 'year', 'sex', 'age', 'cases'], copy=False, axis=1)

df.to_csv('tidy_tb_dataset.csv', index=False)
