import tkinter as tk
import re #  정규식(re) 모듈 추가


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
                # 계산 전에 표현식 전처리 (숫자 앞의 불필요한 0 제거)
                # 정규식 패턴: (^|[-+*/])0+([1-9])
                # - (^|[-+*/]): 문자열 시작(^)이거나 연산자([*+/-]) 뒤를 찾음 (그룹 1: \1)
                # - 0+ : 0이 하나 이상 반복되는 것을 찾음
                # - ([1-9]) : 0이 아닌 1~9 사이의 숫자를 찾음 (그룹 2: \2)
                # 이 패턴에 걸린 '0'들은 제거되어 '03+7'이 '3+7'로 변환됩니다.
                sanitized_expression = re.sub(r'(^|[-+*/])0+([1-9])', r'\1\2', self.expression)
                
                self.expression = str(eval(sanitized_expression))

            except Exception:
                self.expression = "에러"
        else:
            self.expression += str(char)

        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)