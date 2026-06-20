import pandas as pd

df = pd.read_csv("students.csv")

print(df)

#First 5 rows
print(df.head())

#Last 5 rows
print(df.tail())

#Information
print(df.info())

#Statistics - > gets u Mean, Max, Min, Count, Std Deivation
print(df.describe())