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

    # 금액 기준 검색 메서드
    def search_by_amount(self, target_amount, condition):
        condition: 'up' (이상) 또는 'down' (이하)
        filtered_expenses = []
        
        if condition == 'up':
            # 이상 조건 필터링
            filtered_expenses = [e for e in self.expenses if e.amount >= target_amount]
            cond_text = "이상"
        elif condition == 'down':
            # 이하 조건 필터링
            filtered_expenses = [e for e in self.expenses if e.amount <= target_amount]
            cond_text = "이하"
        
        if not filtered_expenses:
            print(f"\n{target_amount}원 {cond_text}의 지출 내역이 없습니다.\n")
            return

        print(f"\n[{target_amount}원 {cond_text} 지출 목록]")
        for idx, e in enumerate(filtered_expenses, 1):
            print(f"{idx}. {e}")
        print()
