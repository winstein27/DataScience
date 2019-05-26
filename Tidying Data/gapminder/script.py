import pandas as pd

df = pd.read_csv('gapminder_dataset.csv', index_col=0)

df = df.rename(columns={'Life expectancy': 'Country'})
df = pd.melt(df, id_vars=['Country'], var_name='Year', value_name='Life Excpectancy')

df.to_csv('tidy_gapminder_dataset.csv', index=False)
