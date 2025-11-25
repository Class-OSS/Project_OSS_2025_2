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
    
     def total_spent_category(self):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return

        category_summary = {}
        for expense in self.expenses:
            category = expense.category
            category_summary[category] = category_summary.get(category, 0) + expense.amount
        
        print("\n[카테고리별 지출 내역]")
        for category, total_amount in category_summary.items():
            print(f"- {category}: {total_amount}원")
        
        total_category = sum(category_summary.values())
        print(f"총 지출: {total_category}원\n")