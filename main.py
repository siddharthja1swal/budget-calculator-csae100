"""
Project: Budget Calculator
Lead Developer: [SHUBHAM BATRA] (@ShubhamBatra23)
Implemented in Python using VS Code.
"""

# Calculate total monthly expenses
# can set monthly budget limit
# visualise the expense pictorialy
# can see complete expense list


import csv
import os
from datetime import datetime
import matplotlib.pyplot as plt

def add_expense():

    print("\n===== ADD NEW EXPENSE =====")

    amount = float(input("Enter amount (Rs.): "))

    if amount <= 0:
        print("Amount must be greater than zero!")
        return

    print("\nSelect Category:")
    print("1. Food")
    print("2. Clothes")
    print("3. Accessories")
    print("4. Sports")
    print("5. Travel")
    print("6. Entertainment")
    print("7. Education")
    print("8. Others")

    categories = {
        1: "Food",
        2: "Clothes",
        3: "Accessories",
        4: "Sports",
        5: "Travel",
        6: "Entertainment",
        7: "Education",
        8: "Others"
    }

    category_choice = int(input("Choose category: "))

    if category_choice not in categories:
        print("Invalid category!")
        return

    category = categories[category_choice]

    date = input("Enter date (DD-MM-YYYY): ")

    try:
        datetime.strptime(date, "%d-%m-%Y")
    except ValueError:
        print("Invalid date!")
        return

    description = input("Enter description: ")

    file_exists = os.path.isfile("expenses.csv")

    with open("expenses.csv", "a", newline="") as file:

        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["Amount", "Category", "Date", "Description"])

        writer.writerow([amount, category, date, description])

    print("\nExpense added successfully!")
    
def view_all_expenses():

    if not os.path.exists("expenses.csv"):
        print("\nNo expense records found!")
        return

    total = 0

    with open("expenses.csv", "r") as file:
        reader = csv.DictReader(file)

        print("\n===== ALL EXPENSES =====")

        count = 0

        for row in reader:

            print("\nAmount: ₹", row["Amount"])
            print("Category:", row["Category"])
            print("Date:", row["Date"])
            print("Description:", row["Description"])

            total += float(row["Amount"])
            count += 1

    if count == 0:
        print("\nNo expenses available!")
        return

    print("\n================================")
    print("TOTAL NUMBER OF EXPENSES:", count)
    print("GRAND TOTAL: ₹", total)
    print("================================")
        
