import csv
from datetime import datetime

class ExpenseTracker:
    def __init__(self, filename="expenses.csv"):
        self.filename = filename
        self.expenses = []
        self.load_expenses()

    def load_expenses(self):
        try:
            with open(self.filename, mode='r') as file:
                reader = csv.DictReader(file)
                self.expenses = list(reader)
        except FileNotFoundError:
            self.expenses = []

    def save_expenses(self):
        with open(self.filename, mode='w', newline='') as file:
            fieldnames = ["date", "amount", "category", "note"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for exp in self.expenses:
                writer.writerow(exp)

    def add_expense(self, amount, category, note=""):
        expense = {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "amount": str(amount),
            "category": category,
            "note": note
        }
        self.expenses.append(expense)
        self.save_expenses()
        print("Expense added successfully!")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded.")
            return
        for exp in self.expenses:
            print(f"{exp['date']} - ${exp['amount']} - {exp['category']} - {exp['note']}")

    def view_totals_by_category(self):
        totals = {}
        for exp in self.expenses:
            cat = exp['category']
            amt = float(exp['amount'])
            totals[cat] = totals.get(cat, 0) + amt
        print("\nTotal spent by category:")
        for cat, total in totals.items():
            print(f"{cat}: ${total:.2f}")

# -------- User Interface --------

def show_menu():
    print("\n--- Expense Tracker ---")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Totals by Category")
    print("4. Exit")

tracker = ExpenseTracker()

while True:
    show_menu()
    choice = input("Choose an option (1-4): ").strip()

    if choice == '1':
        try:
            amount = float(input("Enter amount: $"))
            category = input("Enter category (food, travel, etc.): ").strip()
            note = input("Optional note: ").strip()
            tracker.add_expense(amount, category, note)
        except ValueError:
            print("Invalid amount. Please enter a number.")
            
    elif choice == '2':
        tracker.view_expenses()
    elif choice == '3':
        tracker.view_totals_by_category()
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
