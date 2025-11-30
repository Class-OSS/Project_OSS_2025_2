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

    def monthly_category_ranking(self, year, month):
        monthly_expenses = []
        for e in self.expenses:
            try:
                y, m, _ = map(int, e.date.split("-"))
            except:
                continue

            if y == year and m == month:
                monthly_expenses.append(e)

        if not monthly_expenses:
            print(f"\n{year}년 {month}월 지출 내역이 없습니다.\n")
            return

        category_total = {}
        for e in monthly_expenses:
            category_total[e.category] = category_total.get(e.category, 0) + e.amount

        sorted_result = sorted(category_total.items(), key=lambda x: x[1], reverse=True)

        print(f"\n=== {year}년 {month}월 카테고리 지출 순위 ===")
        for idx, (cat, total) in enumerate(sorted_result, 1):
            print(f"{idx}위: {cat} - {total}원")
        print()


