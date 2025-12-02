import tkinter as tk


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("300x420")

        # 저장변수
        self.expression = ""
        self.history = []  # 계산 기록 저장용 리스트

        # 입력창
        self.entry = tk.Entry(root, font=("Arial", 24), justify="right")
        self.entry.grid(row=0, column=0, columnspan=4,
                        padx=10, pady=10, ipadx=8, ipady=15)

        # 버튼 구성
        buttons = [
            ['x²', '1/x', '|x|', 'Hist'],
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', 'C', '='],
        ]

        for r, row in enumerate(buttons, start=1):
            for c, char in enumerate(row):
                btn = tk.Button(
                    self.root,
                    text=char,
                    font=("Arial", 18),
                    command=lambda ch=char: self.on_click(ch)
                )
                btn.grid(row=r, column=c, padx=5, pady=5, sticky="nsew")

        # 크기 늘려도 버튼 크기 맞게 반영
        for i in range(1, 6):
            self.root.rowconfigure(i, weight=1)
        for j in range(4):
            self.root.columnconfigure(j, weight=1)

    def on_click(self, char):

        if char == 'C':
            self.expression = ""

        # 제곱 기능
        elif char == 'x²':
            try:
                value = eval(self.expression)
                result = value ** 2
                self.expression = str(result)
                self.history.append(f"{value}^2 = {result}")
            except:
                self.expression = "error"

        # 역수 기능
        elif char == '1/x':
            try:
                value = eval(self.expression)
                result = 1 / float(value)
                self.expression = str(result)
                self.history.append(f"1/({value}) = {result}")
            except:
                self.expression = "error"

        # 절댓값 기능
        elif char == '|x|':
            try:
                value = eval(self.expression)
                result = abs(float(value))
                self.expression = str(result)
                self.history.append(f"|{value}| = {result}")
            except:
                self.expression = "error"

        # 기록창 열기
        elif char == 'Hist':
            self.show_history_window()

        # = 연산 실행
        elif char == '=':
            try:
                expr = self.expression
                result = eval(expr)
                self.expression = str(result)
                self.history.append(f"{expr} = {result}")  # 기록 저장
            except:
                self.expression = "error"

        else:
            self.expression += str(char)

        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)

    def show_history_window(self):
        """계산 기록 보여주는 창"""
        win = tk.Toplevel(self.root)
        win.title("계산 기록")
        win.geometry("260x300")

        listbox = tk.Listbox(win, font=("Arial", 12))
        listbox.pack(side="left", fill="both", expand=True, padx=5, pady=5)

        scrollbar = tk.Scrollbar(win, command=listbox.yview)
        scrollbar.pack(side="right", fill="y")
        listbox.config(yscrollcommand=scrollbar.set)

        if not self.history:
            listbox.insert(tk.END, "기록이 없습니다.")
        else:
            for item in self.history:
                listbox.insert(tk.END, item)
