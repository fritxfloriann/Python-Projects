
import tkinter

button_values = [
    ["AC", "+/-", "%", "÷"],
    ["7", "8", "9", "×"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "⌫", "="]
]

right_symbols = ["÷", "×", "-", "+", "="]
top_symbols = ["AC", "+/-", "%"]

row_count = len(button_values)
column_count = len(button_values[0])

color_light_grey = "#D4D4D2"
color_black = "#000000"
color_dark_grey = "#505050"
color_orange = "#FF9500"
color_white = "#FFFFFF"

# Create calculator window

window = tkinter.Tk()

window.title("Calculator Main")
window.resizable(False, False)

frame = tkinter.Frame(window)

label = tkinter.Label(
    frame,
    text="0",
    font=("Arial", 45),
    background=color_black,
    foreground=color_white,
    anchor="e",
    width=column_count
)

label.grid(
    row=0,
    column=0,
    columnspan=column_count,
    sticky="we"
)

# Create calculator buttons

for row in range(row_count):
    for column in range(column_count):

        value = button_values[row][column]

        button = tkinter.Button(
            frame,
            text=value,
            font=("Arial", 30),
            width=column_count-1,
            height=1,
            command=lambda value=value: button_clicked(value)
        )

        if value in top_symbols:
            button.config(
                foreground=color_black,
                background=color_light_grey
            )

        elif value in right_symbols:
            button.config(
                foreground=color_white,
                background=color_orange
            )

        else:
            button.config(
                foreground=color_white,
                background=color_dark_grey
            )

        button.grid(row=row + 1, column=column)

frame.pack()

# Calculator variables

A = "0"
operator = None
B = None
math_error = False


def clear_all():
    global A, B, operator

    A = "0"
    operator = None
    B = None


def remove_zero_decimal(num):

    if num % 1 == 0:
        num = int(num)

    return str(num)


def button_clicked(value):

    global A, B, operator, math_error

    # Handle recovery after Math Error

    if math_error:

        if value == "AC":
            math_error = False
            clear_all()
            label["text"] = "0"
            return

        elif value in "0123456789.":
            math_error = False
            clear_all()
            label["text"] = "0"

        else:
            return

    # Handle arithmetic operators

    if value in right_symbols:

        if value == "=":

            if A is not None and operator is not None:

                B = label["text"]

                numA = float(A)
                numB = float(B)

                if operator == "+":
                    result = numA + numB

                elif operator == "-":
                    result = numA - numB

                elif operator == "×":
                    result = numA * numB

                elif operator == "÷":

                    # Division by zero protection

                    if numB == 0:
                        label["text"] = "Math Error"
                        clear_all()
                        math_error = True
                        return

                    else:
                        result = numA / numB

                label["text"] = remove_zero_decimal(result)

                clear_all()

        elif value in "+-×÷":

            if operator is None:
                A = label["text"]
                label["text"] = "0"
                B = "0"

            operator = value

    # Handle special buttons

    elif value in top_symbols:

        if value == "AC":
            clear_all()
            label["text"] = "0"

        elif value == "+/-":

            result = float(label["text"]) * -1
            label["text"] = remove_zero_decimal(result)

        elif value == "%":

            result = float(label["text"]) / 100
            label["text"] = remove_zero_decimal(result)

    # Handle backspace

    elif value == "⌫":

        current_text = label["text"]

        if len(current_text) > 1:

            label["text"] = current_text[:-1]

            if label["text"] == "-":
                label["text"] = "0"

        else:
            label["text"] = "0"

    # Handle numbers and decimal points

    else:

        if value == ".":

            if value not in label["text"]:
                label["text"] += value

        elif value in "0123456789":

            if label["text"] == "0":
                label["text"] = value

            else:
                label["text"] += value


# Keyboard input

def keyboard_input(event):

    key = event.keysym
    char = event.char

    # Special keyboard keys

    key_map = {
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
        "KP_0": "0",
        "KP_1": "1",
        "KP_2": "2",
        "KP_3": "3",
        "KP_4": "4",
        "KP_5": "5",
        "KP_6": "6",
        "KP_7": "7",
        "KP_8": "8",
        "KP_9": "9"
    }

    if key in key_map:
        button_clicked(key_map[key])
        return "break"

    # Regular keyboard characters

    char_map = {
        "+": "+",
        "-": "-",
        "*": "×",
        "/": "÷",
        "=": "=",
        ".": ".",
        "%": "%"
    }

    if char in "0123456789":
        button_clicked(char)
        return "break"

    elif char in char_map:
        button_clicked(char_map[char])
        return "break"


# Connect keyboard to calculator

window.bind_all("<Key>", keyboard_input)


# Centre calculator window

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width / 2) - (window_width / 2))
window_y = int((screen_height / 2) - (window_height / 2))

window.geometry(
    f"{window_width}x{window_height}+{window_x}+{window_y}"
)

window.mainloop()
