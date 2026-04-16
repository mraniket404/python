# LISTS IN PYTHON

# LIST METHODS CHEAT SHEET

# # Adding elements
# list.append(x)        # Add at end
# list.insert(i, x)     # Add at index i
# list.extend(iterable) # Add multiple elements

# # Removing elements
# list.remove(x)        # Remove first occurrence of x
# list.pop(i)           # Remove and return index i
# list.clear()          # Remove all elements

# # Information
# list.index(x)         # Return index of first x
# list.count(x)         # Count occurrences of x
# len(list)             # Get length

# # Ordering
# list.sort()           # Sort ascending
# list.sort(reverse=True) # Sort descending
# list.reverse()        # Reverse the list

# # Copying
# list.copy()           # Create shallow copy

# # Common operations
# x in list             # Check if exists
# list1 + list2         # Concatenate
# list * n              # Repeat n times

# ========== CREATING LISTS ==========
print("=== CREATING LISTS ===")

# Empty list
my_list = []
print(f"Empty list: {my_list}")

# List with elements
fruits = ["apple", "banana", "orange"]
print(f"Fruits: {fruits}")

# Mixed data types
mixed = [1, "hello", 3.14, True]
print(f"Mixed list: {mixed}")

# Using list() constructor
numbers = list((1, 2, 3, 4, 5))
print(f"Using list(): {numbers}")

# List comprehension
squares = [x**2 for x in range(5)]
print(f"Squares: {squares}")

print("\n" + "="*50 + "\n")

# ========== LIST METHODS ==========
print("=== LIST METHODS ===\n")

# 1. append() - Add element at the end
print("1. append()")
fruits = ["apple", "banana"]
fruits.append("orange")
print(f"After append: {fruits}")
print()

# 2. insert() - Add element at specific position
print("2. insert()")
fruits = ["apple", "banana", "orange"]
fruits.insert(1, "mango")  # Insert at index 1
print(f"After insert: {fruits}")
print()

# 3. extend() - Add multiple elements
print("3. extend()")
fruits = ["apple", "banana"]
more_fruits = ["orange", "mango"]
fruits.extend(more_fruits)
print(f"After extend: {fruits}")
print()

# 4. remove() - Remove first occurrence
print("4. remove()")
fruits = ["apple", "banana", "apple", "orange"]
fruits.remove("apple")  # Removes first 'apple'
print(f"After remove: {fruits}")
print()

# 5. pop() - Remove and return element at index
print("5. pop()")
fruits = ["apple", "banana", "orange"]
removed = fruits.pop(1)  # Removes index 1
print(f"Removed: {removed}")
print(f"List after pop: {fruits}")
print()

# 6. clear() - Remove all elements
print("6. clear()")
fruits = ["apple", "banana", "orange"]
fruits.clear()
print(f"After clear: {fruits}")
print()

# 7. index() - Find index of element
print("7. index()")
fruits = ["apple", "banana", "orange"]
index = fruits.index("banana")
print(f"Index of 'banana': {index}")
print()

# 8. count() - Count occurrences
print("8. count()")
fruits = ["apple", "banana", "apple", "orange", "apple"]
count = fruits.count("apple")
print(f"Count of 'apple': {count}")
print()

# 9. sort() - Sort the list
print("9. sort()")
numbers = [3, 1, 4, 1, 5, 9, 2]
numbers.sort()  # Ascending
print(f"Ascending sort: {numbers}")

numbers.sort(reverse=True)  # Descending
print(f"Descending sort: {numbers}")

# Sort strings
fruits = ["banana", "apple", "orange", "mango"]
fruits.sort()
print(f"Sorted fruits: {fruits}")
print()

# 10. reverse() - Reverse the list
print("10. reverse()")
fruits = ["apple", "banana", "orange"]
fruits.reverse()
print(f"After reverse: {fruits}")
print()

# 11. copy() - Create a shallow copy
print("11. copy()")
original = [1, 2, 3]
copied = original.copy()
copied.append(4)
print(f"Original: {original}")
print(f"Copied: {copied}")
print()

print("="*50 + "\n")

# ========== LIST OPERATIONS ==========
print("=== LIST OPERATIONS ===\n")

# Accessing elements
fruits = ["apple", "banana", "orange", "mango"]
print(f"First element: {fruits[0]}")
print(f"Last element: {fruits[-1]}")
print(f"Slicing [1:3]: {fruits[1:3]}")
print()

# Changing elements
fruits[1] = "kiwi"
print(f"After change: {fruits}")
print()

# Concatenation
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print(f"Concatenated: {combined}")
print()

# Repetition
repeat = ["Hi"] * 3
print(f"Repetition: {repeat}")
print()

# Check if exists
fruits = ["apple", "banana", "orange"]
print(f"Is 'apple' in list? {'apple' in fruits}")
print(f"Is 'grape' in list? {'grape' in fruits}")
print()

# Length of list
print(f"Length of fruits: {len(fruits)}")
print()

# Loop through list
print("Looping through list:")
for fruit in fruits:
    print(f"  {fruit}")
print()

# ========== PRACTICAL EXAMPLES ==========
print("=== PRACTICAL EXAMPLES ===\n")

# Example 1: To-do list
todo = []
todo.append("Buy groceries")
todo.append("Clean room")
todo.append("Study Python")
print(f"Todo list: {todo}")
todo.remove("Clean room")
print(f"After completing task: {todo}")
print()

# Example 2: Student marks
marks = [85, 92, 78, 90, 88]
marks.sort()
print(f"Sorted marks: {marks}")
print(f"Highest mark: {marks[-1]}")
print(f"Lowest mark: {marks[0]}")
print(f"Average: {sum(marks)/len(marks)}")
print()

# Example 3: Remove duplicates
numbers = [1, 2, 2, 3, 3, 3, 4, 5, 5]
unique = []
for num in numbers:
    if num not in unique:
        unique.append(num)
print(f"Original: {numbers}")
print(f"Without duplicates: {unique}")