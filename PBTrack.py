from expense import Expense  
import calendar
import datetime
import os
import matplotlib.pyplot as plt


# Function to clear the console screen
def screen_clearence():
    os.system('cls' if os.name == 'nt' else 'clear')


# Function to display the menu
def display_menu():
    screen_clearence()
    print("Personal Budget Tracker")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Budget")
    print("4. Exit")


# Function to add income
def add_income(inc):
    amount = float(input("Enter the income amount: "))
    inc += amount
    print(f"Income of Rs{amount} added successfully!")
    return inc


# Function to add expense
def add_expense(expen):
    categories = input("Enter the category of expense: ")
    amount = float(input("Enter the expense amount: "))
    if categories in expen:
        expen[categories] += amount
    else:
        expen[categories] = amount
    print(f"Expense of Rs{amount} under '{categories}' added successfully!")
    return expen


# Function to view budget
def view_budget(inc, expen):
    total_expense = sum(expen.values())
    budget = inc - total_expense
    print("\nBudget Summary")
    print("--------------")
    print(f"Income: Rs{inc}")
    print("Expenses:")
    for category, amount in expen.items():
        print(f"{category}: Rs{amount}")
    print(f"Total Expense: Rs{total_expense}")
    print(f"Remaining Budget: Rs{budget}")


# Function to display expense analysis
def display_expense_analysis(expen):
    categories = list(expen.keys())
    amounts = list(expen.values())
    plt.figure(figsize=(8, 6))
    plt.pie(amounts, labels=categories, autopct='%1.1f%%')
    plt.title('Expense Analysis')
    plt.axis('equal')
    plt.show()


# Function to save data to file
def save_data(inc, expen):
    total_expense = sum(expen.values())
    remaining_budget = inc - total_expense

    with open("budget_data.txt", "w") as file:
        file.write(f"Income: {inc}\n")
        file.write("Expenses:\n")
        for category, amount in expen.items():
            file.write(f"{category}: {amount}\n")
        file.write(f"Remaining Budget: {remaining_budget}\n")


# Function to load data
def load_data():
    inc = 0
    expen = {}
    file_path = "budget_data.txt"
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            lines = file.readlines()
            if lines:  # Check if lines is not empty
                if lines[0].startswith("Income:"):
                    inc = float(lines[0].split(": ")[1])
                for line in lines[2:]:
                    if line.strip():  # Check if line is not empty
                        category, amount = line.split(": ")
                        expen[category] = float(amount)
    else:
        print("Data file not found. Creating a new file.")
        with open(file_path, "w") as file:
            file.write("Income: 0\n")
            file.write("Expenses:\n")
    return inc, expen


# Main function
def main():
    inc, expen = load_data()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            inc = add_income(inc)
        elif choice == "2":
            expen = add_expense(expen)
        elif choice == "3":
            view_budget(inc, expen)
            input("Press Enter to continue...")
            display_expense_analysis(expen)
        elif choice == "4":
            save_data(inc, expen)
            print("Data saved successfully!")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()