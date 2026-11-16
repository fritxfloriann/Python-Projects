"""Core conversion logic for the unit converter.

Supports four categories: length, mass, volume, and temperature.
Linear categories (length, mass, volume) use a simple "convert to a
base unit, then convert out" approach. Temperature is handled
separately because Celsius/Fahrenheit/Kelvin conversions involve an
offset, not just a scale factor.
"""


class ConversionError(Exception):
    """Raised when a conversion can't be performed (unknown unit, etc.)."""


# Conversion factors into a base unit for each category.
LENGTH_TO_METERS = {
    "mm": 0.001,
    "cm": 0.01,
    "m": 1.0,
    "km": 1000.0,
    "in": 0.0254,
    "ft": 0.3048,
    "yd": 0.9144,
    "mi": 1609.344,
}

MASS_TO_GRAMS = {
    "mg": 0.001,
    "g": 1.0,
    "kg": 1000.0,
    "oz": 28.349523125,
    "lb": 453.59237,
    "st": 6350.29318,
    "t": 1_000_000.0,  # metric tonne
}

VOLUME_TO_LITERS = {
    "ml": 0.001,
    "l": 1.0,
    "tsp": 0.00492892,
    "tbsp": 0.0147868,
    "cup": 0.24,
    "pt": 0.473176,
    "qt": 0.946353,
    "gal": 3.78541,
}

CATEGORY_TABLES = {
    "length": LENGTH_TO_METERS,
    "mass": MASS_TO_GRAMS,
    "volume": VOLUME_TO_LITERS,
}

TEMPERATURE_UNITS = {
    "c": "celsius",
    "celsius": "celsius",
    "f": "fahrenheit",
    "fahrenheit": "fahrenheit",
    "k": "kelvin",
    "kelvin": "kelvin",
}


def _convert_linear(value, from_unit, to_unit, table):
    if from_unit not in table:
        raise ConversionError(f"Unknown unit: {from_unit!r}")
    if to_unit not in table:
        raise ConversionError(f"Unknown unit: {to_unit!r}")
    base_value = value * table[from_unit]
    return base_value / table[to_unit]


def _convert_temperature(value, from_unit, to_unit):
    from_name = TEMPERATURE_UNITS.get(from_unit)
    to_name = TEMPERATURE_UNITS.get(to_unit)
    if from_name is None:
        raise ConversionError(f"Unknown temperature unit: {from_unit!r}")
    if to_name is None:
        raise ConversionError(f"Unknown temperature unit: {to_unit!r}")

    # Normalize to Celsius first.
    if from_name == "celsius":
        celsius = value
    elif from_name == "fahrenheit":
        celsius = (value - 32) * 5 / 9
    else:  # kelvin
        celsius = value - 273.15

    # Then convert out to the target unit.
    if to_name == "celsius":
        return celsius
    elif to_name == "fahrenheit":
        return celsius * 9 / 5 + 32
    else:  # kelvin
        return celsius + 273.15


def convert(value, from_unit, to_unit, category=None):
    """Convert `value` from `from_unit` to `to_unit`.

    If `category` is omitted, it's inferred from `from_unit`. Pass it
    explicitly if you want to be strict about which category a unit
    belongs to (useful if you add units that collide across categories).
    """
    from_unit = from_unit.strip().lower()
    to_unit = to_unit.strip().lower()

    if category == "temperature" or (category is None and from_unit in TEMPERATURE_UNITS):
        return _convert_temperature(value, from_unit, to_unit)

    if category is not None:
        table = CATEGORY_TABLES.get(category)
        if table is None:
            raise ConversionError(f"Unknown category: {category!r}")
        return _convert_linear(value, from_unit, to_unit, table)

    for table in CATEGORY_TABLES.values():
        if from_unit in table:
            return _convert_linear(value, from_unit, to_unit, table)

    raise ConversionError(f"Unrecognized unit: {from_unit!r}")


def supported_units():
    """Return a dict of category -> sorted list of unit abbreviations."""
    result = {cat: sorted(table.keys()) for cat, table in CATEGORY_TABLES.items()}
    result["temperature"] = ["c", "f", "k"]
    return result
