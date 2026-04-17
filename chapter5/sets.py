# # SET METHODS CHEAT SHEET

# # Creating
# set()                       # Empty set
# {1, 2, 3}                   # Set literal
# set([1, 2, 3])             # From list
# set("hello")               # From string

# # Adding elements
# set.add(element)           # Add single element
# set.update(iterable)       # Add multiple elements

# # Removing elements
# set.remove(element)        # Remove (error if not exists)
# set.discard(element)       # Remove (no error if not exists)
# set.pop()                  # Remove and return arbitrary element
# set.clear()                # Remove all elements

# # Set operations
# set1.union(set2)           # All elements (|)
# set1.intersection(set2)    # Common elements (&)
# set1.difference(set2)      # In set1 not in set2 (-)
# set1.symmetric_difference(set2) # In either but not both (^)

# # Comparisons
# set1.issubset(set2)        # All elements in set2? (<=)
# set1.issuperset(set2)      # Contains all of set2? (>=)
# set1.isdisjoint(set2)      # No common elements?

# # Copying
# set.copy()                 # Shallow copy

# # Properties
# len(set)                   # Number of elements
# element in set             # Fast membership test
# element not in set         # Fast non-membership test

# # Frozen set (immutable)
# frozenset([1, 2, 3])       # Immutable set (can be dict key)

# # Set comprehension
# {x**2 for x in range(5)}   # Set comprehension


# SETS IN PYTHON

# ========== CREATING SETS ==========
print("=== CREATING SETS ===\n")

# Empty set (Note: {} is empty dict, not set)
empty_set = set()
print(f"Empty set: {empty_set}")
print(f"Type: {type(empty_set)}")

# Set with elements
fruits = {"apple", "banana", "orange"}
print(f"Fruits set: {fruits}")

# Using set() constructor
numbers = set([1, 2, 3, 4, 5])
print(f"From list: {numbers}")

# From string
chars = set("hello")
print(f"From string 'hello': {chars}")

# From tuple
colors = set(("red", "green", "blue"))
print(f"From tuple: {colors}")

print("\n" + "="*60 + "\n")

# ========== SET METHODS ==========
print("=== SET METHODS ===\n")

# 1. add() - Add single element
print("1. add()")
fruits = {"apple", "banana"}
print(f"Before add: {fruits}")
fruits.add("orange")
print(f"After add: {fruits}")
fruits.add("apple")  # Duplicate won't be added
print(f"Adding duplicate 'apple': {fruits}")
print()

# 2. update() - Add multiple elements
print("2. update()")
fruits = {"apple", "banana"}
print(f"Before update: {fruits}")
fruits.update(["orange", "mango", "kiwi"])
print(f"After update with list: {fruits}")
fruits.update(("grape", "berry"))
print(f"After update with tuple: {fruits}")
print()

# 3. remove() - Remove element (error if not found)
print("3. remove()")
fruits = {"apple", "banana", "orange"}
print(f"Before remove: {fruits}")
fruits.remove("banana")
print(f"After remove: {fruits}")
try:
    fruits.remove("grape")  # This will give error
except KeyError as e:
    print(f"Error: '{e}' not found in set")
print()

# 4. discard() - Remove element (no error if not found)
print("4. discard()")
fruits = {"apple", "banana", "orange"}
print(f"Before discard: {fruits}")
fruits.discard("banana")
print(f"After discard 'banana': {fruits}")
fruits.discard("grape")  # No error
print(f"After discard 'grape' (not exists): {fruits}")
print()

# 5. pop() - Remove and return arbitrary element
print("5. pop()")
fruits = {"apple", "banana", "orange", "mango"}
print(f"Before pop: {fruits}")
removed = fruits.pop()
print(f"Removed element: {removed}")
print(f"After pop: {fruits}")
print()

# 6. clear() - Remove all elements
print("6. clear()")
fruits = {"apple", "banana", "orange"}
print(f"Before clear: {fruits}")
fruits.clear()
print(f"After clear: {fruits}")
print()

