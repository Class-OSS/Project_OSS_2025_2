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

    def spent_rank(self):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return

        #e.amount 기준으로 내림차순 정렬
        sorted_expenses = sorted(self.expenses, key=lambda x: x.amount, reverse=True)

        #출력
        print("\n[지출 목록 순위]")
        for idx, e in enumerate(sorted_expenses, 1): #enumerate가 알아서 리스트 크기 확인함, len()과 인덱스를 안써도 됨.
            print(f"{idx}위: [{e.date}] {e.category} - {e.description} ({e.amount}원)")
        print()

