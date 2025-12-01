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
            idx = int(input("수정할 번호를 입력하세요: "))
        except ValueError:
            print("잘못된 번호입니다.\n")
            return

        if not (1 <= idx <= len(self.expenses)):
            print("존재하지 않는 번호입니다.\n")
            return

        expense = self.expenses[idx - 1]

        print(f"\n선택한 지출: {expense}\n")

        print(f"현재 카테고리: {expense.category}")
        new_category = input("새 카테고리 (그대로 두려면 Enter): ")
        if new_category.strip():
            expense.category = new_category.strip()

        print(f"현재 설명: {expense.description}")
        new_description = input("새 설명 (그대로 두려면 Enter): ")
        if new_description.strip():
            expense.description = new_description.strip()

        print(f"현재 금액: {expense.amount}원")
        new_amount_str = input("새 금액(원) (그대로 두려면 Enter): ")
        if new_amount_str.strip():
            try:
                new_amount = int(new_amount_str)
                expense.amount = new_amount
            except ValueError:
                print("잘못된 금액입니다. 금액은 변경하지 않습니다.")

        print("\n지출이 수정되었습니다.\n")

    def delete_expense(self):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return

        self.list_expenses()

        try:
            idx = int(input("삭제할 번호를 입력하세요: "))
        except ValueError:
            print("잘못된 번호입니다.\n")
            return

        if not (1 <= idx <= len(self.expenses)):
            print("존재하지 않는 번호입니다.\n")
            return

        expense = self.expenses[idx - 1]
        print(f"\n선택한 지출: {expense}")
        confirm = input("정말 삭제하시겠습니까? (y/n): ").strip().lower()

        if confirm == "y":
            del self.expenses[idx - 1]
            print("지출이 삭제되었습니다.\n")
        else:
            print("삭제를 취소했습니다.\n")

    def total_by_month(self):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return

        month = input("조회할 월을 입력하세요 (예: 2025-12): ").strip()

        if len(month) != 7 or month[4] != '-':
            print("형식이 올바르지 않습니다. 예: 2025-12\n")
            return

        monthly_expenses = [e for e in self.expenses if e.date.startswith(month)]

        if not monthly_expenses:
            print(f"{month} 월의 지출 내역이 없습니다.\n")
            return

        total = sum(e.amount for e in monthly_expenses)

        print(f"\n[{month} 월 지출 내역]")
        for idx, e in enumerate(monthly_expenses, 1):
            print(f"{idx}. {e}")
        print(f"\n{month} 월 총 지출: {total}원\n")

    def view_by_category(self):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return

        categories = sorted(set(e.category for e in self.expenses))
        print("\n[등록된 카테고리]")
        for c in categories:
            print(f"- {c}")
        print()

        category = input("조회할 카테고리 이름을 입력하세요 (예: 식비): ").strip()
        if not category:
            print("카테고리를 입력하지 않았습니다.\n")
            return

        filtered = [e for e in self.expenses if e.category == category]

        if not filtered:
            print(f"'{category}' 카테고리의 지출 내역이 없습니다.\n")
            return

        print(f"\n[{category} 카테고리 지출 내역]")
        total = 0
        for idx, e in enumerate(filtered, 1):
            print(f"{idx}. {e}")
            total += e.amount

        print(f"\n{category} 카테고리 총 지출: {total}원\n")

