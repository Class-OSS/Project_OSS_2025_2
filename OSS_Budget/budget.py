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

    def delete_expense(self, index):
        if 0 <= index < len(self.expenses):
            removed = self.expenses.pop(index)
            print(f"삭제 완료: {removed.description} ({removed.amount}원)\n")
        else:
            print("잘못된 번호입니다.\n")
# 저축 기능 추가
    def __init__(self):
       self.expenses = []
       self.goal_amount = None
       self.saved_amount = 0

    def set_goal(self, goal):
       self.goal_amount = goal
       print(f"목표 금액이 {goal}원으로 설정되었습니다.\n")

    def add_saving(self, amount):
       self.saved_amount += amount
       print(f"{amount}원 저축되었습니다.\n")

    def show_goal_status(self):
        if self.goal_amount is None:
            print("저축 목표가 설정되지 않았습니다.\n")
            return

        remaining = self.goal_amount - self.saved_amount

        print("\n[저축 목표 현황]")
        print(f"목표 금액: {self.goal_amount}원")
        print(f"현재 저축액: {self.saved_amount}원")
        print(f"남은 금액: {remaining}원")

        try:
            months = int(input("남은 기간(개월) 입력 > "))
            if months > 0:
                required_per_month = remaining / months
                print(f"목표 달성을 위해 매달 {required_per_month:,.0f}원씩 저축 필요\n")
        except ValueError:
            print("잘못된 입력입니다.\n")



