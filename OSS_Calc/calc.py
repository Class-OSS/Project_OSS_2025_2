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
            ['sqrt', '^2', '=']   # 기능 추가된 부분
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
            
        elif char == 'sqrt':
            try:
                # 식이 비어있지 않을 때만 계산
                if self.expression:
                    val = eval(self.expression)
                    if val < 0:
                        self.expression = "에러" # 음수 제곱근 방지
                    else:
                        self.expression = str(math.sqrt(val))
            except:
                self.expression = "에러"

        elif char == '^2':
            try:
                if self.expression:
                    # 입력된 식을 괄호로 묶고 제곱
                    self.expression = str(eval(self.expression) ** 2)
            except:
                self.expression = "에러"

        elif char == '=':
            try:
                self.expression = str(eval(self.expression))
            except Exception:
                self.expression = "에러"
        else:
            self.expression += str(char)

        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)