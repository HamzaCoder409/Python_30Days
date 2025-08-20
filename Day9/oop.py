# 1. What is OOP? (OOP kya hota hai?)

# OOP = A way of programming that organizes code into objects.
# (OOP ek aisa tareeqa hai jo code ko objects me organize karta hai.)

# Objects = things that have properties (attributes) and actions (methods).
# (Objects wo cheezein hain jinke paas properties aur actions hoti hain.)


# Creating a Class (Class banana)
class Car:
    def __init__(self, brand, model):
        self.brand = brand   # property
        self.model = model   # property
    
    def drive(self):  # method
        print(f"{self.brand} {self.model} is driving...")


# Creating an Object (Object banana)
my_car = Car("Toyota", "Corolla")
print(my_car.brand)   # Output: Toyota
print(my_car.model)   # Output: Corolla

my_car.drive()        # Output: Toyota Corolla is driving...        