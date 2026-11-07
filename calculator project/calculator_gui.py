
import tkinter

button_values = [
    ["AC", "+/-", "%", "÷"],
    ["7", "8", "9", "×"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "✓", "="]
]

right_symbols = ["÷", "×", "-", "+", "="]
top_symbols = ["AC", "+/-", "%"]

row_count = len(button_values) #5
column_count = len(button_values[0]) #4


color_light_grey = "#D4D4D2"
color_black = "#000000"
color_dark_grey = "#505050"
color_orange = "#FF9500"
color_white = "#FFFFFF"

# This imports the window for the calculator

window = tkinter.Tk() # Create the window

window.title("Calculator Main")

window.resizable(False, False)

window.mainloop()
