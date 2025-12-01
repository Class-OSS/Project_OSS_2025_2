import tkinter as tk
from tkinter import messagebox
import math

class CylinderVolumeCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("원기둥 부피 계산기")
        self.root.geometry("320x250")

        # 반지름 입력
        tk.Label(root, text="반지름 (r)", font=("Arial", 14)).pack(pady=5)
        self.radius_entry = tk.Entry(root, font=("Arial", 18), justify="center")
        self.radius_entry.pack(ipadx=5, ipady=3)

        # 높이 입력
        tk.Label(root, text="높이 (h)", font=("Arial", 14)).pack(pady=5)
        self.height_entry = tk.Entry(root, font=("Arial", 18), justify="center")
        self.height_entry.pack(ipadx=5, ipady=3)

        # 계산 버튼
        calc_btn = tk.Button(root, text="부피 계산", font=("Arial", 16), command=self.calculate_volume)
        calc_btn.pack(pady=15)

        # 결과 출력
        self.result_label = tk.Label(root, text="", font=("Arial", 16))
        self.result_label.pack()

        # Enter 키 둘 다 지원
        root.bind("<Return>", self.calculate_volume_event)

    # Enter 키용
    def calculate_volume_event(self, event):
        self.calculate_volume()

    def calculate_volume(self):
        try:
            r = float(self.radius_entry.get())
            h = float(self.height_entry.get())

            volume = math.pi * (r ** 2) * h

            self.result_label.config(text=f"부피: {volume:.3f}")
        except ValueError:
            messagebox.showerror("입력 오류", "숫자를 정확히 입력하세요!")

# 실행
root = tk.Tk()
app = CylinderVolumeCalculator(root)
root.mainloop()
