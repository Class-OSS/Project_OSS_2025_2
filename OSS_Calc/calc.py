import tkinter as tk
import math # 팩토리얼 계산을 위해 math 모듈 추가

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("300x400")

        self.expression = ""

        # 입력창
        self.entry = tk.Entry(root, font=("Arial", 24), justify="right")
        self.entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

        # 버튼 생성: 팩토리얼 버튼 '!' 추가
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', 'C', '+'],
            ['!', '='] # '!' 버튼을 추가하여 레이아웃 조정
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
        
        # 팩토리얼 처리 로직
        elif char == '!':
            current_expr = self.expression
            
            # 현재 입력창이 비어있거나 숫자 형태가 아닐 경우 오류 처리 (예: 10+ 상태)
            if not current_expr:
                self.expression = "오류: 숫자를 먼저 입력하세요"
            else:
                try:
                    # 1. 현재 표현식을 평가하여 값(float)을 가져옵니다.
                    # eval()은 사칙연산만 처리하므로, 현재 self.expression에 사칙연산 기호가 없어야 함
                    value = float(eval(current_expr))
                    
                    # 2. 팩토리얼은 0 이상의 정수에 대해서만 정의됩니다.
                    if value < 0 or value != int(value):
                        self.expression = "팩토리얼 오류: 0 이상의 정수만 가능"
                    else:
                        # 3. math.factorial을 사용하여 계산하고 문자열로 변환합니다.
                        result = math.factorial(int(value))
                        self.expression = str(result)
                        
                except (ValueError, TypeError, SyntaxError):
                    # eval 오류, math.factorial 범위 초과 오류 등을 처리
                    self.expression = "오류: 잘못된 입력 형식"
        
        elif char == '=':
            try:
                # 팩토리얼 연산이 이미 처리되었거나 순수 사칙연산만 남았을 경우 eval 수행
                self.expression = str(eval(self.expression)) 
            except Exception:
                self.expression = "에러"
        
        else:
            self.expression += str(char)

        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)
