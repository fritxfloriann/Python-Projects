
# Basic Addition Calculator

def add(x, y):
    return x + y

print("Welcome to a basic calculator program. This section of the program will do additions.\n")

print("Enter the first number and then the second number to add.\n")

try:
    x = float(input("First number: "))
    y = float(input("Second number: "))
    result = add(x, y)
    print(f"The answer is {result}.")

except ValueError:
    print("Invalid input! Please enter a valid number.")