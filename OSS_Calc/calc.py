import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("300x450")  # 버튼 추가로 높이 약간 증가

        self.expression = ""

        # 입력창
        self.entry = tk.Entry(root, font=("Arial", 24), justify="right")
        self.entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

        # 버튼 생성 (괄호 및 abs 버튼 포함)
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', 'C', '+'],
            ['(', ')', 'abs', '=']  # 괄호 버튼 추가
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
                # 안전하게 abs 함수만 허용
                self.expression = str(eval(self.expression, {"__builtins__": None}, {"abs": abs}))
            except Exception:
                self.expression = "에러"
        elif char == 'abs':
            self.expression += "abs("  # abs 입력
        else:
            self.expression += str(char)  # 숫자, 연산자, 괄호 모두 처리

        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)


if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
