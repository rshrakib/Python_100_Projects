import csv

from unicodedata import category


class ExpenseTracker:
    def __init__(self):
        self.expanses= []
        self.filename = "expenses.csv"

    def add_expense(self, category, amount):
        self.expanses.append({"Category": category, "Amount": amount})
        self.save_to_file()
    def display_expenses(self):
        self.load_from_file()

        if not self.expanses:
            print("No expenses recorded yet")
        else:
            print("Expenses list: ")
            for expanse in self.expanses:
                print(f"Category: {expanse['Category']}, Amount: {expanse['Amount']}")

    def save_to_file(self):
        with open(self.filename, mode='w', newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["Category", "Amount"])
            writer.writeheader()
            writer.writerows(self.expanses)
    def load_from_file(self):
        try:
            with open(self.filename, mode="r") as file:
                reader = csv.DictReader(file)
                self.expanses = list(reader)
        except FileNotFoundError:
            pass

expenses_tracker = ExpenseTracker()

while True:
    print("\nExpenses Tracker Menu: ")
    print("1. Add expenses")
    print("2. Display expenses")
    print("3. Exit")
    user_input = input("Enter your choice (1,2,3) : ")

    if user_input == '1':
        category = input("Input your Expense category: ")
        amount = float(input("Input your Expense: "))
        expenses_tracker.add_expense(category, amount)
    elif user_input == '2':
        expenses_tracker.display_expenses()

    elif user_input == "3":
        exit()
    else:
        print("Invalid choice. Enter correctly!!!\n")