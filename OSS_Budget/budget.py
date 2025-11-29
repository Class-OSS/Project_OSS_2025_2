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

    def show_labor_value(self):
        total = sum(e.amount for e in self.expenses)
        
        min_wage = 10320
        work_hours = total / min_wage
        
        print(f"총 지출: {total}원")
        print(f"최저시급 기준 약 {work_hours:.2f}시간 일해야 합니다.")
        print("돈을 아껴 씁시다! \n")

