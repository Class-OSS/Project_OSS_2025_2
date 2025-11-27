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
            ['00', '000', '0000'],
            ['10%dc', '20%dc', '30%dc'],
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
                # 일반 계산
                self.expression = str(eval(self.expression))
            except Exception:
                self.expression = "에러"

        elif char == '0000':
            self.expression += "0000"
        elif char == '000':
            self.expression += "000"
        elif char == '00':
            self.expression += "00"

        elif 'dc' in char:
            try:
                current_val = float(eval(self.expression))
                # 할인율 적용
                if char == '10%dc':
                    result = current_val * 0.9
                elif char == '20%dc':
                    result = current_val * 0.8
                elif char == '30%dc':
                    result = current_val * 0.7
                
                self.expression = str(int(result)) # 정수형으로 저장
                
            except Exception:
                self.expression = "에러"

        else:
            self.expression += str(char)

        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)



