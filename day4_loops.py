for variable in range("start, end, step"):
    # code yahan likho
    for i in range(5):  # 0 se 4 tak
        print(i)


# while loop
while condition:
    # code


count = 1
while count <= 5:
    print(count)
    count += 1

# Example 2: User se input lete raho jab tak wo 'stop' na likhe


command = ""
while command != "stop":
    command = input("Type 'stop' to end: ")


# 4. break aur continue

# break → loop ko turant band kar deta hai.

# # continue → current step skip karta hai aur agle step par chala jata hai

for i in range(1, 10):
    if i == 5:
        break  # loop yahan ruk jayega
    print(i)



