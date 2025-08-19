# Mini Banking System 

import json
import os

# File to store user data
DATA_FILE = "bank_users.json"

# Load user data from file
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    else:
        return {}

# Save user data to file
def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

# Create a new account
def create_account(data):
    print("\n--- Create New Account ---")
    username = input("Enter username: ")
    if username in data:
        print("Account already exists!")
        return
    password = input("Enter password: ")
    data[username] = {"password": password, "balance": 0.0}
    save_data(data)
    print(f"Account for '{username}' created successfully!\n")

# Login to account
def login(data):
    print("\n--- Login ---")
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in data and data[username]["password"] == password:
        print(f"Welcome, {username}!\n")
        return username
    else:
        print("Invalid username or password!\n")
        return None

# Check balance
def check_balance(data, username):
    print(f"Your current balance is: ${data[username]['balance']:.2f}\n")

# Deposit money
def deposit(data, username):
    amount = float(input("Enter amount to deposit: $"))
    if amount > 0:
        data[username]["balance"] += amount
        save_data(data)
        print(f"${amount:.2f} deposited successfully!\n")
    else:
        print("Invalid amount!\n")

# Withdraw money
def withdraw(data, username):
    amount = float(input("Enter amount to withdraw: $"))
    if amount <= data[username]["balance"] and amount > 0:
        data[username]["balance"] -= amount
        save_data(data)
        print(f"${amount:.2f} withdrawn successfully!\n")
    else:
        print("Insufficient balance or invalid amount!\n")

# Main banking menu
def banking_system():
    data = load_data()
    while True:
        print("=== Mini Banking System ===")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            create_account(data)
        elif choice == "2":
            user = login(data)
            if user:
                while True:
                    print("1. Check Balance")
                    print("2. Deposit Money")
                    print("3. Withdraw Money")
                    print("4. Logout")
                    action = input("Choose action: ")
                    if action == "1":
                        check_balance(data, user)
                    elif action == "2":
                        deposit(data, user)
                    elif action == "3":
                        withdraw(data, user)
                    elif action == "4":
                        print(f"Logging out {user}...\n")
                        break
                    else:
                        print("Invalid option!\n")
        elif choice == "3":
            print("Exiting... Thank you!")
            break
        else:
            print("Invalid choice! Try again.\n")

# Run the banking system
if __name__ == "__main__":
    banking_system()
