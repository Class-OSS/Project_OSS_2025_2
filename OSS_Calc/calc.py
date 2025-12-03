import tkinter as tk
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("공학용 계산기")
        self.root.geometry("300x450")

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
            ['x²', '√', '^', '=']   # <--- [핵심] 버튼을 4개로 늘려서 UI를 완성했습니다
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
        try:
            if char == 'C':
                self.expression = ""
            
            elif char == '=':
                # eval 함수를 통해 수식을 계산
                self.expression = str(eval(self.expression))
            
            elif char == 'x²':
                val = eval(self.expression)
                self.expression = str(val ** 2)
            
            elif char == '√':
                val = eval(self.expression)
                self.expression = str(math.sqrt(val))
            
            # --- [신규 기능] 거듭제곱 (^) ---
            elif char == '^':
                # 파이썬에서 거듭제곱은 ** 기호를 사용합니다.
                # 예: 2의 3승 -> 2**3
                self.expression += "**"
            
            else:
                self.expression += str(char)
            
            # 화면 갱신
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, self.expression)

        except Exception:
            self.expression = "에러"
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, self.expression)
            self.expression = ""
