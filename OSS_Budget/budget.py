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

    def search_expenses(self, word):
        found = [] 

        for e in self.expenses:
            if word in e.category or word in e.description:
                found.append(e)

        if not found:
            print(f"'{word}' 로 찾은 지출이 없습니다.\n")
            return

        print(f"\n검색 결과 ('{word}')")
        total = 0

        for i, item in enumerate(found, 1):
            print(f"{i}. {item}")
            total += item.amount

        print(f"검색된 지출 합계: {total}원\n")


