# # CONDITIONALS CHEAT SHEET

# # Basic if
# if condition:
#     # code

# # if-else
# if condition:
#     # code
# else:
#     # code

# # if-elif-else
# if condition1:
#     # code
# elif condition2:
#     # code
# else:
#     # code

# # Nested if
# if condition1:
#     if condition2:
#         # code

# # Multiple conditions
# if condition1 and condition2:  # Both must be True
# if condition1 or condition2:   # At least one must be True
# if not condition:              # Reverse the condition

# # Comparison operators
# ==    # Equal to
# !=    # Not equal to
# >     # Greater than
# <     # Less than
# >=    # Greater than or equal to
# <=    # Less than or equal to

# # Membership operators
# in        # Exists in sequence
# not in    # Does not exist in sequence

# # Identity operators
# is        # Same object
# is not    # Different object

# # Ternary operator
# value_if_true if condition else value_if_false

# # Pass statement (placeholder)
# if condition:
#     pass  # Do nothing


# CONDITIONAL STATEMENTS IN PYTHON

# ========== IF STATEMENT ==========
print("=== IF STATEMENT ===\n")

# Basic if
age = 18
if age >= 18:
    print("You are eligible to vote")

# If with single line
if age >= 18: print("You can drive")

print()

# ========== IF-ELSE STATEMENT ==========
print("=== IF-ELSE STATEMENT ===\n")

age = 16
if age >= 18:
    print("You are adult")
else:
    print("You are minor")

# Example
marks = 75
if marks >= 33:
    print("You passed!")
else:
    print("You failed!")

print()

# ========== IF-ELIF-ELSE STATEMENT ==========
print("=== IF-ELIF-ELSE STATEMENT ===\n")

# Grade calculator
marks = 85

if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
else:
    grade = "F"

print(f"Marks: {marks}")
print(f"Grade: {grade}")
print()

# Another example
temperature = 30

if temperature > 35:
    print("It's very hot!")
elif temperature > 25:
    print("It's warm")
elif temperature > 15:
    print("It's cool")
else:
    print("It's cold!")

print()

# ========== NESTED CONDITIONS ==========
print("=== NESTED CONDITIONS ===\n")

age = 25
has_license = True

if age >= 18:
    print("You are old enough")
    if has_license:
        print("You can drive")
    else:
        print("But you need a license first")
else:
    print("You cannot drive")

print()

# ========== MULTIPLE CONDITIONS ==========
print("=== MULTIPLE CONDITIONS ===\n")

# AND operator (both conditions must be True)
age = 20
has_id = True

if age >= 18 and has_id:
    print("You can enter the club")
else:
    print("You cannot enter")

# OR operator (at least one condition must be True)
is_weekend = True
is_holiday = False

if is_weekend or is_holiday:
    print("No work today!")
else:
    print("Time to work")

# NOT operator (reverses the condition)
is_raining = False

if not is_raining:
    print("You can go outside")
else:
    print("Take an umbrella")

print()

# ========== PRACTICAL EXAMPLES ==========
print("=== PRACTICAL EXAMPLES ===\n")

# Example 1: Even or Odd
print("1. Even or Odd:")
num = 7
if num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")
print()

# Example 2: Positive, Negative, or Zero
print("2. Number type:")
num = -5
if num > 0:
    print(f"{num} is positive")
elif num < 0:
    print(f"{num} is negative")
else:
    print("Number is zero")
print()

# Example 3: Leap Year
print("3. Leap Year Checker:")
year = 2024
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
print()

# Example 4: Largest of three numbers
print("4. Largest of three numbers:")
a, b, c = 10, 25, 15
if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c
print(f"Numbers: {a}, {b}, {c}")
print(f"Largest: {largest}")
print()

# Example 5: Login system
print("5. Login System:")
username = "admin"
password = "1234"

input_user = "admin"
input_pass = "1234"

if input_user == username and input_pass == password:
    print("Login successful!")
elif input_user != username:
    print("Invalid username")
else:
    print("Invalid password")
print()

# Example 6: Discount calculator
print("6. Discount Calculator:")
amount = 5000
if amount >= 5000:
    discount = 20
elif amount >= 3000:
    discount = 15
elif amount >= 1000:
    discount = 10
else:
    discount = 0

final_amount = amount - (amount * discount / 100)
print(f"Original amount: ₹{amount}")
print(f"Discount: {discount}%")
print(f"Final amount: ₹{final_amount}")
print()

# Example 7: Vowel or Consonant
print("7. Vowel or Consonant:")
char = 'a'
if char in 'aeiouAEIOU':
    print(f"'{char}' is a vowel")
