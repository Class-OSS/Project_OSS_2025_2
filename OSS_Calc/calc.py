import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("300x450")

        self.expression = ""

        # 입력창
        self.entry = tk.Entry(root, font=("Arial", 24), justify="right")
        self.entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

        # 버튼 구성
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', 'C', '+'],
            ['='],
            ['C→F', 'F→C']
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

    # 섭씨 → 화씨 변환
    def c_to_f(self, c):
        return (c * 9/5) + 32

    # 화씨 → 섭씨 변환
    def f_to_c(self, f):
        return (f - 32) * 5/9

    def on_click(self, char):
        # 초기화
        if char == 'C':
            self.expression = ""

        # 계산 실행 (=)
        elif char == '=':
            try:
                self.expression = str(eval(self.expression))
            except Exception:
                self.expression = "에러"

        # 섭씨 → 화씨 버튼
        elif char == 'C→F':
            try:
                value = float(self.expression)
                self.expression = str(self.c_to_f(value))
            except:
                self.expression = "에러"

        # 화씨 → 섭씨 버튼
        elif char == 'F→C':
            try:
                value = float(self.expression)
                self.expression = str(round(self.f_to_c(value), 2))
            except:
                self.expression = "에러"

        # 숫자/기호 입력
        else:
            self.expression += str(char)

        # 화면에 출력
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)
