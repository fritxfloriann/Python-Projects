
# Basic Percentage Calculator With Python

def percentage(x, y):
    return (x / y) * 100

print("Welcome to a basic calculator program. This section of the program will calculate percentages.\n")

print("Enter the first number and then the second number to calculate the percentage.\n")

try:
    x = float(input("First number: "))
    y = float(input("Second number: "))

    if y == 0:
        print("Error! The second number cannot be zero.")
    else:
        result = percentage(x, y)
        print(f"The answer is {result:.2f}%.")

except ValueError:
    print("Invalid input! Please enter a valid number.")
