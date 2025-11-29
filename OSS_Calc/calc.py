import tkinter as tk


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("300x450")

        self.expression = ""
        self.history = []  # 계산 이력 저장 리스트

        # 입력창
        self.entry = tk.Entry(root, font=("Arial", 24), justify="right")
        self.entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

        # 이력 보기 버튼
        history_btn = tk.Button(root, text="이력 보기", font=("Arial", 14), command=self.show_history)
        history_btn.pack(fill="x", padx=10, pady=5)

        # 버튼 구성
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', 'C', '+'],
            ['=']
        ]

        # 버튼 UI 생성
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
        """버튼 클릭 처리"""
        if char == 'C':  # 초기화
            self.expression = ""

        elif char == '=':  # 계산 실행
            try:
                result = str(eval(self.expression))

                # 이력 저장: "표현식 = 결과"
                self.history.append(self.expression + " = " + result)

                self.expression = result
            except Exception:
                self.expression = "에러"

        else:
            self.expression += str(char)

        # 입력창 업데이트
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)

    def show_history(self):
        """이력 창 띄우기"""
        history_window = tk.Toplevel(self.root)
        history_window.title("계산 이력")
        history_window.geometry("300x400")

        tk.Label(history_window, text="📜 계산 이력", font=("Arial", 16)).pack(pady=10)

        # 이력 하나씩 출력
        for record in self.history:
            label = tk.Label(history_window, text=record, font=("Arial", 12), anchor="w")
            label.pack(fill="x", padx=10)
