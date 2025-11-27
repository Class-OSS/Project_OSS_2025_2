import tkinter as tk
import math

def calculate_AVG_SD(data): # 입력한 숫자가 전체 모집단이라 볼 때의 표준편차임.
    avg = sum(data)/len(data) # 평균
    pre_var = 0
    for x in data:
        diff = x - avg # 값 - 평균
        sqr_diff = diff**2  # 차의 제곱
        pre_var += sqr_diff # 차의 제곱을 더하기
        var = pre_var / len(data) # 분산
        sd = math.sqrt(var) # 표준편차
    return avg, sd # 평균과 표준편차 리턴


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("350x450") # 크기 확장

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
            ['avg & σ', '='] # 평균과 표준편차 버튼 추가
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
            
        elif char == 'avg & σ': # 예를 들어 3+5+1 를 누르고 avg & σ를 누르면 평균과 표준편차 출력
            try:
                num = self.expression.split('+') # +로 숫자 구분하여 num 배열에 저장
                data = [] # 빈 배열
                for s in num: # 데이터를 float으로 변환하여 데이터 삽입
                    data.append(float(s))
                avg, sd = calculate_AVG_SD(data) # 평균과 표준편차
                self.expression = "avg = {:.2f}, σ= {:.2f}".format(avg,sd)
            except Exception:
                self.expression = "에러"

        elif char == '=':
            try:
                self.expression = str(eval(self.expression))
            except Exception:
                self.expression = "에러"
        else:
            self.expression += str(char)

        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)



