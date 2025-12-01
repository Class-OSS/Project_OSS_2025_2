import tkinter as tk
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기 - 진법 변환 완벽판")
        self.root.geometry("400x580")
        self.root.resizable(False, False)

        self.expression = ""
        self.current_base = 10  # 10=DEC, 2=BIN, 8=OCT, 16=HEX

        # 입력창
        self.entry = tk.Entry(root, font=("맑은 고딕", 24), justify="right", bd=12, relief="sunken")
        self.entry.pack(fill="both", ipadx=10, ipady=25, padx=15, pady=15)

        # 현재 진법 표시
        self.base_label = tk.Label(root, text="DEC", font=("Arial", 16, "bold"), fg="blue")
        self.base_label.pack(pady=8)

        # 버튼들
        buttons = [
            ['C',  '←',  'BIN', 'OCT'],
            ['7',  '8',  '9',  '/'],
            ['4',  '5',  '6',  '*'],
            ['1',  '2',  '3',  '-'],
            ['0',  '.',  '=',  '+'],
            ['A',  'B',  'C',  'HEX'],
            ['D',  'E',  'F',  'DEC'],
            ['√',  'π',  '',   '']
        ]

        frame = tk.Frame(root)
        frame.pack(expand=True, fill="both", padx=10, pady=5)

        self.buttons = {}
        for r, row in enumerate(buttons):
            for c, text in enumerate(row):
                if not text: 
                    continue
                btn = tk.Button(frame, text=text, font=("Arial", 18),
                               bg="#ffeb3b" if text in ['BIN','OCT','HEX','DEC'] else "#f0f0f0",
                               fg="red" if text in ['BIN','OCT','HEX','DEC'] else "black",
                               command=lambda t=text: self.click(t))
                btn.grid(row=r, column=c, sticky="nsew", padx=2, pady=2)
                self.buttons[text] = btn

        for i in range(8):
            frame.grid_rowconfigure(i, weight=1)
        for i in range(4):
            frame.grid_columnconfigure(i, weight=1)

        self.update_buttons()

    def update_buttons(self):
        # 현재 진법에 따라 숫자 버튼 활성화/비활성화
        enabled = set()
        if self.current_base == 10:
            enabled = {'0','1','2','3','4','5','6','7','8','9','.'}
        elif self.current_base == 2:
            enabled = {'0','1'}
        elif self.current_base == 8:
            enabled = {'0','1','2','3','4','5','6','7'}
        elif self.current_base == 16:
            enabled = {'0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F'}

        for text, btn in self.buttons.items():
            if text in '0123456789ABCDEF.':
                if text in enabled:
                    btn.config(state="normal", bg="#ffffff")
                else:
                    btn.config(state="disabled", bg="#cccccc")
            else:
                btn.config(state="normal")

    def to_base(self, num, base):
        if num == 0: return "0"
        if base == 10: return str(num)
        if base == 2:  return bin(num)[2:].upper()
        if base == 8:  return oct(num)[2:].upper()
        if base == 16: return hex(num)[2:].upper()
        return str(num)

    def change_base(self, new_base):
        try:
            if not self.expression.strip() or self.expression == "에러":
                value = 0
            else:
                value = int(self.expression, self.current_base)
            self.current_base = new_base
            self.expression = self.to_base(value, new_base)
            self.entry.delete(0, tk.END)
            self.entry.insert(0, self.expression)

            labels = {2: "BIN", 8: "OCT", 10: "DEC", 16: "HEX"}
            colors = {2: "green", 8: "orange", 10: "blue", 16: "purple"}
            self.base_label.config(text=labels[new_base], fg=colors[new_base])
            self.update_buttons()
        except:
            self.expression = "에러"
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "에러")

    def click(self, char):
        if char == 'C':
            self.expression = ""
        elif char == '←':
            self.expression = self.expression[:-1]
        elif char == '=':
            try:
                # 항상 10진수로 계산
                if self.current_base != 10:
                    temp = int(self.expression, self.current_base)
                    result = eval(str(temp))
                else:
                    result = eval(self.expression)
                self.expression = str(result)
            except:
                self.expression = "에러"
        elif char in ['BIN','OCT','DEC','HEX']:
            base_map = {'BIN':2, 'OCT':8, 'DEC':10, 'HEX':16}
            self.change_base(base_map[char])
            return
        elif char == '√':
            try:
                val = float(self.expression) if self.current_base == 10 else int(self.expression, self.current_base)
                self.expression = str(math.sqrt(val))
            except:
                self.expression = "에러"
        elif char == 'π':
            self.expression += str(math.pi)
        else:
            self.expression += char

        self.entry.delete(0, tk.END)
        self.entry.insert(0, self.expression)
        self.update_buttons()
