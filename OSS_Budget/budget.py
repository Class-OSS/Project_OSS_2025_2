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

    def modify_expense(self, index, sub_choice, category=None, description=None, amount=0):
        idx = index - 1
        
        if not (0 <= idx < len(self.expenses)):
            print(("잘못된 지출 번호입니다.\n"))
            return
        
        if sub_choice == "1":
            target = self.expenses[idx]
            target.category = category
            target.description = description
            target.amount = amount
            print(f"{index}번 항목이 수정되었습니다.\n")

        elif sub_choice == "2":
            self.expenses.pop(idx)
            print(f"{index}번 항목이 삭제되었습니다.\n")

        else:   
            print("잘못된 번호입니다.\n")



