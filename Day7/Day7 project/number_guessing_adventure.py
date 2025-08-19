import random
import time

print("🌟 Welcome to Number Guessing Adventure 🌟")
print("""
Rules:
1. Guess the secret number in given range.
2. You have limited tries per level.
3. Number 13 is cursed — it skips your turn!
""")

level = 1
score = 0

while True:
    number_range = level * 10  # Difficulty increases
    secret_number = random.randint(1, number_range)
    attempts = max(3, 7 - level)  # Tries decrease with levels

    print(f"\n🎯 Level {level}")
    print(f"Guess a number between 1 and {number_range}")
    print(f"You have {attempts} attempts.")

    for attempt in range(1, attempts + 1):
        guess = int(input(f"Attempt {attempt}/{attempts} → Enter your guess: "))

        if guess == 13:
            print("⚠️ Cursed number! Turn skipped...")
            continue

        if guess == secret_number:
            print("✅ Correct! Moving to next level...")
            score += 10 * level
            level += 1
            break

        else:
            print("❌ Wrong guess! Countdown before next attempt:")
            countdown = 3
            while countdown > 0:
                print(countdown, end=" ", flush=True)
                time.sleep(1)
                countdown -= 1
            print()

    else:
        print(f"💀 Game Over! The number was {secret_number}")
        print(f"🏆 Your final score: {score}")
        break

print("👋 Thanks for playing!")
