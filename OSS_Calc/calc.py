import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("300x450")

        self.x = ""      
        self.h = []      

        self.entry = tk.Entry(root, font=("Arial", 24), justify="right")
        self.entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

        self.hl = tk.Label(root, font=("Arial", 10), justify="left", anchor="w")
        self.hl.pack(fill="both", padx=10, pady=5)

        btns = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', 'C', '+'],
            ['=']
        ]

        for row in btns:
            f = tk.Frame(root)
            f.pack(expand=True, fill="both")
            for ch in row:
                b = tk.Button(
                    f,
                    text=ch,
                    font=("Arial", 18),
                    command=lambda z=ch: self.click(z)
                )
                b.pack(side="left", expand=True, fill="both")

    def click(self, ch):
        if ch == 'C':
            self.x = ""
        elif ch == '=':
            try:
                bx = self.x          
                r = str(eval(self.x)) 
                self.x = r

                t = bx + " = " + r   
                self.h.append(t)

                if len(self.h) > 3:
                    self.h.pop(0)

                self.show_h()

            except:
                self.x = "에러"
        else:
            self.x += str(ch)

        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.x)

    def show_h(self):
        s = ""
        for i in self.h:
            s += i + "\n"
        self.hl.config(text=s)
