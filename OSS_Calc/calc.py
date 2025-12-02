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
            ['1', '2', '3', 'DEL'], #  'DEL' 버튼 추가
            ['0', '.', 'C', '-'],   
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
        
        # 백스페이스 기능 (DEL) 로직 추가 
        if char == 'DEL': 
            current_sequence = self.expression 
            
            if current_sequence:
                self.expression = current_sequence[0:len(current_sequence)-1]
        
        # 'C' (초기화) 
        elif char == 'C':
            self.expression = ""

        # '=' (계산) 로직
        elif char == '=':
            try:
                final_calc = str(eval(self.expression))
                self.expression = final_calc
            except Exception:
                self.expression = "Compute Error"
        
        # 나머지 숫자/연산자 입력
        else:
            self.expression += str(char)

        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)

