import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기 - 실용 기능 추가")
        self.root.geometry("360x500")

        self.expression = ""

        # 입력창
        self.entry = tk.Entry(root, font=("Arial", 28), justify="right", bd=10)
        self.entry.pack(fill=tk.X, padx=10, pady=10, ipady=15)

        # 버튼들
        buttons = [
            ['C',  'CE', '←',  '/'],
            ['7',  '8',  '9',  '*'],
            ['4',  '5',  '6',  '-'],
            ['1',  '2',  '3',  '+'],
            ['0',  '.',  '=', 'Copy']
        ]

        frame = tk.Frame(root)
        frame.pack(expand=True, fill="both", padx=10, pady=5)

        for i, row in enumerate(buttons):
            for j, text in enumerate(row):
                btn = tk.Button(frame, text=text, font=("Arial", 20),
                               bg="#ffd700" if text in ['CE','Copy'] else "#f0f0f0",
                               command=lambda t=text: self.click(t))
                btn.grid(row=i, column=j, sticky="nsew", padx=2, pady=2)
            frame.grid_rowconfigure(i, weight=1)
        for j in range(4):
            frame.grid_columnconfigure(j, weight=1)

    def click(self, char):
        if char == 'C':
            self.expression = ""
        elif char == 'CE':           # 새 기능: 현재 입력만 지우기
            self.expression = ""
            messagebox.showinfo("CE", "입력값이 지워졌습니다!")
        elif char == '←':
            self.expression = self.expression[:-1]
        elif char == '=':
            try:
                self.expression = str(eval(self.expression))
            except:
                self.expression = "에러"
        elif char == 'Copy':         # 새 기능: 결과 클립보드 복사
            if self.expression and self.expression != "에러":
                self.root.clipboard_clear()
                self.root.clipboard_append(self.expression)
                messagebox.showinfo("복사 완료", f"{self.expression} → 클립보드에 복사됨!")
            else:
                messagebox.showwarning("복사 실패", "복사할 숫자가 없습니다!")
        else:
            self.expression += char

        self.entry.delete(0, tk.END)
        self.entry.insert(0, self.expression)

