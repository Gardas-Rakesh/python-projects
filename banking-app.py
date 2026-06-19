balance=0.0
transactions = [ ]


def check_balance():
    print(f"Your current balance is: {balance}")
def deposit(amount):
    global balance
    balance += amount
    transactions.append(f"Deposited:{amount}")
    print(f"Deposited Successfull:{amount}.  your's New balance:{balance}")

def withdraw(amount):
    global balance
    if amount > balance:
        print("Insufficient funds. Withdrawal failed.")
    else:
        balance -= amount
        transactions.append(f"Withdrew:{amount}")
        print(f"Withdrawal successful: {amount}. Your new balance: {balance}")
def transaction_history():
    if not transactions:
        print("No transactions yet.")
    else:
        print("----Transaction History-----")
        for t in transactions:
            print(t)

def menu():
    while True:
        print("Welcome to the Banking App")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. transaction history")
        print("5.Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            check_balance()
        elif choice == '2':
            amount = float(input("Enter the amount to deposit: "))
            deposit(amount)
        elif choice == '3':
            amount = float(input("Enter the amount to withdraw: "))
            withdraw(amount)
        elif choice == '4':
            transaction_history()
        elif choice == '5':
            print("Thank you for using the Banking App!")
            break
        else:
            print("Invalid choice. Please try again.")
menu()