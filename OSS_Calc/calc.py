import tkinter as tk


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("300x400")

        self.expression = ""
        self.is_dark_mode = False
        self.buttons = []
        self.frames = []

        # 색상 설정 (라이트/다크)
        self.colors = {
            'light': {
                'bg': '#F0F0F0', 'fg': 'black',
                'entry_bg': 'white', 'entry_fg': 'black',
                'btn_bg': 'white', 'btn_fg': 'black',
                'active_bg': '#E0E0E0'
            },
            'dark': {
                'bg': '#2E2E2E', 'fg': 'white',
                'entry_bg': '#1C1C1C', 'entry_fg': 'white',
                'btn_bg': '#424242', 'btn_fg': 'white',
                'active_bg': '#616161'
            }
        }

        # 입력창
        self.entry = tk.Entry(root, font=("Arial", 24), justify="right", bd=0)
        self.entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

        # 버튼 생성
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', 'C', '+'],
            ['=', 'Theme']
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
                self.buttons.append(btn)

        self.apply_theme('light')

    def on_click(self, char):
        if char == 'Theme':
            self.toggle_theme()
        elif char == 'C':
            self.expression = ""
        elif char == '=':
            try:
                self.expression = str(eval(self.expression))
            except Exception:
                self.expression = "에러"
            self.updata_entry()
        else:
            self.expression += str(char)
            self.updata_entry()

    
    def update_entry(self):
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)

    def toggle_theme(self):
        self.is_dark_mode = not self.is_dark_mode
        mode = 'dark' if self.is_dark_mode else 'light'
        self.apply_theme(mode)

    def apply_theme(self, mode):
        c = self.colors[mode]
        self.root.configure(bg=c['bg'])
        self.entry.configure(bg=c['entry_bg'], fg=c['entry_fg'], insertbackground=c['fg'])

        for frame in self.frames:
            frame.configure(bg=c['bg'])

        for btn in self.buttons:
            btn.configure(
                bg=c['btn_bg'],
                fg=c['btn_fg'],
                activebackground=c['active_bg'],
                activeforeground=c['fg']
            )