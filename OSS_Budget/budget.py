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
def search_by_category(self):
        print("\n--- 카테고리별 검색 ---")
        category = input("검색할 카테고리를 입력하세요: ")
        
        print(f"\n[ {category} 검색 결과 ]")
        found = False
        total = 0
        
        for expense in self.expenses:
            if expense.category == category:
                print(f"날짜: {expense.date}, 내용: {expense.description}, 금액: {expense.amount}")
                total += int(expense.amount)
                found = True
        
        if not found:
            print("해당 카테고리의 내역이 없습니다.")
        else:
            print(f"-------------------------")
            print(f"{category} 총 지출액: {total}원")
        print("")


