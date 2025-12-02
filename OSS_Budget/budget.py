import datetime
from expense import Expense
from expense import Income
class Budget:
    def __init__(self):
        self.expenses = []

    def add_income(self1, category, description, amount):
        today = datetime.date.today().isoformat()
        income = Income(today, category, description, amount)
        self1.expenses.append(income)
        print("수입이 추가되었습니다.\n")

    def list_income(self1):
        if not self1.expenses:
            print("수입 내역이 없습니다.\n")
            return
        print("\n[지출/수입 목록]")
        for idx, e in enumerate(self1.expenses, 1):
            print(f"{idx}. {e}")
        print()

    def add_expense(self, category, description, amount):
        today = datetime.date.today().isoformat()
        expense = Expense(today, category, description, -amount)
        self.expenses.append(expense)
        print("지출이 추가되었습니다.\n")

    def list_expenses(self):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return
        print("\n[지출/수입 목록]")
        for idx, e in enumerate(self.expenses, 1):
            print(f"{idx}. {e}")
        print()

    def total(self):
        total = sum(e.amount for e in self.expenses)
        print(f"총 지출+수입: {total}원\n")



