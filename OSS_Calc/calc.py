import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("300x420")

        self.expression = ""

        # 입력창
        self.entry = tk.Entry(root, font=("Arial", 24), justify="right")
        self.entry.grid(row=0, column=0, columnspan=4,
                        padx=10, pady=10, ipadx=8, ipady=15)
        
        # 새로 추가한 기능: x², 1/x, |x|
        buttons = [
            ['x²', '1/x', '|x|', 'C'],
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+']
        ]

        
        for r, row in enumerate(buttons, start=1):
            for c, char in enumerate(row):
                btn = tk.Button(
                    root,
                    text=char,
                    font=("Arial", 18),
                    command=lambda ch=char: self.on_click(ch)
                )
                btn.grid(row=r, column=c, padx=5, pady=5, sticky="nsew")

      
        for i in range(5):    
            self.root.rowconfigure(i, weight=1)
        for j in range(4):  
            self.root.columnconfigure(j, weight=1)

    def on_click(self, char):
        
        if char == 'C':
            self.expression = ""

        # 제곱
        elif char == 'x²':
            try:
                if self.expression == "":
                    return
                value = eval(self.expression)
                self.expression = str(value ** 2)
            except Exception:
                self.expression = "error"

        # 역수
        elif char == '1/x':
            try:
                if self.expression == "":
                    return
                value = eval(self.expression)
                self.expression = str(1 / float(value))
            except Exception:
                self.expression = "error"

        # 절댓값
        elif char == '|x|':
            try:
                if self.expression == "":
                    return
                value = eval(self.expression)
                self.expression = str(abs(float(value)))
            except Exception:
                self.expression = "error"

        elif char == '=':
            try:
                self.expression = str(eval(self.expression))
            except Exception:
                self.expression = "error"

        else:
            self.expression += str(char)

        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)
