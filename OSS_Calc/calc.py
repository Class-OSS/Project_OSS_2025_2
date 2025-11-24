import tkinter as tk
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("380x450")  # Backspace 버튼 공간 확보

        self.expression = ""

        # 입력창
        self.entry = tk.Entry(root, font=("Arial", 24), justify="right")
        self.entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

        # 버튼 배열 (Backspace 추가)
        buttons = [
            ['7', '8', '9', '/', 'sin'],
            ['4', '5', '6', '*', 'cos'],
            ['1', '2', '3', '-', 'tan'],
            ['0', '.', 'C', 'Back', '+'],
            ['(', ')', '=']
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

        # 삼각함수 안전 처리
        self.safe_dict = {
            "sin": lambda x: math.sin(math.radians(x)),
            "cos": lambda x: math.cos(math.radians(x)),
            "tan": lambda x: math.tan(math.radians(x)),
            "pi": math.pi,
            "e": math.e,
        }

    def on_click(self, char):
        if char == 'C':
            self.expression = ""
        elif char == 'Back':
            # 마지막 글자 제거
            if self.expression:
                self.expression = self.expression[:-1]
        elif char == '=':
            try:
                # 자동 괄호 닫기
                open_count = self.expression.count('(')
                close_count = self.expression.count(')')
                expr = self.expression + ')' * (open_count - close_count)

                # 안전하게 eval 실행
                result = eval(expr, {"__builtins__": None}, self.safe_dict)

                # 소수점 깔끔하게
                if isinstance(result, float):
                    result = round(result, 6)

                self.expression = str(result)
            except Exception:
                self.expression = "에러"
        elif char in ['sin', 'cos', 'tan']:
            self.expression += char + "("
        else:
            self.expression += str(char)

        # 결과 표시
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)
