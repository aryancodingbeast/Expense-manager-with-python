

---

# Daily Expense Tracker

The **Daily Expense Tracker** is a simple desktop application built using Python and Tkinter. It allows users to track their daily expenses, categorize them (e.g., Food, Transport, Entertainment), and view summaries of total spending by category. The data is stored in an SQLite database, ensuring persistence across sessions.

## Features

- **Add Expenses**: Input a description, amount, and category for each expense.
- **View Expenses**: Display a list of all recorded expenses in the GUI.
- **Category Summary**: View the total amount spent in each category.
- **Persistent Storage**: Expenses are saved in an SQLite database, ensuring they are retained between sessions.

## Technologies Used

- **Python**: Core programming language.
- **Tkinter**: Used for creating the graphical user interface.
- **SQLite**: Database used for storing expenses.

## Requirements

- Python 3.x
- Tkinter (usually pre-installed with Python)
- SQLite (comes with Python)

## Installation

1. Clone the repository or download the script:
   ```bash
   git clone https://github.com/yourusername/daily-expense-tracker.git
   ```

2. Navigate to the project directory:
   ```bash
   cd daily-expense-tracker
   ```

3. Run the program:
   ```bash
   python expense_tracker.py
   ```

## How to Use

1. **Add an Expense**:
   - In the input fields, type a description of the expense, enter the amount, and select a category from the dropdown menu.
   - Click the "Add Expense" button to save the expense.
   - The expense will appear in the expense list below.

2. **View Expense Summary**:
   - To see how much you have spent in each category (e.g., Food, Transport), click the "Show Summary" button.
   - The summary will be displayed below the expense list, showing the total amount spent for each category.

3. **Expense List**:
   - All expenses are displayed in the list with their description, amount, and category.

## Screenshots

### Main Interface
![Main Interface](screenshot1.png)

### Category Summary
![Category Summary](screenshot2.png)

## License

This project is licensed under the MIT License.

---
