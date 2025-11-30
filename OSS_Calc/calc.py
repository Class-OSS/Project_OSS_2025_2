import tkinter as tk
import math


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("300x400")

        # 현재 수식
        self.expression = ""

        # 계산 기록 저장용 리스트
        self.history = []

        # 입력창
        self.entry = tk.Entry(root, font=("Arial", 24), justify="right")
        self.entry.pack(fill="both", ipadx=8, ipady=15, padx=8, pady=8)

        # 버튼 배열
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', 'C', '+'],
            ['sqrt', '^', 'fact', '='],
            ['history', 'clear', '']
        ]

        # 버튼 생성
        for row in buttons:
            frame = tk.Frame(root)
            frame.pack(expand=True, fill="both")
            for char in row:
                if char == "":
                    # 빈 칸은 모양 맞추려고 비어 있는 라벨로 처리
                    lbl = tk.Label(frame)
                    lbl.pack(side="left", expand=True, fill="both")
                    continue

                btn = tk.Button(
                    frame,
                    text=char,
                    font=("Arial", 18),
                    command=lambda ch=char: self.on_click(ch)
                )
                btn.pack(side="left", expand=True, fill="both")

    def on_click(self, char):
        if char == 'C':
            # 전체 지우기
            self.expression = ""

        elif char == 'history':
            # 계산 기록 창 띄우기
            self.show_history()

        elif char == 'clear':
            # 기록만 삭제
            self.history = []

        elif char == 'sqrt':
            # 현재 수식을 평가해서 제곱근
            try:
                if self.expression == "":
                    value = 0
                else:
                    value = float(eval(self.expression))
                result = math.sqrt(value)
                # history에도 저장
                self.history.append(f"sqrt({value}) = {result}")
                self.expression = str(result)
            except Exception:
                self.expression = "에러"

        elif char == '^':
            # 제곱 연산자: 파이썬은 ** 가 제곱
            self.expression += '**'

        elif char == 'fact':
            # 현재 수식을 정수로 평가해서 팩토리얼 계산
            try:
                if self.expression == "":
                    n = 0
                else:
                    n = int(eval(self.expression))

                if n < 0:
                    raise ValueError("음수 팩토리얼 불가")

                result = 1
                for i in range(1, n + 1):
                    result *= i

                # history에도 저장
                self.history.append(f"{n}! = {result}")
                self.expression = str(result)
            except Exception:
                self.expression = "에러"

        elif char == '=':
            # 일반 계산 (= 버튼)
            try:
                result = eval(self.expression)
                # "수식 = 결과" 형태로 기록 저장
                self.history.append(f"{self.expression} = {result}")
                self.expression = str(result)
            except Exception:
                self.expression = "에러"

        else:
            # 숫자, 연산자 등 일반 입력
            self.expression += str(char)

        # 화면 갱신
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)

    def show_history(self):
        """계산 기록을 새 창에 출력"""
        history_window = tk.Toplevel(self.root)
        history_window.title("History")
        history_window.geometry("300x400")

        text = tk.Text(history_window, font=("Arial", 14))
        text.pack(expand=True, fill="both")

        if not self.history:
            text.insert(tk.END, "기록이 없습니다.\n")
        else:
            for item in self.history:
                text.insert(tk.END, item + "\n")
