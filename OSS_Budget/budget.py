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

    def edit_expense(self):
        if not self.expenses:
            print("수정할 지출 내역이 없습니다.\n")
            return

        self.list_expenses()

        try:
            id = int(input("수정할 번호: ")) - 1
            if id < 0 or id >= len(self.expenses):
                print("잘못된 번호입니다.\n")
                return
        except ValueError:
            print("숫자를 입력해주세요.\n")
            return

        expense = self.expenses[id]
        print(f"현재 항목: {expense}")

        new_category = input(f"새 카테고리 (기존 유지는 Enter: {expense.category}) : ") or expense.category
        new_description = input(f"새 설명 (기존 유지는 Enter: {expense.description}) : ") or expense.description
        
        try:
            new_amount_input = input(f"새 금액 (기존 유지는 Enter: {expense.amount}) : ")
            new_amount = int(new_amount_input) if new_amount_input else expense.amount
        except:
            print("잘못된 금액입니다.\n")
            return

        expense.category = new_category
        expense.description = new_description
        expense.amount = new_amount

        print("지출이 수정되었습니다.\n")
    
    def delete_expense(self):
        if not self.expenses:
            print("삭제할 내역이 없습니다.\n")
            return

        self.list_expenses()

        try:
            idx = int(input("삭제할 번호: ")) - 1
            if idx < 0 or idx >= len(self.expenses):
                print("잘못된 번호입니다.\n")
                return
        except ValueError:
            print("숫자를 입력해주세요.\n")
            return

        deleted = self.expenses.pop(idx)
        print(f"삭제되었습니다.: {deleted}\n")

    def total_spent(self):
        total = sum(e.amount for e in self.expenses)
        print(f"총 지출: {total}원\n")