else:
    print(f"'{char}' is a consonant")
print()

# Example 8: Triangle type
print("8. Triangle Type:")
side1, side2, side3 = 5, 5, 5
if side1 == side2 == side3:
    print("Equilateral triangle")
elif side1 == side2 or side2 == side3 or side1 == side3:
    print("Isosceles triangle")
else:
    print("Scalene triangle")
print()

# Example 9: Calculator
print("9. Simple Calculator:")
num1, num2 = 10, 5
operator = '+'

if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero"
else:
    result = "Invalid operator"

print(f"{num1} {operator} {num2} = {result}")
print()

# Example 10: Grade with remarks
print("10. Student Grade with Remarks:")
marks = 85
if marks >= 90:
    grade = "A+"
    remark = "Excellent!"
elif marks >= 75:
    grade = "A"
    remark = "Very Good!"
elif marks >= 60:
    grade = "B"
    remark = "Good"
elif marks >= 45:
    grade = "C"
    remark = "Average"
elif marks >= 33:
    grade = "D"
    remark = "Pass"
else:
    grade = "F"
    remark = "Fail - Need improvement"

print(f"Marks: {marks}")
print(f"Grade: {grade}")
print(f"Remark: {remark}")
print()

# ========== TERNARY OPERATOR (Condition in one line) ==========
print("=== TERNARY OPERATOR ===\n")

# Syntax: value_if_true if condition else value_if_false

age = 20
status = "Adult" if age >= 18 else "Minor"
print(f"Age {age}: {status}")

# Example
num = 7
result = "Even" if num % 2 == 0 else "Odd"
print(f"{num} is {result}")

# Multiple ternary
marks = 75
grade = "Pass" if marks >= 33 else "Fail"
print(f"Marks {marks}: {grade}")
print()

# ========== CONDITIONS WITH LISTS ==========
print("=== CONDITIONS WITH LISTS ===\n")

fruits = ["apple", "banana", "orange"]

# Check if item exists
if "apple" in fruits:
    print("Apple is in the list")

# Check if list is empty
my_list = []
if my_list:
    print("List has elements")
else:
    print("List is empty")

# Check length
if len(fruits) > 2:
    print("More than 2 fruits")
print()

# ========== CONDITIONS WITH DICTIONARIES ==========
print("=== CONDITIONS WITH DICTIONARIES ===\n")

student = {"name": "John", "age": 20}

# Check if key exists
if "name" in student:
    print(f"Name: {student['name']}")

# Check if value exists
if 20 in student.values():
    print("Age 20 exists")

# Check if dictionary is empty
empty_dict = {}
if empty_dict:
    print("Dict has items")
else:
    print("Dict is empty")
print()

# ========== CONDITIONS WITH STRINGS ==========
print("=== CONDITIONS WITH STRINGS ===\n")

text = "Hello World"

# Check if string starts with
if text.startswith("Hello"):
    print("Starts with Hello")

# Check if string ends with
if text.endswith("World"):
    print("Ends with World")

# Check if string contains
if "lo Wo" in text:
    print("Contains 'lo Wo'")

# Check if string is empty
empty_string = ""
if empty_string:
    print("String has content")
else:
    print("String is empty")

# Check if string is numeric
num_str = "123"
if num_str.isdigit():
    print(f"'{num_str}' is numeric")
print()

# ========== COMBINING MULTIPLE CONDITIONS ==========
print("=== COMBINING MULTIPLE CONDITIONS ===\n")

age = 25
income = 50000
credit_score = 750

# Complex condition
if age >= 21 and age <= 60 and income >= 30000 and credit_score >= 700:
    print("Eligible for loan")
elif age < 21:
    print("Too young for loan")
elif age > 60:
    print("Too old for loan")
elif income < 30000:
    print("Income too low")
elif credit_score < 700:
    print("Credit score too low")
else:
    print("Not eligible")
print()

# ========== SHORT-CIRCUIT EVALUATION ==========
print("=== SHORT-CIRCUIT EVALUATION ===\n")

def check_first():
    print("Checking first condition")
    return True

def check_second():
    print("Checking second condition")
    return False

# AND - stops at first False
print("AND operator:")
if check_first() and check_second():
    print("Both true")
else:
    print("At least one false")

# OR - stops at first True
print("\nOR operator:")
if check_first() or check_second():
    print("At least one true")
print()

# ========== PASS STATEMENT ==========
print("=== PASS STATEMENT ===\n")

# Pass is used when you need a statement but don't want to do anything
age = 18
if age >= 18:
    pass  # TODO: Add logic later
else:
    print("Too young")
print("Code continues...")