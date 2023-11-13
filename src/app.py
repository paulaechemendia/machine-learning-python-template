import pandas as pd



df = pd.read_csv('/workspaces/machine-learning-python-template/data/raw/data.csv')
drops = ['id', 'host_id', 'name', 'host_name', 'neighbourhood', 'last_review']
df = df.drop(drops, axis=1)
print(df.describe())