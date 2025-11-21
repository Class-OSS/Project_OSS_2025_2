import tkinter as tk


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("300x450")

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
            ['=']
            ['USD->KRW', 'KRW->USD']
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
            try:
                self.expression = str(eval(self.expression, {"__builtins__": None}))
            except Exception:
                self.expression = "에러"
        elif char == 'USD->KRW':
            try:
                amount = float(self.expression)
                result = self.convert_currency(amount, 'USD', 'KRW') 
                self.expression = f"USD: {amount} -> KRW: {result:.2f}"
            except ValueError:
                self.expression = "금액 오류"
                
        elif char == 'KRW->USD':
            try:
                amount = float(self.expression)
                result = self.convert_currency(amount, 'KRW', 'USD') 
                self.expression = f"KRW: {amount} -> USD: {result:.2f}"
            except ValueError:
                self.expression = "금액 오류"
                
        else:
            self.expression += str(char)

        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)
        
    def convert_currency(self, amount, from_currency, to_currency):
        # 1 USD = 1350 KRW (예시 고정 환율)
        USD_TO_KRW_RATE = 1350
        
        rates = {
            'KRW': {'USD': 1 / USD_TO_KRW_RATE, 'KRW': 1},
            'USD': {'KRW': USD_TO_KRW_RATE, 'USD': 1}
        }
        
        if from_currency not in rates or to_currency not in rates:
            return 0.0

        try:
            conversion_rate = rates[from_currency][to_currency]
            result = amount * conversion_rate
            return result
        except KeyError:
            return 0.0
        except TypeError:
            return 0.0

if __name__ == '__main__':
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()

    
