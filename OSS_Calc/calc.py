import tkinter as tk
import math # e와 π의 값을 추가하기 위함 


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("300x400")

        self.expression = ""

        # 입력창
        self.entry = tk.Entry(root, font=("Arial", 24), justify="right")
        self.entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

        # 버튼 생성, e, π, ^(거듭제곱) 기호를 추가.
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', 'C', '+'],
            ['e', 'π','^', '=']
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
                self.expression = self.expression.replace('e', str(math.e))# e를 정확한 값으로 변경
                self.expression = self.expression.replace('π', str(math.pi))# π를 정확한 값으로 변경
                self.expression = self.expression.replace('^', '**')# 거듭제곱 기호를 **로 치환
                self.expression = str(eval(self.expression))
            except Exception:
                self.expression = "에러"
        elif char == '^': # 거듭제곱 기호가 눌리면
            self.expression += '^'
        elif char == 'e': # e가 눌리면 e를 수식에 추가 
            self.expression += 'e'
        elif char == 'π': # π가 눌리면 π를 수식에 추가 
            self.expression += 'π'
        else:
            self.expression += str(char)

        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)



