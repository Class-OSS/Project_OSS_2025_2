import tkinter as tk
from datetime import datetime
import re

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("300x400")

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
            ['DATE', '='] # <-- 'DATE' 버튼 추가
        ]

        for row in buttons:
            frame = tk.Frame(root)
            frame.pack(expand=True, fill="both")
            for char in row:
                if char == 'DATE':
                    btn = tk.Button(
                        frame,
                        text=char,
                        font=("Arial", 18),
                        command=self.open_date_calculator # <-- 새로운 함수 연결
                    )
                else:
                    btn = tk.Button(
                        frame,
                        text=char,
                        font=("Arial", 18),
                        command=lambda ch=char: self.on_click(ch)
                    )
                btn.pack(side="left", expand=True, fill="both")

    # ----------------------------------------------------
    #  날짜 계산기 팝업 창 열기 함수
    def open_date_calculator(self):
        # Toplevel 윈도우 생성 (팝업 창)
        date_win = tk.Toplevel(self.root)
        date_win.title("날짜 계산기")
        date_win.geometry("300x200")

        tk.Label(date_win, text="날짜 차이 계산 (YYYYMMDD)").pack(pady=5)

        # 시작 날짜 입력
        tk.Label(date_win, text="시작 날짜:").pack()
        start_date_entry = tk.Entry(date_win, width=20)
        start_date_entry.pack()

        # 끝 날짜 입력
        tk.Label(date_win, text="끝 날짜:").pack()
        end_date_entry = tk.Entry(date_win, width=20)
        end_date_entry.pack()
        
        # 결과 표시 라벨
        result_label = tk.Label(date_win, text="결과: ", pady=10)
        result_label.pack()

        # 계산 버튼
        calc_button = tk.Button(
            date_win,
            text="차이 계산",
            command=lambda: self.calculate_date_difference(
                start_date_entry.get(),
                end_date_entry.get(),
                result_label
            )
        )
        calc_button.pack(pady=10)

    # 날짜 차이 계산 로직
    def calculate_date_difference(self, start_date_str, end_date_str, result_label):
        DATE_FORMAT = "%Y%m%d"
        try:
            start_date = datetime.strptime(start_date_str, DATE_FORMAT).date()
            end_date = datetime.strptime(end_date_str, DATE_FORMAT).date()

            # 날짜 차이 계산
            difference = end_date - start_date
            
            # 일수만 추출
            days = difference.days
            
            result_label.config(text=f"결과: {days}일 차이")
            
        except ValueError:
            result_label.config(text="에러: YYYYMMDD 형식으로 입력하세요.")
        except Exception:
            result_label.config(text="에러: 계산 실패")


    # 3. 기존 on_click 함수 (기존 계산기 기능 유지)
    def on_click(self, char):
        if char == 'C':
            self.expression = ""
        elif char == '=':
            try:
                # 순수 계산 로직
                self.expression = str(eval(self.expression))
            except Exception:
                self.expression = "에러"
        else:
            self.expression += str(char)

        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)