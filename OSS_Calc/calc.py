import tkinter as tk
import math 

EXCHANGE_RATES = {
    'KRW_TO_USD': 0.00075,
    'KRW_TO_CNY': 0.0054,
    'KRW_TO_JPY': 0.11,
    'USD_TO_KRW': 1333.33,
    'CNY_TO_KRW': 185.18,
    'JPY_TO_KRW': 9.09,
    'KRW': 1.0, 'USD': 1.0, 'CNY': 1.0, 'JPY': 1.0 
}
CURRENCIES = ['KRW', 'USD', 'CNY', 'JPY'] 

def convert_currency(amount, from_unit, to_unit):
    if from_unit == to_unit:
        return amount

    if from_unit == 'KRW':
        amount_krw = amount
    elif f'{from_unit}_TO_KRW' in EXCHANGE_RATES:
        amount_krw = amount * EXCHANGE_RATES[f'{from_unit}_TO_KRW']
    else:
        return None 
    
    if to_unit == 'KRW':
        return amount_krw
    elif f'KRW_TO_{to_unit}' in EXCHANGE_RATES:
        return amount_krw * EXCHANGE_RATES[f'KRW_TO_{to_unit}']
    else:
        return None

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("300x500")

        self.expression = ""

        # 입력창
        self.entry = tk.Entry(root, font=("Arial", 24), justify="right")
        self.entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

        convert_frame = tk.Frame(root)
        convert_frame.pack(expand=True, fill="x", padx=10, pady=5)

        self.from_currency = tk.StringVar(root)
        self.from_currency.set(CURRENCIES[0])
        self.to_currency = tk.StringVar(root)
        self.to_currency.set(CURRENCIES[1])

        tk.Label(convert_frame, text="From:", font=("Arial", 12)).pack(side="left")
        from_menu = tk.OptionMenu(convert_frame, self.from_currency, *CURRENCIES)
        from_menu.config(font=('Arial', 12))
        from_menu.pack(side="left", expand=True, fill="x")

        tk.Label(convert_frame, text="To:", font=("Arial", 12)).pack(side="left", padx=(10, 0))
        to_menu = tk.OptionMenu(convert_frame, self.to_currency, *CURRENCIES)
        to_menu.config(font=('Arial', 12))
        to_menu.pack(side="left", expand=True, fill="x")

        convert_btn = tk.Button(
            root,
            text="통화 변환",
            font=("Arial", 14),
            command=self.on_convert
        )
        convert_btn.pack(fill="x", padx=10, pady=5)
        
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
                    command=lambda ch=char: self.on_click(ch) 
                )
                btn.pack(side="left", expand=True, fill="both")

    def on_convert(self):
        from_unit = self.from_currency.get()
        to_unit = self.to_currency.get()

        try:
            amount = float(self.expression)
            
            result = convert_currency(amount, from_unit, to_unit)
            
            if result is not None:
                self.expression = f"{result:.2f}"
            else:
                self.expression = "변환불가"
                
        except ValueError:
            self.expression = "숫자입력"
        except Exception:
            self.expression = "에러"

        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)
        
    def on_click(self, char):
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