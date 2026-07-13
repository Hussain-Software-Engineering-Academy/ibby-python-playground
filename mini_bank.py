print("=== MINI BANK ===")
print("1. Check Balance")
print("2. Deposit Money")
print("3. Withdraw Money")
print("4. Exit")
balance = 100
while True:
    input_choice = input("Enter your choice (1-4): ")

    if input_choice == "1":
        print(f"Your current balance is: ${balance}")

    elif input_choice == "2":
        deposit = float(input("How much would you like to deposit? $"))
        balance = balance + deposit
        print(f"Your new balance is: ${balance}")

    elif input_choice == "3":
        withdraw = float(input("How much would you like to withdraw? $"))

        if withdraw > balance:
            print("Insufficient funds.")
        else:
            balance = balance - withdraw
            print(f"Your new balance is: ${balance}")

    elif input_choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")

print()