import tkinter as tk


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("350x400") 

        self.expression = ""

        # 입력창
        self.entry = tk.Entry(root, font=("Arial", 24), justify="right")
        self.entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)
        buttons = [
            ['7', '8', '9', '/', ''], 
            ['4', '5', '6', '*', ''],
            ['1', '2', '3', '-', ''],
            ['0', '.', 'C', '←', '+'],  # '←' 버튼을 추가
            ['=', '', '', '', '']      # 빈 문자열 추가
        ]

        for row in buttons:
            frame = tk.Frame(root)
            frame.pack(expand=True, fill="both")
            for char in row:
                if char == '':
                    dummy_frame = tk.Frame(frame, width=0, height=0)
                    dummy_frame.pack(side="left", expand=True, fill="both")
                else:
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
        elif char == '←': # 백스페이스 기능 로직
            self.expression = self.expression[:-1] if self.expression else ""
        elif char == '=':
            try:
                self.expression = str(eval(self.expression))
            except Exception:
                self.expression = "에러"
        elif char != '': # 빈 버튼이 아닌 경우에만 표현식에 추가
            self.expression += str(char)

        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)

if __name__ == '__main__':
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
