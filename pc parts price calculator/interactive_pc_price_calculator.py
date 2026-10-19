
# Welcome to PPPC. PC Parts Price Calculator.

import math

PARTS = ("CPU", "GPU", "Motherboard", "RAM", "Storage", "Case", "Cooling", "PSU")

def get_model(part: str) -> str:
    """Ask for a non-empty model name for a component."""
    print(f"{part} model:")
    while True:
        model = input("Enter model: ").strip()
        if model:
            return model
        print("Please enter a model.")


def get_price(part: str) -> float:
    """Keep asking until the user enters a valid, non-negative price."""
    print(f"{part} price:")
    while True:
        raw = input("Enter Price: $").strip()

        try:
            price = float(raw)
        except ValueError:
            print("Please enter a valid number.")
            continue

        if not math.isfinite(price):
            print("Please enter a finite number.")
        elif price < 0:
            print("Price can't be negative.")
        else:
            return price


def get_parts_from_user() -> dict[str, tuple[str, float]]:
    """Ask for a model and price for each standard PC component."""
    print("Welcome to PC Price Calculator! Enter wisely to get the most accurate answer.")
    print("Enter each component's model and price in United States Dollars (USD).")
    return {
        part: (get_model(part), get_price(part))
        for part in PARTS
    }


def calculate_total(parts: dict[str, tuple[str, float]]) -> float:
    """Return the sum of all part prices."""
    return sum(price for _, price in parts.values())


def print_breakdown(parts: dict[str, tuple[str, float]]) -> None:
    """Print a formatted model and price breakdown with the total."""
    label_width = max(len("Total"), *(len(part) for part in parts))
    model_width = max(len("Model"), *(len(model) for model, _ in parts.values()))
    price_width = max(len("Price"), *(len(f"${price:.2f}") for _, price in parts.values()))
    separator_width = label_width + model_width + price_width + 4

    print("\nPC Build Price Breakdown")
    print("-" * separator_width)
    print(f"{'Component':<{label_width}}  {'Model':<{model_width}}  {'Price':>{price_width}}")
    for part, (model, price) in parts.items():
        print(f"{part:<{label_width}}  {model:<{model_width}}  ${price:>{price_width - 1}.2f}")
    print("-" * separator_width)
    print(f"{'Total':<{label_width}}  {'':<{model_width}}  ${calculate_total(parts):>{price_width - 1}.2f}")


def main() -> None:
    parts = get_parts_from_user()
    print_breakdown(parts)


if __name__ == "__main__":
    main()

# Once the program runs, you can start using it as a calculator for your PC Build by calculating the prices of each component.
