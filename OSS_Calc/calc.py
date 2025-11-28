import tkinter as tk


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("300x450")

        self.expression = ""

        # 색상 순환 리스트
        self.colors = ["red", "orange", "yellow", "green", "blue", "purple"]
        self.color_index = 0

        # 모든 버튼을 저장할 리스트
        self.buttons_widgets = []

        # 입력창
        self.entry = tk.Entry(root, font=("Arial", 24), justify="right")
        self.entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

        # 색상 변경 버튼
        color_btn = tk.Button(
            root,
            text="🎨 색상 변경",
            font=("Arial", 14),
            command=self.change_color
        )
        color_btn.pack(fill="both", padx=10, pady=5)
        self.buttons_widgets.append(color_btn)

        # 계산기 버튼
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

                # 버튼을 리스트에 저장
                self.buttons_widgets.append(btn)

    # 색상 변경 함수 (배경 + 모든 버튼)
    def change_color(self):
        self.color_index = (self.color_index + 1) % len(self.colors)
        new_color = self.colors[self.color_index]

        # 창 배경 변경
        self.root.configure(bg=new_color)

        # 모든 버튼 색상 변경
        for btn in self.buttons_widgets:
            btn.configure(bg=new_color, activebackground=new_color)

    def on_click(self, char):
        if char == 'C':
            self.expression = ""
        elif char == '=':
            try:
                self.expression = str(eval(self.expression))
            except Exception:
                self.expression = "에러"
        else:
            self.expression += str(char)

        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)


if __name__ == "__main__":
    root = tk.Tk()
    Calculator(root)
    root.mainloop()
