# 🛠 Day 4 Ultimate Loops Project – Mini Game Center

# Goal:
# User ko ek game menu milega jisme wo 3 mini-games choose karega:

# Multiplication Table (for loop)

# Countdown Timer (while loop + break)

# Pattern Maker (nested loops + continue)

import time

print("🎮 Welcome to Mini Game Center 🎮")

while True:
    print("\nMenu")
    print("1. Multiplication Table")
    print("2. Countdown Timer")
    print("3. Pattern Maker")
    print("4. Exit")

    choice = input("Choose a game (1-4): ")

    if choice == "1":
        num = int(input("Enter a number for Table: "))
        for i in range(1, 11):
            print(num, "x", i, "=", num * i)

    elif choice == "2":
        start = int(input("Enter countdown start number: "))
        while start >= 0:
            print(start)
            time.sleep(1)  # 1 second pause
            start -= 1
        print("⏰ Time's up!")

    elif choice == "3":
        rows = int(input("Enter number of rows: "))
        for i in range(1, rows + 1):
            if i == 3:
                print("(Row 3 skipped)")
                continue
            for j in range(1, i + 1):
                print("*", end=" ")
            print()

    elif choice == "4":
        print("👋 Thanks for playing!")
        break

    else:
        print("❌ Invalid choice! Try again.")
