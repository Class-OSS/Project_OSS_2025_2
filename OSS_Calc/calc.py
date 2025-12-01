import tkinter as tk


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("팁(rate) 계산기")
        self.root.geometry("300x450")

        self.expression = ""

       
        self.entry = tk.Entry(root, font=("Arial", 24), justify="right")
        self.entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

        
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', 'C', '+'],
            ['5%','10%','20%','30%'],
            
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

        elif char == '5%':
            try:
                amount = float(self.expression)
                tip= amount * 0.05
                self.expression = str(round (tip,2))

            except Exception:
                self.expression = "에러"

     
        elif char == '10%':
            try:
                amount = float(self.expression)
                tip= amount * 0.1
                self.expression = str(round (tip,2))

            except Exception:
                self.expression = "에러"

      
        elif char == '20%':
            try:
                amount = float(self.expression)
                tip= amount * 0.2
                self.expression = str(round (tip,2))
                
            except Exception:
                self.expression = "에러"
        
        elif char == '30%':
            try:
                amount = float(self.expression)
                tip= amount * 0.3
                self.expression = str(round (tip,2))
                
            except Exception:
                self.expression = "에러"
        
      
      
        else:
            self.expression += str(char)

       
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)
