import tkinter as tk
from tkinter import scrolledtext

#GUI 출력 기능
class userInterface:
    def __init__(self, root, budget):
        self.root = root
        self.root.title("간단 가계부")
        self.root.geometry("800x400")
        self.budget = budget

        #상부
        upperFrame = tk.Frame(root, height=50)
        upperFrame.pack(side='top', fill='x', padx=5, pady=5)

        #하부
        lowerFrame = tk.Frame(root) 
        lowerFrame.pack(fill='both', expand=True, padx=5, pady=(0, 5))
        self.outputString = scrolledtext.ScrolledText(lowerFrame, wrap=tk.WORD, state=tk.DISABLED, bg="#ffffff", fg="#000000", font=('Arial', 12))
        self.outputString.pack(fill='both', expand=True)
        
        #버튼
        button_showExpense = tk.Button(upperFrame, text="지출 목록", command=self.showExpenses)
        button_showExpense.grid(row=0, column=1, sticky="e", padx=5, pady=5)
        button_totalExpense = tk.Button(upperFrame, text="총 지출", command=self.shoeTotal)
        button_totalExpense.grid(row=0, column=2, sticky="e", padx=5, pady=5)

    #출력 헬퍼
    def printGraphics(self, content):
        self.outputString.config(state=tk.NORMAL)
        self.outputString.delete('1.0', tk.END)
        self.outputString.insert(tk.END, content)
        self.outputString.config(state=tk.DISABLED)
        self.outputString.see(tk.END)
    
    #지출 목록 출력
    def showExpenses(self):
        output_str = self.budget.list_expenses()
        print(output_str)
        self.printGraphics(output_str)

    #총 지출 출력
    def shoeTotal(self):
        output_str = self.budget.total_spent()
        print(output_str)
        self.printGraphics(output_str)