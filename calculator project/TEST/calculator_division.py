
# Basic Calculator using Division in Python

def divide(x, y):
    return x / y

print("Welcome to a basic calculator program. This section of the program will do divisions.\n")

print("Enter the first number and then the second number to divide.\n")

try:
    x = float(input("First number: "))
    y = float(input("Second number: "))
    result = divide(x, y)
    print(f"The answer is {result}.")

except ValueError:
    print("Invalid input! Please enter a valid number.")