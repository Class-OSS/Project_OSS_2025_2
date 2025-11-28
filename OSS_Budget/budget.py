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

    def list_expenses_by_period(self, start_date, end_date):
        """기간별 지출 조회"""
        filtered = [e for e in self.expenses if start_date <= e.date <= end_date]

        if not filtered:
            print(f"\n{start_date} ~ {end_date} 사이 지출 내역이 없습니다.\n")
            return

        print(f"\n{start_date} ~ {end_date} 사이 지출 목록")
        for idx, e in enumerate(filtered, 1):
            print(f"{idx}. {e}")

        total = sum(e.amount for e in filtered)
        print(f"/n기간 내 총 지출: {total}원\n")

