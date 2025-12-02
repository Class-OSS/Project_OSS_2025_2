import tkinter as tk
import re

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("300x460")

        self.expression = ""

        self.entry = tk.Entry(root, font=("Arial", 24), justify="right")
        self.entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

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
                    frame, text=char, font=("Arial", 18),
                    command=lambda ch=char: self.on_click(ch)
                )
                btn.pack(side="left", expand=True, fill="both")

    def on_click(self, char):
        if char == "C":
            self.reset()
        elif char == "=":
            self.calculate()
        else:
            self.expression += str(char)
            self.update_entry(self.expression)

    def reset(self):
        self.expression = ""
        self.entry.config(fg="black")
        self.update_entry("")

    def update_entry(self, text):
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, text)

    def calculate(self):
        if not self.expression:
            return

        # 허용된 문자만 입력되었는지 검사
        if not re.match(r'^[0-9+\-*/.]+$', self.expression):
            self.show_error("허용되지 않은 문자가 포함되어 있습니다.")
            return

        # 연속된 연산자 오류
        if re.search(r'[\+\-\*/]{2,}', self.expression):
            self.show_error("연산자가 연속으로 사용되었습니다.")
            return

        # 시작이나 끝이 연산자인 경우
        if self.expression[0] in "*/" or self.expression[-1] in "+-*/":
            self.show_error("잘못된 연산자 위치입니다.")
            return

        try:
            result = str(eval(self.expression))
            self.expression = result
            self.entry.config(fg="black")
            self.update_entry(result)
        except ZeroDivisionError:
            self.show_error("0으로 나눌 수 없습니다.")
        except Exception:
            self.show_error("계산에 실패했습니다.")

    def show_error(self, message):
        self.entry.config(fg="red")
        self.update_entry(message)
        self.expression = ""
