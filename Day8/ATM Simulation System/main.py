from accounts import register_account, verify_account
from transactions import check_balance, deposit, withdraw, transaction_history

def atm_menu(user_id):
    while True:
        print("\n--- ATM Menu ---")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transaction History")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            check_balance(user_id)
        elif choice == "2":
            amount = float(input("Enter amount to deposit: "))
            deposit(user_id, amount)
        elif choice == "3":
            amount = float(input("Enter amount to withdraw: "))
            withdraw(user_id, amount)
        elif choice == "4":
            transaction_history(user_id)
        elif choice == "5":
            print("\nThank you for using Hamza's ATM. Goodbye! 👋")
            break
        else:
            print("\n❌ Invalid option! Please try again.")

def main():
    print("=== Welcome to Hamza's Heavy ATM Platform 🏦 ===")
    while True:
        print("\n1. Register New Account")
        print("2. Login to Existing Account")
        print("3. Exit")
        choice = input("Choose an option (1-3): ")

        if choice == "1":
            register_account()
        elif choice == "2":
            user_id = verify_account()
            if user_id:
                atm_menu(user_id)
        elif choice == "3":
            print("Goodbye! 👋")
            break
        else:
            print("❌ Invalid option! Try again.")

if __name__ == "__main__":
    main()
