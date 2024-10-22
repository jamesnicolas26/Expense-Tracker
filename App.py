import json


class ExpenseTracker:
    def __init__(self, filename="expenses.json"):
        self.filename = filename
        self.expenses = self.load_expenses()

    def load_expenses(self):
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_expenses(self):
        with open(self.filename, 'w') as file:
            json.dump(self.expenses, file)

    def add_expense(self, name, amount):
        self.expenses.append({"name": name, "amount": amount})
        self.save_expenses()

    def delete_expense(self, name, amount):
        self.expenses.pop(self.expenses.index({"name": name, "amount": amount}))
        self.save_expenses()

    def view_expenses(self):
        for expense in self.expenses:
            print(f"{expense['name']}: ₱{expense['amount']}")

    def total_expenses(self):
        return sum(expense['amount'] for expense in self.expenses)


tracker = ExpenseTracker()
while True:
    print("\n1. Add Expense\n2. Delete Expense\n3. View Expenses\n4. Total Expenses\n5. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter expense name: ")
        amount = float(input("Enter amount: "))
        tracker.add_expense(name, amount)
    elif choice == '2':
        name = input("Enter expense name: ")
        amount = float(input("Enter amount: "))
        tracker.delete_expense(name, amount)
    elif choice == '3':
        tracker.view_expenses()
    elif choice == '4':
        print(f"Total Expenses: ₱{tracker.total_expenses()}")
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please try again.")
