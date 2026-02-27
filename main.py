# Expense tracker application

from expense_manager import add_expense, view_expenses, view_summary


def menu():
    while True:
        print("\n===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Summary")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            try:
                amount = float(input("Enter amount: "))
                category = input("Enter category: ")
                note = input("Enter note: ")
                add_expense(amount, category, note)
                print("Expense added successfully!")
            except:
                print("Invalid input!")

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            view_summary()

        elif choice == "4":
            print("Goodbye 👋")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    menu()
