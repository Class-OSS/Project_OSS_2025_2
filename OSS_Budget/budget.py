import datetime
from expense import Expense

class Budget:
    def __init__(self):
        self.expenses = []
        self.monthly_budget = 0 

    def set_budget(self, amount):
        if amount >= 0:
            self.monthly_budget = amount
            print(f"월별 목표 예산이 {amount}원으로 설정되었습니다.\n")
        else:
            print("예산은 0원 이상으로 설정해야 합니다.\n")

    def add_expense(self, category, description, amount, payment_method):
        today = datetime.date.today().isoformat()
        expense = Expense(today, category, description, amount, payment_method)
        self.expenses.append(expense)
        print("지출이 추가되었습니다.\n")
        current_total = self.total_spent(silent=True) # 현재 총액 가져오기
        if self.monthly_budget > 0 and current_total > self.monthly_budget:
            over_amount = current_total - self.monthly_budget
            print(f"※※예산 초과 경고! 현재 지출액이 목표 예산({self.monthly_budget}원)을 {over_amount}원 초과했습니다.※※\n")

    def list_expenses(self):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return
        print("\n[지출 목록]")
        for idx, e in enumerate(self.expenses, 1):
            print(f"{idx}. {e}")
        print()

    def report_by_payment_method(self):
        if not self.expenses:
            print("지출 내역이 없어 통계를 낼 수 없습니다.\n")
            return

        payment_totals = {}

        for expense in self.expenses:
            method = expense.payment_method
            amount = expense.amount

            if method in payment_totals:
                payment_totals[method] += amount
            else:
                payment_totals[method] = amount
        print("\n[결제 수단별 지출 요약]")
        total_sum = 0

        for method, total in payment_totals.items():
            print(f"- {method}: {total}원")
            total_sum += total

        print("-" * 25)
        print(f"총 합계: {total_sum}원\n")

     
    def total_spent(self, silent=False):
        total = sum(e.amount for e in self.expenses)
        if not silent:
            print(f"총 지출: {total}원\n")
        return total

