#Project 2 — ATM Transaction Sequence Simulation
balance = 5000
transactions = []
print("Starting balance:", balance)
print("Enter D for deposit, W for withdrawal, X to stop")
while True:
    choice = input("Enter transaction type: ").upper()
    if choice == "X":
        break
    if choice != "D" and choice != "W":
        print("Invalid transaction type")
        continue
    amount = float(input("Enter amount: "))
    if amount <= 0:
        print("Amount must be positive")
    elif choice == "D":
        balance += amount
        transactions.append(("Deposit", amount))
        print("Deposit successful")
    elif amount > balance:
        print("Insufficient balance")
    else:
        balance -= amount
        transactions.append(("Withdrawal", amount))
        print("Withdrawal successful")
print("\nTransaction Summary")
for kind, amount in transactions:
    print(kind, ":", amount)
print("Final balance:", balance)