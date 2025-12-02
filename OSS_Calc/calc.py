import tkinter as tk
from sympy import symbols, diff, integrate, sympify

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("300x500")

        self.expression = ""  # 입력된 수식 저장 변수
        self.x = symbols('x')  # 미분/적분에 사용될 변수 x 정의 (SymPy용)

        # 입력창
        self.entry = tk.Entry(root, font=("Arial", 24), justify="right")
        self.entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

        # 버튼 배열 — D: 미분, I: 적분
        buttons = [
            ['7', '8', '9', '/', 'D'],  # D = derivative (미분)
            ['4', '5', '6', '*', 'I'],  # I = integral (적분)
            ['1', '2', '3', '-', '('],
            ['0', '.', 'C', '+', ')'],
            ['=']
        ]

        # 버튼 UI 생성
        for row in buttons:
            frame = tk.Frame(root)
            frame.pack(expand=True, fill="both")
            for char in row:
                btn = tk.Button(
                    frame,
                    text=char,
                    font=("Arial", 18),
                    command=lambda ch=char: self.on_click(ch)  # 버튼 클릭 시 호출
                )
                btn.pack(side="left", expand=True, fill="both")

    def on_click(self, char):
        # C: 입력 초기화
        if char == 'C':
            self.expression = ""

        # '=': 일반적인 eval 계산
        elif char == '=':
            try:
                self.expression = str(eval(self.expression))
            except Exception:
                self.expression = "에러"

      
        # D 버튼 → 미분 기능 처리
       
        elif char == 'D':
            try:
                # 입력된 문자열을 SymPy 수식으로 변환
                sym_expr = sympify(self.expression)

                # x에 대한 미분 계산
                result = diff(sym_expr, self.x)

                # 미분 결과를 문자열로 다시 저장
                self.expression = str(result)

            except Exception:
                self.expression = "에러"

        
        # I 버튼 → 적분 기능 처리
        
        elif char == 'I':
            try:
                # 입력된 문자열을 SymPy 수식으로 변환
                sym_expr = sympify(self.expression)

                # x에 대한 적분 계산
                result = integrate(sym_expr, self.x)

                # 적분 결과를 문자열로 저장
                # (여기서는 정적분이 아닌 부정적분)
                self.expression = str(result)

            except Exception:
                self.expression = "에러"

        # 일반 숫자/기호 입력 처리
        else:
            self.expression += str(char)

        # 결과표시
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)


# 실행 코드
root = tk.Tk()
Calculator(root)
root.mainloop()
