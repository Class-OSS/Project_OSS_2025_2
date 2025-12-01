import datetime
from expense import Expense

class Budget:
    def __init__(self):
        self.expenses = []
        self.load_from_txt()

    def add_expense(self, category, description, amount):
        today = datetime.date.today().isoformat()
        expense = Expense(today, category, description, amount)
        self.expenses.append(expense)
        print("지출이 추가되었습니다.")
        self.save_to_txt()

    def list_expenses(self):
        self.load_from_txt()
        
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return
        print("\n[지출 목록]")
        for idx, e in enumerate(self.expenses, 1):
            print(f"{idx}. {e}")
        print()

    def total_spent(self):
        total = sum(e.amount for e in self.expenses)
        print(f"총 지출: {total}원\n")

    def save_to_txt(self):
        with open("expenses.txt", "w", encoding="utf-8") as f:
            for exp in self.expenses:
                f.write(f"{exp.date},{exp.category},{exp.description},{exp.amount}\n")
        print("expenses.txt에 저장되었습니다.\n")

    def load_from_txt(self):
        self.expenses = []
        
        try:
            with open("expenses.txt", "r", encoding="utf-8") as f:
                for line in f:
                    date, category, description, amount = line.strip().split(",")
                    self.expenses.append(Expense(date, category, description, int(amount)))
        except FileNotFoundError:
            pass


