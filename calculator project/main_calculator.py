
import tkinter
import tkinter.font
from decimal import ROUND_HALF_UP, Context, Decimal
from operator import add, mul, sub, truediv

# ---------------------------------------------------------------------------
# Part 1: calculator logic (no tkinter in this part)
# ---------------------------------------------------------------------------

DIGITS = tuple("0123456789")      # a tuple, so "" is not "in" it (a string would say yes)
OPERATIONS = {"+": add, "-": sub, "×": mul, "÷": truediv}

MAX_DIGITS = 9                    # digits you can type, and digits shown in a result
ERROR_TEXT = "Math Error"

# Results are rounded to MAX_DIGITS significant digits for DISPLAY only.
# The calculator itself keeps the full-precision number.
DISPLAY_CONTEXT = Context(prec=MAX_DIGITS, rounding=ROUND_HALF_UP)


def format_number(number):
    """Turn a Decimal into display text: at most 9 significant digits, no trailing zeros."""
    rounded = DISPLAY_CONTEXT.create_decimal(number).normalize()
    if rounded == 0:
        return "0"                      # also hides a negative zero
    if -4 <= rounded.adjusted() < MAX_DIGITS:
        return format(rounded, "f")     # plain notation, e.g. 0.3 or 1234.5
    return format(rounded, "e")         # scientific notation, e.g. 1.5e+12


def calculate(left, symbol, right):
    """Apply one operator to two Decimals. Raises ArithmeticError, e.g. for 1 ÷ 0."""
    return OPERATIONS[symbol](left, right)


class Calculator:
    """The calculator's brain: it holds the state and knows what every button does.

    Usage:  calc = Calculator()
            calc.press("5"); calc.press("+"); calc.press("3"); calc.press("=")
            calc.display_text        # "8"

    Numbers are Decimals, so 0.1 + 0.2 is exactly 0.3 (floats give 0.30000000000000004).
    Operators are applied as you press them, left to right: 5 + 3 × 2 = gives 16.
    """

    def __init__(self):
        self.clear()

    def clear(self):
        """AC: forget everything, including an error."""
        # The number being typed, as text such as "12." or "-0.5".
        # None means the screen shows a calculated number instead.
        self.entry = "0"
        # The calculated number on the screen (used while entry is None).
        # Kept at full precision; only the display rounds it.
        self.number = Decimal(0)
        # A calculation waiting for its second number: the "5 +" in 5 + 3.
        self.left = None
        self.operator = None
        # True right after an operator key, until the next number is started.
        self.awaiting_operand = False
        # (operator, number) that pressing "=" again applies once more.
        self.repeat = None
        self.error = False

    # --- what the GUI reads -------------------------------------------------

    @property
    def display_text(self):
        """The text the screen should show."""
        if self.error:
            return ERROR_TEXT
        if self.entry is not None:
            return self.entry
        return format_number(self.number)

    @property
    def active_operator(self):
        """The operator waiting for its second number (its button is highlighted), or None."""
        return self.operator if self.awaiting_operand else None

    def current_value(self):
        """The number on the screen, as a Decimal."""
        if self.entry is not None:
            return Decimal(self.entry)
        return self.number

    # --- the one entry point: mouse clicks and key presses both end up here ---

    def press(self, key):
        """Handle one button, named by its label: "7", ".", "÷", "=", "AC", "+/-", "%", "⌫"."""
        if self.error:
            # After "Math Error" only AC or a number key gets the calculator going again.
            if key != "AC" and key != "." and key not in DIGITS:
                return
            self.clear()

        try:
            if key in DIGITS:
                self.press_digit(key)
            elif key == ".":
                self.press_decimal_point()
            elif key in OPERATIONS:
                self.press_operator(key)
            elif key == "=":
                self.press_equals()
            elif key == "AC":
                self.clear()
            elif key == "+/-":
                self.press_plus_minus()
            elif key == "%":
                self.press_percent()
            elif key == "⌫":
                self.press_backspace()
        except ArithmeticError:         # division by zero, overflow, ...
            self.clear()
            self.error = True

    # --- typing numbers -----------------------------------------------------

    def press_digit(self, digit):
        self.awaiting_operand = False
        if self.entry is None:
            self.entry = digit                          # start a new number
        elif self.entry in ("0", "-0"):
            self.entry = self.entry[:-1] + digit        # replace a lone leading zero
        elif sum(char.isdigit() for char in self.entry) < MAX_DIGITS:
            self.entry += digit                         # (extra digits are ignored)

    def press_decimal_point(self):
        self.awaiting_operand = False
        if self.entry is None:
            self.entry = "0."
        elif "." not in self.entry:
            self.entry += "."

    def press_backspace(self):
        if self.entry is None:
            return                      # a calculated result can't be edited
        self.entry = self.entry[:-1]
        if self.entry in ("", "-"):
            self.entry = "0"

    def press_plus_minus(self):
        if self.entry is not None:                      # typing: flip the sign of the text
            if self.entry.startswith("-"):
                self.entry = self.entry[1:]
            else:
                self.entry = "-" + self.entry
        elif self.awaiting_operand:                     # 5 × +/- 3 : a negative second number
            self.entry = "-0"
            self.awaiting_operand = False
        else:                                           # a calculated number
            self.number = -self.number

    def press_percent(self):
        self.number = self.current_value() / 100
        self.entry = None
        self.awaiting_operand = False

    # --- operators and equals -----------------------------------------------

    def press_operator(self, symbol):
        if self.operator is not None and not self.awaiting_operand:
            # 5 + 3 ×  ->  finish 5 + 3 first (the screen shows 8), then start the ×
            self.number = calculate(self.left, self.operator, self.current_value())
        elif self.operator is None:
            self.number = self.current_value()
        # else: 5 + ×  ->  there is no second number yet, so just swap the operator
        self.entry = None
        self.left = self.number
        self.operator = symbol
        self.awaiting_operand = True

    def press_equals(self):
        current = self.current_value()
        if self.operator is not None:                   # 5 + 3 =
            left, symbol, right = self.left, self.operator, current
        elif self.repeat is not None:                   # = again: repeat the last operation
            symbol, right = self.repeat
            left = current
        else:                                           # nothing to calculate: just end typing
            self.number = current
            self.entry = None
            return

        self.number = calculate(left, symbol, right)    # may raise ArithmeticError
        self.repeat = (symbol, right)
        self.entry = None
        self.left = None
        self.operator = None
        self.awaiting_operand = False


