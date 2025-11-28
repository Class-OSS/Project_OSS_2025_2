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
            ['f', '=']
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
    def cal_fibo(self, k):
        if k <= 0:
            return 0;
        elif k == 1 or k == 2:
            return 1
        else:
            return self.cal_fibo(k-1) + self.cal_fibo(k-2)

    def on_click(self, char):
        if char == 'C':
            self.expression = ""
        elif char == '=':
            try:
                self.expression = str(eval(self.expression))
            except Exception:
                self.expression = "에러"
        elif char == 'f':
            try:
                k = int(eval(self.expression))
                if k < 0:
                    self.expression = "음수의 값을 입력하지 마시오."
                else:
                    result = self.cal_fibo(k)
                    self.expression = str(result)
            except Exception:
                self.expression = "입력된 값이 잘못되었습니다."
        else:
            self.expression += str(char)

        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)





