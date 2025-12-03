# 22212141 김희곤 역수 버튼 기능 구현해서 소수로 표시시

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

        # 버튼 생성 (1/x 버튼 추가됨)
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', 'C', '+'],
            ['=', '1/x'] 
        ]

        for row in buttons:
            frame = tk.Frame(root)
            frame.pack(expand=True, fill="both")
            for btn_text in row:
                btn = tk.Button(frame, text=btn_text, font=("Arial", 18),
                                command=lambda t=btn_text: self.on_button_click(t))
                btn.pack(side="left", expand=True, fill="both")

    def on_button_click(self, char):
        if char == 'C':
            self.expression = ""
        elif char == '=':
            try:
                # 1/x 기능도 eval로 계산 가능하지만, 명확히 하기 위해 eval 사용
                self.expression = str(eval(self.expression))
            except:
                self.expression = "Error"
        elif char == '1/x':
            try:
                # 역수 계산 (1 나누기 현재값)
                val = eval(self.expression)
                if val == 0:
                    self.expression = "Error"
                else:
                    self.expression = str(1 / val)
            except:
                self.expression = "Error"
        else:
            self.expression += char
        
        self.update_display()

    def update_display(self):
        self.entry.delete(0, tk.END)
        self.entry.insert(0, self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()