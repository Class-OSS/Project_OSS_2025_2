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


    def delete_prev_expense(self):

        if not self.expenses:
            print("지출내역이 하나도 없습니다.")
            return
        expense = self.expenses[-1]
        
        print("지출을 삭제합니다.\n")
        print(f"[삭제된 지출: 카테고리: {expense.category}, 설명: {expense.description}, 금액: {expense.amount}]\n")
        self.expenses.remove(expense)