# 7. copy() - Create shallow copy
print("7. copy()")
original = {"apple", "banana", "orange"}
copied = original.copy()
print(f"Original: {original}")
print(f"Copied: {copied}")
copied.add("mango")
print(f"After adding to copy: {copied}")
print(f"Original unchanged: {original}")
print()

print("="*60 + "\n")

# ========== SET OPERATIONS ==========
print("=== SET OPERATIONS ===\n")

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(f"Set1: {set1}")
print(f"Set2: {set2}")
print()

# 8. union() or | - Combine sets
print("8. union() - All elements from both sets")
union_set = set1.union(set2)
print(f"Union using union(): {union_set}")
print(f"Union using | operator: {set1 | set2}")
print()

# 9. intersection() or & - Common elements
print("9. intersection() - Common elements")
intersection_set = set1.intersection(set2)
print(f"Intersection using intersection(): {intersection_set}")
print(f"Intersection using & operator: {set1 & set2}")
print()

# 10. difference() or - - Elements in set1 but not in set2
print("10. difference() - Elements in set1 not in set2")
diff_set = set1.difference(set2)
print(f"Difference using difference(): {diff_set}")
print(f"Difference using - operator: {set1 - set2}")
print(f"Reverse difference: {set2 - set1}")
print()

# 11. symmetric_difference() or ^ - Elements in either set but not both
print("11. symmetric_difference() - Elements not in both")
sym_diff = set1.symmetric_difference(set2)
print(f"Symmetric difference using symmetric_difference(): {sym_diff}")
print(f"Symmetric difference using ^ operator: {set1 ^ set2}")
print()

# 12. isdisjoint() - Check if no common elements
print("12. isdisjoint() - No common elements?")
set1 = {1, 2, 3}
set2 = {4, 5, 6}
set3 = {3, 4, 5}
print(f"Set1: {set1}, Set2: {set2}")
print(f"Are disjoint? {set1.isdisjoint(set2)}")
print(f"Set1: {set1}, Set3: {set3}")
print(f"Are disjoint? {set1.isdisjoint(set3)}")
print()

# 13. issubset() or <= - Check if all elements are in another set
print("13. issubset() - Is set1 subset of set2?")
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
set3 = {1, 2, 6}
print(f"Set1: {set1}, Set2: {set2}")
print(f"Is subset? {set1.issubset(set2)}")
print(f"Using <= operator: {set1 <= set2}")
print(f"Set1: {set1}, Set3: {set3}")
print(f"Is subset? {set1.issubset(set3)}")
print()

# 14. issuperset() or >= - Check if contains all elements of another set
print("14. issuperset() - Is set1 superset of set2?")
set1 = {1, 2, 3, 4, 5}
set2 = {1, 2, 3}
print(f"Set1: {set1}, Set2: {set2}")
print(f"Is superset? {set1.issuperset(set2)}")
print(f"Using >= operator: {set1 >= set2}")
print()

print("="*60 + "\n")

# ========== SET COMPREHENSION ==========
print("=== SET COMPREHENSION ===\n")

# Basic set comprehension
squares = {x**2 for x in range(5)}
print(f"Squares: {squares}")

# With condition
even_squares = {x**2 for x in range(10) if x % 2 == 0}
print(f"Even squares: {even_squares}")

# From list with duplicates
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique = {x for x in numbers}
print(f"Original list: {numbers}")
print(f"Unique set: {unique}")

# String processing
words = ["hello", "world", "python", "hello"]
unique_lengths = {len(word) for word in words}
print(f"Unique lengths: {unique_lengths}")
print()

# ========== FROZENSET (IMMUTABLE SET) ==========
print("=== FROZENSET (Immutable Set) ===\n")

# Creating frozenset
normal_set = {1, 2, 3}
frozen = frozenset([1, 2, 3, 3, 4])
print(f"Frozenset: {frozen}")
print(f"Type: {type(frozen)}")

# Frozenset operations (same as set but returns frozenset)
fs1 = frozenset([1, 2, 3, 4])
fs2 = frozenset([3, 4, 5, 6])
print(f"fs1: {fs1}")
print(f"fs2: {fs2}")
print(f"Union: {fs1.union(fs2)}")
print(f"Intersection: {fs1.intersection(fs2)}")

