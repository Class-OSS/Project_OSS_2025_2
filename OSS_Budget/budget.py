import datetime
import calendar
from expense import Expense

class Budget:
    def __init__(self):
        self.expenses = []
        self.month_budget = None
        self.daily_recommend = None

    def set_month_budget(self, amount):
        self.month_budget = amount
        today = datetime.date.today()
        days = calendar.monthrange(today.year, today.month)[1]
        self.daily_recommend = amount // days
        print(f"월간 예산 {amount}원이 설정되었습니다.\n")
        print(f"하루 권장 지출 금액 : {self.daily_recommend}원\n")

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

    def month_status(self):
         if self.month_budget is None:
             print("월 예산이 설정되지 않았습니다.\n")
             return
         total_spent = sum(e.amount for e in self.expenses)
         remaining = self.month_budget - total_spent

         print("\n[월 예산 사용 현황]")
         print(f"월 예산: {self.month_budget}원")
         print(f"총 지출: {total_spent}원")
         print(f"남은 예산: {remaining}원")


