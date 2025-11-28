import datetime
from expense import Expense

class Budget:
    def __init__(self):
        self.expenses = []
        self.limit = None

    def add_expense(self, category, description, amount):
        today = datetime.date.today().isoformat()
        expense = Expense(today, category, description, amount)
        self.expenses.append(expense)
        print("지출이 추가되었습니다.\n")

        #지출시 목표금액 확인
        self.check_limit()

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


        #목표 금액 설정
    def goal_spend(self, goal):
        self.limit = goal
        print(f"이번달 목표 금액: {goal}(원)\n")

        #목표 금액을 넘는지 확인
    def check_limit(self):
        if self.limit is None:
            return  # 목표 금액이 설정되지 않았으면 검사하지 않음

        total = sum(e.amount for e in self.expenses)
        
        if total > self.limit:
            over_amount = total - self.limit
            print(f"!!!!!!!!!경고: 목표 금액({self.limit}(원)에서 {over_amount}원 초과!!!!!!!!")
        else:
            print(f"남은 예산: {self.limit - total}원 (목표: {self.limit}원)")
