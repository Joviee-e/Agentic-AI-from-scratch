import pandas as pd

data = {
    "Name" : ["John" , "Aksah", "Neo"],
    "Age" : [ 21, 20, 19]
}

df = pd.DataFrame(data)

print(df)

#specific table

print(df["Name"])

#avr
print(int(df["Age"].mean()))

#max
print(int(df["Age"].max()))

#filtering
print(df[df["Age"] >= 20])

#adding new column
df["Grade"] = ["A+" , "A" , "A"]
print(df)