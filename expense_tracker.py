from datetime import datetime

expenses = []

try:

    file = open("expenses.txt", "r")

    for line in file:

        parts = line.strip().split(" | ")

        date = parts[0]

        item_part = parts[1]

        item, amount = item_part.split(": $")

        expenses.append((date, item, float(amount)))

    file.close()

except:

    pass

while True:

    print("\n=== Expense Tracker ===")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("\nChoose option: ").strip()

    if choice == "1":

        item = input("Expense name: ")

        amount = float(input("Expense amount: "))

        date = str(datetime.now().date())

        expenses.append((date, item, amount))

        file = open("expenses.txt", "a")

        file.write(f"{date} | {item}: ${amount}\n")

        file.close()

        print("Expense added and saved.")

    elif choice == "2":

        print("\n=== Expenses ===")

        total = 0

        for date, item, amount in expenses:

            print(f"{date} | {item}: ${amount}")

            total += amount

        print(f"\nTotal Spent: ${total}")

        if len(expenses) > 0:

            highest = max(expenses, key=lambda x: x[2])

            print(f"Highest Expense: {highest[1]} - ${highest[2]}")

    elif choice == "3":

        print("Tracker closed.")

        break

    else:

        print("Invalid option.")
