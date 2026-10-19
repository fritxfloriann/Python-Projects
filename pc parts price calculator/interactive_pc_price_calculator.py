
import math

PARTS = ("CPU", "GPU", "Motherboard", "RAM", "Storage (SSD or HDD)", "Case", "Cooling", "PSU")

# Interactive PC Part Calculator with input and functions.

def get_parts_from_user():
    """Ask for a price for each standard PC component."""
    print("Welcome to PC Price Calculator! Enter wisely to get the most accurate answer.")
    print("Enter each component's price in United States Dollars (USD).")
    parts = {part: get_price(part) for part in PARTS}
    return parts

def get_price(part):
    """Keep asking until the user enters a valid, non-negative price."""
    print(f"{part} price")
    while True:
        raw = input("Enter Price: $").strip()

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
