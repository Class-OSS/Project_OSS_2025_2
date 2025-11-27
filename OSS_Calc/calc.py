import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("300x400")

        self.expression = ""

        self.entry = tk.Entry(root, font=("Arial", 24), justify="right")
        self.entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', 'C', '+'],
            ['Prime', '=']  # 소인수분해 버튼 'prime' 추가
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

    def on_click(self, char):
        if char == 'C':
            self.expression = ""

        elif char == '=':
            try:
                self.expression = str(eval(self.expression))
            except Exception:
                self.expression = "에러"

        # 소인수분해 기능 처리 부분
        elif char == 'Prime':
            try:
                n = int(self.entry.get())  

                # 양수 및 1000 이하 조건 체크
                if n <= 0 or n > 1000:
                    self.expression = "1~1000만 가능"
                else:
                    factors = []
                    temp = n

                    # 2로 나누어 떨어지는 경우 처리
                    while temp % 2 == 0:
                        factors.append(2)
                        temp //= 2

                    # 3 이상 홀수 소수 체크
                    i = 3
                    while i * i <= temp:
                        while temp % i == 0:
                            factors.append(i)
                            temp //= i
                        i += 2

                    # 마지막 남은 값이 1보다 크면 추가
                    if temp > 1:
                        factors.append(temp)

                    # 결과 표현
                    self.expression = " ".join(map(str, factors))

            except:
                self.expression = "에러"

        else:
            self.expression += str(char)

        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)
