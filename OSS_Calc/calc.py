import tkinter as tk
from tkinter import ttk  # 콤보박스(드롭다운) 사용을 위해 추가

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기 & 단위변환기")
        self.root.geometry("350x500") # 화면 요소가 늘어남에 따라 크기 조절

        self.mode = "CALC" # 현재 모드: "CALC" (계산기) 또는 "CONV" (단위변환)
        self.expression = "" # 계산기 수식 저장
        self.conv_expression = "" # 단위변환기 입력 숫자 저장

        # === 상단 메뉴 영역 ===
        menu_frame = tk.Frame(root, bg="#ddd")
        menu_frame.pack(side="top", fill="x")
        
        self.menu_btn = tk.Button(menu_frame, text="≡ 메뉴", command=self.toggle_mode, relief="flat", bg="#ddd")
        self.menu_btn.pack(side="left", padx=5, pady=5)
        
        self.title_label = tk.Label(menu_frame, text="표준 계산기", bg="#ddd", font=("Arial", 12, "bold"))
        self.title_label.pack(side="right", padx=10)

        # === 메인 화면 영역 (계산기 화면 & 변환기 화면을 교체할 컨테이너) ===
        self.screen_container = tk.Frame(root)
        self.screen_container.pack(fill="both", expand=True, padx=10, pady=5)

        # 1. 계산기 화면 구성
        self.calc_frame = tk.Frame(self.screen_container)
        self.calc_entry = tk.Entry(self.calc_frame, font=("Arial", 24), justify="right")
        self.calc_entry.pack(fill="both", ipadx=8, ipady=15)
        
        # 2. 단위 변환 화면 구성
        self.conv_frame = tk.Frame(self.screen_container)
        
        # 입력값 표시
        self.conv_entry = tk.Entry(self.conv_frame, font=("Arial", 20), justify="right")
        self.conv_entry.pack(fill="x", pady=(0, 5))

        # 단위 선택 영역 (From -> To)
        unit_frame = tk.Frame(self.conv_frame)
        unit_frame.pack(fill="x", pady=5)

        # 단위 정의 (길이 예시)
        self.units = {
            "미터 (m)": 1.0,
            "센티미터 (cm)": 0.01,
            "킬로미터 (km)": 1000.0,
            "인치 (in)": 0.0254,
            "피트 (ft)": 0.3048
        }
        unit_names = list(self.units.keys())

        # From 단위
        self.combo_from = ttk.Combobox(unit_frame, values=unit_names, state="readonly")
        self.combo_from.current(0) # 기본값: 미터
        self.combo_from.pack(side="left", expand=True, fill="x", padx=2)

        tk.Label(unit_frame, text="→").pack(side="left")

        # To 단위
        self.combo_to = ttk.Combobox(unit_frame, values=unit_names, state="readonly")
        self.combo_to.current(1) # 기본값: 센티미터
        self.combo_to.pack(side="left", expand=True, fill="x", padx=2)

        # 결과 표시 라벨
        self.result_label = tk.Label(self.conv_frame, text="결과: 0", font=("Arial", 16, "bold"), fg="blue", anchor="e")
        self.result_label.pack(fill="x", pady=10)


        # 초기 화면 설정 (계산기 표시)
        self.calc_frame.pack(fill="both", expand=True)


        # === 버튼 영역 (공통 사용) ===
        # 버튼을 하단에 배치
        button_area = tk.Frame(root)
        button_area.pack(fill="both", expand=True, padx=10, pady=10)

        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', 'C', '+'],
            ['=']
        ]

        for row in buttons:
            frame = tk.Frame(button_area)
            frame.pack(expand=True, fill="both")
            for char in row:
                btn = tk.Button(
                    frame,
                    text=char,
                    font=("Arial", 18),
                    command=lambda ch=char: self.on_click(ch)
                )
                btn.pack(side="left", expand=True, fill="both")

    def toggle_mode(self):
        """계산기 모드와 단위 변환 모드를 전환합니다."""
        if self.mode == "CALC":
            # 변환 모드로 전환
            self.mode = "CONV"
            self.title_label.config(text="단위 변환기 (길이)")
            self.calc_frame.pack_forget() # 계산기 숨김
            self.conv_frame.pack(fill="both", expand=True) # 변환기 표시
            
            # 사칙연산 버튼 비활성화 (선택적) - 여기선 단순화를 위해 그냥 둠
            # 변환기 초기화
            self.conv_expression = ""
            self.conv_entry.delete(0, tk.END)
            self.result_label.config(text="결과: 0")

        else:
            # 계산기 모드로 복귀
            self.mode = "CALC"
            self.title_label.config(text="표준 계산기")
            self.conv_frame.pack_forget() # 변환기 숨김
            self.calc_frame.pack(fill="both", expand=True) # 계산기 표시

    def on_click(self, char):
        if self.mode == "CALC":
            self.handle_calc(char)
        else:
            self.handle_conv(char)

    def handle_calc(self, char):
        """계산기 모드 로직"""
        if char == 'C':
            self.expression = ""
        elif char == '=':
            try:
                self.expression = str(eval(self.expression))
            except Exception:
                self.expression = "에러"
        else:
            self.expression += str(char)
        
        self.calc_entry.delete(0, tk.END)
        self.calc_entry.insert(tk.END, self.expression)

    def handle_conv(self, char):
        """단위 변환 모드 로직"""
        # 사칙연산 기호는 단위 변환에서 쓰지 않으므로 무시하거나 경고 처리
        if char in ['+', '-', '*', '/']:
            return 

        if char == 'C':
            self.conv_expression = ""
            self.result_label.config(text="결과: 0")
        elif char == '=':
            # 변환 실행
            self.convert_unit()
            return
        else:
            self.conv_expression += str(char)
        
        self.conv_entry.delete(0, tk.END)
        self.conv_entry.insert(tk.END, self.conv_expression)

    def convert_unit(self):
        """단위 변환 계산 함수"""
        try:
            if not self.conv_expression:
                return

            val = float(self.conv_expression)
            from_unit = self.combo_from.get()
            to_unit = self.combo_to.get()

            # 기준 단위(m)로 변환 후, 목표 단위로 변환
            # 공식: 값 * (From단위값 / To단위값)
            base_val = val * self.units[from_unit] # 미터로 변환
            result_val = base_val / self.units[to_unit] # 목표 단위로 변환

            # 소수점 4자리까지 표시
            self.result_label.config(text=f"결과: {result_val:.4f}")
            
        except Exception:
            self.result_label.config(text="오류")