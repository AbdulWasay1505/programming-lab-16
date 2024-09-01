expenses = {}

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        category = input("Enter category: ")
        amount = float(input("Enter amount: "))
        expenses[category] = expenses.get(category, 0) + amount
    elif choice == "2":
        print("\nExpenses:")
        for category, amount in expenses.items():
            print(f"{category}: {amount}")
        print(f"\nTotal: {sum(expenses.values())}")
    elif choice == "3":
        break
    else:
        print("Invalid option. Please choose again.")