import tkinter as tk


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("300x400")

        self.expression = ""
        self.should_reset = False

        # 입력창
        self.entry = tk.Entry(root, font=("Arial", 24), justify="right")
        self.entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

        self.entry.focus_set()
        self.entry.bind("<Key>", self.process_key)

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

    def process_key(self, event):
        key = event.keysym
        char = event.char

        if key == "Return":
            self.on_click('=')

        elif key == "BackSpace":
            self.on_click('C')
    
        elif char in '0123456789.+-*/':
            self.on_click(char)
        
        return "break"

    def on_click(self, char):
        if self.should_reset:
            if char in '0123456789':  
                self.expression = ""
            self.should_reset = False

        if char == 'C':
            self.expression = ""

        elif char == '=':
            try:
                result = str(eval(self.expression))

                if result.endswith(".0"):
                    result = result[:-2]
                    
                self.expression = result
                self.should_reset = True

            except Exception:
                self.expression = "에러"
                self.should_reset = True
        else:
            if self.expression == "에러":
                self.expression = ""
            self.expression += str(char)
        
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)
