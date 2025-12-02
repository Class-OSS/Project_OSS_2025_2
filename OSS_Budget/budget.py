import datetime
from expense import Expense

class Budget:
    def __init__(self):
        self.expenses = []
        self.monthly_limit = None   # 월 지출 한도
        self.monthly_spent = 0      # 이번 달 누적 지출

    def set_limit(self, amount):
        """월 지출 한도 설정"""
        self.monthly_limit = amount
        print(f"이번 달 예산이 {amount}원으로 설정되었습니다.\n")

    def add_expense(self, category, description, amount):
        """지출 추가"""
        today = datetime.date.today().isoformat()
        expense = Expense(today, category, description, amount)
        self.expenses.append(expense)

        # 누적 지출 업데이트
        self.monthly_spent += amount

        print("지출이 추가되었습니다.\n")

        # 예산 초과 여부 확인
        if self.monthly_limit is not None:
            self.check_limit()

    def check_limit(self):
        """예산 초과 여부 확인"""
        if self.monthly_spent > self.monthly_limit:
            exceeded = self.monthly_spent - self.monthly_limit
            print(f"⚠ 경고! 이번 달 예산 {self.monthly_limit}원을 초과했습니다!")
            print(f"현재 총 지출: {self.monthly_spent}원 (초과 {exceeded}원)\n")
        else:
            remaining = self.monthly_limit - self.monthly_spent
            print(f"현재 총 지출: {self.monthly_spent}원")
            print(f"예산까지 {remaining}원 남았습니다.\n")

    def delete_expense(self, index):
        """지출 삭제 기능"""
        if not self.expenses:
            print("삭제할 지출이 없습니다.\n")
            return

        if index < 1 or index > len(self.expenses):
            print("잘못된 번호입니다.\n")
            return

        # 삭제할 금액을 예산 계산에서 빼줌
        removed_amount = self.expenses[index - 1].amount
        self.monthly_spent -= removed_amount

        # 리스트에서 삭제
        removed = self.expenses.pop(index - 1)
        print(f"삭제 완료: {removed}\n")

    def list_expenses(self):
        """지출 내역 출력"""
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return
        print("\n[지출 목록]")
        for idx, e in enumerate(self.expenses, 1):
            print(f"{idx}. {e}")
        print()

    def total_spent(self):
        """총 지출 출력"""
        total = sum(e.amount for e in self.expenses)
        print(f"총 지출: {total}원\n")
