# 22212121 신동엽 오픈 소스 SW의 이해 과제 4 (3개 중 두 번째)
# 추가한 기능 : 기존 계산기는 입력을 위한 터미널의 크기 제한이 없어 입력이 그대로 되어 버리고 설령, 계산이 되었다
# 하더라도 너무 긴 수식은 계산기 화면에 표시되지 않는 문제 확인
# 애초에 입력, 출력 길이를 제한(약 15~16자가 적절했음)하여 사용자가 정확하게 값을 인식 할 수 있을 정도로만 계산 수용
# 범위 변경
# 그리고 터미널의 길이를 초과했을 때 초과했다는 문구가 뜨고 0.5초 후 기존 입력 했던 값을 수정할 수 있도록 상태 복구
import tkinter as tk


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
    
    # [기능추가] 알림 메시지 표시 후 원래 수식을 복구하는 함수
    def restore_display(self):
        """알림 메시지를 지우고 원래 수식으로 복구합니다."""
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression) 

    def on_click(self, char):
        
        # 1. Clear / Equal 버튼 처리
        if char == 'C':
            self.expression = ""
        elif char == '=':
            try:
                self.expression = str(eval(self.expression))
            except Exception:
                self.expression = "에러"
        
        # [기능추가] 입력 길이 제한 (16자) 및 피드백 로직
        else:
            # 16자 미만일 때만 추가합니다.
            if len(self.expression) < 16: # 16자로 변경
                self.expression += str(char)
            else:
                # 16자 초과 시:
                # 1. 입력창에 경고 메시지 표시
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "길이 제한 초과!")
                
                # 2. 500ms(0.5초) 후 restore_display 함수를 호출하여 복구합니다.
                self.root.after(500, self.restore_display) 
                
                # 입력이 추가되지 않았으므로 아래의 화면 업데이트 로직을 건너뛰고 함수를 종료합니다.
                return 

        # 2. 입력창 업데이트
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)



