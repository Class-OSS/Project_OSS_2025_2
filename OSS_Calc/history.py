# 간단한 GUI 계산기에 계산 기록(History) 기능을 추가한 프로그램입니다.
import tkinter as tk


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("300x500")  # 기록 영역 때문에 세로를 조금 늘림

        self.expression = ""
        self.history = []  # 계산 기록을 저장할 리스트

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

        # ----- 계산 기록 영역 추가 -----
        history_label = tk.Label(root, text="계산 기록", font=("Arial", 12), anchor="w")
        history_label.pack(fill="x", padx=10, pady=(5, 0))

        self.history_listbox = tk.Listbox(root, height=6)  # 최근 몇 개만 보이게
        self.history_listbox.pack(fill="both", expand=True, padx=10, pady=5)

        # 기록 더블클릭 시 식을 다시 불러오는 기능 (선택 사항)
        self.history_listbox.bind("<Double-Button-1>", self.on_history_double_click)

    def on_click(self, char):
        if char == 'C':
            self.expression = ""
        elif char == '=':
            self.calculate()
        else:
            # 에러 상태에서 숫자/연산자를 누르면 새로 시작하도록 처리
            if self.expression == "에러":
                self.expression = ""
            self.expression += str(char)

        self.update_entry()

    def calculate(self):
        """수식을 계산하고, 성공하면 기록에 추가."""
        try:
            result = str(eval(self.expression))
            # 계산 기록에 '식 = 결과' 형태로 추가
            record = f"{self.expression} = {result}"
            self.history.append(record)
            self.history_listbox.insert(tk.END, record)

            self.expression = result  # 결과를 다음 계산의 시작값으로
        except Exception:
            self.expression = "에러"

    def update_entry(self):
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)

    def on_history_double_click(self, event):
        """기록을 더블클릭하면 해당 결과를 입력창에 다시 불러오기."""
        selection = self.history_listbox.curselection()
        if not selection:
            return
        record = self.history_listbox.get(selection[0])
        # "식 = 결과"에서 결과만 다시 사용하고 싶다면 split 사용
        if " = " in record:
            expr, result = record.split(" = ", 1)
            self.expression = result
        else:
            self.expression = record
        self.update_entry()


if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
