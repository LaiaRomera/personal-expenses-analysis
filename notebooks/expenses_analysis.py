import pandas as pd
import matplotlib.pyplot as plt

def load_data(path):
    """Load the CSV file."""
    return pd.read_csv(path)

def clean_data(df):
    """Basic cleaning."""
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce") #converts to NaN if there is any problem.
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df = df.dropna(subset=["amount", "date"])  #remove missing values.
    return df

def analyze_expenses(df):
    """Calculate total expenses and expenses by category."""
    total = df["amount"].sum()
    by_category = df.groupby("category")["amount"].sum()
    return total, by_category

def graphic(expenses_by_category):
    """graphic to view the expenses."""
    expenses_by_category.plot(kind="bar", cmap = "cividis")
    plt.title("Expenses by Category")
    plt.xlabel("Category")
    plt.ylabel("Amount (€)")
    plt.tight_layout()
    plt.show()

def main():
    df = load_data("data/expenses.csv")
    total, expenses_by_category = analyze_expenses(df)
    print(f"Total expenses: {total:.2f} €")
    print("\nExpenses by category:")
    print(expenses_by_category)
    graphic(expenses_by_category)

if __name__ == "__main__":
    main()
