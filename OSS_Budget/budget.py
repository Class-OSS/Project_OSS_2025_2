import datetime

class Expense:
    def __init__(self, date, category, description, amount):
        self.date = date
        self.category = category
        self.description = description
        self.amount = amount

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
        for expense in self.expenses:
            print(f"날짜: {expense.date}, 카테고리: {expense.category}, 내용: {expense.description}, 금액: {expense.amount}원")
        print()

    def total_spent(self):
        total = sum(e.amount for e in self.expenses)
        print(f"\n총 지출액: {total}원\n")

    def category_summary(self):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return

        summary = {}
        for e in self.expenses:
            summary[e.category] = summary.get(e.category, 0) + e.amount

        print("\n[카테고리별 지출 합계]")
        for cat, total in summary.items():
            print(f"{cat}: {total}원")
        print()
