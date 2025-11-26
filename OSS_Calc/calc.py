import tkinter as tk
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("300x400")

        self.expression = ""

        #입력창
        self.entry = tk.Entry(root, font=("Arial", 24), justify="right")
        self.entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

        #버튼 생성
        buttons = [
            ['(', ')', '√', '/'], #괄호와 루트 기호 추가
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '.', 'C', '='], 
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
                #루트 기호 '√'를 계산 가능한 'math.sqrt(' 문자열로 변환
                calculation_expression = self.expression.replace('√', 'math.sqrt(')
                
                #'math.sqrt(' 사용으로 닫는 괄호 ')'가 부족해진 경우 자동으로 추가
                open_count = calculation_expression.count('(')
                close_count = calculation_expression.count(')')
                
                if open_count > close_count:
                    calculation_expression += ')' * (open_count - close_count)

                #계산 실행
                result = str(eval(calculation_expression))
                
                #결과가 정수 형태일 때 불필요한 소수점(.0) 제거
                if result.endswith('.0'):
                    result = result[:-2]
                
                self.expression = result
            except Exception:
                self.expression = "에러"

        elif char == '√':
            #루트 버튼 클릭 시 수식에 '√(' 추가 (사용자가 값을 입력하도록 유도)
            self.expression += '√('
        elif char in ('(', ')'):
            #괄호는 수식에 그대로 추가
            self.expression += str(char)
        else:
            self.expression += str(char)

        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)
