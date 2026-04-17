# # DICTIONARY METHODS CHEAT SHEET

# # Creating
# {}                          # Empty dict
# dict()                      # Empty dict
# {"key": "value"}           # With items
# dict(key="value")          # Using constructor

# # Adding/Updating
# dict[key] = value          # Add or update
# dict.update(other_dict)    # Merge another dict
# dict.setdefault(key, default) # Get or set

# # Removing
# del dict[key]              # Delete key
# dict.pop(key)              # Remove and return value
# dict.popitem()             # Remove and return last item
# dict.clear()               # Remove all items

# # Accessing
# dict[key]                  # Direct access (KeyError if missing)
# dict.get(key, default)     # Safe access
# dict.keys()                # Get all keys
# dict.values()              # Get all values
# dict.items()               # Get all (key, value) pairs

# # Copying
# dict.copy()                # Shallow copy

# # Creating from keys
# dict.fromkeys(keys, value) # Create dict from sequence

# # Checking
# key in dict                # Check if key exists
# len(dict)                  # Number of items

# # Looping
# for key in dict:           # Loop through keys
# for key, value in dict.items(): # Loop through items

# # Comprehension
# {x: x**2 for x in range(5)} # Dict comprehension

# # Merge (Python 3.9+)
# dict1 | dict2              # Merge dictionaries
# dict1 |= dict2             # Update dict1 with dict2


# DICTIONARY METHODS IN PYTHON

# ========== CREATING DICTIONARIES ==========
print("=== CREATING DICTIONARIES ===\n")

# Empty dictionary
empty_dict = {}
print(f"Empty dict: {empty_dict}")

# Using curly braces
student = {
    "name": "John",
    "age": 25,
    "city": "New York"
}
print(f"Student: {student}")

# Using dict() constructor
person = dict(name="Alice", age=30, city="London")
print(f"Using dict(): {person}")

# From list of tuples
pairs = [("a", 1), ("b", 2), ("c", 3)]
dict_from_pairs = dict(pairs)
print(f"From pairs: {dict_from_pairs}")

print("\n" + "="*60 + "\n")

# ========== DICTIONARY METHODS ==========
print("=== DICTIONARY METHODS ===\n")

# 1. clear() - Remove all items
print("1. clear()")
student = {"name": "John", "age": 25, "city": "NYC"}
print(f"Before clear: {student}")
student.clear()
print(f"After clear: {student}")
print()

# 2. copy() - Shallow copy
print("2. copy()")
original = {"name": "John", "age": 25, "hobbies": ["reading", "coding"]}
copied = original.copy()
print(f"Original: {original}")
print(f"Copied: {copied}")
# Modify copied
copied["name"] = "Jane"
copied["hobbies"].append("gaming")
print(f"After modifying copy:")
print(f"  Original: {original}")
print(f"  Copied: {copied}")
print()

# 3. fromkeys() - Create dict from keys
print("3. fromkeys()")
keys = ["name", "age", "city"]
default_dict = dict.fromkeys(keys, "unknown")
print(f"From keys with default: {default_dict}")

custom_dict = dict.fromkeys(["a", "b", "c"], 0)
print(f"Custom dict: {custom_dict}")
print()

# 4. get() - Get value with default if key not found
print("4. get()")
student = {"name": "John", "age": 25}
print(f"Student: {student}")
print(f"Get 'name': {student.get('name')}")
print(f"Get 'city' (not exists): {student.get('city')}")
print(f"Get 'city' with default: {student.get('city', 'Not Found')}")
print()

# 5. items() - Get all key-value pairs
print("5. items()")
student = {"name": "John", "age": 25, "city": "NYC"}
items = student.items()
print(f"Items: {items}")
print(f"Type: {type(items)}")
print("Looping through items:")
for key, value in student.items():
    print(f"  {key}: {value}")
print()

# 6. keys() - Get all keys
print("6. keys()")
student = {"name": "John", "age": 25, "city": "NYC"}
keys = student.keys()
print(f"Keys: {keys}")
print(f"Type: {type(keys)}")
print("Looping through keys:")
for key in student.keys():
    print(f"  {key}")
print()

# 7. values() - Get all values
print("7. values()")
student = {"name": "John", "age": 25, "city": "NYC"}
values = student.values()
print(f"Values: {values}")
print(f"Type: {type(values)}")
print("Looping through values:")
for value in student.values():
    print(f"  {value}")
print()

# 8. pop() - Remove and return value for key
print("8. pop()")
student = {"name": "John", "age": 25, "city": "NYC"}
print(f"Before pop: {student}")
removed_value = student.pop("age")
print(f"Removed value: {removed_value}")
print(f"After pop: {student}")

# Pop with default
removed = student.pop("country", "Not Found")
print(f"Pop non-existing with default: {removed}")
print()

# 9. popitem() - Remove and return last inserted item
print("9. popitem()")
student = {"name": "John", "age": 25, "city": "NYC"}
print(f"Before popitem: {student}")
removed_item = student.popitem()
print(f"Removed item: {removed_item}")
print(f"After popitem: {student}")
print()

# 10. setdefault() - Get value, set if not exists
print("10. setdefault()")
student = {"name": "John", "age": 25}
print(f"Original: {student}")

