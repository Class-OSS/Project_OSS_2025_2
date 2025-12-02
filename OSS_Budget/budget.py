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

    def search_expenses(self, keyword):
        results = []
        for real_idx, e in enumerate(self.expenses):
            if (keyword in e.category) or (keyword in e.description):
                results.append((real_idx, e))
        return results

    def delete_expense(self, real_idx):
        try:
            deleted = self.expenses.pop(real_idx)
            print(f"지출 내역이 삭제되었습니다: {deleted.description} ({deleted.amount}원)\n")
            return True
        except IndexError:
            print("잘못된 인덱스입니다.\n")
            return False
