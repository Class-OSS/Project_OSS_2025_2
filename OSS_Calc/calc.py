import tkinter as tk


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("300x400+600+300")  # 위치 고정(흔들기용)

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

    def shake_window(self):
        """창을 좌우로 흔들기"""
        original_x = 600
        original_y = 300

        # 흔들기 패턴 (좌우 이동)
        shake_positions = [original_x - 10, original_x + 10,
                           original_x - 6, original_x + 6,
                           original_x - 3, original_x + 3, original_x]

        # 순차적으로 after 호출하여 흔들기
        for i, pos in enumerate(shake_positions):
            self.root.after(i * 50, lambda p=pos: self.root.geometry(f"300x400+{p}+{original_y}"))

    def on_click(self, char):
        if char == 'C':
            self.expression = ""
        elif char == '=':
            try:
                self.expression = str(eval(self.expression))

            except Exception:
                # 에러 발생 → 흔들기 실행
                self.shake_window()
                self.expression = "에러"

        else:
            self.expression += str(char)

        # 입력창 업데이트
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)
