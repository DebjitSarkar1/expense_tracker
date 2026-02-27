import json
from datetime import datetime

DATA_FILE = "data.json"


def load_expenses():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except:
        return []


def save_expenses(expenses):
    with open(DATA_FILE, "w") as file:
        json.dump(expenses, file, indent=4)


def add_expense(amount, category, note):
    expenses = load_expenses()

    expense = {
        "amount": amount,
        "category": category,
        "note": note,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }

    expenses.append(expense)
    save_expenses(expenses)


def view_expenses():
    expenses = load_expenses()

    if not expenses:
        print("No expenses found.")
        return

    for i, exp in enumerate(expenses, start=1):
        print(
            f"{i}. ₹{exp['amount']} | {exp['category']} | {exp['note']} | {exp['date']}"
        )
