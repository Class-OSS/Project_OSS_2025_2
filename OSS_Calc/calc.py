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
            ['7', '8', '9', '/', 'C'],
            ['4', '5', '6', '*', '('],
            ['1', '2', '3', '-', ')'],
            ['0', '.', 'i', '+', '=']
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
                # 사용자가 입력한 'i'를 파이썬의 허수 단위 'j'로 변환
                calc_expression = self.expression.replace('i', 'j')
                
                # eval()로 계산 
                result = eval(calc_expression)
                
                # 결과에서 'j'를 다시 'i'로 변환하고, 괄호 제거 ( 파이썬은 괄호를 같이 출력 하기 때문 )
                self.expression = str(result).replace('j', 'i').replace('(', '').replace(')', '')
            except Exception:
                self.expression = "에러"
        else:
            self.expression += str(char)

        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)



