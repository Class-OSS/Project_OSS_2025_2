import datetime
from expense import Expense

class Budget:
    def __init__(self):
        self.expenses = []

    def add_expense(self, category, description, amount):
        today = datetime.date.today().isoformat()
        expense = Expense(today, category, description, amount)
        self.expenses.append(expense)
        print("지출이 추가되었습니다.\n")

    def list_expenses(self):
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


    def total_spent_usd(self, rate=1400):
        total = sum(e.amount for e in self.expenses)
        usd = total / rate
        print(f"총 지출(달러 환산): {usd:.2f} USD (환율: 1달러={rate}원)\n")
