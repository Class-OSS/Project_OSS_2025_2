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

    def delete_expense(self, index):
        if index < 0 or index >= len(self.expenses):
            print("잘못된 번호입니다. 목록에 있는 번호를 입력해주세요.\n")
            return
        
        removed_expense = self.expenses.pop(index)
        print(f"삭제됨: {removed_expense.description}")
        print("지출이 성공적으로 삭제되었습니다.\n")

    def total_spent(self):
        total = sum(e.amount for e in self.expenses)
        print(f"총 지출: {total}원\n")


