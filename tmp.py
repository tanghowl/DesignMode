import pandas as pd
df = pd.read_table('Deleted.GT.xls')
sample_df = df.iloc[:, 4:]
tmp = sample_df.isna().sum(axis=1)
