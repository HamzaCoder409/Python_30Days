# Exercise 1: Function to return maximum number from a list

# Step 1: Define a function
# Step 2: Use a loop to compare numbers
# Step 3: Return the maximum number



def max_in_list(numbers):
    max_num = numbers[0]  # Assume first number is max
    for num in numbers:
        if num > max_num:
            max_num = num  # Update if we find a bigger number
    return max_num

my_list = [10, 5, 22, 8, 15]
print("Maximum number is:", max_in_list(my_list))


# Exercise 2: Function to print student name and age from dictionary

# Step 1: Function me dictionary pass karein
# Step 2: Print keys name aur age


def student_info(student):
    print("Name:", student["name"])
    print("Age:", student["age"])

student1 = {"name": "Hamza", "age": 20}
student_info(student1)



# Exercise 3: Function to check if number is prime

# Step 1: Function define karein aur check 2 se start karein
# Step 2: Loop me divide kar ke check karein
# Step 3: Return True/False


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

print(is_prime(7))   # True
print(is_prime(10))  # False




# Exercise 4: Nested function example

# Step 1: Outer function define karein
# Step 2: Inner function define karein
# Step 3: Inner function ko call karein

def greet_user(name):
    def inner_greet():
        print("Hello", name)
    inner_greet()

greet_user("Hamza")
