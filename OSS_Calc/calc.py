import tkinter as tk
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("300x400")

        self.expression = ""

        # 입력창
        self.entry = tk.Entry(root, font=("Arial", 24), justify="right")
        self.entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

        # 버튼 생성
        buttons = [
            ['log', 'ln', '(', ')'],   # 로그 및 괄호
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
        elif char == '=':
            try:
                expr = self.expression
                expr = expr.replace('log', 'math.log10') # 상용로그
                expr = expr.replace('ln', 'math.log')    # 자연로그
                
                self.expression = str(eval(expr))
            except Exception:
                self.expression = "에러"
        else:
            if char in ['log', 'ln']:
                self.expression += char + "("
            else:
                self.expression += str(char)

        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)
