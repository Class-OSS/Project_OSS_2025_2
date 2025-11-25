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

    def list_by_period(self, start, end):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return

        try:
            start_date = datetime.datetime.time(start, "%Y-%m-%d").date()
            end_date = datetime.datetime.time(end, "%Y-%m-%d").date()
        except ValueError:
            print("날짜 형식이 잘못되었습니다.")
            return

        print(f"\n[{start} ~ {end} 지출 기록]")

        filtered = []
        for e in self.expenses:
            e_date = datetime.datetime.time(e.date, "%Y-%m-%d").date()
            if start_date <= e_date <= end_date:
                filtered.append(e)

        if not filtered:
            print("지출이 없습니다.\n")
            return

        for e in filtered:
            print(e)
        print()



