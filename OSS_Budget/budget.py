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

     def total_by_month(self, year, month):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return

        ym = f"{year:04d}-{month:02d}"
        total = 0

        for e in self.expenses:
            if hasattr(e, "date") and isinstance(e.date, str) and e.date.startswith(ym):
                total += e.amount

        print(f"\n[{year}년 {month}월 지출 합계]")
        print(f"총 지출: {total}원\n")
