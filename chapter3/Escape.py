# escape.py - Comprehensive examples of escape sequences in Python

# 1. NEWLINE - \n
print("=== NEWLINE Example ===")
print("Hello\nWorld")
print("Line1\nLine2\nLine3")
print()

# 2. TAB - \t
print("=== TAB Example ===")
print("Name\tAge\tCity")
print("John\t25\tNYC")
print("Alice\t30\tLA")
print()

# 3. BACKSLASH - \\
print("=== BACKSLASH Example ===")
print("C:\\Users\\Documents\\file.txt")
print("Directory: Python\\Projects\\escape.py")
print()

# 4. SINGLE QUOTE - \'
print("=== SINGLE QUOTE Example ===")
print('It\'s a beautiful day')
print('She said, \'Hello!\'')
print()

# 5. DOUBLE QUOTE - \"
print("=== DOUBLE QUOTE Example ===")
print("He said, \"Python is awesome!\"")
print("\"Hello World\" in quotes")
print()

# 6. CARRIAGE RETURN - \r
print("=== CARRIAGE RETURN Example ===")
print("Loading...\rDone!    ")
print("12345\rABC")
print()

# 7. BACKSPACE - \b
print("=== BACKSPACE Example ===")
print("Hello\bWorld")  # Removes 'o'
print("Python\b\b\bJava")  # Removes 'hon'
print()

# 8. FORM FEED - \f
print("=== FORM FEED Example ===")
print("Page 1\fPage 2")  # May not be visible in console
print()

# 9. VERTICAL TAB - \v
print("=== VERTICAL TAB Example ===")
print("Line1\vLine2\vLine3")  # May not be visible in console
print()

# 10. OCTAL VALUE - \ooo
print("=== OCTAL VALUE Example ===")
print("\110\145\154\154\157")  # Hello in octal
print("\101\102\103")  # ABC in octal
print()

# 11. HEXADECIMAL VALUE - \xhh
print("=== HEXADECIMAL VALUE Example ===")
print("\x48\x65\x6c\x6c\x6f")  # Hello in hex
print("\x41\x42\x43")  # ABC in hex
print()

# 12. UNICODE - \u (4-digit hex) and \U (8-digit hex)
print("=== UNICODE Example ===")
print("\u03A9")  # Omega symbol (Ω)
print("\u2764")  # Heart symbol (❤)
print("\U0001F600")  # Grinning face emoji (😀)
print("\u00A9")  # Copyright symbol (©)
print()

# 13. RAW STRINGS (ignores escape sequences)
print("=== RAW STRINGS Example ===")
print(r"C:\Users\New\file.txt")  # Raw string - no escape
print(r"Hello\nWorld")  # Prints literal \n
print()

# 14. COMBINING ESCAPE SEQUENCES
print("=== COMBINING SEQUENCES Example ===")
print("Name:\tJohn Doe\nAge:\t30\nCity:\tNYC")
print("File path: C:\\Users\\John\\Documents\\\"my file\".txt")
print()

# 15. PRACTICAL EXAMPLES
print("=== PRACTICAL EXAMPLES ===")

# Creating a table
print("Product\t\tPrice\tQuantity")
print("Laptop\t\t$999\t5")
print("Mouse\t\t$25\t50")
print("Keyboard\t$75\t30")

# Multi-line string
print("\nMulti-line string:")
message = "Line 1\nLine 2\nLine 3"
print(message)

# Path with backslashes
path = "C:\\Program Files\\Python\\Scripts"
print(f"\nWindows Path: {path}")

# Quotes in string
quote = "She said, \"Python is amazing!\""
print(f"\nQuote: {quote}")

# Progress indicator
import time
print("\nProgress:", end=" ")
for i in range(5):
    print(f"\rProgress: {i*25}%", end="")
    time.sleep(0.5)
print("\rProgress: 100%   ")

# 16. STRING WITH MULTIPLE ESCAPES
print("\n=== MULTIPLE ESCAPES Example ===")
complex_string = "Line1\n\tLine2 (tabbed)\n\"Quoted text\"\nBackslash: \\\nUnicode: \u2728"
print(complex_string)

# 17. ESCAPE SEQUENCES IN f-STRINGS
print("\n=== f-STRINGS with ESCAPES ===")
name = "John"
print(f"Hello {name}\nWelcome!")
print(f"Path: C:\\Users\\{name}\\Documents")

# 18. AVOIDING ESCAPES
print("\n=== AVOIDING ESCAPES ===")
# Method 1: Raw strings
print(r"C:\new\folder\file.txt")

# Method 2: Double backslashes
print("C:\\new\\folder\\file.txt")

# Method 3: Forward slashes (works in Python)
print("C:/new/folder/file.txt")