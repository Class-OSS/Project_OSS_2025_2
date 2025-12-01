import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        
        self.root.geometry("550x400")

        self.expression = ""

        
        main_frame = tk.Frame(root)
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        
        left_frame = tk.Frame(main_frame)
        left_frame.pack(side="left", fill="both", expand=True)

        
        self.entry = tk.Entry(left_frame, font=("Arial", 24), justify="right")
        self.entry.pack(fill="x", ipadx=8, ipady=15, pady=(0, 10))

        
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', 'C', '+'],
            ['=']
        ]

        
        for row in buttons:
            frame = tk.Frame(left_frame)
            frame.pack(expand=True, fill="both")
            for char in row:
                btn = tk.Button(
                    frame,
                    text=char,
                    font=("Arial", 18),
                    command=lambda ch=char: self.on_click(ch)
                )
                btn.pack(side="left", expand=True, fill="both")

        
        right_frame = tk.Frame(main_frame)
        right_frame.pack(side="right", fill="both", expand=True, padx=(10, 0))

        
        tk.Label(right_frame, text="기록", font=("Arial", 12, "bold")).pack(anchor="w")

        
        self.history_list = tk.Listbox(right_frame, font=("Arial", 12), selectmode="extended")
        self.history_list.pack(side="left", fill="both", expand=True)

        
        scrollbar = tk.Scrollbar(right_frame, orient="vertical", command=self.history_list.yview)
        scrollbar.pack(side="right", fill="y")
        self.history_list.config(yscrollcommand=scrollbar.set)


    def on_click(self, char):
        if char == 'C':
            self.expression = ""
        elif char == '=':
            try:
                
                original_expr = self.expression
                
                result = str(eval(self.expression))
                self.expression = result
                
                
                history_text = f"{original_expr} = {result}"
                self.history_list.insert(tk.END, history_text)
                
                
                self.history_list.see(tk.END)
                
            except Exception:
                self.expression = "에러"
        else:
            self.expression += str(char)

        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)
