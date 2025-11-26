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

## 지출 내역 수정
    def edit_expense(self, index, n_category, n_description, n_amount):
        if 0 <= index < len(self.expenses):
            e = self.expenses[index]
            e.category = n_category
            e.description = n_description
            e.amount = n_amount
        else:
            print("잘못된 번호입니다.\n")
    
## 지출 내역 삭제
    def delete_expense(self, index):
        if 0 <= index < len(self.expenses):
            del self.expenses[index]
            print("목록이 제거되었습니다\n.")
        else:
            print("잘못된 번호입니다.\n")

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



