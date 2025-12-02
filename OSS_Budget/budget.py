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

    def summary_by_category(self):
        if not self.expenses:
            print(f"지출 내역이 없습니다.\n")
            return
        
        summary = {}
        for e in self.expenses:
            summary[e.category] = summary.get(e.category, 0) + e.amount

        print("\n[카테고리별 지출 요약]")
        for cat, total in summary.items():
            print(f"{cat}: {total}원")
        print()

     def search_by_date(self, start_date, end_date):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return
        print(f"\n[{start_date} ~ {end_date} 지출 내역]")

        found = False
        for e in self.expenses:
            if start_date <= e.date <= end_date:
                print(e)
                found = True
        
        if not found:
            print("해당되는 기간 내 지출이 없습니다.")
        
        print()
