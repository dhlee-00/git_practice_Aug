import pandas as pd
df = pd.read_csv("data/sales.csv")
df["order_date"] = pd.to_datetime(df["order_date"])
df["month"] = df["order_date"].dt.to_period("M").astype(str)
monthly_sales = (
    df.groupby("month")["sales_amount"]
    .sum()
    .sort_index()
)
print(monthly_sales)