import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("300x470")

        self.expression = ""

        # 입력창
        self.entry = tk.Entry(root, font=("Arial", 24), justify="right")
        self.entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

        # 버튼 구성
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '(', '+'],
            [')', 'C', '=', 'Unit']
        ]

        for row in buttons:
            frame = tk.Frame(root)
            frame.pack(expand=True, fill="both")
            for char in row:
                if char == 'Unit':
                    btn = tk.Button(frame, text=char, font=("Arial", 18),
                                    command=self.convert_unit)
                else:
                    btn = tk.Button(frame, text=char, font=("Arial", 18),
                                    command=lambda ch=char: self.on_click(ch))
                btn.pack(side="left", expand=True, fill="both")

    def on_click(self, char):
        # 초기 입력 오류 방지
        if char == 'C':
            self.expression = ""
        elif char == '=':
            self.calculate()
        else:
            self.handle_input(char)

        self.update_display()

    def handle_input(self, char):
        # 숫자 뒤에 바로 '('가 올 때 괄호 자동 완성
        if char == '(':
            if self.expression and self.expression[-1].isdigit():
                # 자동 곱셈 방지
                self.expression += "*()"
            else:
                self.expression += "()"
            return

        self.expression += str(char)

    def calculate(self):
        try:
            # 열린 괄호 자동 닫음
            open_cnt = self.expression.count("(")
            close_cnt = self.expression.count(")")
            if close_cnt < open_cnt:
                self.expression += ")" * (open_cnt - close_cnt)

            self.expression = str(eval(self.expression))
        except:
            self.expression = "에러"

    def convert_unit(self):
        """
        자동 단위 변환 기능
        지원 변환:
        cm <-> m, kg <-> g
        """
        text = self.expression

        try:
            if text.endswith("cm"):
                value = float(text[:-2]) / 100
                self.expression = str(value) + "m"
            elif text.endswith("m"):
                value = float(text[:-1]) * 100
                self.expression = str(int(value)) + "cm"
            elif text.endswith("kg"):
                value = float(text[:-2]) * 1000
                self.expression = str(int(value)) + "g"
            elif text.endswith("g"):
                value = float(text[:-1]) / 1000
                self.expression = str(value) + "kg"
            else:
                # 단위가 없거나 인식 불가 시 에러
                pass
        except:
            self.expression = "에러"

        self.update_display()

    def update_display(self):
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)


if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
