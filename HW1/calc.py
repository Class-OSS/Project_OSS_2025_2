import math
import tkinter as tk

class ScientificCalculator:

    def __init__(self, root):
        self.root = root
        self.root.title("공학용 계산기")
        self.root.geometry("500x700")

        self.expression = ""

        self.entry = tk.Entry(root, font=("Arial", 24), justify="right")
        self.entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

        self.entry.bind("<Key>", self.key_input)
        self.entry.bind("<Return>", self.enter_pressed)
        self.entry.bind("<BackSpace>", self.backspace_pressed)

        sci_buttons = [
            ['sin', 'cos', 'tan', 'log'],
            ['sqrt', '^', '(', ')'],
        ]
        for row in sci_buttons:
            frame = tk.Frame(root)
            frame.pack(expand=True, fill="both")
            for char in row:
                self.make_buttons(frame, char, 14)

        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', 'C', '+'],
            ['=', '←']
        ]
        for row in buttons:
            frame = tk.Frame(root)
            frame.pack(expand=True, fill="both")
            for char in row:
                self.make_buttons(frame, char, 18)

    def make_buttons(self, frame, char, size):
        btn = tk.Button(
            frame,
            text=char,
            font=("Arial", size),
            command=lambda ch=char: self.on_click(ch)
        )
        btn.pack(side="left", expand=True, fill="both")

    def on_click(self, char):
        if char == 'C':
            self.expression = ""
        elif char == '←':
            self.expression = self.expression[:-1]
        elif char == '=':
            self.calculate()
        elif char == '^':
            self.expression += "**"
        else:
            self.expression += str(char)
        self.update_entry()

    def update_entry(self):
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)

    def key_input(self, event):
        allowed = "0123456789+-*/()."
        if event.char.lower() in allowed:
            self.expression += event.char
            self.update_entry()
        return "break"

    def calculate(self):
        try:
            expr = self.expression
            math_functions = {
                'sin': lambda x: math.sin(math.radians(x)),
                'cos': lambda x: math.cos(math.radians(x)),
                'tan': lambda x: math.tan(math.radians(x)),
                'log': math.log10, 
                'sqrt': math.sqrt
            }
            self.expression = str(eval(expr, {}, math_functions))
        except Exception:
            self.expression = "error"

    def enter_pressed(self, event):
        self.calculate()
        self.update_entry()
        return "break"

    def backspace_pressed(self, event):
        self.expression = self.expression[:-1]
        self.update_entry()
        return "break"