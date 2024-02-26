import pandas as pd

df = pd.read_csv("salaries_by_college_major.csv")
pd.options.display.float_format = '{:,.2f}'.format
# print(df)

# print(df.shape)
# (51, 6)
# first n rows from top
# print(df.head())
# last n rows
# print(df.tail(2))
# print(df.columns)
# nan -> not a number
# print(df.isna())
# dropna method drop all nan values and returns new dataframe
clean_df = df.dropna()
# print(clean_df.tail())
# find college major with Highest Starting Salaries
# print(clean_df['Starting Median Salary'].idxmax())
# 43
# print(clean_df['Undergraduate Major'].loc[43])
# print(clean_df['Undergraduate Major'][43])
# print(clean_df.loc[43])

# print(clean_df['Mid-Career Median Salary'].idxmax())
# print(clean_df.loc[8])
# Chemical Engineering
# $107000

# print(clean_df['Starting Median Salary'].idxmin())
# print(clean_df.loc[49])
# Spanish
# 34000

# print(clean_df['Mid-Career Median Salary'].idxmin())
# print(clean_df.loc[18])

spread_col = clean_df['Mid-Career 90th Percentile Salary'] - clean_df['Mid-Career 10th Percentile Salary']
# print(spread_col)
clean_df.insert(1, 'Spread', spread_col)
# print(clean_df.head())
# print(clean_df.loc[clean_df['Spread'].idxmin()])
low_risk = clean_df.sort_values('Spread')
# print(low_risk[['Undergraduate Major','Spread']].head())

highest_potential = clean_df.sort_values('Mid-Career 90th Percentile Salary', ascending=False)
# print(highest_potential[['Mid-Career 90th Percentile Salary', 'Undergraduate Major']].head())

highest_spread = clean_df.sort_values('Spread', ascending=False)
# print(highest_spread[['Mid-Career 90th Percentile Salary', 'Undergraduate Major']].head())

print(clean_df.groupby('Group').mean(numeric_only=True))
