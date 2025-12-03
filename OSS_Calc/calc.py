import tkinter as tk
import math 

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("300x400")

        self.expression = ""

        # 입력창
        self.entry = tk.Entry(root, font=("Arial", 20), justify="right")
        self.entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

        # 버튼 생성 
        buttons = [
            ['\u221A', 'x\u00B2', 'C', '/'], # PR 3: 루트, 제곱 기능
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '.', 'DEL', '='], # PR 2: DEL 기능
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
        current_sequence = self.expression 

        # 1. 루트 (SQRT) 기능 
        if char == '\u221A':
            try:
                # 입력된 숫자를 계산하여 math.sqrt로 처리 (변수명 'val_for_sqrt'로 변경)
                val_for_sqrt = float(eval(current_sequence))
                if val_for_sqrt < 0:
                    self.expression = "Invalid Input" 
                else:
                    self.expression = str(math.sqrt(val_for_sqrt))
            except Exception:
                self.expression = "sqrt error" 

        # 2. 제곱 (POWER) 기능
        elif char == 'x\u00B2':
            try:
                # 입력된 숫자를 계산하여 ** 연산자를 이용해 제곱 계산
                val_for_pow = float(eval(current_sequence))
                self.expression = str(val_for_pow ** 2) 
            except Exception:
                self.expression = "power error" 
                
        # 3. 백스페이스 (DEL) 기능 
        elif char == 'DEL':
            if current_sequence:
                self.expression = current_sequence[0:len(current_sequence)-1]

        # 4. 초기화 (Clear) 기능
        elif char == 'C':
            self.expression = ""

        # 5. 등호 (Equal) 기능
        elif char == '=':
            try:
                result_calc = str(eval(self.expression)) 
                self.expression = result_calc
            except Exception:
                self.expression = "Calc Error" 

        # 6. 숫자 및 연산자 입력
        else:
            self.expression += str(char) 

        # 입력창 업데이트
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)


