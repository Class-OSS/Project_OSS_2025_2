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
                self.expression = str(eval(self.expression))
            except Exception:
                self.expression = "에러"
        else:
            self.expression += str(char)

        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)
def continuous_calc(expression: str):
    """
    문자열로 된 수식을 계산하는 함수
    예: "3 + 5 * 2 - 4" → 9
    """

    # 1) 공백 제거
    expression = expression.replace(" ", "")

    # 2) 숫자와 연산자를 토큰 분리
    tokens = []
    num = ""
    for ch in expression:
        if ch.isdigit():
            num += ch
        else:
            tokens.append(int(num))
            tokens.append(ch)
            num = ""
    tokens.append(int(num))

    # 3) 1차: *, / 먼저 계산
    stack = []
    i = 0
    while i < len(tokens):
        if tokens[i] == '*':
            prev = stack.pop()
            next_num = tokens[i+1]
            stack.append(prev * next_num)
            i += 2
        elif tokens[i] == '/':
            prev = stack.pop()
            next_num = tokens[i+1]
            stack.append(prev / next_num)
            i += 2
        else:
            stack.append(tokens[i])
            i += 1

    # 4) 2차: +, - 계산
    result = stack[0]
    i = 1
    while i < len(stack):
        op = stack[i]
        num = stack[i+1]
        if op == '+':
            result += num
        else:
            result -= num
        i += 2

    return result