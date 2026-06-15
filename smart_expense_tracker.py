import pandas as pd
import matplotlib.pyplot as plt
import os

FILE = "expenses.csv"

if not os.path.exists(FILE):
    df = pd.DataFrame(columns=["Date", "Category", "Description", "Amount"])
    df.to_csv(FILE, index=False)

def add_expense():
    date = input("Enter Date (YYYY-MM-DD): ")
    category = input("Enter Category: ")
    description = input("Enter Description: ")
    amount = float(input("Enter Amount: "))

    new_data = pd.DataFrame([[date, category, description, amount]],
                            columns=["Date", "Category", "Description", "Amount"])

    df = pd.read_csv(FILE)
    df = pd.concat([df, new_data], ignore_index=True)
    df.to_csv(FILE, index=False)

    print("Expense Added Successfully!")

def view_expenses():
    df = pd.read_csv(FILE)

    if df.empty:
        print("No Expenses Found!")
    else:
        print(df)

def summary():
    df = pd.read_csv(FILE)

    if df.empty:
        print("No Data Available!")
        return

    total = df["Amount"].sum()

    print("\nTotal Expenses:", total)

def chart():
    df = pd.read_csv(FILE)

    if df.empty:
        print("No Data Available!")
        return

    category_total = df.groupby("Category")["Amount"].sum()

    plt.figure(figsize=(8,5))
    category_total.plot(kind="bar")

    plt.title("Expenses by Category")
    plt.xlabel("Category")
    plt.ylabel("Amount")

    plt.show()

while True:

    print("\n===== SMART EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Expense Summary")
    print("4. Expense Chart")
    print("5. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        add_expense()

    elif choice == 2:
        view_expenses()

    elif choice == 3:
        summary()

    elif choice == 4:
        chart()

    elif choice == 5:
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")