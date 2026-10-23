
# Basic Subtraction Program with Python

def subtract(x, y):
    return x - y

print("Welcome to a basic subtraction program that handles basic subtraction.")

print("Enter your first and second number to get started.")

try:
    x = float(input("Enter your first number: \n"))
    y = float(input("Enter your second number: \n"))
    result = subtract (x, y) 
    print(f"The answer is {result}.")

except ValueError:
    print("Invalid input! Enter a valid number.")