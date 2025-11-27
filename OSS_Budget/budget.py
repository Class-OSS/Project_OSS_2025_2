import datetime
from expense import Expense

class Budget:
    def __init__(self):
        self.expenses = []

    def add_expense(self, category , description, amount):
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

    # 지출 삭제 기능 추가
    def delete_expense(self, index):
        if (1 <= index <= len(self.expenses)):
            del self.expenses[index - 1]
            print(f"{index}번 지출이 삭제되었습니다.\n")
        else:
            print("잘못된 번호입니다.\n")

    # 지출 수정 기능 추가
    def edit_expense(self, index, new_category, new_description, new_amount):
        if (1 <= index <= len(self.expenses)):
            expense = self.expenses[index - 1]
            expense.category = new_category
            expense.description = new_description
            expense.amount = new_amount
            print(f"{index}번 지출이 수정되었습니다 => {expense}\n")
        else:
            print("잘못된 번호입니다.\n")
