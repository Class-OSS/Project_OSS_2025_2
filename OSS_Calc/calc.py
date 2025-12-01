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
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', 'C', '+'],
            ['=', '√', 'x²']
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
                self.expression = str(eval(self.expression))
            except Exception:
                self.expression = "에러"
        elif char == '√':
            try:
                num = float(self.entry.get())
                result = sqrt_number(num)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
                self.expression = str(result)
            except Exception:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "에러")
                self.expression = ""
        elif char == 'x²':
            try:
                num = float(self.entry.get())
                result = square_number(num)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
                self.expression = str(result)
            except Exception:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "에러")
                self.expression = ""
        else:
            self.expression += str(char)

        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)
def sqrt_number(n):
    """Return square root of a number"""
    if n < 0:
        raise ValueError("음수의 제곱근은 계산할 수 없습니다.")
        return math.sqrt(n)
def square_number(n):
    """Return square of a number"""
    return n ** 2



