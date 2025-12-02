import datetime
from expense import Expense

class Budget:
    def __init__(self, income=0):
        self.expenses = []
        self.income = income

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
    
    def savings_rate(self):
        total = sum(e.amount for e in self.expenses)
        saving = (self.income - total) / self.income * 100
        print(f"저축률: {saving:.2f}%\n")


    def category_stats(self):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return

        category_sum = {}
        for e in self.expenses:
            category_sum[e.category] = category_sum.get(e.category, 0) + e.amount

        total = sum(category_sum.values())

        print("\n[카테고리별 지출 금액 및 비율]")
        for category, amount in category_sum.items():
            percent = (amount / total) * 100
            print(f"{category}: {amount}원 ({percent:.2f}%)")
        