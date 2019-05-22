import pandas as pd

df = pd.read_csv('airquality_dataset.csv')

df = pd.melt(df, id_vars=['Month', 'Day'], var_name='Measurement', value_name='Reading')

df.to_csv('tidy_airquality_dataset.csv', index=False)
