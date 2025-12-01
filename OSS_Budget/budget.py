import datetime
from expense import Expense

class Budget:
    def __init__(self):
        self.expenses = []

    def add_expense(self, category, description, amount, payment_method):
        today = datetime.date.today().isoformat()
        expense = Expense(today, category, description, amount, payment_method)
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

     
    def total_spent(self):
        total = sum(e.amount for e in self.expenses)
        print(f"총 지출: {total}원\n")


