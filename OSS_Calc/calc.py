import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("300x400")

        self.expression = ""
        self.is_dark_mode = False # 초기: 라이트 모드

        # 입력창
        self.entry = tk.Entry(root, font=("Arial", 24), justify="right")
        self.entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

        # 초기 테마
        self.set_theme("light")

        # 버튼 생성
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', 'C', '+'],
            ['(', ')', 'DEL', '=', 'Mode'] 
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

    def set_theme(self, mode):
        if mode == "dark":
            bg = "#444444" 
            fg = "white"
            entry_bg = "#444444"
        else: # "light"
            bg = "#f0f0f0" 
            fg = "black" 
            entry_bg = "white" 

        self.root.config(bg=bg)
        
        self.entry.config(bg=entry_bg, fg=fg, insertbackground=fg)

        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Frame):
                widget.config(bg=bg)
                for btn in widget.winfo_children():
                    if isinstance(btn, tk.Button):
                        btn.config(bg=bg, fg=fg, activebackground=bg, activeforeground=fg)

    def on_click(self, char):
        if char == 'Mode':
            self.is_dark_mode = not self.is_dark_mode
            self.set_theme("dark" if self.is_dark_mode else "light")
            return
            
        if char == 'C':
            self.expression = ""
        elif char == 'DEL':
            self.expression = self.expression[:-1]
        elif char == '=':
            try:
                self.expression = str(eval(self.expression))
            except Exception:
                self.expression = "에러"
        else:
            self.expression += str(char)

        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)
        