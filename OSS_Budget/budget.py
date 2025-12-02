import datetime
from expense import Expense

class Budget:
    def __init__(self):
        self.expenses = []

    def add_expense(self, category, description, amount):
        today = datetime.date.today().isoformat()
        expense = Expense(today, category, description, amount)
        self.expenses.append(expense)
        print(f"지출 내역이 추가되었습니다: {description}\n")

    def list_expenses(self):
        if not self.expenses:
            print("작성된 지출 내역이 없습니다.\n")
            return
        print("\n[전체 지출 목록]")
        for idx, e in enumerate(self.expenses, 1):
            print(f"{idx}. {e}")
        print()

    def total_spent(self):
        total = sum(e.amount for e in self.expenses)
        print(f"현재까지 총 지출액: {total}원\n")

    def sort_by_amount(self):
        if not self.expenses:
            print("정렬할 데이터가 없습니다.\n")
            return
        
        sorted_list = sorted(self.expenses, key=lambda x: x.amount, reverse=True)
        
        print("\n[금액순 지출 목록 (높은순)]")
        for idx, e in enumerate(sorted_list, 1):
            print(f"{idx}. {e}")
        print()