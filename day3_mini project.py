print("== Student Report Card ==")

# variable + input

name = input("Enter your name: ") #string
age = int(input("Enter your age: ")) #int

# Data type (list of marks)

subjects = ["Math", "English", "Science", "History", "Geography"]
marks = []

for subject in subjects:
    score = float(input(f"Enter marks for {subject}: (out of 100) "))
    marks.append(score)

# operators

total_marks = sum(marks)
percentage = (total_marks / (len(subjects) * 100)) * 100 

# Condtionals for grades

if percentage >= 95:
    grade = "A+"

elif percentage >= 90:
    grade = "A-"

elif percentage >= 85:
    grade = "A"

elif percentage >= 82:
    grade = "B+"

elif percentage >= 80:
    grade = "B-"

elif percentage >= 75:
    grade = "B"  

elif percentage >= 70:
    grade = "C+"

elif percentage >= 65:
    grade = "C-"

elif percentage >= 60:
    grade = "C"

elif percentage >= 55:
    grade = "D+"

elif percentage >= 50:
    grade = "D"

else:
    grade = "F"


# output

print ("== Final Report == ")    
print (f"Name: {name}")
print (f"Age: {age}")
print(f"Total Marks: {total_marks}")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")

# Pass/Fail

if grade != "F":
    print("Status: pass")

else:
    print("Status: fail")




