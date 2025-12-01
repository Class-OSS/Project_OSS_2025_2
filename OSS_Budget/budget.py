import datetime
import random
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

    def predict_next_month_expense(self):
        """이번 달 지출 총액을 기반으로 다음 달 예상 지출을 랜덤 변동 포함 계산"""
        if not self.expenses:
            print("예측할 지출 데이터가 없습니다.\n")
            return

        today = datetime.date.today()
        current_month = today.month
        current_year = today.year

        # 이번 달 지출만 필터링
        current_month_expenses = [
            e.amount for e in self.expenses
            if datetime.date.fromisoformat(e.date).month == current_month
            and datetime.date.fromisoformat(e.date).year == current_year
        ]

        if not current_month_expenses:
            print("이번 달 지출 데이터가 없습니다.\n")
            return

        # 이번 달 총 지출
        total_current_month = sum(current_month_expenses)

        # 랜덤 변동 적용: ±10%
        fluctuation = random.uniform(-0.1, 0.1)  # -10% ~ +10%
        predicted_next_month = int(total_current_month * (1 + fluctuation))

        print(f"이번 달 총 지출: {total_current_month}원")
        print(f"다음 달 예상 지출: {predicted_next_month}원\n")
