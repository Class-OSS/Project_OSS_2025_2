import tkinter as tk
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        # 글자 수가 많아서 가로 폭 증가
        self.root.geometry("400x400")

        self.expression = ""

        # 입력창
        self.entry = tk.Entry(root, font=("Arial", 24), justify="right")
        self.entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

        # 버튼 생성
        buttons = [
            ['arcsin', 'arccos', 'arctan', '(', ')'], 
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
                original_expr = self.expression
                expr = self.expression
                
                # 함수 이름 치환
                expr = expr.replace('arcsin', 'math.asin')
                expr = expr.replace('arccos', 'math.acos')
                expr = expr.replace('arctan', 'math.atan')
                
                # 아크 함수 포함 여부 확인 및 조건부 변환
                arc_keywords = ['arcsin', 'arccos', 'arctan']
                
                # original_expr에 아크 함수 키워드가 하나라도 포함되어 있는지 확인
                is_arc_function_present = any(kw in original_expr for kw in arc_keywords)
                
                # 치환된 수식을 기본 계산 수식으로 설정
                full_expr = expr
                
                # 아크 함수가 있으면 math.degrees()로 감싸서 각도로 변환
                if is_arc_function_present:
                    full_expr = f"math.degrees({expr})"
                
                # 계산 및 결과 저장
                self.expression = str(eval(full_expr))
                
            except Exception:
                self.expression = "에러"
        else:
            if char in ['arcsin', 'arccos', 'arctan']:
                self.expression += char
            else:
                self.expression += str(char)

        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)