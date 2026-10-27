
# Basic Multiplication Calculator Made with Python

def multiply(x, y):
    return x * y

print("Welcome to a basic calculator program. This section of the program will do multiplications.\n")

print("Enter the first number and then the second number to multiply.\n")

try:
    x = float(input("First number: "))
    y = float(input("Second number: "))
    result = multiply(x, y)
    print(f"The answer is {result}.")

except ValueError:
    print("Invalid input! Please enter a valid number.")