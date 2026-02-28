import tkinter as tk
from tkinter import messagebox
from expense_manager import add_expense, view_summary


def add_expense_gui():
    try:
        amount = float(amount_entry.get())
        category = category_entry.get()
        note = note_entry.get()

        add_expense(amount, category, note)

        messagebox.showinfo("Success", "Expense added successfully!")

        amount_entry.delete(0, tk.END)
        category_entry.delete(0, tk.END)
        note_entry.delete(0, tk.END)

    except:
        messagebox.showerror("Error", "Invalid input!")


def show_summary():
    view_summary()


root = tk.Tk()
root.title("Expense Tracker")
root.geometry("350x300")

tk.Label(root, text="Amount").pack()
amount_entry = tk.Entry(root)
amount_entry.pack()

tk.Label(root, text="Category").pack()
category_entry = tk.Entry(root)
category_entry.pack()

tk.Label(root, text="Note").pack()
note_entry = tk.Entry(root)
note_entry.pack()

tk.Button(root, text="Add Expense", command=add_expense_gui).pack(pady=10)
tk.Button(root, text="Show Summary (Check Terminal)", command=show_summary).pack()

root.mainloop()
