import tkinter as tk
from datetime import datetime

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("350x450") 
        self.root.resizable(False, False)

        self.expression = ""
        self.history_visible = False # 기록창 상태 변수

        #상단 
        menu_frame = tk.Frame(root)
        menu_frame.pack(fill="x", padx=5, pady=2)
        
        # 기록 보기
        self.hist_btn = tk.Button(menu_frame, text="기록 보기", command=self.toggle_history, 
                                  font=("Arial", 10), relief="flat", bg="#e0e0e0")
        self.hist_btn.pack(side="right")

        #메인
        self.main_container = tk.Frame(root)
        self.main_container.pack(fill="both", expand=True)

        #계산기
        self.calc_frame = tk.Frame(self.main_container)
        self.calc_frame.pack(side="left", fill="both", expand=True)

        # 입력창
        self.entry = tk.Entry(self.calc_frame, font=("Arial", 24), justify="right", bd=2)
        self.entry.pack(fill="x", ipadx=8, ipady=15, padx=10, pady=10)

        # 버튼 인터페이스
        buttons = [
            ['7', '8', '9', '/', 'C'], 
            ['4', '5', '6', '*', '←'],
            ['1', '2', '3', '-', '('],
            ['0', '.', '=', '+', ')'] 
        ]

        btn_frame = tk.Frame(self.calc_frame)
        btn_frame.pack(expand=True, fill="both", padx=5, pady=5)

        for r, row in enumerate(buttons):
            for c, char in enumerate(row):
                # 버튼 색상
                bg_color = "#f0f0f0"
                if char in ['=', '+', '-', '*', '/']:
                    bg_color = "#d9e8fc"
                elif char == 'C':
                    bg_color = "#ffdddd"

                btn = tk.Button(
                    btn_frame,
                    text=char,
                    font=("Arial", 16),
                    bg=bg_color,
                    command=lambda ch=char: self.on_click(ch)
                )
                btn.grid(row=r, column=c, sticky="nsew", padx=2, pady=2)
                btn_frame.grid_columnconfigure(c, weight=1)
                btn_frame.grid_rowconfigure(r, weight=1)

        #기록
        self.history_frame = tk.Frame(self.main_container, bg="#dddddd", width=0)
        
        # 기록 제목
        tk.Label(self.history_frame, text="계산 기록", bg="#dddddd", font=("Arial", 11, "bold")).pack(pady=5)

        # 기록 리스트박스
        self.history_list = tk.Listbox(self.history_frame, font=("Arial", 10), bd=0, bg="#dddddd")
        self.history_list.pack(fill="both", expand=True, padx=5, pady=5)
        
        # 기록 초기화
        tk.Button(self.history_frame, text="기록 삭제", command=self.clear_history).pack(fill="x", padx=5, pady=5)


    def toggle_history(self):
        if not self.history_visible:
            self.root.geometry("550x450") #길이 확장
            self.history_frame.pack(side="right", fill="both", expand=True)
            self.hist_btn.config(text="기록 닫기")
            self.history_visible = True
        else:
            self.history_frame.pack_forget() # 기록창 숨김
            self.root.geometry("350x450") # 원래 크기로
            self.hist_btn.config(text="기록 보기")
            self.history_visible = False

    def clear_history(self):
        self.history_list.delete(0, tk.END)

    def add_history(self, expression, result):
        """현재 시간과 함께 계산 결과를 리스트에 추가"""
        current_time = datetime.now().strftime("%H:%M:%S")
        self.history_list.insert(0, f"[{current_time}] {expression}")
        self.history_list.insert(1, f"   = {result}")
        self.history_list.insert(2, "") # 공백

    def on_click(self, char):
        if char == 'C':
            self.expression = ""
        elif char == '←':
            self.expression = self.expression[:-1] if self.expression else ""
        elif char == '=':
            try:
                result = str(eval(self.expression))
                self.add_history(self.expression, result) # 기록 추가
                self.expression = result
            except Exception:
                self.expression = "Error"
        else:
            self.expression += str(char)

        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)

if __name__ == '__main__':
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