# ---------------------------------------------------------------------------
# Part 2: the tkinter window
# ---------------------------------------------------------------------------

BUTTON_VALUES = [
    ["AC", "+/-", "%", "÷"],
    ["7", "8", "9", "×"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "⌫", "="],
]

RIGHT_SYMBOLS = ["÷", "×", "-", "+", "="]
TOP_SYMBOLS = ["AC", "+/-", "%"]

COLUMN_COUNT = len(BUTTON_VALUES[0])

COLOR_LIGHT_GREY = "#D4D4D2"
COLOR_BLACK = "#000000"
COLOR_DARK_GREY = "#505050"
COLOR_ORANGE = "#FF9500"
COLOR_WHITE = "#FFFFFF"

# Colours for each kind of button. The "active" colours show while it is pressed.
STYLE_TOP = {
    "foreground": COLOR_BLACK, "background": COLOR_LIGHT_GREY,
    "activeforeground": COLOR_BLACK, "activebackground": "#F2F2F2",
}
STYLE_RIGHT = {
    "foreground": COLOR_WHITE, "background": COLOR_ORANGE,
    "activeforeground": COLOR_WHITE, "activebackground": "#FFC266",
}
STYLE_NUMBER = {
    "foreground": COLOR_WHITE, "background": COLOR_DARK_GREY,
    "activeforeground": COLOR_WHITE, "activebackground": "#737373",
}

DISPLAY_FONT_FAMILY = "Arial"
DISPLAY_FONT_SIZE = 45
MIN_DISPLAY_FONT_SIZE = 16
DISPLAY_PADDING = 12              # pixels between the text and the edge of the display

# Special keys, by tkinter's key name (event.keysym).
KEYSYM_TO_BUTTON = {
    "Return": "=",
    "KP_Enter": "=",
    "KP_Equal": "=",
    "BackSpace": "⌫",
    "Escape": "AC",
    "KP_Add": "+",
    "KP_Subtract": "-",
    "KP_Multiply": "×",
    "KP_Divide": "÷",
    "KP_Decimal": ".",
    **{f"KP_{digit}": digit for digit in DIGITS},
}

