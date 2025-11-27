import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("300x400")

        self.expression = ""

        # 입력창
        self.entry = tk.Entry(root, font=("Arial", 24), justify="right")
        self.entry.pack(fill="both", padx=8, ipady=15, pady=10)

        # 버튼 세팅
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '(', ')', '+'],
            ['C', '=']
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
        # 커서 위치 얻기
        cursor_pos = self.entry.index(tk.INSERT)

        # 전체 초기화
        if char == 'C':
            self.expression = ""
            self.entry.delete(0, tk.END)
            return

        # 괄호 자동완성
        elif char == '(':
            self.expression = (
                self.expression[:cursor_pos] + "()" + self.expression[cursor_pos:]
            )

            self.entry.delete(0, tk.END)
            self.entry.insert(0, self.expression)

            # 커서를 () 안으로 이동
            self.entry.icursor(cursor_pos + 1)
            return

        # ) 그냥 입력
        elif char == ')':
            self.expression = (
                self.expression[:cursor_pos] + ")" + self.expression[cursor_pos:]
            )
            self.entry.delete(0, tk.END)
            self.entry.insert(0, self.expression)
            self.entry.icursor(cursor_pos + 1)
            return

        # 계산
        elif char == '=':
            try:
                self.expression = str(eval(self.expression))
            except Exception:
                self.expression = "에러"

            self.entry.delete(0, tk.END)
            self.entry.insert(0, self.expression)
            return

        # 일반 숫자/연산자 입력
        else:
            self.expression = (
                self.expression[:cursor_pos] + str(char) + self.expression[cursor_pos:]
            )

            self.entry.delete(0, tk.END)
            self.entry.insert(0, self.expression)
            self.entry.icursor(cursor_pos + 1)