# Key exists
name = student.setdefault("name", "Default Name")
print(f"Existing key 'name': {name}")

# Key doesn't exist
city = student.setdefault("city", "Unknown")
print(f"New key 'city': {city}")
print(f"After setdefault: {student}")

# Another example
counts = {}
counts.setdefault("apple", 0)
counts["apple"] += 1
print(f"Counts: {counts}")
print()

# 11. update() - Update/add multiple items
print("11. update()")
student = {"name": "John", "age": 25}
print(f"Original: {student}")

# Update with another dict
student.update({"age": 26, "city": "NYC"})
print(f"After update with dict: {student}")

# Update with tuples
student.update([("grade", "A"), ("subject", "Math")])
print(f"After update with tuples: {student}")

# Update with keyword arguments
student.update(hobby="coding", country="USA")
print(f"After update with kwargs: {student}")
print()

# 12. | operator (Python 3.9+) - Merge dictionaries
print("12. | operator (Merge)")
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged = dict1 | dict2
print(f"Dict1: {dict1}")
print(f"Dict2: {dict2}")
print(f"Merged: {merged}")

# Update with |=
dict1 |= dict2
print(f"Dict1 after |= : {dict1}")
print()

print("="*60 + "\n")

# ========== DICTIONARY OPERATIONS ==========
print("=== DICTIONARY OPERATIONS ===\n")

# Accessing values
student = {"name": "John", "age": 25}
print(f"Student: {student}")
print(f"Access with key: {student['name']}")
print(f"Access with get(): {student.get('age')}")
print()

# Adding/updating values
student["city"] = "NYC"  # Add new
student["age"] = 26      # Update existing
print(f"After add/update: {student}")
print()

# Checking if key exists
print(f"Is 'name' in dict? {'name' in student}")
print(f"Is 'country' in dict? {'country' in student}")
print()

# Length of dict
print(f"Length: {len(student)}")
print()

# Deleting items
del student["city"]
print(f"After del: {student}")
print()

# Loop through dictionary
print("Different ways to loop:")
print("1. Just keys:")
for key in student:
    print(f"  {key}")

print("2. Keys and values:")
for key, value in student.items():
    print(f"  {key}: {value}")
print()

# ========== DICTIONARY COMPREHENSION ==========
print("=== DICTIONARY COMPREHENSION ===\n")

# Square numbers
squares = {x: x**2 for x in range(5)}
print(f"Squares: {squares}")

# Filter items
numbers = {1: "one", 2: "two", 3: "three", 4: "four"}
filtered = {k: v for k, v in numbers.items() if k > 2}
print(f"Filtered (keys > 2): {filtered}")

# Swap keys and values
original = {"a": 1, "b": 2, "c": 3}
swapped = {v: k for k, v in original.items()}
print(f"Original: {original}")
print(f"Swapped: {swapped}")
print()

# ========== PRACTICAL EXAMPLES ==========
print("=== PRACTICAL EXAMPLES ===\n")

# Example 1: Word counter
print("1. Word Counter:")
text = "hello world hello python world hello"
words = text.split()
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
print(f"Text: {text}")
print(f"Word count: {word_count}")
print()

# Example 2: Student grades
print("2. Student Grades:")
grades = {
    "John": 85,
    "Alice": 92,
    "Bob": 78,
    "Jane": 88
}
print(f"Grades: {grades}")
print(f"Average grade: {sum(grades.values()) / len(grades):.2f}")
print(f"Highest scorer: {max(grades, key=grades.get)}")
print(f"Lowest scorer: {min(grades, key=grades.get)}")
print()

# Example 3: Phonebook
print("3. Phonebook:")
phonebook = {
    "John": "123-456-7890",
    "Alice": "987-654-3210",
    "Bob": "555-123-4567"
}
print(f"Phonebook: {phonebook}")
# Search
name = "Alice"
print(f"{name}'s number: {phonebook.get(name, 'Not found')}")
# Add new
phonebook["Charlie"] = "777-888-9999"
print(f"After adding Charlie: {phonebook}")
print()

# Example 4: Character frequency
print("4. Character Frequency:")
string = "programming"
char_freq = {}
for char in string:
    char_freq[char] = char_freq.get(char, 0) + 1
print(f"String: {string}")
print(f"Character frequency: {char_freq}")
print()

# Example 5: Nested dictionary
print("5. Nested Dictionary:")
students = {
    "student1": {"name": "John", "age": 20, "grade": "A"},
    "student2": {"name": "Alice", "age": 22, "grade": "B"},
    "student3": {"name": "Bob", "age": 21, "grade": "A"}
}
print("Student details:")
for student_id, details in students.items():
    print(f"  {student_id}:")
    for key, value in details.items():
        print(f"    {key}: {value}")
print()

# Example 6: Default dict behavior
print("6. Using setdefault for grouping:")
words = ["apple", "banana", "apricot", "blueberry", "avocado"]
grouped = {}
for word in words:
    first_letter = word[0]
    grouped.setdefault(first_letter, []).append(word)
print(f"Words: {words}")
print(f"Grouped by first letter: {grouped}")