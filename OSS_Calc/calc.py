import tkinter as tk
import math


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("300x400")

        # 수식 문자열
        self.expression = ""

        # 입력창
        self.entry = tk.Entry(root, font=("Arial", 24), justify="right")
        self.entry.pack(fill="both", ipadx=8, ipady=15, padx=8, pady=8)

        # 버튼 배열
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', 'C', '+'],
            ['sqrt', '^', 'fact', '='],
        ]

        # 버튼 생성
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
            # 전체 지우기
            self.expression = ""

        elif char == 'sqrt':
            # 현재 수식을 평가한 뒤 제곱근
            try:
                if self.expression == "":
                    value = 0
                else:
                    value = float(eval(self.expression))
                self.expression = str(math.sqrt(value))
            except Exception:
                self.expression = "에러"

        elif char == '^':
            # 제곱 연산자: 파이썬은 ** 가 제곱
            self.expression += '**'

        elif char == 'fact':
            # 현재 수식을 정수로 평가해서 팩토리얼 계산
            try:
                if self.expression == "":
                    n = 0
                else:
                    n = int(eval(self.expression))

                if n < 0:
                    raise ValueError("음수 팩토리얼 불가")

                result = 1
                for i in range(1, n + 1):
                    result *= i
                self.expression = str(result)
            except Exception:
                self.expression = "에러"

        elif char == '=':
            # 일반 계산
            try:
                self.expression = str(eval(self.expression))
            except Exception:
                self.expression = "에러"

        else:
            # 숫자, + - * / . 등 일반 입력
            self.expression += str(char)

        # 화면에 반영
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)




