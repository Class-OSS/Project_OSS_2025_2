import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("300x200")

        self.expression = ""

        # 입력창
        self.entry = tk.Entry(root, font=("Arial", 24), justify="right")
        self.entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

        # 결과 판별 라벨
        self.result_label = tk.Label(root, text="", font=("Arial", 16), fg="blue")
        self.result_label.pack(pady=(0,10))

        # '=' 버튼
        equal_btn = tk.Button(root, text='=', font=("Arial", 18), command=self.calculate)
        equal_btn.pack(expand=True, fill="both", padx=10, pady=10)

        # 키보드 입력 반영
        self.entry.bind("<KeyRelease>", self.update_expression)

    def update_expression(self, event):
        self.expression = self.entry.get()

    def calculate(self):
        try:
            result = eval(self.expression)
            if isinstance(result, float) and not result.is_integer():
                self.result_label.config(text="소수입니다.")
            else:
                self.result_label.config(text="소수가 아닙니다.")
        except Exception:
            self.result_label.config(text="잘못된 입력입니다.")

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
