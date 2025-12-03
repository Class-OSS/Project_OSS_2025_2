def on_click(self, char):
    if char == 'C':
        # 전체 지우기
        self.expression = ""

    elif char == '√':
        # 현재 식을 평가해서 제곱근 계산
        try:
            if self.expression != "":
                value = eval(self.expression)
                self.expression = str(math.sqrt(value))
            else:
                # 아무것도 없을 때 √ 누르면 0으로 처리
                self.expression = "0"
        except Exception:
            self.expression = "에러"

    elif char == '=':
        try:
            self.expression = str(eval(self.expression))
        except Exception:
            self.expression = "에러"

    else:
        # 숫자/연산자 입력 처리
        self.expression += str(char)

    # 화면에 표시 갱신
    self.entry.delete(0, tk.END)
    self.entry.insert(tk.END, self.expression)