# Frozenset can be used as dictionary key (normal set cannot)
location = {
    frozenset([1, 2, 3]): "Group A",
    frozenset([4, 5, 6]): "Group B"
}
print(f"Dict with frozenset keys: {location}")
print()

# ========== PRACTICAL EXAMPLES ==========
print("=== PRACTICAL EXAMPLES ===\n")

# Example 1: Remove duplicates from list
print("1. Remove duplicates from list:")
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5]
unique_numbers = list(set(numbers))
print(f"Original: {numbers}")
print(f"Without duplicates: {unique_numbers}")
print()

# Example 2: Find common elements between lists
print("2. Find common elements:")
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common = set(list1) & set(list2)
print(f"List1: {list1}")
print(f"List2: {list2}")
print(f"Common elements: {common}")
print()

# Example 3: Find unique characters in string
print("3. Unique characters in string:")
text = "hello world"
unique_chars = set(text)
print(f"String: '{text}'")
print(f"Unique characters: {unique_chars}")
print(f"Unique characters (sorted): {sorted(unique_chars)}")
print()

# Example 4: Vowel counter
print("4. Vowel counter:")
def count_vowels(text):
    vowels = set("aeiouAEIOU")
    text_set = set(text)
    return len(text_set & vowels)

text = "Hello World Python"
count = count_vowels(text)
print(f"Text: '{text}'")
print(f"Number of unique vowels: {count}")
print()

# Example 5: Find missing items
print("5. Find missing items:")
required = {"apple", "banana", "orange", "mango", "grape"}
available = {"apple", "banana", "orange"}
missing = required - available
print(f"Required: {required}")
print(f"Available: {available}")
print(f"Missing: {missing}")
print()

# Example 6: Check if two lists have any common elements
print("6. Check for common elements:")
def have_common(list1, list2):
    return bool(set(list1) & set(list2))

list_a = [1, 2, 3, 4]
list_b = [5, 6, 7, 8]
list_c = [4, 5, 6, 7]

print(f"List A: {list_a}, List B: {list_b}")
print(f"Have common? {have_common(list_a, list_b)}")
print(f"List A: {list_a}, List C: {list_c}")
print(f"Have common? {have_common(list_a, list_c)}")
print()

# Example 7: Set operations on customer data
print("7. Customer analysis:")
customers_jan = {"John", "Alice", "Bob", "Jane", "Mike"}
customers_feb = {"Alice", "Jane", "Tom", "Sarah", "Bob"}

print(f"January customers: {customers_jan}")
print(f"February customers: {customers_feb}")
print(f"New customers in Feb: {customers_feb - customers_jan}")
print(f"Lost customers from Jan: {customers_jan - customers_feb}")
print(f"Returning customers: {customers_jan & customers_feb}")
print(f"All customers (either month): {customers_jan | customers_feb}")
print()

# Example 8: Email spam filter
print("8. Email spam filter:")
spam_words = {"free", "winner", "click", "urgent", "cash"}
email = "You have won a free prize! Click here to claim your cash"
email_words = set(email.lower().split())
spam_score = len(email_words & spam_words)
print(f"Email: '{email}'")
print(f"Spam words found: {email_words & spam_words}")
print(f"Spam score: {spam_score}")
print()

# Example 9: Find unique elements across multiple lists
print("9. Unique elements across lists:")
list1 = [1, 2, 3]
list2 = [2, 3, 4]
list3 = [3, 4, 5]

unique_all = set(list1) ^ set(list2) ^ set(list3)
print(f"List1: {list1}")
print(f"List2: {list2}")
print(f"List3: {list3}")
print(f"Elements appearing odd number of times: {unique_all}")
print()

# Example 10: Set membership testing (fast)
print("10. Fast membership testing:")
large_list = list(range(10000))
large_set = set(large_list)

import time
# Test in list
start = time.time()
result_list = 9999 in large_list
list_time = time.time() - start

# Test in set
start = time.time()
result_set = 9999 in large_set
set_time = time.time() - start

print(f"List membership time: {list_time:.6f} seconds")
print(f"Set membership time: {set_time:.6f} seconds")
print(f"Set is faster! (O(1) vs O(n))")