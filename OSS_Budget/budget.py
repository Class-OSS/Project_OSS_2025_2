import datetime
from expense import Expense

class Budget:
    def __init__(self):
        self.expenses = []

    # user_name 인자 추가
    def add_expense(self, category, description, amount, user_name):
        today = datetime.date.today().isoformat()
        # Expense 객체 생성 시 user_name 전달
        expense = Expense(today, category, description, amount, user_name)
        self.expenses.append(expense)
        print(f"{user_name}님의 지출이 추가되었습니다.\n")

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
