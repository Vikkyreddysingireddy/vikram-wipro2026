import pandas as pd

df = pd.read_excel("sales_data.xlsx", sheet_name="2025", engine="openpyxl")

df["Total"] = df["Quantity"] * df["Price"]

df.to_excel("sales_summary.xlsx", index=False, engine="openpyxl")

print(df)
