import tkinter as tk
from calc import Calculator
from matrix import MatrixOps
import ast

# 기존 Calculator 클래스는 그대로 두고, on_click에서 '=' 처리 시 행렬 연산 가능하게 수정
class MatrixCalculator(Calculator):
    def on_click(self, char):
        if char == 'C':
            self.expression = ""
        elif char == '=':
            try:
                expr = self.expression.replace(' ', '')
                # 행렬 연산 체크: 문자열이 '['로 시작하면 MatrixOps 사용
                if expr.startswith('[') and ( '+' in expr or '-' in expr or '*' in expr):
                    # 단순 parsing: '+' '-' '*' 분리
                    if '+' in expr:
                        a_str, b_str = expr.split('+')
                        a = ast.literal_eval(a_str)
                        b = ast.literal_eval(b_str)
                        result = MatrixOps.add(a, b)
                    elif '-' in expr:
                        a_str, b_str = expr.split('-')
                        a = ast.literal_eval(a_str)
                        b = ast.literal_eval(b_str)
                        result = MatrixOps.subtract(a, b)
                    elif '*' in expr:
                        a_str, b_str = expr.split('*')
                        a = ast.literal_eval(a_str)
                        b = ast.literal_eval(b_str)
                        result = MatrixOps.multiply(a, b)
                    self.expression = str(result)
                else:
                    self.expression = str(eval(self.expression))
            except Exception:
                self.expression = "에러"
        else:
            self.expression += str(char)

        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)


if __name__ == "__main__":
    root = tk.Tk()
    calc = MatrixCalculator(root)  # 기존 Calculator 대신 MatrixCalculator 사용
    root.mainloop()
