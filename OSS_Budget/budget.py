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

    def list_remove(self, category): # 제거함수 구현
        if not self.expenses:
            print("제거할 지출 내역이 없습니다.\n")
            return
        # 사용자가 입력한 카테고리와 다른 것들만 모아서 새로운 리스트 구성
        self.expenses = [iist for iist in self.expenses if iist.category != category]
        print("목록: ",category,"제거 완료했습니다.\n")



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


