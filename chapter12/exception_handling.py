try:
    a = int(input("Enter a number: "))
    result = 10 / a
    print(f"The result is: {result}")
except ZeroDivisionError:
    print("Error: You cannot divide by zero!")
except ValueError:
    print("Error: Invalid input! Please enter a valid number.")
    