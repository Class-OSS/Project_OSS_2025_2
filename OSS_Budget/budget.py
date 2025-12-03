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
    def delete_expense(self, index: int):
        if 1 <= index <= len(self.expenses):
            removed = self.expenses.pop(index - 1)
            print(f"삭제됨 → {removed}\n")
        else:
            print("잘못된 번호입니다.\n")

    def get_statistics(self):
        if not self.expenses:
            return None

        amounts = [e.amount for e in self.expenses]
        total = sum(amounts)
        avg = total / len(amounts)
        max_expense = max(self.expenses, key=lambda x: x.amount)
        min_expense = min(self.expenses, key=lambda x: x.amount)

        return {
            "average": avg,
            "max": max_expense,
            "min": min_expense
        }

