# calc.py
import tkinter as tk
from tkinter import messagebox
import ast
import operator
import math
import re

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("420x400")  # 히스토리 공간을 위해 넓게
        self.expression = ""
        self.memory = 0.0

        # 레이아웃: 왼쪽 계산기, 오른쪽 히스토리
        main_frame = tk.Frame(root)
        main_frame.pack(fill="both", expand=True)

        left = tk.Frame(main_frame)
        left.pack(side="left", fill="both", expand=True, padx=5, pady=5)

        right = tk.Frame(main_frame, width=140)
        right.pack(side="right", fill="y", padx=5, pady=5)

        # 입력창
        self.entry = tk.Entry(left, font=("Arial", 24), justify="right")
        self.entry.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)
        self.entry.insert(0, self.expression)

        # 버튼 설정 (grid)
        btn_text = [
            ['MC', 'MR', 'M+', 'M-'],
            ['(', ')', '⌫', 'C'],
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['+/-', '0', '.', '+'],
            ['%', '=', '', '']
        ]

        for r, row in enumerate(btn_text, start=1):
            for c, char in enumerate(row):
                if not char: 
                    continue
                btn = tk.Button(left, text=char, font=("Arial", 16),
                                command=lambda ch=char: self.on_click(ch))
                btn.grid(row=r, column=c, sticky="nsew", padx=3, pady=3)

        # 그리드 행/열 가중치
        for i in range(4):
            left.grid_columnconfigure(i, weight=1)
        for i in range(len(btn_text)+1):
            left.grid_rowconfigure(i, weight=1)

        # 히스토리 리스트박스
        tk.Label(right, text="히스토리", font=("Arial", 12)).pack(anchor="nw")
        self.history_box = tk.Listbox(right, height=20)
        self.history_box.pack(fill="both", expand=True)
        self.history_box.bind("<Double-Button-1>", self.on_history_double)

        # 키보드 바인딩
        root.bind("<Key>", self.on_key)
        root.bind("<Return>", lambda e: self.on_click('='))
        root.bind("<BackSpace>", lambda e: self.on_click('⌫'))
        root.bind("<Escape>", lambda e: self.on_click('C'))

    def on_history_double(self, event):
        sel = self.history_box.curselection()
        if sel:
            expr = self.history_box.get(sel[0])
            # 리스트 항목은 "expr = result" 형식이므로 왼쪽 부분만 사용
            expr = expr.split(" = ")[0]
            self.expression = expr
            self.update_entry()

    def on_key(self, event):
        key = event.keysym
        char = event.char
        if char in '0123456789.+-*/()%':
            # 문자로 넣어도 됨
            self.expression += char
            self.update_entry()
        elif key == "Return":
            self.on_click('=')
        elif key == "BackSpace":
            self.on_click('⌫')
        elif key.lower() == 'c' and event.state & 0x4:  # Ctrl+C 등은 기본 복사 처리
            return
        # 기타 단축키(예: m for memory recall) 원하면 추가 가능

    def on_click(self, char):
        if char == 'C':
            self.expression = ""
            self.update_entry()
        elif char == '⌫':
            self.expression = self.expression[:-1]
            self.update_entry()
        elif char == '=':
            self.evaluate()
        elif char == 'M+':
            val = self.safe_eval(self.expression)
            if val is not None:
                self.memory += val
        elif char == 'M-':
            val = self.safe_eval(self.expression)
            if val is not None:
                self.memory -= val
        elif char == 'MR':
            # 메모리 불러오기
            self.expression += str(self.memory)
            self.update_entry()
        elif char == 'MC':
            self.memory = 0.0
        elif char == '%':
            # 간단 구현: 현재 표현식의 마지막 숫자에 대해 /100 처리
            self.apply_percent()
        elif char == '+/-':
            self.toggle_plus_minus()
        else:
            self.expression += str(char)
            self.update_entry()

    def update_entry(self):
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)

    def add_history(self, expr, result):
        item = f"{expr} = {result}"
        self.history_box.insert(0, item)  # 최신을 위로

    def evaluate(self):
        expr = self.expression.strip()
        if not expr:
            return
        val = self.safe_eval(expr)
        if val is None:
            # 에러 메시지는 safe_eval에서 이미 처리할 수 있음
            self.expression = "에러"
            self.update_entry()
            return
        # 소수점 정리: 정수면 정수로
        if isinstance(val, float) and val.is_integer():
            val = int(val)
        self.add_history(expr, val)
        self.expression = str(val)
        self.update_entry()

    def apply_percent(self):
        # 정규식으로 마지막 숫자(또는 소수)를 찾아서 (num/100)으로 바꾼다.
        m = re.search(r'(\d+(\.\d+)?)(?!.*\d)', self.expression)
        if m:
            num = m.group(1)
            start, end = m.span(1)
            self.expression = self.expression[:start] + f"({num}/100)" + self.expression[end:]
        else:
            # 숫자가 없으면 무시
            self.expression += "/100"
        self.update_entry()

    def toggle_plus_minus(self):
        # 표현식의 마지막 숫자에 대해 부호 변경 시도
        m = re.search(r'(\d+(\.\d+)?)(?!.*\d)', self.expression)
        if m:
            num = m.group(1)
            start, end = m.span(1)
            # 이미 괄호로 음수 표현이면 감싸기 방식은 간단히 (-num)
            if start >= 1 and self.expression[start-1] == '-':
                # 앞의 마이너 연산자 제거 (간단 처리)
                self.expression = self.expression[:start-1] + self.expression[start:]
            else:
                self.expression = self.expression[:start] + f"(-{num})" + self.expression[end:]
        else:
            # 전체가 비어있다면 "- " 넣기
            self.expression = "-" + self.expression
        self.update_entry()

    # 안전한 평가: ast를 이용해 허용된 연산만 수행
    def safe_eval(self, expr):
        if not expr:
            return 0
        # 허용 문자 필터(간단한 방어)
        if re.search(r'[a-zA-Z]', expr):
            messagebox.showerror("에러", "허용되지 않는 문자 포함")
            return None
        try:
            tree = ast.parse(expr, mode='eval')
            return self._eval_node(tree.body)
        except ZeroDivisionError:
            messagebox.showerror("에러", "0으로 나눌 수 없습니다.")
            return None
        except Exception as e:
            messagebox.showerror("에러", f"잘못된 수식입니다.\n{e}")
            return None

    def _eval_node(self, node):
        # 숫자
        if isinstance(node, ast.Constant):  # Python 3.8+
            if isinstance(node.value, (int, float)):
                return node.value
            else:
                raise ValueError("허용되지 않는 상수")
        if isinstance(node, ast.Num):  # 이전 버전
            return node.n
        # 이항 연산
        if isinstance(node, ast.BinOp):
            left = self._eval_node(node.left)
            right = self._eval_node(node.right)
            op = node.op
            ops = {
                ast.Add: operator.add,
                ast.Sub: operator.sub,
                ast.Mult: operator.mul,
                ast.Div: operator.truediv,
                ast.Pow: operator.pow,
                ast.Mod: operator.mod,
                ast.FloorDiv: operator.floordiv
            }
            for t, fn in ops.items():
                if isinstance(op, t):
                    return fn(left, right)
            raise ValueError("허용되지 않는 연산자")
        # 단항 연산
        if isinstance(node, ast.UnaryOp):
            operand = self._eval_node(node.operand)
            if isinstance(node.op, ast.UAdd):
                return +operand
            if isinstance(node.op, ast.USub):
                return -operand
            raise ValueError("허용되지 않는 단항 연산자")
        # 괄호는 AST에서 이미 그룹화되어 위로 처리됨
        raise ValueError("허용되지 않는 표현식")

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()