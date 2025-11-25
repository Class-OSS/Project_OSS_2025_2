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

    # 추가 내용
    def delete_expense(self, index):
        """
        인덱스(1 기반)를 받아 해당 지출을 삭제한다.
        - index: 1부터 시작하는 정수
        반환값: 삭제 성공하면 True, 실패하면 False
        """
        # 유효성 검사
        if not isinstance(index, int):
            print("인덱스는 정수여야 합니다.\n")
            return False

        if index < 1 or index > len(self.expenses):
            print("잘못된 인덱스입니다.\n")
            return False

        removed = self.expenses.pop(index - 1)
        print(f"삭제되었습니다: {removed}\n")
        return True