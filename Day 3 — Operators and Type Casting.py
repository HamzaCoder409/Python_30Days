# Step 1) Arithmetic Operators **(+ - * / // % )

print(7 + 3)      # 10
print(7 - 3)      # 4
print(7 * 3)      # 21
print(7 / 3)      # 2.3333333333333335
print(7 // 3)     # 2
print(7 % 3)      # 1
print(2 ** 5)     # 32


# Step 2) Comparison Operators (== != > < >= <=)

print(5 == 5)   # True
print(5 != 3)   # True
print(7 > 9)    # False
print(2 <= 2)   # True


# Step 3) Logical Operators (and, or, not)

is_adult = True
has_cnic = False

print(is_adult and has_cnic)  # False
print(is_adult or has_cnic)   # True
print(not is_adult)           # False

# Step 4) Assignment Operators **(=, +=, -=, *=, /=, //=, %=, =)

x = 10     # assign
x += 5     # x = x + 5  -> 15
x -= 3     # 12
x *= 2     # 24
x /= 4     # 6.0
x //= 2    # 3
x %= 2     # 1
x = 3
x **= 3    # 27
print(x)


# Step 5) Type Casting (int(), float(), str())

a = "10"
b = "20"
print(a + b)          # "1020" (string concatenation)

a = int(a)
b = int(b)
print(a + b)          # 30 (now integers)


price = float(input("Enter price: "))       # user types 199.99
qty   = int(input("Enter quantity: "))      # user types 3
total = price * qty
print("Total:", total)                      # Total: 599.97


# Step 6) Operator Precedence (Order of Operations)

print(2 + 3 * 4)        # 14 (3*4 first)
print((2 + 3) * 4)      # 20
print(2 ** 3 ** 2)      # 512 (3**2 first -> 9, then 2**9)
print((2 ** 3) ** 2)    # 64





