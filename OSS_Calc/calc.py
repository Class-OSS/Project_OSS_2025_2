import tkinter as tk


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("300x400")

        self.expression = ""

        self.entry = tk.Entry(root, font=("Arial", 24), justify="right")
        self.entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

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
                    cursor="hand2",
                    relief="raised",
                    bd=2,
                    command=lambda ch=char, b=frame: None 
                )

                btn.default_bg = btn.cget("bg")
                btn.default_relief = btn.cget("relief")

                btn.config(command=lambda ch=char, b=btn: self.on_click(ch, b))

                btn.pack(side="left", expand=True, fill="both")

    def animate_button(self, btn):
        original_bg = btn.default_bg
        original_relief = btn.default_relief

        btn.config(bg="#d0d0ff", relief="sunken")
        self.root.after(
            120,
            lambda: btn.config(bg=original_bg, relief=original_relief)
        )

    def on_click(self, char, btn):
        self.animate_button(btn)

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
