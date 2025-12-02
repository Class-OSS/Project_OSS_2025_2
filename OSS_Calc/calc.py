import tkinter as tk
from tkinter import ttk
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("공학용 계산기 & 변환기")
        self.root.geometry("350x600") 

        self.mode = "CALC"
        self.expression = ""
        self.conv_expression = ""

        # === 상단 메뉴 영역 ===
        menu_frame = tk.Frame(root, bg="#ddd")
        menu_frame.pack(side="top", fill="x")
        
        self.menu_btn = tk.Button(menu_frame, text="≡ 메뉴", command=self.toggle_mode, relief="flat", bg="#ddd")
        self.menu_btn.pack(side="left", padx=5, pady=5)
        
        self.title_label = tk.Label(menu_frame, text="표준 계산기", bg="#ddd", font=("Arial", 12, "bold"))
        self.title_label.pack(side="right", padx=10)

        # === 메인 화면 영역 ===
        self.screen_container = tk.Frame(root)
        self.screen_container.pack(fill="both", expand=True, padx=10, pady=5)

        # 1. 계산기 화면
        self.calc_frame = tk.Frame(self.screen_container)
        self.calc_entry = tk.Entry(self.calc_frame, font=("Arial", 24), justify="right")
        self.calc_entry.pack(fill="both", ipadx=8, ipady=15)
        
        # 2. 단위 변환 화면
        self.conv_frame = tk.Frame(self.screen_container)
        self.conv_entry = tk.Entry(self.conv_frame, font=("Arial", 20), justify="right")
        self.conv_entry.pack(fill="x", pady=(0, 5))

        unit_frame = tk.Frame(self.conv_frame)
        unit_frame.pack(fill="x", pady=5)

        self.units = {
            "미터 (m)": 1.0,
            "센티미터 (cm)": 0.01,
            "킬로미터 (km)": 1000.0,
            "인치 (in)": 0.0254,
            "피트 (ft)": 0.3048
        }
        unit_names = list(self.units.keys())

        self.combo_from = ttk.Combobox(unit_frame, values=unit_names, state="readonly")
        self.combo_from.current(0)
        self.combo_from.pack(side="left", expand=True, fill="x", padx=2)

        tk.Label(unit_frame, text="→").pack(side="left")

        self.combo_to = ttk.Combobox(unit_frame, values=unit_names, state="readonly")
        self.combo_to.current(1)
        self.combo_to.pack(side="left", expand=True, fill="x", padx=2)

        self.result_label = tk.Label(self.conv_frame, text="결과: 0", font=("Arial", 16, "bold"), fg="blue", anchor="e")
        self.result_label.pack(fill="x", pady=10)

        self.calc_frame.pack(fill="both", expand=True)

        # === 버튼 영역 ===
        button_area = tk.Frame(root)
        button_area.pack(fill="both", expand=True, padx=10, pady=10)

        # 버튼 레이아웃 수정 (삼각함수 행 추가)
        buttons = [
            ['sin', 'cos', 'tan', 'π'],  # 새로 추가된 행
            ['C', '(', ')', '%'],
            ['√', 'x²', '/', '*'],
            ['7', '8', '9', '-'],
            ['4', '5', '6', '+'],
            ['1', '2', '3', '='],
            ['0', '.', '', '']
        ]

        # 버튼 배치 루프
        for r_idx, row in enumerate(buttons):
            for c_idx, char in enumerate(row):
                if char == '': continue

                bg_color = "#f0f0f0"
                # 특수 기능 버튼 색상 지정
                if char in ['=', '+', '-', '*', '/', 'C', '√', 'x²', '%', '(', ')', 'sin', 'cos', 'tan', 'π']:
                    bg_color = "#e0e0e0"
                
                btn = tk.Button(
                    button_area,
                    text=char,
                    font=("Arial", 14), # 폰트 크기 약간 조정
                    bg=bg_color,
                    command=lambda ch=char: self.on_click(ch)
                )
                
                btn.grid(row=r_idx, column=c_idx, sticky="nsew", padx=1, pady=1)

        # 그리드 가중치 설정 (행이 늘어났으므로 7행까지)
        for i in range(7):
            button_area.grid_rowconfigure(i, weight=1)
        for i in range(4):
            button_area.grid_columnconfigure(i, weight=1)

    # === 삼각함수 도(Degree) 계산용 헬퍼 메서드 ===
    def sin_deg(self, x):
        return math.sin(math.radians(x))

    def cos_deg(self, x):
        return math.cos(math.radians(x))
    
    def tan_deg(self, x):
        return math.tan(math.radians(x))

    def toggle_mode(self):
        if self.mode == "CALC":
            self.mode = "CONV"
            self.title_label.config(text="단위 변환기")
            self.calc_frame.pack_forget()
            self.conv_frame.pack(fill="both", expand=True)
            self.conv_expression = ""
            self.conv_entry.delete(0, tk.END)
            self.result_label.config(text="결과: 0")
        else:
            self.mode = "CALC"
            self.title_label.config(text="표준 계산기")
            self.conv_frame.pack_forget()
            self.calc_frame.pack(fill="both", expand=True)

    def on_click(self, char):
        if self.mode == "CALC":
            self.handle_calc(char)
        else:
            self.handle_conv(char)

    def handle_calc(self, char):
        if char == 'C':
            self.expression = ""
        elif char == '=':
            final_expr = self.expression
            # 괄호 자동 닫기
            open_count = final_expr.count('(')
            close_count = final_expr.count(')')
            if open_count > close_count:
                final_expr += ')' * (open_count - close_count)
            
            # === 수식 변환 로직 ===
            # 삼각함수: self.sin_deg 등의 메서드로 연결하여 Degree 단위로 계산
            final_expr = final_expr.replace("sin(", "self.sin_deg(")
            final_expr = final_expr.replace("cos(", "self.cos_deg(")
            final_expr = final_expr.replace("tan(", "self.tan_deg(")
            final_expr = final_expr.replace("π", "math.pi")
            
            final_expr = final_expr.replace("√(", "math.sqrt(")
            final_expr = final_expr.replace("^2", "**2")
            final_expr = final_expr.replace("%", "*0.01")
            
            try:
                result = eval(final_expr)
                
                if isinstance(result, (int, float)):
                    if result == int(result):
                        self.expression = str(int(result))
                    else:
                        self.expression = str(round(result, 8))
            except Exception:
                self.expression = "수식 오류"
        
        # === 입력 처리 ===
        elif char in ['sin', 'cos', 'tan', '√']:
            self.expression += f"{char}("
        elif char == 'x²':
            self.expression += "^2"
        elif char == '%':
            self.expression += "%"
        else:
            self.expression += str(char)
            
        self.calc_entry.delete(0, tk.END)
        self.calc_entry.insert(tk.END, self.expression)

    def handle_conv(self, char):
        if char in ['sin', 'cos', 'tan', 'π', '√', 'x²', '%', '(', ')', '+', '-', '*', '/']: return 
        
        if char == 'C':
            self.conv_expression = ""
            self.result_label.config(text="결과: 0")
        elif char == '=':
            self.convert_unit()
            return
        else:
            self.conv_expression += str(char)
        
        self.conv_entry.delete(0, tk.END)
        self.conv_entry.insert(tk.END, self.conv_expression)

    def convert_unit(self):
        try:
            if not self.conv_expression: return
            val = float(self.conv_expression)
            from_u = self.combo_from.get()
            to_u = self.combo_to.get()
            res = val * self.units[from_u] / self.units[to_u]
            self.result_label.config(text=f"결과: {res:.4f}")
        except:
            self.result_label.config(text="오류")