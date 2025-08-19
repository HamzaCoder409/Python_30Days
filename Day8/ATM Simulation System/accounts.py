import json

DB_FILE = "database.json"

def load_data():
    with open(DB_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=4)

def register_account():
    data = load_data()
    user_id = input("Enter ATM Number or Email: ")
    if user_id in data["users"]:
        print("❌ Account already exists!")
        return
    pin = input("Set a 4-digit PIN: ")
    balance = float(input("Enter initial deposit amount: "))
    data["users"][user_id] = {
        "pin": pin,
        "balance": balance,
        "transactions": []
    }
    save_data(data)
    print("✅ Account created successfully!")

def verify_account():
    data = load_data()
    user_id = input("Enter ATM Number or Email: ")
    if user_id not in data["users"]:
        print("❌ Account not found!")
        return None
    attempts = 3
    while attempts > 0:
        pin = input("Enter your PIN: ")
        if pin == data["users"][user_id]["pin"]:
            print("✅ Access Granted!")
            return user_id
        else:
            attempts -= 1
            print(f"❌ Incorrect PIN! Attempts left: {attempts}")
    print("🚨 Too many wrong attempts! Account locked.")
    return None
