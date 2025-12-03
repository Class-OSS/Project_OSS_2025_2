import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("300x450")

        self.expression = ""

        # 입력창
        self.entry = tk.Entry(root, font=("Arial", 24), justify="right", bd=0)
        self.entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

        # 다크모드 스위치 버튼 추가
        self.is_dark = False
        self.theme_btn = tk.Button(root, text="🌙 다크모드 켜기", command=self.toggle_theme, font=("Arial", 10))
        self.theme_btn.pack(fill="x", padx=10, pady=5)

        # 버튼 생성
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', 'C', '+'],
            ['=']
        ]

        # 버튼 및 프레임 객체들을 저장할 리스트
        self.btns = []
        self.frames = []

        for row in buttons:
            frame = tk.Frame(root)
            frame.pack(expand=True, fill="both")
            self.frames.append(frame)  # [중요] 프레임 객체 저장

            for char in row:
                btn = tk.Button(
                    frame,
                    text=char,
                    font=("Arial", 18),
                    relief="flat",
                    command=lambda ch=char: self.on_click(ch)
                )
                btn.pack(side="left", expand=True, fill="both", padx=1, pady=1)
                self.btns.append(btn)  # 버튼 객체 저장

    def on_click(self, char):
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

    # 다크모드 전환 메서드
    def toggle_theme(self):
        if not self.is_dark:
            # === 다크 모드 적용 ===
            self.root.configure(bg="#202020")
            self.entry.configure(bg="#303030", fg="white", insertbackground="white")
            
            # 스위치 버튼 스타일
            self.theme_btn.configure(
                text="☀️ 라이트모드 켜기", 
                bg="#404040", fg="white", 
                activebackground="#505050", activeforeground="white"
            )
            
            # 버튼 줄(프레임) 배경도 어둡게 (버튼 사이 틈새 색상)
            for frm in self.frames:
                frm.configure(bg="#202020")

            # 숫자 버튼들 스타일
            for btn in self.btns:
                btn.configure(
                    bg="#333333", fg="white", 
                    activebackground="#555555", activeforeground="white"
                )
            
            self.is_dark = True
        else:
            # === 라이트 모드 복구 ===
            self.root.configure(bg="#F0F0F0")
            self.entry.configure(bg="white", fg="black", insertbackground="black")
            
            self.theme_btn.configure(
                text="🌙 다크모드 켜기", 
                bg="#E0E0E0", fg="black", 
                activebackground="#D0D0D0", activeforeground="black"
            )

            for frm in self.frames:
                frm.configure(bg="#F0F0F0")
            
            for btn in self.btns:
                btn.configure(
                    bg="white", fg="black", 
                    activebackground="#E0E0E0", activeforeground="black"
                )
            
            self.is_dark = False