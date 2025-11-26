# 22212121 신동엽 오픈 소스 SW의 이해 과제 4 (3개 중 첫 번째)
# 추가한 기능 : 입력 숫자 혹은 출력 숫자에 대하여 1000단위로 ,(comma)를 통해 분리하는 기능
import tkinter as tk
import re 


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("300x400")

        self.expression = ""
        # [기능추가] 화면 표시에 쉼표를 포함하기 위한 별도 변수 (계산용 expression과 분리)
        self.display_expression = "" 

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

    # [기능추가] 쉼표 삽입을 위한 헬퍼 함수
    def format_number(self, s):
        """숫자 부분에 쉼표를 삽입하여 반환합니다."""
        if not s or s in ("에러", "에러"):  # 에러나 빈 문자열은 그대로 반환
            return s
            
        # 연산자([*/+-])를 기준으로 수식을 분리합니다. (예: "123+456.7" -> ['123', '+', '456.7', ''])
        parts = re.split('([*/+-])', s)
        
        formatted_parts = []
        for part in parts:
            if part in '*/+-':
                # 연산자는 그대로 유지합니다.
                formatted_parts.append(part)
            else:
                try:
                    # 숫자인 경우 쉼표를 삽입합니다.
                    if part.startswith('.'): # 소수점만 있는 경우 (예: .5)
                         formatted_parts.append(f"0{part}")
                         continue
                         
                    if '.' in part:
                        # 소수점이 있는 경우, 정수부만 쉼표 처리합니다.
                        integer_part, decimal_part = part.split('.', 1)
                        is_negative = integer_part.startswith('-')
                        if is_negative:
                            integer_part = integer_part[1:]
                        
                        # 정수부를 쉼표로 포맷팅
                        formatted_integer = format(int(integer_part) if integer_part else 0, ',')
                        
                        if is_negative:
                            formatted_integer = "-" + formatted_integer
                            
                        formatted_parts.append(f"{formatted_integer}.{decimal_part}")
                    else:
                        # 정수인 경우 쉼표를 삽입합니다.
                        # int() 변환 시 음수 부호 처리가 자동으로 됩니다.
                        formatted_parts.append(format(int(part) if part else 0, ','))
                except ValueError:
                    # 숫자가 아닌 문자열 (예: 빈 문자열, 잘못된 입력 등)은 그대로 유지합니다.
                    formatted_parts.append(part)
        
        # 분리된 부분을 다시 합칩니다.
        return "".join(formatted_parts)

    def on_click(self, char):
        # 1. self.expression 업데이트 (원본 수식 문자열)
        if char == 'C':
            self.expression = ""
        elif char == '=':
            try:
                # 쉼표가 없는 원본 expression으로 계산을 수행합니다.
                self.expression = str(eval(self.expression))
            except Exception:
                self.expression = "에러"
        else:
            self.expression += str(char)

        # 2. self.display_expression 업데이트 (화면 표시용 문자열 생성)
        if self.expression == "에러":
            self.display_expression = "에러"
        elif self.expression == "":
             self.display_expression = ""
        else:
            # [기능추가] 헬퍼 함수를 사용하여 쉼표를 삽입합니다.
            self.display_expression = self.format_number(self.expression)

        # 3. 입력창 업데이트
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.display_expression) # [기능수정] 표시용 문자열(쉼표 포함) 사용
            



