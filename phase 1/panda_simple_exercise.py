import pandas as pd

data = {
    "Name" : ["John" , "Mike"],
    "Marks" : [ 80 , 90]
}
df = pd.DataFrame(data)

print(df)
print("Average:",df["Marks"].mean())
print("Highest:",df["Marks"].max())
highest =  df["Marks"].max()
print(df[df["Marks"] == highest]["Name"])