
# New Tkinter Calculator 

import operator
import tkinter
import tkinter.font
from decimal import ROUND_HALF_UP, Context, Decimal

BUTTON_VALUES = [
    ["AC", "+/-", "%", "÷"],
    ["7", "8", "9", "×"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    [".", "0", "⌫", "="],
]

RIGHT_SYMBOLS = ["÷", "×", "-", "+", "="]
TOP_SYMBOLS = ["AC", "+/-", "%"]

COLUMN_COUNT = len(BUTTON_VALUES[0])

COLOR_LIGHT_GREY = "#D4D4D2"
COLOR_BLACK = "#000000"
COLOR_DARK_GREY = "#505050"
COLOR_ORANGE = "#FF9500"
COLOR_WHITE = "#FFFFFF"

# Lighter shades that show while a button is held down
COLOR_LIGHT_GREY_PRESSED = "#EBEBE9"
COLOR_DARK_GREY_PRESSED = "#7A7A7A"
COLOR_ORANGE_PRESSED = "#FFB84D"
COLOR_WHITE_PRESSED = "#F2F2F2"

FONT_FAMILY = "Arial"
BUTTON_FONT = (FONT_FAMILY, 30)
DISPLAY_FONT_SIZES = (45, 40, 35, 30, 25, 20)  # biggest first; long numbers shrink
DISPLAY_PADDING = 12  # space between the display text and the window edge

MAX_DIGITS = 9  # most digits you can type, and most digits a result shows
ERROR_TEXT = "Math Error"
DIGITS = tuple("0123456789")

# Each operator symbol maps to the function that performs it.
OPERATIONS = {
    "+": operator.add,
    "-": operator.sub,
    "×": operator.mul,
    "÷": operator.truediv,
}

# Rounds to MAX_DIGITS significant digits. Used for the DISPLAY only - the
# full-precision number is kept internally, so no accuracy is lost.
DISPLAY_CONTEXT = Context(prec=MAX_DIGITS, rounding=ROUND_HALF_UP)


# ---------------------------------------------------------------------------
# Calculator logic (no Tkinter in here)
# ---------------------------------------------------------------------------

def format_number(number):
    """Turn a Decimal into display text: 0.3, -5, 1234.5, 1.23456789e+10."""
    if number == 0:
        return "0"  # also turns -0 into 0
    rounded = DISPLAY_CONTEXT.create_decimal(number).normalize()  # drops trailing zeros
    exponent = rounded.adjusted()  # position of the first digit: 1234 -> 3, 0.05 -> -2
    if -6 <= exponent < MAX_DIGITS:
        return format(rounded, "f")  # plain notation
    return format(rounded, "e")  # scientific notation for huge / tiny numbers


def calculate(left, symbol, right):
    """Work out `left symbol right`. Raises ZeroDivisionError for x ÷ 0."""
    if symbol == "÷" and right == 0:
        raise ZeroDivisionError("division by zero")
    return OPERATIONS[symbol](left, right)


class Calculator:
    """The calculator's brain: feed it button symbols with press().

    Numbers are Decimals, not floats, so 0.1 + 0.2 is exactly 0.3.
    Sums run left to right as you press the keys, like a basic iPhone
    calculator (2 + 3 × 4 = 20, not 14).
    """

    def __init__(self):
        self.clear()

    def clear(self):
        """AC: go back to the start-up state (this resets everything)."""
        self.entry = "0"  # text of the number being typed, e.g. "-12.5"
        self.typing = False  # True while the display shows a typed number
        self.value = Decimal(0)  # the number shown whenever we are not typing
        self.left_operand = None  # first number of an unfinished calculation
        self.pending_operator = None  # operator waiting to be calculated
        self.awaiting_operand = False  # True right after an operator key
        self.last_operator = None  # remembered so "=" can repeat the sum
        self.last_operand = None
        self.error = False

    # --- what the GUI reads ------------------------------------------------

    @property
    def display_text(self):
        """The text the display should show right now."""
        if self.error:
            return ERROR_TEXT
        if self.typing:
            return self.entry
        return format_number(self.value)

    @property
    def waiting_operator(self):
        """The operator that is waiting for its second number (or None)."""
        return self.pending_operator if self.awaiting_operand else None

    def current_value(self):
        """The number on the display, as a Decimal."""
        return Decimal(self.entry) if self.typing else self.value

    # --- the one entry point -------------------------------------------------

    def press(self, key):
        """Handle one button press. `key` is a symbol from BUTTON_VALUES."""
        if self.error:
            if key not in DIGITS and key not in (".", "AC"):
                return  # while the error shows, only AC or a new number works
            self.clear()  # recover, then handle the key as normal below
        try:
            if key in DIGITS:
                self.input_digit(key)
            elif key == ".":
                self.input_decimal()
            elif key in OPERATIONS:
                self.choose_operator(key)
            elif key == "=":
                self.equals()
            elif key == "AC":
                self.clear()
            elif key == "+/-":
                self.toggle_sign()
            elif key == "%":
                self.percent()
            elif key == "⌫":
                self.backspace()
        except ArithmeticError:  # division by zero, number too big, ...
            self.clear()
            self.error = True

    # --- typing numbers ------------------------------------------------------

    def start_entry(self, text):
        """Begin typing a new number."""
        self.entry = text
        self.typing = True
        self.awaiting_operand = False

    def digit_count(self):
        """How many digits have been typed so far."""
        return len(self.entry.replace("-", "").replace(".", ""))

    def input_digit(self, digit):
        if not self.typing:
            self.start_entry(digit)
        elif self.digit_count() < MAX_DIGITS:
            if self.entry in ("0", "-0"):
                self.entry = self.entry[:-1] + digit  # replace the lone zero
            else:
                self.entry += digit

    def input_decimal(self):
        if not self.typing:
            self.start_entry("0.")
        elif "." not in self.entry and self.digit_count() < MAX_DIGITS:
            self.entry += "."

    def backspace(self):
        """⌫: delete the last typed character (results can't be edited)."""
        if not self.typing:
            return
        self.entry = self.entry[:-1]
        if self.entry in ("", "-"):
            self.entry = "0"

    def toggle_sign(self):
        """+/-: flip the sign of the number on the display."""
        if self.typing:
            if self.entry.startswith("-"):
                self.entry = self.entry[1:]
            else:
                self.entry = "-" + self.entry
        elif self.awaiting_operand or self.value == 0:
            self.start_entry("-0")  # start typing a negative number
        else:
            self.value = -self.value

    def percent(self):
        """%: divide the number on the display by 100."""
        self.value = self.current_value() / 100
        self.typing = False
        self.awaiting_operand = False

    # --- calculating ---------------------------------------------------------

    def choose_operator(self, symbol):
        """+ - × ÷ : remember the operator, finishing any earlier sum first."""
        if self.pending_operator is None:
            # First operator: the number on the display becomes the left side.
            self.left_operand = self.current_value()
        elif not self.awaiting_operand:
            # "5 + 3 ×": finish 5 + 3 first (left to right, like the iPhone).
            self.left_operand = calculate(
                self.left_operand, self.pending_operator, self.current_value()
            )
        # Otherwise ("5 + ×") no second number was entered, so the new
        # operator simply replaces the old one.
        self.value = self.left_operand
        self.typing = False
        self.pending_operator = symbol
        self.awaiting_operand = True

    def equals(self):
        """=: finish the sum, or repeat the last one if there is nothing pending."""
        if self.pending_operator is not None:
            right = self.current_value()  # "5 + =" uses 5 again, like the iPhone
            result = calculate(self.left_operand, self.pending_operator, right)
            self.last_operator, self.last_operand = self.pending_operator, right
        elif self.last_operator is not None:
            # "5 + 3 = =": repeat "+ 3" on whatever is on the display.
            result = calculate(self.current_value(), self.last_operator, self.last_operand)
        else:
            result = self.current_value()  # nothing to calculate: "5 =" shows 5
        self.value = result
        self.typing = False
        self.left_operand = None
        self.pending_operator = None
        self.awaiting_operand = False


# ---------------------------------------------------------------------------
# Tkinter window
# ---------------------------------------------------------------------------

# Keyboard: special keys (by Tk key name) and ordinary characters.
KEYSYM_MAP = {
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
    **{"KP_" + digit: digit for digit in DIGITS},
}

CHAR_MAP = {
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


def button_colors(symbol, selected=False):
    """Button options (colours) for one calculator button."""
    if symbol in TOP_SYMBOLS:
        text, background, pressed = COLOR_BLACK, COLOR_LIGHT_GREY, COLOR_LIGHT_GREY_PRESSED
    elif symbol in RIGHT_SYMBOLS and selected:
        # The operator waiting for its second number is shown inverted.
        text, background, pressed = COLOR_ORANGE, COLOR_WHITE, COLOR_WHITE_PRESSED
    elif symbol in RIGHT_SYMBOLS:
        text, background, pressed = COLOR_WHITE, COLOR_ORANGE, COLOR_ORANGE_PRESSED
    else:
        text, background, pressed = COLOR_WHITE, COLOR_DARK_GREY, COLOR_DARK_GREY_PRESSED
    return {
        "foreground": text,
        "background": background,
        "activeforeground": text,
        "activebackground": pressed,
    }


class CalculatorApp:
    """The Tkinter window: draws the calculator and passes presses to Calculator."""

    def __init__(self, window):
        self.window = window
        self.calculator = Calculator()
        self.buttons = {}  # symbol -> Button, so the operators can be recoloured

        window.title("Calculator Main")
        window.resizable(False, False)

        self.frame = tkinter.Frame(window, background=COLOR_BLACK)
        self.create_display()
        self.create_buttons()
        self.frame.pack()

        # Keyboard presses go through the same code as the mouse buttons.
        window.bind_all("<Key>", self.on_key_press)

        window.update_idletasks()  # let Tk work out the real widget sizes
        # Keep the display row the same height when the font shrinks, and
        # remember how much room the text has.
        self.frame.rowconfigure(0, minsize=self.display.winfo_reqheight())
        self.display_width = self.frame.winfo_reqwidth() - 2 * DISPLAY_PADDING

        self.refresh_display()
        self.centre_window()

    def create_display(self):
        # One Font per size; keeping them in a list stops Tk from discarding them.
        self.display_fonts = [
            tkinter.font.Font(root=self.window, family=FONT_FAMILY, size=size)
            for size in DISPLAY_FONT_SIZES
        ]
        self.display = tkinter.Label(
            self.frame,
            text="0",
            font=self.display_fonts[0],
            background=COLOR_BLACK,
            foreground=COLOR_WHITE,
            anchor="e",
            width=COLUMN_COUNT,
            padx=DISPLAY_PADDING,
            borderwidth=0,
        )
        self.display.grid(row=0, column=0, columnspan=COLUMN_COUNT, sticky="we")

    def create_buttons(self):
        for row, row_symbols in enumerate(BUTTON_VALUES):
            for column, symbol in enumerate(row_symbols):
                button = tkinter.Button(
                    self.frame,
                    text=symbol,
                    font=BUTTON_FONT,
                    width=COLUMN_COUNT - 1,
                    height=1,
                    relief="flat",
                    borderwidth=0,
                    highlightthickness=0,
                    # "symbol=symbol" makes each button remember its own symbol.
                    command=lambda symbol=symbol: self.on_button_click(symbol),
                    **button_colors(symbol),
                )
                button.grid(row=row + 1, column=column, padx=1, pady=1)
                self.buttons[symbol] = button

    def on_button_click(self, symbol):
        self.calculator.press(symbol)
        self.refresh_display()

    def on_key_press(self, event):
        symbol = KEYSYM_MAP.get(event.keysym) or CHAR_MAP.get(event.char)
        if symbol is None:
            return None  # not a calculator key (Shift, arrows, F1, ...)
        self.on_button_click(symbol)
        return "break"

    def fit_font(self, text):
        """Return the biggest display font in which `text` still fits."""
        for font in self.display_fonts:
            if font.measure(text) <= self.display_width:
                return font
        return self.display_fonts[-1]  # nothing fits, so use the smallest

    def refresh_display(self):
        """Show the calculator's current state on screen."""
        text = self.calculator.display_text
        self.display.config(text=text, font=self.fit_font(text))

        # Invert the operator that is waiting for its second number.
        waiting = self.calculator.waiting_operator
        for symbol in OPERATIONS:
            self.buttons[symbol].config(**button_colors(symbol, selected=(symbol == waiting)))

    def centre_window(self):
        self.window.update_idletasks()
        width = self.window.winfo_reqwidth()
        height = self.window.winfo_reqheight()
        x = (self.window.winfo_screenwidth() - width) // 2
        y = (self.window.winfo_screenheight() - height) // 2
        self.window.geometry(f"+{x}+{y}")


def main():
    window = tkinter.Tk()
    CalculatorApp(window)
    window.mainloop()


if __name__ == "__main__":
    main()