import datetime
from expense import Expense

class Budget:
    def __init__(self):
        self.expenses = []
        self.budget_limit = None

    def set_budget(self, budget_limit):
        self.budget_limit = budget_limit
        print(f"예산: {budget_limit}원\n")

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
        if total == 0:
            print("지출 내역이 없습니다.\n")
            pass
        else:
            print(f"총 지출: {total}원\n")
            return total     

    def calc_remaining(self):
        if self.budget_limit is None:
            # print("예산이 설정되지 않았습니다.\n")
            return None
        
        total = sum(e.amount for e in self.expenses)
        remaining = self.budget_limit - total
        print(f"잔액: {remaining}원\n")
        return remaining