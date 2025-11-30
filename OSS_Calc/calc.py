import tkinter as tk


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("300x450")

        self.expression = ""

       
        self.entry = tk.Entry(root, font=("Arial", 24), justify="right")
        self.entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

        
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', 'C', '+'],
            ['=', 'W->$']   # ★ 원화 → 달러 버튼 추가
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

        # ★ 원화 → 달러 변환 기능
        elif char == 'W->$':
            try:
                rate = 1350  # 고정 환율 (원화 1350원 = 1달러)
                won = float(self.expression)  # 입력 숫자
                dollar = won / rate
                self.expression = str(round(dollar, 2))  # 소수 둘째 자리까지 표시
            except Exception:
                self.expression = "에러"

      
        elif char == '=':
            try:
                self.expression = str(eval(self.expression))
            except Exception:
                self.expression = "에러"

      
        else:
            self.expression += str(char)

       
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)
