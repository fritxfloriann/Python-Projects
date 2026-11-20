import tkinter as tk
from tkinter import ttk

from converter import convert, supported_units, ConversionError

CATEGORY_LABELS = {
    "length": "Length",
    "mass": "Mass",
    "volume": "Volume",
    "temperature": "Temperature",
}


class ConverterApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Unit Converter")
        self.resizable(False, False)

        self.units_by_category = supported_units()

        self._build_widgets()
        self._on_category_change()

    def _build_widgets(self):
        pad = {"padx": 10, "pady": 6}
        frame = ttk.Frame(self, padding=16)
        frame.grid(row=0, column=0, sticky="nsew")

        # Category
        ttk.Label(frame, text="Category").grid(row=0, column=0, sticky="w", **pad)
        self.category_var = tk.StringVar(value="length")
        category_box = ttk.Combobox(
            frame,
            textvariable=self.category_var,
            values=list(self.units_by_category.keys()),
            state="readonly",
            width=18,
        )
        category_box.grid(row=0, column=1, columnspan=2, sticky="ew", **pad)
        category_box.bind("<<ComboboxSelected>>", lambda e: self._on_category_change())

        # Value entry
        ttk.Label(frame, text="Value").grid(row=1, column=0, sticky="w", **pad)
        self.value_var = tk.StringVar(value="1")
        value_entry = ttk.Entry(frame, textvariable=self.value_var, width=20)
        value_entry.grid(row=1, column=1, columnspan=2, sticky="ew", **pad)
        value_entry.bind("<KeyRelease>", lambda e: self._convert())

        # From unit
        ttk.Label(frame, text="From").grid(row=2, column=0, sticky="w", **pad)
        self.from_var = tk.StringVar()
        self.from_box = ttk.Combobox(frame, textvariable=self.from_var, state="readonly", width=10)
        self.from_box.grid(row=2, column=1, sticky="ew", **pad)
        self.from_box.bind("<<ComboboxSelected>>", lambda e: self._convert())

        swap_btn = ttk.Button(frame, text="⇄", width=3, command=self._swap_units)
        swap_btn.grid(row=2, column=2, sticky="ew", **pad)

        # To unit
        ttk.Label(frame, text="To").grid(row=3, column=0, sticky="w", **pad)
        self.to_var = tk.StringVar()
        self.to_box = ttk.Combobox(frame, textvariable=self.to_var, state="readonly", width=10)
        self.to_box.grid(row=3, column=1, sticky="ew", **pad)
        self.to_box.bind("<<ComboboxSelected>>", lambda e: self._convert())

        # Result
        ttk.Separator(frame, orient="horizontal").grid(
            row=4, column=0, columnspan=3, sticky="ew", pady=(10, 10)
        )
        self.result_var = tk.StringVar(value="")
        result_label = ttk.Label(
            frame, textvariable=self.result_var, font=("TkDefaultFont", 13, "bold")
        )
        result_label.grid(row=5, column=0, columnspan=3, sticky="w", padx=10)

        self.error_var = tk.StringVar(value="")
        error_label = ttk.Label(frame, textvariable=self.error_var, foreground="#b00020")
        error_label.grid(row=6, column=0, columnspan=3, sticky="w", padx=10)

        for col in range(3):
            frame.columnconfigure(col, weight=1)

    def _on_category_change(self):
        category = self.category_var.get()
        units = self.units_by_category.get(category, [])
        self.from_box["values"] = units
        self.to_box["values"] = units
        if units:
            self.from_var.set(units[0])
            self.to_var.set(units[1] if len(units) > 1 else units[0])
        self._convert()

    def _swap_units(self):
        old_from, old_to = self.from_var.get(), self.to_var.get()
        self.from_var.set(old_to)
        self.to_var.set(old_from)
        self._convert()

    def _convert(self):
        self.error_var.set("")
        value_text = self.value_var.get().strip()
        from_unit = self.from_var.get()
        to_unit = self.to_var.get()

        if not value_text or not from_unit or not to_unit:
            self.result_var.set("")
            return

        try:
            value = float(value_text)
        except ValueError:
            self.result_var.set("")
            self.error_var.set("Enter a valid number")
            return

        try:
            result = convert(value, from_unit, to_unit, category=self.category_var.get())
        except ConversionError as e:
            self.result_var.set("")
            self.error_var.set(str(e))
            return

        self.result_var.set(f"{value:g} {from_unit} = {result:.6g} {to_unit}")


if __name__ == "__main__":
    app = ConverterApp()
    app.mainloop()
