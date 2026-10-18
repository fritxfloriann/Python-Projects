
# Interactive PC Part Calculator with input and functions.

# In this mini-project, I will be adding inputs, functions, and more refined enhancements from my previous project, pc  price calculator.py

# This program offers interactable inputs and catches errors when the user enters an invalid and illegal answer.

def get_parts_from_user():
    """Let the user enter up to eight part names and prices."""
    parts = {}
    print("Welcome to PC Price Calculator! Enter wisely to get the most accurate answer.")

    print(f"Enter up to {MAX_PARTS} PC parts (type 'done' to finish early)\n")

    print("Suggested parts: CPU, GPU, Motherboard, RAM, Storage (SSD or HDD),")
    
    print("Case, Cooling, and PSU. The currency used is United States Dollar (USD).\n")

    # The limitation of the quantity of the parts ensure that the program doesn't loop the questions asked.

    while len(parts) < MAX_PARTS:
        name = input(f"Part name ({len(parts) + 1}/{MAX_PARTS}): ").strip()
        if name.lower() == "done":
            break
        if not name:
            print("Part name can't be empty.\n")
            continue
        if name in parts:
            print("That part has already been entered.\n")
            continue

        price = get_price()
        parts[name] = price
        print(f"Added {name}: ${price:.2f}\n")

    if len(parts) == MAX_PARTS:
        print(f"You've entered all {MAX_PARTS} parts.\n")

    return parts

# The code above makes the user input their component and the price of the component they enter. This combines four fundamentals in Python.

# IMPORTANT !! Type done once you're done answering the questions provided.

# Below is how Python handles errors, loops, functions, and how it computes.

import math

MAX_PARTS = 8

def get_price():
    """Keep asking until the user enters a valid, non-negative price."""
    while True:
        raw = input("Price: $").strip()

        try:
            price = float(raw)

            if not math.isfinite(price):
                print("Please enter a finite number.")
                continue

            if price < 0:
                print("Price can't be negative.")
                continue

            return price

        except ValueError:
            print("Please enter a valid number.")

# Below, is the code where it adds up the cost for the part prices.

def calculate_total(parts):
    """Return the sum of all part prices."""
    return sum(parts.values())

# The next code takes the dictionary made by the user to be formatted into a readable input.

def print_breakdown(parts):
    """Print a formatted price breakdown and total."""
    print("\nPC Build Price Breakdown")
    print("-" * 30)
    for part, price in parts.items():
        print(f"{part:<12} ${price:>7.2f}")
    print("-" * 30)
    print(f"{'Total':<12} ${calculate_total(parts):>7.2f}")

# The code below makes the program coordinates the code together.

def main():
    parts = get_parts_from_user()
    if parts:
        print_breakdown(parts)
    else:
        print("No parts entered.")

# These lines of code helps the program run.

if __name__ == "__main__":
    main()

# Once the program runs, you can start using it as a calculator for your PC Build by calculating the prices of each component.