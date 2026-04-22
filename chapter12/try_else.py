try:
    # Code that might raise an exception
    result = 10 / 2
except ZeroDivisionError:
    print("Division by zero!")
else:
    # This block runs only if no exception occurs
    print("No exception occurred. Result:", result)