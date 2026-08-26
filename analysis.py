import pandas as pd
df = pd.read_csv("data/sales.csv")
print(df.groupby("category")["sales_amount"].sum())
