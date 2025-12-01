import tkinter as tk
from tkinter import simpledialog

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("300x400")

        self.expression = ""

        # 입력창
        self.entry = tk.Entry(root, font=("Arial", 24), justify="right")
        self.entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

        # 버튼 생성 (1/N 버튼 포함)
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', 'C', '+'],
            ['=', '1/N']
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
               
                self.expression = str(eval(self.expression))
            except Exception:
                self.expression = "에러"
        elif char == '1/N':
            # 더치페이 기능
            try:
                total = simpledialog.askinteger("더치페이", "총 금액을 입력하세요")
                if total: # 금액을 입력 했다면
                    people = simpledialog.askinteger("더치페이", "인원 수를 입력하세요")
                    if people and people > 0:
                        result = total // people
                        self.expression = str(result)
                    else:
                        self.expression = "인원 오류"
            except:
                self.expression = "오류"
        else:
            self.expression += str(char)
        
        # 화면 갱신
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)


if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
        
