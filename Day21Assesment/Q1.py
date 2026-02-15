import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [25000, 27000, 30000, 28000, 32000, 31000]

data = pd.DataFrame({
    "Month": months,
    "Sales": sales
})

plt.figure(figsize=(8, 5))
plt.plot(months, sales, marker='o', color='blue', linestyle='-')

plt.title("Monthly Sales Trend (Matplotlib)")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)
plt.savefig("linechart.png")
plt.show()

plt.figure(figsize=(8, 5))
sns.barplot(x="Month", y="Sales", data=data)
plt.title("Monthly Sales Bar Chart (Seaborn)")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)
plt.savefig("barplot.png")
plt.show()
