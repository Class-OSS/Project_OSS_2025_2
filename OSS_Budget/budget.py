import datetime
from expense import Expense
from exchange import Exchange

class Budget:
    def __init__(self):
        self.expenses = []

    def add_expense(self, category, description, amount, currency):
        ex=Exchange()
        today = datetime.date.today().isoformat()
        after_calc_amount=ex.calc_excange(amount, currency)
        expense = Expense(today, category, description, amount, currency)
        expense.amount = after_calc_amount
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