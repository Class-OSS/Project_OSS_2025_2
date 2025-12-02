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

    def search_by_category(self, category):
        # 검색 결과를 보여주는 시작 메시지 출력
        print(f"\n[검색 결과: {category}]")
        # 검색 결과가 있는지 확인
        found = False
        
        for idx, e in enumerate(self.expenses, 1):
            if e.category == category:
                print(f"{idx}. {e}")
                found = True
        
        if not found:
            print("해당 카테고리에 지출 내역이 없습니다.")
        print()


