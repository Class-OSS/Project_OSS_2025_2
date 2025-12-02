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

      # 추가 기능: 3개월(90일) 지난 지출 자동 삭제
   
    def remove_old_expenses_3months(self):
        """3개월(90일)보다 오래된 지출 자동 삭제"""
        today = datetime.date.today()
        threshold = today - datetime.timedelta(days=90)

        before = len(self.expenses)

        # 90일 이내 기록만 남김
        self.expenses = [
            e for e in self.expenses
            if datetime.date.fromisoformat(e.date) >= threshold
        ]

        deleted = before - len(self.expenses)
        print(f"3개월 이상 지난 지출 {deleted}개 삭제 완료.\n")
