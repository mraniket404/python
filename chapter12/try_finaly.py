try:
    # Code that might raise an exception
    print("Executing code in try block")
    # For example, open a file or perform an operation
    file = open("example.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("File not found")
finally:
    # Cleanup code that always runs
    print("This will always execute")  # ye line hamesha execute hogi, chahe exception aaye ya na aaye
    # Close the file if it was opened
    try:
        file.close()
    except NameError:
        pass  # File was not opened