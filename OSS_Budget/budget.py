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

    def check_over_budget(self, limit_amount):
        """
        해당 월의 총 지출이 limit_amount를 초과하는지 확인합니다.
        limit_amount: 허용 예산 한도
        return: 초과 시 경고 메시지, 아니면 현재 지출 금액 안내
        """
        
        # 총 지출 금액 계산
        total_expense = sum(e.amount for e in self.expenses)

        # 예산 초과 여부 확인
        if total_expense > limit_amount:
            return f"[경고] 예산을 초과했습니다! (현재 지출: {total_expense}원 / 한도: {limit_amount}원)"
        else:
            return f"현재 지출: {total_expense}원 (한도: {limit_amount}원)"