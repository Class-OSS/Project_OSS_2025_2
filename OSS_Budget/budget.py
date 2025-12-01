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

    
    # 추가 기능: 오래된 지출 자동 삭제
 
    def remove_old_expenses(self, days):
        today = datetime.date.today()
        threshold = today - datetime.timedelta(days=days)

        before_count = len(self.expenses)

        # 지출 날짜 기준으로 필터링
        self.expenses = [
            e for e in self.expenses
            if datetime.date.fromisoformat(e.date) >= threshold
        ]

        deleted_count = before_count - len(self.expenses)
        print(f"{days}일 이상 지난 지출 {deleted_count}개 삭제 완료.\n")
