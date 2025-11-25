import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("350x450") # 창 크기 확장

        self.expression = ""

        # 입력창
        self.entry = tk.Entry(root, font=("Arial", 24), justify="right")
        self.entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

        # 버튼 생성: 진수 변환 버튼 추가
        buttons = [
            ['BIN', 'OCT', 'HEX', '/'], # 진수 변환 버튼 추가
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '.', 'C', '='],
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

    # [기능추가] 진수 변환 헬퍼 함수
    def convert_base(self, value, target_base):
        """10진수 정수를 target_base (bin, oct, hex)로 변환합니다."""
        if target_base == 'BIN':
            # bin()은 '0b' 접두사를 붙이므로, [2:]로 잘라냅니다.
            return bin(value)[2:]
        elif target_base == 'OCT':
            # oct()은 '0o' 접두사를 붙이므로, [2:]로 잘라냅니다.
            return oct(value)[2:]
        elif target_base == 'HEX':
            # hex()은 '0x' 접두사를 붙이므로, [2:]로 잘라내고 대문자로 변환합니다.
            return hex(value)[2:].upper()
        return "오류"


    def on_click(self, char):
        if char == 'C':
            self.expression = ""
        
        # [기능추가] 진수 변환 처리 로직 (BIN, OCT, HEX)
        elif char in ('BIN', 'OCT', 'HEX'):
            current_expr = self.expression
            
            if not current_expr:
                self.expression = "오류: 10진수를 입력하세요"
            else:
                try:
                    # 1. 현재 표현식을 10진수 정수로 변환 시도
                    # eval()을 사용하여 사칙연산 결과도 변환 가능하게 함 (예: '10+5'를 15로 평가)
                    value = float(eval(current_expr))
                    
                    # 2. 진수 변환은 정수(Integer)에 대해서만 유효
                    if value != int(value):
                        self.expression = "진수 변환 오류: 정수만 가능"
                    else:
                        # 3. 헬퍼 함수를 호출하여 변환 실행
                        self.expression = self.convert_base(int(value), char)
                        
                except Exception:
                    self.expression = "오류: 잘못된 입력 형식"
        
        elif char == '=':
            try:
                # 계산 실행 시 진수 변환된 문자열이 있으면 에러 방지
                if char not in ('BIN', 'OCT', 'HEX'): # 변환 버튼이 아닌 경우에만 eval
                    self.expression = str(eval(self.expression))
                else:
                    # 이미 진수 변환된 상태에서 '='을 누르면 아무것도 안 함
                    pass 
            except Exception:
                self.expression = "에러"
        
        else:
            self.expression += str(char)

        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)
