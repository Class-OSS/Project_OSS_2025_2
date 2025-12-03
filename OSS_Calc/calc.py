import tkinter as tk
import re

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("300x400")

        self.expression = ""
        self.should_reset = False

        self.entry = tk.Entry(root, font=("Arial", 24), justify="right")
        self.entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

        self.entry.focus_set()
        self.entry.bind("<Key>", self.process_key)

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

    def process_key(self, event):
        key = event.keysym
        char = event.char

        if key == "Return":
            self.on_click('=')
        elif key == "BackSpace":
            self.expression = self.expression[:-1]
            self.update_display()
            return "break"
        elif key == "Escape":
            self.on_click('C')
        elif char in '0123456789.+-*/':
            self.on_click(char)
       
        return "break"

    def on_click(self, char):
        if self.should_reset:
            if char in '0123456789':  
                self.expression = ""
            self.should_reset = False

        if char == 'C':
            self.expression = ""
            self.should_reset = False

        elif char == '=':
            try:
                fixed = self.fix_cal(self.expression)
                result = str(eval(fixed))

                if result.endswith(".0"):
                    result = result[:-2]
                   
                self.expression = result
                self.should_reset = True

            except Exception as e:
                self.expression = "에러"
                self.should_reset = True
        else:
            if self.expression == "에러":
                self.expression = ""
            
            if self.input_check(char):
                self.expression += str(char)
       
        self.update_display()

    def input_check(self, char): 
        if not self.expression:
            if char in '*/+':
                return False
            return True
        
        last_char = self.expression[-1]
        
        if char in '+*/' and last_char in '+*/':
            self.expression = self.expression[:-1]
            return True
        
        if char == '.':
            numbers = re.split(r'[+\-*/]', self.expression)
            if numbers and '.' in numbers[-1]:
                return False
        
        return True

    def update_display(self):
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)

    def fix_cal(self, expr):
        if not expr:
            return "0"

        while expr and expr[0] in '+*/':
            expr = expr[1:]
        
        if not expr:
            return "0"

        expr = re.sub(r'([+*/])\1+', r'\1', expr) 
        expr = re.sub(r'([+*/])\s*([+*/])', r'\2', expr)  
        
        while len(expr) > 0 and expr[-1] in "+-*/.":
            expr = expr[:-1]
        
        if not expr:
            return "0"

        expr = re.sub(r'(?<!\d)\.(\d)', r'0.\1', expr)
        expr = re.sub(r'([+\-*/])\.(\d)', r'\g<1>0.\2', expr)
        
        expr = re.sub(r'([+\-*/])\.', r'\g<1>0.', expr)

        return expr if expr else "0"

   