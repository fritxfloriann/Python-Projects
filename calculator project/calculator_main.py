
# A Calculator Made in Python

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def percentage(x, y):
    return (x / y) * 100

print("Welcome to calculator_main!\n")
print("Choose what mathematical operation you want to do.\n")

print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
print("5. Percentage (%)\n")

try:
    choice = input("Enter the operation you want to do: ")

    x = float(input("Enter your first number: "))
    y = float(input("Enter the second number: "))


if choice == "1":
    result = add(x, y)
    print(f"The answer is {result}.")

elif choice == "2":
    result = subtract(x, y)
    print(f"The answer is {result}.")

elif choice == "3":
    result = multiply(x, y)
    print(f"The answer is {result}.")

elif choice == "4":
    if y == 0:
        print("Error! Can't divide by zero.")
    else:  
        result = divide(x, y)
    print(f"The answer is {result}.")

elif choice == "5":
    if y == 0:
        print("Error! Can't divide by zero.")
    else:
        result = divide(x, y)
    print(f"The answer is {result}.")

else:
    print("Invalid input! Please select the following list of operations from 1-5.")

except ValueError:
print("Invalid input! Please enter a valid number.")
