import datetime
from expense import Expense

class Budget:
    def __init__(self):
        self.expenses = []
        self.goal_savings = 0
        self.monthly_savings = {}
        self.total_money = {}

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

    def set_goal_savings(self, amount):
        if amount >= 0:
            self.goal_savings = amount
            print(f"!!목표 저축 금액이 {amount}원입니다!!\n")
        else:
            print("목표 금액은 음수가 될 수 없습니다.\n")

    def add_savings(self, date_month, amount):
        if amount > 0:
            self.monthly_savings[date_month] = self.monthly_savings.get(date_month, 0) + amount
            print(f"{date_month}에 {amount}원이 저축액에 추가되었습니다.")
            self.track_savings()
        else:
            print("저축 금액은 양수여야 합니다.\n")

    def track_savings(self):
        total_money = sum(self.monthly_savings.values())
        remaining = self.goal_savings - total_money
        
        print(f"\n[저축 현황]")
        print(f"목표 저축 금액: {self.goal_savings}원")
        print(f"현재까지 총 저축 금액: {total_money}원") 

        if self.goal_savings == 0:
            print("목표 저축 금액이 설정되지 않았습니다.")
        elif remaining > 0:
            print(f"목표까지 남은 금액: {remaining}원")
        elif remaining <= 0:
            plus = abs(remaining)
            print(f"목표 달성! <초과 저축 금액> : {plus}원")
        print()

    def list_monthly_savings(self):
        if not self.monthly_savings:
            print("기록된 저축 내역이 없습니다.\n")
            return
        
        print("\n[월별 저축 내역]")
        for month in sorted(self.monthly_savings.keys()):
            amount = self.monthly_savings[month]
            print(f" - {month}: {amount}원")
        print()
