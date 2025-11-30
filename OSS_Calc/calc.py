import tkinter as tk
import tkinter.simpledialog  # [필수] 팝업창 입력을 위해 추가

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("300x450")

        self.expression = ""

        # 입력창
        self.entry = tk.Entry(root, font=("Arial", 24), justify="right")
        self.entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

        # 버튼 리스트 (맨 윗줄에 ⚖️ 가성비 비교 버튼 추가)
        buttons = [
            ['⚖️', 'C', '%', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '.', '=', '']
        ]

        for row in buttons:
            frame = tk.Frame(root)
            frame.pack(expand=True, fill="both")
            for char in row:
                if char == '': 
                    btn = tk.Label(frame, text="")
                    btn.pack(side="left", expand=True, fill="both")
                    continue
                
                # 버튼 색상 꾸미기
                bg_color = "#f0f0f0" if char in ['⚖️', 'C', '=', '%'] else "SystemButtonFace"
                
                btn = tk.Button(
                    frame,
                    text=char,
                    font=("Arial", 18),
                    bg=bg_color,
                    command=lambda ch=char: self.on_click(ch)
                )
                btn.pack(side="left", expand=True, fill="both")

    def on_click(self, char):
        if char == '⚖️':
            # [신규 기능] 가성비(단가) 비교 로직
            try:
                # 상품 A 정보 입력
                price_a = tk.simpledialog.askfloat("가성비 비교", "상품 A의 가격(원)을 입력하세요:")
                if price_a is None: return
                weight_a = tk.simpledialog.askfloat("가성비 비교", "상품 A의 용량(g/ml/개)을 입력하세요:")
                if weight_a is None: return

                # 상품 B 정보 입력
                price_b = tk.simpledialog.askfloat("가성비 비교", "상품 B의 가격(원)을 입력하세요:")
                if price_b is None: return
                weight_b = tk.simpledialog.askfloat("가성비 비교", "상품 B의 용량(g/ml/개)을 입력하세요:")
                if weight_b is None: return

                # 단가 계산 (가격 / 용량)
                unit_price_a = price_a / weight_a
                unit_price_b = price_b / weight_b

                # 결과 판별
                if unit_price_a < unit_price_b:
                    winner = "상품 A"
                    gap = unit_price_b - unit_price_a
                else:
                    winner = "상품 B"
                    gap = unit_price_a - unit_price_b
                
                # 결과 출력
                self.expression = f"{winner} 승! (단가 {gap:.1f}원 더 저렴)"
            
            except Exception:
                self.expression = "입력 오류"

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