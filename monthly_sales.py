import pandas as pd
df = pd.read_csv("data/sales.csv")
df["order_date"] = pd.to_datetime(df["order_date"])
df["month"] = df["order_date"].dt.to_period("M").astype(str)
monthly_summary = (
    df.groupby("month")
    .agg(
        total_sales=("sales_amount", "sum"),
        order_count=("order_id", "nunique")
    )
    .sort_index()
)
print(monthly_summary)