# Ordinary typed characters (event.char).
CHAR_TO_BUTTON = {
    "+": "+",
    "-": "-",
    "*": "×",
    "x": "×",
    "X": "×",
    "/": "÷",
    "=": "=",
    ".": ".",
    "%": "%",
    **{digit: digit for digit in DIGITS},
}


def button_style(value):
    """Pick the colours for a button."""
    if value in TOP_SYMBOLS:
        return STYLE_TOP
    if value in RIGHT_SYMBOLS:
        return STYLE_RIGHT
    return STYLE_NUMBER


class CalculatorApp:
    """The tkinter window. It only draws things and forwards button presses."""

    def __init__(self, window):
        self.window = window
        self.calculator = Calculator()
        self.operator_buttons = {}          # "+" -> its Button, so we can highlight it

        window.title("Calculator Main")
        window.resizable(False, False)

        self.frame = tkinter.Frame(window)
        self.create_display()
        self.create_buttons()
        self.frame.pack()

        window.bind_all("<Key>", self.on_key_press)

        window.update_idletasks()           # let tkinter work out the layout so we can measure it
        self.lock_display_size()
        self.centre_window()
        self.refresh()

    # --- building the window -------------------------------------------------

    def create_display(self):
        self.display_font = tkinter.font.Font(
            root=self.window, family=DISPLAY_FONT_FAMILY, size=DISPLAY_FONT_SIZE
        )
        self.display = tkinter.Label(
            self.frame,
            text="0",
            font=self.display_font,
            background=COLOR_BLACK,
            foreground=COLOR_WHITE,
            anchor="e",
            width=COLUMN_COUNT,
            padx=DISPLAY_PADDING,
        )
        self.display.grid(row=0, column=0, columnspan=COLUMN_COUNT, sticky="we")

    def create_buttons(self):
        for row, row_values in enumerate(BUTTON_VALUES, start=1):
            for column, value in enumerate(row_values):
                button = tkinter.Button(
                    self.frame,
                    text=value,
                    font=("Arial", 30),
                    width=COLUMN_COUNT - 1,
                    height=1,
                    takefocus=False,        # so Tab/Space can't press a button by accident
                    command=lambda value=value: self.press(value),
                    **button_style(value),
                )
                button.grid(row=row, column=column)

                if value in OPERATIONS:
                    self.operator_buttons[value] = button

    def lock_display_size(self):
        """Measure the display once, so a shrinking font can't make the window jump around."""
        self.frame.grid_rowconfigure(0, minsize=self.display.winfo_reqheight())
        self.text_width = self.frame.winfo_reqwidth() - 2 * DISPLAY_PADDING

    def centre_window(self):
        width = self.window.winfo_reqwidth()
        height = self.window.winfo_reqheight()
        x = (self.window.winfo_screenwidth() - width) // 2
        y = (self.window.winfo_screenheight() - height) // 2
        self.window.geometry(f"{width}x{height}+{x}+{y}")

    # --- input: mouse and keyboard both come through press() -----------------

    def press(self, key):
        self.calculator.press(key)
        self.refresh()

    def on_key_press(self, event):
        key = KEYSYM_TO_BUTTON.get(event.keysym) or CHAR_TO_BUTTON.get(event.char)
        if key is not None:
            self.press(key)
            return "break"              # handled: stop tkinter from also acting on this key

    # --- output: show the calculator's state ---------------------------------

    def refresh(self):
        text = self.calculator.display_text
        self.display["text"] = text
        self.fit_font_to_text(text)
        self.highlight_active_operator()

    def fit_font_to_text(self, text):
        """Use the biggest font size (down to a minimum) at which the text fits the display."""
        size = DISPLAY_FONT_SIZE
        self.display_font.configure(size=size)
        while size > MIN_DISPLAY_FONT_SIZE and self.display_font.measure(text) > self.text_width:
            size -= 1
            self.display_font.configure(size=size)

    def highlight_active_operator(self):
        """Like the iPhone: the operator waiting for its second number turns white."""
        active = self.calculator.active_operator
        for symbol, button in self.operator_buttons.items():
            if symbol == active:
                button.config(background=COLOR_WHITE, foreground=COLOR_ORANGE)
            else:
                button.config(background=COLOR_ORANGE, foreground=COLOR_WHITE)


def main():
    window = tkinter.Tk()
    CalculatorApp(window)
    window.mainloop()


if __name__ == "__main__":
    main()
