import tkinter as tk
import math
import re

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("300x500")

        self.expression = ""
        self.degree = True	# True = deg, False = rad

        # 입력창
        self.entry = tk.Entry(root, font=("Arial", 24), justify="right")
        self.entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

        # 버튼 생성
        buttons = [
            ['sin', 'cos', 'π', 'degree'],
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', 'C', '+'],
            ['(', ')', '%', '=']
        ]
        
        self.degree_button = None

        for row in buttons:
            frame = tk.Frame(root)
            frame.pack(expand=True, fill="both")
            for char in row:
                
                if char == 'degree':
                    btn_text = "deg"
                    cmd = self.toggle
                else:
                    btn_text = char
                    cmd = lambda ch = char: self.on_click(ch)
                
                btn = tk.Button(
                    frame,
                    text=btn_text,
                    font=("Arial", 14),
                    command=cmd
                )
                btn.pack(side="left", expand=True, fill="both")
                
                if char == 'degree':
                    self.degree_button = btn

    def on_click(self, char):
        if char == 'C':
            self.expression = ""
        elif char == '=':
            self.calculate()
        elif char in ['sin', 'cos']:
            self.expression += char + "("
        elif char == 'π':
            self.expression += "π"
        else:
            self.expression += str(char)

        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)
        
    def toggle(self):
        self.degree = not self.degree
        
        if self.degree == True:
            self.degree_button.config(text = "deg")
        else:
            self.degree_button.config(text = "rad")
    
    def calculate(self):
        try:
            expr = self.expression
            expr = re.sub(r'(\d+)%', r'(\1/100)', expr)
            expr = re.sub(r'(\d)(sin|cos|π)', r'(\1*\2)', expr)

            if self.degree == True:
                def my_sin(x): return math.sin(math.radians(x))
                def my_cos(x): return math.cos(math.radians(x))
            else:
                def my_sin(x): return math.sin(x)
                def my_cos(x): return math.cos(x)
            
            safe = {
                "sin": my_sin,
                "cos": my_cos,
                "π": math.pi,
                "__builtins__": {}
            }

            result = eval(expr, safe)
            
            self.expression = str(result)
        except Exception:
            print(Exception)
            self.expression = "에러"
