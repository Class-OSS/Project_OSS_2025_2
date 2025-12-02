import tkinter as tk


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("300x400")

        self.expression = ""

        self.formula_label = tk.Label(root, text="", font=("Arial", 12), fg="gray", anchor="e")
        self.formula_label.pack(fill="both", padx=10)

        self.entry = tk.Entry(root, font=("Arial", 24), justify="right")
        self.entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', 'C', '+'],
            ['=']
        ]

        for row in buttons:
            frame = tk.Frame(root)
            frame.pack(expand=True, fill="both")
            for char in row:
                btn = tk.Button(
                    frame,
                    text=char,
                    font=("Arial", 18),
                    command=lambda ch=char: self.on_click(ch)
                )
                btn.pack(side="left", expand=True, fill="both")

    def on_click(self, char):
        if char == 'C':
            self.expression = ""
            self.formula_label.config(text="")
        elif char == '=':
            try:
                result = str(eval(self.expression))
                self.formula_label.config(text=self.expression)
                self.expression = result
            except Exception:
                self.expression = "error"
                self.formula_label.config(text="")
        else:
            if self.expression == "error":
                self.expression = ""
            self.expression += str(char)
            self.formula_label.config(text=self.expression)

        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)
