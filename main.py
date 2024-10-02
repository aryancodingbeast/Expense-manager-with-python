from tkinter import *
from tkinter import messagebox
import sqlite3

# Initialize the database
def init_db():
    conn = sqlite3.connect('expenses.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS expenses
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, description TEXT, amount REAL, category TEXT)''')
    conn.commit()
    conn.close()

# Add expense to database
def add_expense(description, amount, category):
    conn = sqlite3.connect('expenses.db')
    c = conn.cursor()
    c.execute("INSERT INTO expenses (description, amount, category) VALUES (?, ?, ?)", (description, amount, category))
    conn.commit()
    conn.close()

# Retrieve expenses from database
def get_expenses():
    conn = sqlite3.connect('expenses.db')
    c = conn.cursor()
    c.execute("SELECT * FROM expenses")
    expenses = c.fetchall()
    conn.close()
    return expenses

# Calculate total expenses by category
def get_category_summary():
    conn = sqlite3.connect('expenses.db')
    c = conn.cursor()
    c.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category")
    summary = c.fetchall()
    conn.close()
    return summary

# Add expense from the GUI
def add_expense_from_gui():
    description = desc_entry.get()
    try:
        amount = float(amount_entry.get())
        category = category_var.get()
        if description and category:
            add_expense(description, amount, category)
            desc_entry.delete(0, END)
            amount_entry.delete(0, END)
            display_expenses()
        else:
            messagebox.showwarning("Input Error", "Please enter a valid description and category.")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid amount.")

# Display all expenses in the GUI
def display_expenses():
    expenses = get_expenses()
    expense_listbox.delete(0, END)  # Clear the listbox before updating
    for expense in expenses:
        expense_listbox.insert(END, f"Description: {expense[1]}, Amount: {expense[2]}, Category: {expense[3]}")

# Display summary of expenses by category
def display_category_summary():
    summary = get_category_summary()
    summary_listbox.delete(0, END)  # Clear the listbox before updating
    for category, total in summary:
        summary_listbox.insert(END, f"Category: {category}, Total: {total}")

# Main GUI setup
def create_gui():
    global desc_entry, amount_entry, expense_listbox, summary_listbox, category_var

    root = Tk()
    root.title("Daily Expense Tracker")

    # Description Input
    Label(root, text="Description").grid(row=0, column=0)
    desc_entry = Entry(root, width=30)
    desc_entry.grid(row=0, column=1)

    # Amount Input
    Label(root, text="Amount").grid(row=1, column=0)
    amount_entry = Entry(root, width=30)
    amount_entry.grid(row=1, column=1)

    # Category Input
    Label(root, text="Category").grid(row=2, column=0)
    category_var = StringVar(root)
    category_var.set("Food")  # default value
    category_menu = OptionMenu(root, category_var, "Food", "Transport", "Entertainment", "Health", "Other")
    category_menu.grid(row=2, column=1)

    # Add Expense Button
    add_expense_btn = Button(root, text="Add Expense", command=add_expense_from_gui)
    add_expense_btn.grid(row=3, column=1)

    # Expense Listbox
    Label(root, text="Expenses").grid(row=4, column=0, columnspan=2)
    expense_listbox = Listbox(root, width=50, height=10)
    expense_listbox.grid(row=5, column=0, columnspan=2)

    # Category Summary Button
    summary_btn = Button(root, text="Show Summary", command=display_category_summary)
    summary_btn.grid(row=6, column=1)

    # Summary Listbox
    Label(root, text="Category Summary").grid(row=7, column=0, columnspan=2)
    summary_listbox = Listbox(root, width=50, height=5)
    summary_listbox.grid(row=8, column=0, columnspan=2)

    # Run display
    display_expenses()

    root.mainloop()

# Main loop
def main():
    init_db()
    create_gui()

if __name__ == "__main__":
    main()