def monthly_report():

    if not os.path.exists("expenses.csv"):
        print("\nNo expense records found!")
        return

    month = input("Enter month (MM): ")
    year = input("Enter year (YYYY): ")

    total = 0

    with open("expenses.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            expense_date = datetime.strptime(row["Date"], "%d-%m-%Y")

            if expense_date.strftime("%m") == month and expense_date.strftime("%Y") == year:
                total += float(row["Amount"])

    print("\n===== MONTHLY EXPENSE REPORT =====")
    print("Month:", month)
    print("Year:", year)
    print("Total Expense: ₹", total)
    
def category_analysis():

    if not os.path.exists("expenses.csv"):
        print("\nNo expense records found!")
        return

    category_totals = {}

    with open("expenses.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            category = row["Category"]
            amount = float(row["Amount"])

            if category in category_totals:
                category_totals[category] += amount
            else:
                category_totals[category] = amount

    print("\n===== CATEGORY-WISE EXPENSE ANALYSIS =====")

    for category, total in category_totals.items():
        print(category, ": ₹", total)
        
def spending_analysis():

    if not os.path.exists("expenses.csv"):
        print("\nNo expense records found!")
        return

    daily_expenses = {}

    with open("expenses.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            date = row["Date"]
            amount = float(row["Amount"])

            if date in daily_expenses:
                daily_expenses[date] += amount
            else:
                daily_expenses[date] = amount

    print("\n===== SPENDING PATTERN ANALYSIS =====")

    for date, total in sorted(daily_expenses.items(),
                              key=lambda item: datetime.strptime(item[0], "%d-%m-%Y")):
        print(date, ": ₹", total)

    if daily_expenses:
        highest_day = max(daily_expenses, key=daily_expenses.get)

        print("\nHighest Spending Day:", highest_day)
        print("Total Spent: ₹", daily_expenses[highest_day])
        
def set_budget():

    budget = float(input("\nEnter your monthly budget: ₹"))

    if budget <= 0:
        print("Please enter a valid budget!")
        return

    with open("budget.txt", "w") as file:
        file.write(str(budget))

    print("\nMonthly budget set successfully!")
    print("Your Monthly Budget: ₹", budget)
    
def detect_overspending():

    if not os.path.exists("budget.txt"):
        print("\nPlease set your monthly budget first using Option 6!")
        return

    if not os.path.exists("expenses.csv"):
        print("\nNo expense records found!")
        return

    with open("budget.txt", "r") as file:
        budget = float(file.read())

    current_month = datetime.now().strftime("%m")
    current_year = datetime.now().strftime("%Y")

    total_expense = 0

    with open("expenses.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            expense_date = datetime.strptime(row["Date"], "%d-%m-%Y")

            if (expense_date.strftime("%m") == current_month and
                    expense_date.strftime("%Y") == current_year):
                total_expense += float(row["Amount"])

    print("\n===== OVERSPENDING DETECTION =====")
    print("Monthly Budget: ₹", budget)
    print("Total Expenses: ₹", total_expense)

    if total_expense > budget:
        print("\nWARNING! You have exceeded your monthly budget.")
        print("Amount exceeded: ₹", total_expense - budget)

    else:
        remaining = budget - total_expense
        print("\nYou are within your monthly budget!")
        print("Remaining Budget: ₹", remaining)
        
def saving_suggestions():

    if not os.path.exists("expenses.csv"):
        print("\nNo expense records found!")
        return

    category_totals = {}

    with open("expenses.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            category = row["Category"]
            amount = float(row["Amount"])

            if category in category_totals:
                category_totals[category] += amount
            else:
                category_totals[category] = amount

    if not category_totals:
        print("\nNo expenses available for analysis!")
        return

    highest_category = max(category_totals, key=category_totals.get)
    highest_amount = category_totals[highest_category]
    
    print("\n===== SMART SAVING SUGGESTIONS =====")

    print("\nYour highest spending category is:", highest_category)
    print("Total spent: ₹", highest_amount)

    print("\nSUGGESTIONS:")

    print("1. Try reducing unnecessary expenses in", highest_category)
    print("2. Compare prices before making purchases.")
    print("3. Set a spending limit for each category.")
    print("4. Avoid impulsive purchases.")
    print("5. Save a small amount from your monthly budget.")
    
def generate_graphs():

    if not os.path.exists("expenses.csv"):
        print("\nNo expense records found!")
        return

    category_totals = {}

    with open("expenses.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            category = row["Category"]
            amount = float(row["Amount"])

            if category in category_totals:
                category_totals[category] += amount
            else:
                category_totals[category] = amount

    if not category_totals:
        print("\nNo expenses available to generate graphs!")
        return

    categories = list(category_totals.keys())
    amounts = list(category_totals.values())

    # Pie Chart
    plt.figure(figsize=(7, 7))
    plt.pie(amounts, labels=categories, autopct="%1.1f%%")
    plt.title("Category-wise Expense Distribution")
    plt.show()

    # Bar Graph
    plt.figure(figsize=(8, 5))
    plt.bar(categories, amounts)
    plt.xlabel("Categories")
    plt.ylabel("Amount (₹)")
    plt.title("Category-wise Expense Comparison")
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.show()
    
def new_record():

    print("\n===== START A NEW RECORD =====")

    if os.path.exists("expenses.csv"):

        confirm = input("Are you sure? All previous expenses will be deleted (yes/no): ")

        if confirm.lower() == "yes":
            os.remove("expenses.csv")
            print("\nPrevious expenses deleted successfully!")
            print("You can now start a fresh record.")

        else:
            print("\nNew record cancelled!")

    else:
        print("\nNo previous expenses found!")
        print("You can start adding new expenses.")

while True:

    print("\n==========================================")
    print("     SMART BUDGET & EXPENSE ANALYZER")
    print("==========================================")

    print("\n1. Add Expense")
    print("2. View All Expenses")
    print("3. Monthly Expense Report")
    print("4. Category-wise Analysis")
    print("5. Spending Pattern Analysis")
    print("6. Set Monthly Budget")
    print("7. Overspending Detection")
    print("8. Smart Saving Suggestions")
    print("9. Generate Expense Graphs")
    print("10. Exit")
    print("11. New Record")

    print("\n==========================================")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_expense()

    elif choice == 2:
        view_all_expenses()

    elif choice == 3:
        monthly_report()

    elif choice == 4:
        category_analysis()

    elif choice == 5:
        spending_analysis()

    elif choice == 6:
        set_budget()
    
    elif choice == 7:
        detect_overspending()

    elif choice == 8:
        saving_suggestions()

    elif choice == 9:
        generate_graphs()

    elif choice == 10:
        print("\nThank you for using Smart Budget & Expense Analyzer!")
        print("Your expense records are safely saved.")
        print("Have a great day!")
        break
    elif choice == 11:
        new_record()

    else:
        print("Invalid choice!")
