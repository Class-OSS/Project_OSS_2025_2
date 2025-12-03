import tkinter as tk


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("300x450")

        self.expression = ""
        self.history = []  # ⭐ 계산 이력 저장

        # 입력창
        self.entry = tk.Entry(root, font=("Arial", 24), justify="right")
        self.entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

        # 버튼 구성
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

        # ⭐ 이력 보기 버튼
        history_btn = tk.Button(
            root,
            text="이력 보기",
            font=("Arial", 16),
            command=self.show_history
        )
        history_btn.pack(fill="x", padx=10, pady=5)

    def on_click(self, char):
        if char == 'C':
            self.expression = ""

        elif char == '=':
            try:
                result = str(eval(self.expression))
                self.history.append(self.expression + " = " + result)  # ⭐ 계산 이력 저장
                self.expression = result
            except Exception:
                self.expression = "에러"

        else:
            self.expression += str(char)

        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)

    # ⭐ 이력 팝업창 열기
    def show_history(self):
        history_window = tk.Toplevel(self.root)
        history_window.title("계산 이력")
        history_window.geometry("300x400")

        text_box = tk.Text(history_window, font=("Arial", 14))
        text_box.pack(expand=True, fill="both")

        for item in self.history:
            text_box.insert(tk.END, item + "\n")

        clear_btn = tk.Button(history_window, text="이력 지우기", command=self.clear_history)
        clear_btn.pack(fill="x")

    def clear_history(self):
        self.history = []


