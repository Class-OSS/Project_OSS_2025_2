import tkinter as tk
import tkinter.simpledialog  # [필수] 팝업창 입력을 위해 추가

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("300x450") # UI 크기 조정

        self.expression = ""

        # 입력창
        self.entry = tk.Entry(root, font=("Arial", 24), justify="right")
        self.entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

        buttons = [
            ['🚀', 'C', '%', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '.', '=', '']
        ]

        for row in buttons:
            frame = tk.Frame(root)
            frame.pack(expand=True, fill="both")
            for char in row:
                if char == '': # 빈 공간 처리
                    btn = tk.Label(frame, text="")
                    btn.pack(side="left", expand=True, fill="both")
                    continue
                
                # 특수 버튼 색상 구분
                bg_color = "#f0f0f0" if char in ['🚀', 'C', '=', '%'] else "SystemButtonFace"
                
                btn = tk.Button(
                    frame,
                    text=char,
                    font=("Arial", 18),
                    bg=bg_color,
                    command=lambda ch=char: self.on_click(ch)
                )
                btn.pack(side="left", expand=True, fill="both")

    def on_click(self, char):
        if char == '🚀':
            # [신규 기능] 수익률(PnL) 계산 로직
            try:
                # 1. 매수 평단가 입력
                buy_price = tk.simpledialog.askfloat("수익률 계산", "매수 평단가(원)를 입력하세요:")
                if buy_price is None: return

                # 2. 매도(목표) 가격 입력
                sell_price = tk.simpledialog.askfloat("수익률 계산", "매도 목표가(원)를 입력하세요:")
                if sell_price is None: return

                # 3. 보유 수량 입력 (선택 사항 - 기본값 1)
                amount = tk.simpledialog.askfloat("수익률 계산", "보유 수량(개)을 입력하세요 (모르면 1):")
                if amount is None: amount = 1.0

                # 4. 수익률 계산
                profit_loss = (sell_price - buy_price) * amount
                # 수익률(%) = (수익금 / 투자원금) * 100
                roi = ((sell_price - buy_price) / buy_price) * 100

                # 5. 결과 출력 (수익이면 +, 손실이면 - 표시)
                sign = "+" if profit_loss >= 0 else ""
                self.expression = f"{sign}{roi:.2f}% ({sign}{int(profit_loss)}원)"
            
            except Exception:
                self.expression = "계산 오류"

        elif char == 'C':
            self.expression = ""
        
        elif char == '=':
            try:
                self.expression = str(eval(self.expression))
            except Exception:
                self.expression = "에러"
        
        else:
            self.expression += str(char)

        # 화면 갱신
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)