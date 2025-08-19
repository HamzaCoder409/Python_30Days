# Heavy Currency Converter

def show_currencies():
    print("\nAvailable Currencies:")
    for code in rates.keys():
        print(f"{code} - {currencies[code]}")
    print()

# Currency data (simulated exchange rates)
currencies = {
    "USD": "US Dollar",
    "EUR": "Euro",
    "PKR": "Pakistani Rupee",
    "GBP": "British Pound",
    "JPY": "Japanese Yen"
}

# Exchange rates relative to USD
rates = {
    "USD": 1.0,
    "EUR": 0.93,
    "PKR": 342.0,
    "GBP": 0.81,
    "JPY": 142.0
}

# Convert currency
def convert(amount, from_currency, to_currency):
    try:
        # Convert from source to USD
        amount_in_usd = amount / rates[from_currency]
        # Convert from USD to target currency
        converted = amount_in_usd * rates[to_currency]
        return converted
    except KeyError:
        return None

# Main converter system
def currency_converter():
    print("=== Welcome to Currency Converter ===")
    while True:
        show_currencies()
        from_curr = input("Convert from (currency code): ").upper()
        to_curr = input("Convert to (currency code): ").upper()
        
        if from_curr not in rates or to_curr not in rates:
            print("Invalid currency code! Try again.\n")
            continue
        
        try:
            amount = float(input(f"Enter amount in {from_curr}: "))
            if amount <= 0:
                print("Amount must be positive!\n")
                continue
        except ValueError:
            print("Invalid amount! Enter a number.\n")
            continue
        
        result = convert(amount, from_curr, to_curr)
        if result is not None:
            print(f"{amount:.2f} {from_curr} = {result:.2f} {to_curr}\n")
        else:
            print("Conversion error! Try again.\n")
        
        again = input("Do you want to convert again? (yes/no): ").lower()
        if again != "yes":
            print("Exiting Currency Converter. Goodbye!")
            break

# Run the converter
if __name__ == "__main__":
    currency_converter()
