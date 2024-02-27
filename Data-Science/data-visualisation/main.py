import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('QueryResults.csv', names=['DATE', 'TAG', 'POSTS'], header=0)
df.head()
df.groupby('TAG').sum(numeric_only=True)
df.groupby('TAG').count()
df['DATE'] = pd.to_datetime(df['DATE'])
reshaped_df = df.pivot(index='DATE', columns='TAG', values='POSTS')
reshaped_df.head()
reshaped_df.fillna(0, inplace=True)
reshaped_df.isna().values.any()
roll_df = reshaped_df.rolling(window=12).mean()
plt.figure(figsize=(12, 8))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel("Dates")
plt.ylabel("Number of posts")
plt.ylim(0, 35000)
for column in roll_df.columns:
    plt.plot(roll_df.index, roll_df[column], label=roll_df[column].name)
plt.legend(fontsize=16)
