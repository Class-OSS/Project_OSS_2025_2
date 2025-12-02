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
    def edit_expense(self):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return

        self.list_expenses()
        try:
            idx = int(input("수정할 번호를 선택하세요: ")) - 1
        except ValueError:
            print("잘못된 입력입니다.\n")
            return

        if idx < 0 or idx >= len(self.expenses):
            print("해당 번호는 존재하지 않습니다.\n")
            return

        expense = self.expenses[idx]
        print(f"\n현재 선택한 지출: {expense}")

        print("수정하지 않으려면 엔터를 그대로 누르세요.\n")

        new_category = input(f"카테고리 [{expense.category}]: ") or expense.category
        new_description = input(f"설명 [{expense.description}]: ") or expense.description

        new_amount_input = input(f"금액 [{expense.amount}원]: ")
        if new_amount_input.strip() == "":
            new_amount = expense.amount
        else:
            try:
                new_amount = int(new_amount_input)
            except ValueError:
                print("잘못된 금액입니다. 수정이 취소됩니다.\n")
                return

        expense.category = new_category
        expense.description = new_description
        expense.amount = new_amount

        print("지출이 성공적으로 수정되었습니다.\n")
