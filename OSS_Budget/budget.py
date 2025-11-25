import datetime
from expense import Expense

class Budget:
    def __init__(self):
        self.expenses = []
        self.budget_limit = 0

    def set_budget(self, amount):
        if amount >=0:
        self.budget_limit = amount
            print(f"예산은 {self.budget_limit}원입니다.\n")
        else:
            print("예산은 0원 이상입니다.\n")

    def get_total_spent(self):
        return sum(e.amount for e in self.expenses)

    def add_expense(self, category, description, amount):
        today = datetime.date.today().isoformat()
        expense = Expense(today, category, description, amount)
        self.expenses.append(expense)
        print("지출이 추가되었습니다.\n")

        if self.budget_limit > 0 and self.get_total_spent() > self.budget_limit:
            print("예산을 초과했습니다.")
        print()

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

        if self.budget_limit > 0:
            print(f"설정한 예산: {self.budget_limit}원")
            if total > self.budget_limit:
                 print("예산을 초과했습니다.")
        print()


