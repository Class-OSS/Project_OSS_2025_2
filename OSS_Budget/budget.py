import datetime
from expense import Expense

class Budget:
    def __init__(self):
        self.expenses = []
        self.monthly_budget = {}
 
    def set_budget(self, month, amount):
        self.monthly_budget[month] = amount
        print(f"{month}의 예산이 {amount}원으로 설정되었습니다.\n")

    def add_expense(self, category, description, amount):
        today = datetime.date.today().isoformat()
        current_month = today[:7]
        expense = Expense(today, category, description, amount)
        self.expenses.append(expense)

        self._check_budget_warning(current_month, amount)
        print("지출이 추가되었습니다.\n")

    def list_expenses(self):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return
        print("\n[지출 목록]")
        for idx, e in enumerate(self.expenses, 1):
            print(f"{idx}. {e}")
        print()

    def _check_budget_warning(self, month, new_expense_amount):
        if month in self.monthly_budget:
            budget_amount = self.monthly_budget[month]
            
            # 현재 월의 총 지출 계산
            spent_this_month = sum(
                e.amount for e in self.expenses 
                if e.date.startswith(month)
            )

            remaining = budget_amount - spent_this_month
            
            if spent_this_month > budget_amount:
                print(f"예산 초과 경고!")
                print(f"{month} 지출({spent_this_month}원)이 예산({budget_amount}원)을 {abs(remaining)}원 초과했습니다!")
            elif remaining <= budget_amount * 0.1 and remaining > 0:
                print(f"예산 근접 경고!")
                print(f"{month}의 남은 예산이 {remaining}원입니다. 예산의 10% 미만입니다!")

    def total_spent(self):
        total = sum(e.amount for e in self.expenses)
        print(f"총 지출: {total}원\n")


