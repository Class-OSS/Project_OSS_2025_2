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
        
        #새로 추가된 코드1 >> 히스토리 리스트 박스 생성
        self.history = tk.Listbox(root, font=("Arial", 12))
        self.history.pack(side="right", fill="both", padx=5)
        
        #새로 추가된 코드2 >> 스크롤 추가
        scroll = tk.Scrollbar(root)
        scroll.pack(side="right", fill="y")

        self.history.config(yscrollcommand=scroll.set)
        scroll.config(command=self.history.yview)

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

    def on_click(self, char):
        if char == 'C':
            self.expression = ""
        elif char == '=':
        
        #새로 추가된 코드3 >> 이전 계산기록 수식 저장
        old_exp = self.expression
        
            try:
                self.expression = str(eval(self.expression))
                #새로 추가된 코드4 >> 리스트 박스에 기록추가
                self.history.insert(tk.END, f"{old_exp} = {self.expression}")
            except Exception:
                self.expression = "에러"
        else:
            self.expression += str(char)

        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)



