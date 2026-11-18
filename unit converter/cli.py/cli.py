# This file is required for cli.py and unit_converter.py to work.

"""Command-line interface for the unit converter.

Usage:
    python cli.py <value> <from_unit> <to_unit>
    python cli.py --list

Examples:
    python cli.py 5 km mi
    python cli.py 98.6 f c
    python cli.py 2.5 gal l
"""

import argparse

from converter import convert, supported_units, ConversionError


def main():
    parser = argparse.ArgumentParser(
        description="Convert between units of length, mass, volume, and temperature."
    )
    parser.add_argument("value", type=float, nargs="?", help="Numeric value to convert")
    parser.add_argument("from_unit", nargs="?", help="Unit to convert from (e.g. km, lb, c)")
    parser.add_argument("to_unit", nargs="?", help="Unit to convert to (e.g. mi, kg, f)")
    parser.add_argument(
        "--list", action="store_true", help="List all supported units by category and exit"
    )
    args = parser.parse_args()

    if args.list:
        for category, units in supported_units().items():
            print(f"{category}: {', '.join(units)}")
        return

    if args.value is None or args.from_unit is None or args.to_unit is None:
        parser.error("value, from_unit, and to_unit are required (or pass --list)")

    try:
        result = convert(args.value, args.from_unit, args.to_unit)
    except ConversionError as e:
        parser.error(str(e))
        return

    print(f"{args.value:g} {args.from_unit} = {result:.6g} {args.to_unit}")


if __name__ == "__main__":
    main()
    
# This program is terminal-based. Check for commands and the instructions on the README.
