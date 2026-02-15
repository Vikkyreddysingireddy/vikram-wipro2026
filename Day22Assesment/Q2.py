import pandas as pd
import numpy as np

df = pd.read_csv("sales.csv")
print("Sales Data:")
print(df)

df["Total"] = df["Quantity"] * df["Price"]
total_sales = np.sum(df["Total"])
avg_sales = np.mean(df["Total"])
std_sales = np.std(df["Total"])

print("Total Sales:", total_sales)
print("Average Daily Sales:", avg_sales)
print("Standard Deviation:", std_sales)

best_product = df.groupby("Product")["Quantity"].sum().idxmax()
print("Best Selling Product:", best_product)
