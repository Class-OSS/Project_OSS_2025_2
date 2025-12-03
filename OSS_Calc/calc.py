import tkinter as tk
from tkinter import messagebox 

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        
        self.root.geometry("550x600") 

        self.expression = ""

        main_frame = tk.Frame(root)
        main_frame.pack(fill="both", expand=True)

        calc_frame = tk.Frame(main_frame)
        calc_frame.pack(side="left", fill="both", expand=True)

        # 기록 표시 영역 (사이드바)
        history_frame = tk.Frame(main_frame, width=200, bg="lightgray")
        history_frame.pack(side="right", fill="both")

        # (( *** 왼쪽 계산기 UI 구현 ! *** ))
        self.entry = tk.Entry(calc_frame, font=("Arial", 24), justify="right")
        self.entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', 'C', '+'],
            ['=']
        ]

        for row in buttons:
            frame = tk.Frame(calc_frame)
            frame.pack(expand=True, fill="both")
            for char in row:
                btn = tk.Button(
                    frame,
                    text=char,
                    font=("Arial", 18),
                    command=lambda ch=char: self.on_click(ch)
                )
                btn.pack(side="left", expand=True, fill="both")

        # (( *** 오른쪽 기록 UI 구현 *** ))
        tk.Label(history_frame, text="계산 기록", bg="lightgray", font=("Arial", 12, "bold")).pack(pady=5)

        # ( 중간 프레임! 버튼을 아래에 배치, 리스트박스 크기 조절을 위해서!)
        list_frame = tk.Frame(history_frame)
        list_frame.pack(fill="both", expand=True, padx=5)

        self.remember_index_box = tk.Listbox(list_frame, font=("Arial", 10), bg="white", exportselection=False)
        self.remember_index_box.pack(side="left", fill="both", expand=True)
        
        scrollbar = tk.Scrollbar(list_frame, command=self.remember_index_box.yview)
        scrollbar.pack(side="right", fill="y")
        
        self.remember_index_box.config(yscrollcommand=scrollbar.set)

        # 기록 목록 클릭 이벤트 연결 
        self.remember_index_box.bind("<<ListboxSelect>>", self.load_click_remember)

        # 삭제 버튼 하단 프레입!
        Delete_btn_down_Frame = tk.Frame(history_frame, bg="lightgray")
        Delete_btn_down_Frame.pack(side="bottom", fill="x", pady=5, padx=5)

        # 선택 삭제 버튼
        Delete_Select_btn = tk.Button(Delete_btn_down_Frame, text="선택 삭제", command=self.Delete_select_FunC)
        Delete_Select_btn.pack(side="left", expand=True, fill="x", padx=1)

        # 전체 삭제 버튼
        Delete_All_btn = tk.Button(Delete_btn_down_Frame, text="전체 삭제", command=self.Delete_All_FunC)
        Delete_All_btn.pack(side="right", expand=True, fill="x", padx=1)


    def on_click(self, char):
        if char == 'C':
            self.expression = ""
        elif char == '=':
            try:
                original_expression = self.expression
                result = str(eval(self.expression))
                self.expression = result
                
                remember = f"{original_expression} = {result}"
                self.remember_index_box.insert(0, remember)
                
            except Exception:
                self.expression = "에러"
        else:
            self.expression += str(char)

        self.update_entry()

    def update_entry(self):
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)

    def load_click_remember(self, event):
        remember_num = self.remember_index_box.curselection()
        
        if remember_num:
            index = remember_num[0]
            content = self.remember_index_box.get(index)
            
            remember_value_ = content.split('=')[-1].strip()
            
            self.expression = remember_value_
            self.update_entry()

    # 선택된 항목 삭제 함수
    def Delete_select_FunC(self):
        Select_click_index = self.remember_index_box.curselection()
        
        if Select_click_index:
            # 해당 인덱스 삭제
            self.remember_index_box.delete(Select_click_index[0])
    
    # 전체 삭제 함수
    def Delete_All_FunC(self):
        if self.remember_index_box.size() > 0:
            if messagebox.askyesno("삭제 확인", "모든 기록을 지우시겠습니까?"):
                self.remember_index_box.delete(0, tk.END)



