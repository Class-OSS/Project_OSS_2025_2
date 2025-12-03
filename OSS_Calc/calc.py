def on_click(self, char):
    if char == 'C':
        self.expression = ""

    elif char == '^':
        # ^ 입력 시 파이썬 제곱 연산자 ** 를 넣어준다
        self.expression += "**"

    elif char == '=':
        try:
            self.expression = str(eval(self.expression))
        except Exception:
            self.expression = "에러"

    else:
        self.expression += str(char)

    self.entry.delete(0, tk.END)
    self.entry.insert(tk.END, self.expression)

