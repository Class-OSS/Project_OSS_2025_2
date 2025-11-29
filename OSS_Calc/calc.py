import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("300x400")

        self.expression = ""  # 전체 수식 저장용

        # 입력창
        self.entry = tk.Entry(root, font=("Arial", 24), justify="right")
        self.entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

        # 버튼 구성
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', 'C', '+'],
            ['B', '=']  
        ]

        # 버튼 생성
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

        # 전체 삭제
        if char == 'C':
            self.expression = ""

        # 한 글자 삭제 
        elif char == 'B':
            self.expression = self.expression[:-1]

        # 계산 실행
        elif char == '=':
            try:
                self.expression = str(eval(self.expression))
            except Exception:
                self.expression = "에러"

        # 입력 오류 방지 기능
        elif char in ['+', '-', '*', '/']:

            # (1) 첫 글자가 연산자이면 입력 무시
            if len(self.expression) == 0:
                return

            # (2) 마지막 입력도 연산자면 → 새 연산자로 교체
            if self.expression[-1] in ['+', '-', '*', '/']:
                self.expression = self.expression[:-1] + char
            else:
                self.expression += char

        # 숫자, 소수점
        else:
            self.expression += str(char)

        # 화면 갱신
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)


# 실행부
if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
