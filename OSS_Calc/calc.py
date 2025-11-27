import tkinter as tk
import math


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("350x500")

        self.expression = ""
        
        self.waiting_for_second_number = False
        self.pending_operation = None
        self.first_number = None

        # 입력창
        self.entry = tk.Entry(root, font=("Arial", 24), justify="right")
        self.entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

        # 버튼 생성
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', 'C', '+'],
            ['nCr', 'nPr', '=']
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

    def combination(self, n, r):
        if n < 0 or r < 0:
            raise ValueError("음수는 조합을 계산할 수 없습니다")
        if n != int(n) or r != int(r):
            raise ValueError("정수만 조합을 계산할 수 있습니다")
        if r > n:
            raise ValueError("r은 n보다 클 수 없습니다")
        return math.comb(int(n), int(r))

    def permutation(self, n, r):
        if n < 0 or r < 0:
            raise ValueError("음수는 순열을 계산할 수 없습니다")
        if n != int(n) or r != int(r):
            raise ValueError("정수만 순열을 계산할 수 있습니다")
        if r > n:
            raise ValueError("r은 n보다 클 수 없습니다")
        return math.perm(int(n), int(r))

    def on_click(self, char):
        if char == 'C':
            self.expression = ""
            self.waiting_for_second_number = False
            self.pending_operation = None
            self.first_number = None
            
        elif char in ['nCr', 'nPr']:
            try:
                if self.expression:
                    self.first_number = float(self.expression)
                    self.pending_operation = char
                    self.waiting_for_second_number = True
                    operator_symbol = 'C' if char == 'nCr' else 'P'
                    self.expression = f"{int(self.first_number)}{operator_symbol}"
            except Exception:
                self.expression = "에러"
                
        elif char == '=':
            try:
                if self.waiting_for_second_number and self.pending_operation:
                    operator_symbol = 'C' if self.pending_operation == 'nCr' else 'P'
                    second_part = self.expression.split(operator_symbol)[1]
                    second_number = float(second_part)
                    
                    if self.pending_operation == 'nCr':
                        result = self.combination(self.first_number, second_number)
                    elif self.pending_operation == 'nPr':
                        result = self.permutation(self.first_number, second_number)
                    self.expression = str(int(result))
                    self.waiting_for_second_number = False
                    self.pending_operation = None
                    self.first_number = None
                else:
                    self.expression = str(eval(self.expression))
            except Exception:
                self.expression = "에러"
                self.waiting_for_second_number = False
                self.pending_operation = None
                self.first_number = None
        else:
            self.expression += str(char)

        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)



