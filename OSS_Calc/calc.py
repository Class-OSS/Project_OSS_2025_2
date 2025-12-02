import tkinter as tk
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("300x420")
        self.expression = ""

        self.entry = tk.Entry(root, font=("Arial", 24), justify="right")
        self.entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '%', '+'],
            ['^', '√', 'C', '=']
        ]

        for row in buttons:
            frame = tk.Frame(root)
            frame.pack(expand=True, fill="both")
            for char in row:
                btn = tk.Button(
                    frame, text=char, font=("Arial", 18),
                    command=lambda ch=char: self.on_click(ch)
                )
                btn.pack(side="left", expand=True, fill="both")

    def on_click(self, char):
        if char == 'C':
            self.expression = ""
        
        elif char == '=':
            try:
                exp = self.expression

                # 제곱 연산
                exp = exp.replace("^", "**")

                # math.sqrt()로 변환
                exp = exp.replace("√", "math.sqrt(")

                # √뒤에는 괄호 닫기
                if "math.sqrt(" in exp:
                    
                    open_count = exp.count("math.sqrt(")
                    close_count = exp.count(")")
                    diff = open_count - close_count
                    exp += ")" * diff

                result = eval(exp)
                self.expression = str(result)

            except Exception:
                self.expression = "에러"

        else:
            self.expression += str(char)

        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)
