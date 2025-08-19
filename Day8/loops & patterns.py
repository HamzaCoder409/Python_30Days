# 1. Nested Loops

# Loop ke andar loop.

for i in range(3):        # Outer loop
    for j in range(2):    # Inner loop
        print(f"i={i}, j={j}")





# 2. Simple Pattern (Stars)



for i in range(5):
    print("*" * (i+1))




# 3. Inverted Pattern



for i in range(5, 0, -1):
    print("*" * i)



# 4. Number Pattern



for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end=" ")
    print()


# 5. Right-Aligned Triangle



for i in range(1, 6):
    print(" " * (5 - i) + "*" * i)

