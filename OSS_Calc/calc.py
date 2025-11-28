# 22212121 신동엽 오픈 소스 SW의 이해 과제 4 (3개 중 세 번째)
# 추가한 기능 : 계산기 ON/OFF 기능 구현
# ON/OFF 버튼을 추가하게 되는데 그냥 ON/OFF 버튼만 추가하면 버튼별 균형이 무너져서 괄호 기능과 백분율 기능 추가
import tkinter as tk


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("300x400")

        self.expression = ""
        # [기능수정] 전원 상태 관리 변수 (초기 상태는 OFF)
        self.power_on = False

        # 입력창
        self.entry = tk.Entry(root, font=("Arial", 24), justify="right")
        self.entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

        # [추가] 모든 버튼 위젯을 저장할 리스트
        self.all_buttons = []

        # 버튼 생성
        buttons = [
            ['ON/OFF', '(', ')', '%'], # [기능추가] ON/OFF 버튼 추가
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', 'C', '+'],
            ['=']
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
                # [추가] 생성된 버튼을 리스트에 저장
                self.all_buttons.append(btn)

        # [기능추가] 초기 상태 설정 (ON/OFF 버튼 제외 모든 위젯 비활성화)
        self.entry.insert(tk.END, "POWER OFF")
        self.toggle_widgets(tk.DISABLED)

    # [추가] ON/OFF 버튼을 제외한 모든 위젯의 상태를 변경하는 헬퍼 함수
    def toggle_widgets(self, state):
        """ON/OFF 버튼을 제외한 모든 위젯의 상태를 변경합니다 (tk.NORMAL 또는 tk.DISABLED)."""
        for btn in self.all_buttons:
            if btn['text'] != 'ON/OFF':
                btn['state'] = state

    # [기능추가] 계산기의 전원 상태를 토글하는 함수
    def toggle_power(self):
        self.power_on = not self.power_on
        
        self.entry.delete(0, tk.END)

        if self.power_on:
            self.expression = ""
            self.entry.insert(tk.END, "")
            self.toggle_widgets(tk.NORMAL) # 위젯 활성화 (ON)
        else:
            self.expression = ""
            self.entry.insert(tk.END, "POWER OFF")
            self.toggle_widgets(tk.DISABLED) # 위젯 비활성화 (OFF)

    def on_click(self, char):

        # [기능추가] 1. ON/OFF 버튼 처리
        if char == 'ON/OFF':
            self.toggle_power()
            return
            
        # [기능추가] 2. 전원이 꺼져 있으면 모든 입력을 무시
        if not self.power_on:
            return

        if char == 'C':
            self.expression = ""
        elif char == '=':
            try:
                self.expression = str(eval(self.expression))
            except Exception:
                self.expression = "에러"
        else:
            self.expression += str(char)

        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)



