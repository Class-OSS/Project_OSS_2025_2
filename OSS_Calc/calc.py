import tkinter as tk
from tkinter import messagebox


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("300x450")

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
            ['=', 'FIND']
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

    def find_operations(self, target):
        results = []

        # 범위 설정 (1~target*2 정도면 충분)
        limit = max(20, target * 2)

        for a in range(1, limit + 1):
            for b in range(1, limit + 1):
                if a + b == target:
                    results.append(f"{a} + {b} = {target}")
                if a - b == target:
                    results.append(f"{a} - {b} = {target}")
                if a * b == target:
                    results.append(f"{a} * {b} = {target}")
                if b != 0 and a / b == target:
                    results.append(f"{a} / {b} = {target}")

        return results

    def show_results(self, results, target):
        if not results:
            messagebox.showinfo("결과 없음", f"{target} 을(를) 만들 수 있는 사칙연산이 없습니다.")
            return

        result_text = "\n".join(results)
        messagebox.showinfo("가능한 사칙연산 경우의 수", result_text)

    def on_click(self, char):
        if char == 'C':
            self.expression = ""

        elif char == '=':
            try:
                self.expression = str(eval(self.expression))
            except Exception:
                self.expression = "에러"

        elif char == 'FIND':
            try:
                target = int(eval(self.expression))
                results = self.find_operations(target)
                self.show_results(results, target)
            except Exception:
                messagebox.showerror("오류", "올바른 숫자를 입력하세요.")

        else:
            self.expression += str(char)

        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)



# 실행
if __name__ == "__main__":
    root = tk.Tk()
    Calculator(root)
    root.mainloop()
