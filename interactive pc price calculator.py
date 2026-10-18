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

def calculate_total(parts):
    """Return the sum of all part prices."""
    return sum(parts.values())

def print_breakdown(parts):
    """Print a formatted price breakdown and total."""
    print("\nPC Build Price Breakdown")
    print("-" * 30)
    for part, price in parts.items():
        print(f"{part:<12} ${price:>7.2f}")
    print("-" * 30)
    print(f"{'Total':<12} ${calculate_total(parts):>7.2f}")

def main():
    parts = get_parts_from_user()
    if parts:
        print_breakdown(parts)
    else:
        print("No parts entered.")

if __name__ == "__main__":
    main()
