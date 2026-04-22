# Example of raising an exception in Python
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

if b == 0:
    raise ValueError("Cannot divide by zero!")
result = a / b
print(f"The result of {a} divided by {b} is: {result}")

