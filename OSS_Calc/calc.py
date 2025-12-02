import tkinter as tk
from tkinter import messagebox

class LeapYearCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("윤년 계산기")
        self.root.geometry("300x200")

        # 안내 라벨
        label = tk.Label(root, text="연도를 입력하세요", font=("Arial", 16))
        label.pack(pady=10)

        # 입력창
        self.entry = tk.Entry(root, font=("Arial", 20), justify="center")
        self.entry.pack(ipadx=5, ipady=5)

        # 버튼
        btn = tk.Button(root, text="계산", font=("Arial", 16), command=self.check_leap_year)
        btn.pack(pady=15)

        # 결과 라벨
        self.result_label = tk.Label(root, text="", font=("Arial", 18))
        self.result_label.pack()

        # 🔥 Enter 키 바인딩
        root.bind("<Return>", self.check_leap_year_event)

    # Enter 키 전용 (event 인자 필요)
    def check_leap_year_event(self, event):
        self.check_leap_year()

    # 윤년 판별 함수
    def check_leap_year(self):
        try:
            year = int(self.entry.get())

            # 윤년 조건
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                result = f"{year}년은 윤년입니다!"
            else:
                result = f"{year}년은 평년입니다."

            self.result_label.config(text=result)

        except ValueError:
            messagebox.showerror("입력 오류", "올바른 숫자를 입력하세요!")


# 실행
root = tk.Tk()
app = LeapYearCalculator(root)
root.mainloop()
