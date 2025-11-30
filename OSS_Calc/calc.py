import tkinter as tk
from tkinter import messagebox  

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("300x450")  # BMI 버튼 추가로 인해 세로 길이 약간 늘림

        self.expression = ""

        # 입력창
        self.entry = tk.Entry(root, font=("Arial", 24), justify="right")
        self.entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

        # 버튼 생성 (레이아웃 수정: BMI 버튼 추가)
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', 'C', '+'],
            ['BMI', '=']  
        ]

        for row in buttons:
            frame = tk.Frame(root)
            frame.pack(expand=True, fill="both")
            for char in row:
                btn = tk.Button(
                    frame,
                    text=char,
                    font=("Arial", 18),
                    bg="#f0f0f0" if char != "BMI" else "#e1f5fe",
                    command=lambda ch=char: self.on_click(ch)
                )
                btn.pack(side="left", expand=True, fill="both")

    def on_click(self, char):
        if char == 'C':
            self.expression = ""
        elif char == 'BMI':
            # BMI 계산 모듈 실행 
            self.open_bmi_window()
            return  
        elif char == '=':
            try:
                self.expression = str(eval(self.expression))
            except Exception:
                self.expression = "에러"
        else:
            self.expression += str(char)

        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)

    #비만도(BMI) 계산 모듈
    def open_bmi_window(self):
        # 새로운 팝업창 생성
        bmi_window = tk.Toplevel(self.root)
        bmi_window.title("BMI 계산기")
        bmi_window.geometry("300x250")

        # 키 입력 라벨 및 엔트리
        tk.Label(bmi_window, text="키 (cm):").pack(pady=5)
        entry_height = tk.Entry(bmi_window)
        entry_height.pack(pady=5)

        # 몸무게 입력 라벨 및 엔트리
        tk.Label(bmi_window, text="몸무게 (kg):").pack(pady=5)
        entry_weight = tk.Entry(bmi_window)
        entry_weight.pack(pady=5)

        # 결과 표시 라벨
        result_label = tk.Label(bmi_window, text="결과가 여기에 표시됩니다.", font=("Arial", 10, "bold"))
        result_label.pack(pady=10)

        # 계산 로직 함수
        def calculate():
            try:
                h_cm = float(entry_height.get())
                w_kg = float(entry_weight.get())

                if h_cm <= 0 or w_kg <= 0:
                    result_label.config(text="양수를 입력해주세요.", fg="red")
                    return

                # BMI 공식: 몸무게(kg) / 키(m)^2
                h_m = h_cm / 100
                bmi = w_kg / (h_m ** 2)

                # 비만도 판정
                status = ""
                if bmi < 18.5:
                    status = "저체중"
                elif 18.5 <= bmi < 23:
                    status = "정상"
                elif 23 <= bmi < 25:
                    status = "과체중"
                else:
                    status = "비만"

                result_text = f"BMI: {bmi:.2f}\n판정: {status}"
                result_label.config(text=result_text, fg="blue")

            except ValueError:
                result_label.config(text="숫자만 입력해주세요.", fg="red")

        # 계산 버튼
        btn_calc = tk.Button(bmi_window, text="계산하기", command=calculate, bg="#e1f5fe")
        btn_calc.pack(pady=5)
