import random

print("=== Welcome to the Math Quiz ===")
print("Type 'exit' anytime to quit the game.\n")

while True:
    # Random numbers generate karna
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)

    # Random operation choose karna
    operation = random.choice(["+", "-", "*"])

    # Sahi answer nikalna
    if operation == "+":
        correct_answer = num1 + num2
    elif operation == "-":
        correct_answer = num1 - num2
    else:
        correct_answer = num1 * num2

    # Question
    user_input = input(f"What is {num1} {operation} {num2}? ")

    # Exit check
    if user_input.lower() == "exit":
        print(" Thanks for playing! Goodbye.")
        break

    # Answer check (string → int)
    if user_input.isdigit() or (user_input.startswith('-') and user_input[1:].isdigit()):
        user_answer = int(user_input)
        if user_answer == correct_answer:
            print("Correct! Well done.\n")
        else:
            print(f" Wrong! The correct answer is {correct_answer}.\n")
    else:
        print("⚠ Please enter a valid number or 'exit' to quit.\n")
