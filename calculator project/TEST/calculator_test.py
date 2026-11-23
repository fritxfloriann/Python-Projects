# Test for calculator.py.

import unittest

from main_calculator import Calculator

# (button presses, expected display text)
CASES = [
    # --- the scenarios from the brief ---
    ("5 + 3 =", "8"),
    ("5 + 3 = =", "11"),
    ("5 + 3 = = =", "14"),
    ("0 . 1 + 0 . 2 =", "0.3"),
    ("1 0 ÷ 0 =", "Math Error"),
    ("5 × 2 =", "10"),
    ("1 0 - 1 5 =", "-5"),
    ("5 + × 3 =", "15"),  # the second operator replaces the first
    ("5 + 3 AC", "0"),
    ("5 . 5 ⌫", "5."),
    ("5 . 5 ⌫ ⌫", "5"),
    ("5 . 5 ⌫ ⌫ ⌫", "0"),
    ("5 +/- ⌫", "0"),  # -5 -> - -> 0, never an empty or "-" display
    ("1 2 +/- ⌫", "-1"),
    ("1 . 5 +/- ⌫ ⌫", "-1"),
    # --- equals and operators ---
    ("=", "0"),
    ("5 =", "5"),
    ("5 +", "5"),
    ("5 + =", "10"),  # like the iPhone: 5 + 5
    ("5 + = =", "15"),
    ("5 - 3 = =", "-1"),
    ("5 × 2 = =", "20"),
    ("5 × × × 3 =", "15"),
    ("5 + 3 + 2 =", "10"),
    ("5 + 3 +", "8"),  # the running total shows as soon as you chain
    ("2 + 3 × 4 =", "20"),  # left to right, no operator precedence
    ("5 + 3 = + 2 =", "10"),  # keep going from a result
    ("5 + 3 = 2", "2"),  # typing after = starts a new number
    ("5 + 3 = × 2 =", "16"),
    ("5 + 3 = × =", "64"),
    ("5 + 3 = 2 =", "5"),  # repeat "+ 3" on the new number
    # --- decimals and precision ---
    ("1 . 2 . 3", "1.23"),
    (". .", "0."),
    (". 5", "0.5"),
    ("0 . 1 + 0 . 2 + 0 . 3 =", "0.6"),
    ("0 . 3 - 0 . 1 =", "0.2"),
    ("4 . 3 5 × 1 0 0 =", "435"),  # floats give 434.99999999999994
    ("1 . 1 × 1 . 1 =", "1.21"),
    ("1 ÷ 3 =", "0.333333333"),
    ("2 ÷ 3 =", "0.666666667"),
    ("1 ÷ 3 × 3 =", "1"),  # full precision is kept between steps
    ("1 ÷ 3 0 =", "0.0333333333"),
    # --- long numbers ---
    ("1 2 3 4 5 6 7 8 9 0 1", "123456789"),  # input stops at 9 digits
    ("1 2 3 4 5 6 7 8 9 .", "123456789"),
    ("0 . 1 2 3 4 5 6 7 8 9", "0.12345678"),
    ("0 0 0 7", "7"),
    ("9 9 9 9 9 9 9 9 9 + 1 =", "1e+9"),
    ("9 9 9 9 9 9 9 9 9 × 9 9 9 9 9 9 9 9 9 =", "9.99999998e+17"),
    ("1 2 3 4 5 6 7 8 9 + 1 =", "123456790"),
    ("0 . 0 0 0 0 0 1 ÷ 1 0 =", "1e-7"),
    # --- sign and percent ---
    ("5 +/-", "-5"),
    ("5 +/- +/-", "5"),
    ("+/- 5", "-5"),
    ("5 + 3 = +/-", "-8"),
    ("5 +/- + 3 =", "-2"),
    ("5 + +/- 3 =", "2"),
    ("5 0 %", "0.5"),
    ("5 0 % %", "0.005"),
    ("5 0 % × 4 =", "2"),
    ("5 + 1 0 % ×", "5.1"),
    # --- backspace only edits typed numbers ---
    ("5 + 3 = ⌫", "8"),
    ("5 + ⌫", "5"),
    # --- errors ---
    ("0 ÷ 0 =", "Math Error"),
    ("1 0 ÷ 0 = + 5", "Math Error"),  # only AC or a new number is accepted
    ("1 0 ÷ 0 = ⌫", "Math Error"),
    ("1 0 ÷ 0 = =", "Math Error"),
    ("1 0 ÷ 0 = AC", "0"),
    ("1 0 ÷ 0 = 5", "5"),
    ("1 0 ÷ 0 = . 5", "0.5"),
    ("1 0 ÷ 0 = 5 + 3 =", "8"),  # no leftovers from before the error
    # --- keys that mean nothing are ignored ---
    ("5 abc + 3 =", "8"),
]


def press_keys(keys):
    calculator = Calculator()
    for key in keys.split():
        calculator.press(key)
    return calculator


class CalculatorTests(unittest.TestCase):
    def test_key_sequences(self):
        for keys, expected in CASES:
            with self.subTest(keys=keys):
                self.assertEqual(press_keys(keys).display_text, expected)

    def test_ac_resets_everything(self):
        fresh = vars(Calculator())
        for keys in ("5 + 3 = =", "5 + 3 +", "1 0 ÷ 0 =", "5 +/- %", "7 . 5 × ×"):
            with self.subTest(keys=keys):
                calculator = press_keys(keys + " AC")
                self.assertEqual(vars(calculator), fresh)
                self.assertEqual(calculator.display_text, "0")

    def test_ac_forgets_the_repeat_memory(self):
        self.assertEqual(press_keys("5 + 3 = = AC = =").display_text, "0")

    def test_empty_key_is_ignored(self):
        # Pressing Shift or an arrow key sends an empty string from Tk.
        self.assertEqual(press_keys("5").display_text, "5")
        calculator = press_keys("5")
        calculator.press("")
        self.assertEqual(calculator.display_text, "5")

    def test_waiting_operator(self):
        self.assertIsNone(press_keys("5").waiting_operator)
        self.assertEqual(press_keys("5 +").waiting_operator, "+")
        self.assertEqual(press_keys("5 + ×").waiting_operator, "×")
        self.assertIsNone(press_keys("5 + 3").waiting_operator)
        self.assertIsNone(press_keys("5 + 3 =").waiting_operator)


if __name__ == "__main__":
    unittest.main()