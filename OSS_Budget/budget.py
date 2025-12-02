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
    def delete_expense(self):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return

        self.list_expenses()
        try:
            idx = int(input("삭제할 번호를 선택하세요: ")) - 1
        except ValueError:
            print("잘못된 입력입니다.\n")
            return

        if idx < 0 or idx >= len(self.expenses):
            print("해당 번호는 존재하지 않습니다.\n")
            return

        removed = self.expenses.pop(idx)
        print(f"삭제된 지출: {removed}\n")


