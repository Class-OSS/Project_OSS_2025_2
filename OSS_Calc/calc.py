import tkinter as tk

def prime_factorization(n):
    #문자열->정수
    try:
        n = int(n)
    except ValueError:
        return "에러: 정수만"
        
    if n <= 1:
        return "에러: 1보다 큰 정수"
    
    factors = {}
    
    d = 2
    while n % d == 0:
        factors[d] = factors.get(d, 0) + 1
        n //= d
        
    d = 3
    while d * d <= n:
        while n % d == 0:
            factors[d] = factors.get(d, 0) + 1
            n //= d
        d += 2
        
    if n > 1:
        factors[n] = factors.get(n, 0) + 1

    # 결과를 문자열으로
    result = []
    for base, exponent in sorted(factors.items()):
        if exponent == 1:
            result.append(str(base))
        else:
            result.append(f"{base}^{exponent}")
            
    return " * ".join(result)


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("300x400")

        self.expression = ""

        # 입력창
        self.entry = tk.Entry(root, font=("Arial", 24), justify="right")
        self.entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

        # 버튼 생성
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', 'C', '+'],
            ['=', 'PF'] 
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
        elif char == 'PF': 
            try:
                result = prime_factorization(self.expression)
                
                if result.startswith("에러"):
                    self.expression = result
                else:
                    self.expression = result
                    
            except Exception:
                self.expression = "에러"
        elif char == '=':
            try:
                self.expression = str(eval(self.expression))
            except Exception:
                self.expression = "에러"
        else:
            self.expression += str(char)

        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)