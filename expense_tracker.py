expenses = []
while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total Expense")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter expense name: ")
        amount = float(input("Enter amount: "))
        expenses.append((name, amount))
        print("Expense added successfully.")

    elif choice == "2":
        if not expenses:
            print("No expenses recorded.")
        else:
            print("\nExpenses:")
            for name, amount in expenses:
                print(f"{name} : ₹{amount}")

    elif choice == "3":
        total = sum(amount for _, amount in expenses)
        print(f"\nTotal Expense: ₹{total}")

    elif choice == "4":
        print("Thank you for using Expense Tracker.")
        break

    else:
        print("Invalid choice. Please try again.")
