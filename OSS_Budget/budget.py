import datetime
from collections import defaultdict
from expense import Expense
from asset import Asset
class Budget:
    def __init__(self):
        self.expenses = []
        self.assets = []

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

    def add_asset(self, category, description, amount):
        today = datetime.date.today().isoformat()
        asset = Asset(today, category, description, amount)
        self.assets.append(asset)
        print("자산이 추가되었습니다.\n")
        
    def total_asset(self):

        category_totals = defaultdict(int)
        for a in self.assets:
            category_totals[a.category] += a.amount 

        for category, total in category_totals.items():
            print(f"{category} - {total}원")


        total_assets = sum(category_totals.values())
        print(f"총 자산 - {total_assets}원\n")


