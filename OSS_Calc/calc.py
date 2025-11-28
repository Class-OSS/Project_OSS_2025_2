import tkinter as tk
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("400x500") # 창 크기 조정

        self.expression = ""
        self.current_mode = "basic"
        
        # 입력창 (Entry)
        self.entry = tk.Entry(root, font=("Arial", 28), justify="right", bd=5, relief=tk.SUNKEN)
        self.entry.pack(fill="x", padx=10, pady=(15, 5), ipady=10) 

        # 모드 전환 버튼
        self.mode_btn = tk.Button(
            root,
            text="SCIENTIFIC",
            font=("Arial", 14),
            command=self.toggle_mode
        )
        self.mode_btn.pack(pady=5)

        # 버튼 컨테이너 프레임
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(fill="both", expand=True, padx=10, pady=5)
        
        # 모드별 버튼 프레임 생성
        self.basic_frame = self.create_button_frame(self.button_frame, self.basic_buttons(), mode="basic")
        self.scientific_frame = self.create_button_frame(self.button_frame, self.scientific_buttons(), mode="scientific")
        
        # initial frame
        self.basic_frame.pack(fill="both", expand=True)

    # ------------------ define button ------------------
    
    def basic_buttons(self):
        return [
            ['7', '8', '9', 'C', '/'],
            ['4', '5', '6', '(', '*'],
            ['1', '2', '3', ')', '-'],
            ['0', '.', '=', '+']
        ]

    def scientific_buttons(self):
        # 공학용 모드 버튼 정의
        return [
            ['sin', 'cos', 'tan'],
            ['log', 'ln', 'sqrt', 'e^x', '!'],
            ['7', '8', '9', '(', '/'],
            ['4', '5', '6', ')', '*'],
            ['1', '2', '3', 'C', '-'],
            ['0', '.', '=', '+']
        ]
        
    # ------------------ create Frame and Button ------------------
    def create_button_frame(self, parent, button_list, mode):
        new_frame = tk.Frame(parent)
        for row in button_list:
            frame = tk.Frame(new_frame)
            frame.pack(expand=True, fill="both")
            for char in row:
                if char == '=':
                    cmd = self.evaluate_expression
                elif char == 'C':
                    cmd = lambda: self.clear_expression()
                else:
                    cmd = lambda ch=char, m=mode: self.on_click(ch, m) 

                btn = tk.Button(
                    frame,
                    text=char,
                    font=("Arial", 16),
                    command=cmd 
                )
                btn.pack(side="left", expand=True, fill="both", padx=2, pady=2)
        return new_frame

    # ------------------ 산술 정의 ------------------
    def on_click(self, char, mode):
        # 공학용 계산 함수 처리
        if mode == "scientific":
            if char in ['sin', 'cos', 'tan', 'log', 'ln', 'sqrt', 'e^x']:
                if char == 'ln': char = 'log'
                if char == 'sqrt': char = 'math.sqrt'
                elif char == 'e^x': char = 'math.exp'
                elif char in ['sin', 'cos', 'tan', 'log']: char = f'math.{char}'
                
                self.expression += f"{char}("
                self.update_entry()
                return
            if char == '!':
                self.expression += f"math.factorial("
                self.update_entry()
                return

        # 일반 입력 처리 (모드 공통)
        self.expression += char
        self.update_entry()

    def clear_expression(self):
        self.expression = ""
        self.update_entry()

    # 화면 업데이트
    def update_entry(self):
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)

    # ------------------ 계산 ------------------
    def evaluate_expression(self):
        """기본 및 공학 모드의 계산 실행"""
        try:
            # eval 환경 설정: math 모듈
            allowed_globals = {
                "math": math,
            }
      
            result = str(eval(self.expression, allowed_globals))
            self.expression = result
            
        except Exception:
            self.expression = "Error"

        self.update_entry()
        
    # ------------------ 모드 전환 ------------------

    def toggle_mode(self):
        # 현재 프레임 제거
        if self.current_mode == "basic":
            self.basic_frame.pack_forget()
            self.scientific_frame.pack(fill="both", expand=True)
            self.mode_btn.config(text="BASIC")
            self.current_mode = "scientific"
            
        else: # scientific
            self.scientific_frame.pack_forget()
            self.basic_frame.pack(fill="both", expand=True)
            self.mode_btn.config(text="SCIENTIFIC")
            self.current_mode = "basic"
        
        self.clear_expression() # 모드 전환 시 입력 초기화
