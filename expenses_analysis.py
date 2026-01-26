import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/expenses.csv")

print(df.head())
print("Total expenses:", df["amount"].sum())

expenses_by_category = df.groupby("category")["amount"].sum()
print("\nExpenses by category:")
print(expenses_by_category)

expenses_by_category.plot(kind="bar")
plt.title("Expenses by Category")
plt.xlabel("Category")
plt.ylabel("Amount (€)")
plt.tight_layout()
plt.show()