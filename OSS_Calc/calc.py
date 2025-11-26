import tkinter as tk


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
            ['0', '.', 'C[Esc]', '+'],
            ['(', ')', 'Ans[A]', '='] #괄호, Ans 버튼 추가
        ]

        # Enter 키를 on_enter 함수에 연결
        self.entry.bind("<Return>", self.on_enter)
        self.root.bind("<Return>", self.on_enter)

        # 버튼을 키보드에 할당
        self.root.bind("<Key>", self.on_key)

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
                result = str(eval(self.expression))
                self.expression = result
                self.last_result = result  # 마지막 값 저장
            except Exception:
                self.expression = "에러"

        # 마지막 결과를 현 수식 뒤에 붙이기
        elif char == 'Ans':
            if self.last_result is not None:
                self.expression += str(self.last_result)

        else:
            self.expression += str(char)

        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)

    def on_enter(self, event=None):
        # Enter 키를 누르면 바로 수식 계산 ('='과 동일한 기능)
        self.on_click('=')

    def on_key(self, event):
        key = event.keysym
        char = event.char
        
        # 숫자
        if char.isdigit():
            self.on_click(char)

        # 연산자
        elif char in ['+', '-', '*', '/', '.']:
            self.on_click(char)

        elif key == "BackSpace":
            self.expression = self.expression[:-1]
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, self.expression)   

        # Esc -> 전체 초기화 (C)
        elif key == "Escape":
            self.on_click('C')

        # 괄호
        elif char == '(':
            self.on_click('(')
        elif char == ')':
            self.on_click(')')

        # A  -> Ans
        elif key.lower() == 'a':
            self.on_click('Ans')

        # = 버튼
        elif char == '=':
            self.on_click('=')
