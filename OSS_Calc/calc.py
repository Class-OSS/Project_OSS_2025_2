import tkinter as tk
import os

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("300x400")

        self.expression = ""
        
        #로그 txt파일 생성
        if not os.path.exists("calc_log.txt"):
            with open("calc_log.txt", "w") as f:
                f.write("[계산결과]\n")

        # 입력창
        self.entry = tk.Entry(root, font=("Arial", 24), justify="right")
        self.entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

        # 버튼 생성
        buttons = [
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
            now_expression = self.expression
            result = ""
            try:
                result = str(eval(self.expression))
                self.expression = result
            except Exception:
                self.expression = "에러"
                result = "에러"
            
            #txt파일에 저장
            try:
                with open("calc_log.txt", "a") as f:
                    f.write(f"{now_expression} = {result}\n")
            except Exception:
                print(f"오류 발생")
        else:
            self.expression += str(char)

        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)



