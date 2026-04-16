# TUPLES IN PYTHON

# # TUPLE METHODS CHEAT SHEET

# # Creating tuples
# tuple()               # Empty tuple
# (1, 2, 3)            # With parentheses
# 1, 2, 3              # Without parentheses (packing)
# (1,)                 # Single element (comma needed!)

# # Methods (only 2!)
# tuple.count(x)       # Count occurrences of x
# tuple.index(x)       # Find first index of x

# # Operations
# len(tuple)           # Get length
# x in tuple           # Check if exists
# tuple1 + tuple2      # Concatenate
# tuple * n            # Repeat n times
# tuple[i]             # Access element
# tuple[i:j]           # Slicing

# # Unpacking
# a, b, c = (1, 2, 3)  # Unpack tuple
# a, b = b, a          # Swap variables

# # Conversion
# list(tuple)          # Convert to list
# tuple(list)          # Convert to tuple

# # Key difference
# # List: MUTABLE (can change)
# # Tuple: IMMUTABLE (cannot change)

# ========== CREATING TUPLES ==========
print("=== CREATING TUPLES ===")

# Empty tuple
empty_tuple = ()
print(f"Empty tuple: {empty_tuple}")

# Tuple with elements
fruits = ("apple", "banana", "orange")
print(f"Fruits tuple: {fruits}")

# Without parentheses (tuple packing)
colors = "red", "green", "blue"
print(f"Without parentheses: {colors}")

# Single element tuple (note the comma)
single = ("hello",)  # Comma is necessary
print(f"Single element tuple: {single}")
print(f"Without comma would be string: {('hello')}")

# Mixed data types
mixed = (1, "hello", 3.14, True)
print(f"Mixed tuple: {mixed}")

# Using tuple() constructor
numbers = tuple([1, 2, 3, 4, 5])
print(f"Using tuple(): {numbers}")

print("\n" + "="*50 + "\n")

# ========== TUPLE METHODS ==========
print("=== TUPLE METHODS ===\n")

# Tuples have only 2 methods!

# 1. count() - Count occurrences of an element
print("1. count()")
numbers = (1, 2, 2, 3, 2, 4, 2, 5)
count = numbers.count(2)
print(f"Tuple: {numbers}")
print(f"Count of 2: {count}")

fruits = ("apple", "banana", "apple", "orange", "apple")
apple_count = fruits.count("apple")
print(f"Fruits: {fruits}")
print(f"Count of 'apple': {apple_count}")
print()

# 2. index() - Find first index of an element
print("2. index()")
fruits = ("apple", "banana", "orange", "mango")
index = fruits.index("orange")
print(f"Tuple: {fruits}")
print(f"Index of 'orange': {index}")

# With start and end parameters
numbers = (10, 20, 30, 40, 50, 30, 60)
index = numbers.index(30, 3, 6)  # Search between index 3 and 6
print(f"Numbers: {numbers}")
print(f"Index of 30 (between 3 and 6): {index}")
print()

print("="*50 + "\n")

# ========== TUPLE OPERATIONS ==========
print("=== TUPLE OPERATIONS ===\n")

# Accessing elements
fruits = ("apple", "banana", "orange", "mango")
print(f"First element: {fruits[0]}")
print(f"Last element: {fruits[-1]}")
print(f"Slicing [1:3]: {fruits[1:3]}")
print()

# Cannot change elements (IMMUTABLE)
fruits = ("apple", "banana", "orange")
print(f"Original tuple: {fruits}")
try:
    fruits[1] = "kiwi"  # This will give error
except TypeError as e:
    print(f"Cannot modify tuple: {e}")
print()

# Concatenation
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined = tuple1 + tuple2
print(f"Concatenated: {combined}")
print()

# Repetition
repeat = ("Hi",) * 3
print(f"Repetition: {repeat}")
print()

# Check if exists
fruits = ("apple", "banana", "orange")
print(f"Is 'apple' in tuple? {'apple' in fruits}")
print(f"Is 'grape' in tuple? {'grape' in fruits}")
print()

# Length of tuple
print(f"Length of fruits: {len(fruits)}")
print()

# Loop through tuple
print("Looping through tuple:")
for fruit in fruits:
    print(f"  {fruit}")
print()

# ========== TUPLE PACKING & UNPACKING ==========
print("=== TUPLE PACKING & UNPACKING ===\n")

# Packing
person = "John", 25, "New York"
print(f"Packed tuple: {person}")

# Unpacking
name, age, city = person
print(f"Unpacked:")
print(f"  Name: {name}")
print(f"  Age: {age}")
print(f"  City: {city}")
print()

# Swapping variables using tuples
a = 10
b = 20
print(f"Before swap: a={a}, b={b}")
a, b = b, a  # Tuple unpacking magic!
print(f"After swap: a={a}, b={b}")
print()

# Return multiple values from function
def get_student():
    name = "Alice"
    age = 22
    grade = "A"
    return name, age, grade  # Returns a tuple

student_info = get_student()
print(f"Returned tuple: {student_info}")
name, age, grade = get_student()
print(f"Unpacked: {name} is {age} years old, got grade {grade}")
print()

# ========== COMPARING LISTS VS TUPLES ==========
print("=== LISTS VS TUPLES ===\n")

# List is MUTABLE (can change)
my_list = [1, 2, 3]
print(f"List before: {my_list}")
my_list[1] = 99
print(f"List after change: {my_list}")
print()

# Tuple is IMMUTABLE (cannot change)
my_tuple = (1, 2, 3)
print(f"Tuple: {my_tuple}")
print("Cannot change tuple elements!")
print()

# ========== PRACTICAL EXAMPLES ==========
print("=== PRACTICAL EXAMPLES ===\n")

# Example 1: Days of week (constant data)
days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print(f"Days: {days}")
print(f"Weekend days: {days[5]}, {days[6]}")
print()

# Example 2: Coordinates
point = (10, 20)
x, y = point
print(f"Point coordinates: ({x}, {y})")
print()

# Example 3: RGB Colors
colors = {
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255)
}
print("RGB Colors:")
for color, rgb in colors.items():
    print(f"  {color}: {rgb}")
print()

# Example 4: Student database
students = [
    ("John", 85, "A"),
    ("Alice", 92, "A+"),
    ("Bob", 78, "B+")
]

print("Student Records:")
for name, marks, grade in students:
    print(f"  {name}: {marks} marks, Grade {grade}")
print()

# Example 5: Converting between list and tuple
my_list = [1, 2, 3, 4, 5]
print(f"List: {my_list}")

# List to tuple
my_tuple = tuple(my_list)
print(f"List to tuple: {my_tuple}")

# Tuple to list
new_list = list(my_tuple)
print(f"Tuple to list: {new_list}")
new_list.append(6)
print(f"Modified list: {new_list}")
print()

# Example 6: Using tuple as dictionary key (list cannot be used as key)
location = {
    (40.7128, 74.0060): "New York",
    (51.5074, 0.1278): "London",
    (48.8566, 2.3522): "Paris"
}
print("Dictionary with tuple keys:")
for coords, city in location.items():
    print(f"  {city}: {coords}")