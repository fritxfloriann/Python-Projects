# This is a test. Ignore this file.

import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from converter import convert, ConversionError, supported_units


def test_length():
    assert math.isclose(convert(1, "km", "m"), 1000)
    assert math.isclose(convert(1, "mi", "km"), 1.609344, rel_tol=1e-6)
    assert math.isclose(convert(12, "in", "ft"), 1.0)


def test_mass():
    assert math.isclose(convert(1, "kg", "lb"), 2.2046226, rel_tol=1e-5)
    assert math.isclose(convert(16, "oz", "lb"), 1.0, rel_tol=1e-6)


def test_volume():
    assert math.isclose(convert(1, "gal", "l"), 3.78541, rel_tol=1e-5)
    assert math.isclose(convert(4, "cup", "l"), 0.96, rel_tol=1e-6)


def test_temperature():
    assert math.isclose(convert(0, "c", "f"), 32)
    assert math.isclose(convert(212, "f", "c"), 100)
    assert math.isclose(convert(0, "c", "k"), 273.15)
    assert math.isclose(convert(273.15, "k", "c"), 0)


def test_case_insensitive_and_whitespace():
    assert math.isclose(convert(1, " KM ", "M"), 1000)


def test_unknown_unit_raises():
    try:
        convert(1, "xyz", "m")
        assert False, "expected ConversionError"
    except ConversionError:
        pass


def test_mismatched_category_raises():
    try:
        convert(1, "km", "kg")
        assert False, "expected ConversionError"
    except ConversionError:
        pass


def test_supported_units_shape():
    units = supported_units()
    assert "length" in units and "mass" in units and "volume" in units and "temperature" in units
    assert "km" in units["length"]


def run_all():
    tests = [v for k, v in globals().items() if k.startswith("test_") and callable(v)]
    for test in tests:
        test()
        print(f"  ok  {test.__name__}")
    print(f"\n{len(tests)} tests passed.")


if __name__ == "__main__":
    run_all()
