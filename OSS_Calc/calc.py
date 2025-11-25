import tkinter as tk
from tkinter import messagebox

history = []

def add_to_history(expression, result):
    """ expression = 계산식, result = 결과 """
    entry = f"{expression} = {result}"
    history.append(entry)

def show_history():
    """ 계산 기록을 팝업창으로 표시 """
    if not history:
        messagebox.showinfo("History", "계산 기록이 없습니다.")
        return

    text = "\n".join(history[-20:])
    messagebox.showinfo("History", text)

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("300x420")

        self.expression = ""

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

        # 히스토리 버튼
        top_frame = tk.Frame(root)
        top_frame.pack(expand=False, fill="both")
        history_btn = tk.Button(
            top_frame,
            text="History",
            font=("Arial", 14),
            command=show_history
        )
        history_btn.pack(side="right", padx=10, pady=5)

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
                result = str(eval(self.expression))

                # 기록 추가
                add_to_history(self.expression, result)

                self.expression = result
            except Exception:
                self.expression = "에러"

        else:
            self.expression += str(char)

        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)
