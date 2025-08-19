import json
from accounts import load_data, save_data

def check_balance(user_id):
    data = load_data()
    balance = data["users"][user_id]["balance"]
    print(f"\n💰 Your current balance: {balance} PKR")
    return balance

def deposit(user_id, amount):
    data = load_data()
    data["users"][user_id]["balance"] += amount
    data["users"][user_id]["transactions"].append(f"Deposited {amount} PKR")
    save_data(data)
    print(f"\n✅ {amount} PKR deposited successfully.")
    check_balance(user_id)

def withdraw(user_id, amount):
    data = load_data()
    if amount > data["users"][user_id]["balance"]:
        print("\n❌ Insufficient balance!")
    else:
        data["users"][user_id]["balance"] -= amount
        data["users"][user_id]["transactions"].append(f"Withdrawn {amount} PKR")
        save_data(data)
        print(f"\n✅ {amount} PKR withdrawn successfully.")
        check_balance(user_id)

def transaction_history(user_id):
    data = load_data()
    print("\n--- Transaction History ---")
    if data["users"][user_id]["transactions"]:
        for t in data["users"][user_id]["transactions"]:
            print(t)
    else:
        print("No transactions yet.")
