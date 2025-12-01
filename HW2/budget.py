import datetime
from expense import Expense

class Budget:
    def __init__(self):
        self.expenses = []
        self.cashback_balance = 0

    def add_expense(self, category, description, amount):
        today = datetime.date.today().isoformat()
        expense = Expense(today, category, description, amount)
        self.expenses.append(expense)

        cashback_rates = {
            "식비": 0.02,
            "교통": 0.05,
            "문화생활": 0.03,
            "취미": 0.01,
            "자기개발": 0.02
        }
        rate = cashback_rates.get(category, 0.01)
        cashback = int(amount * rate)

        self.cashback_balance += cashback
        print(f"지출이 추가되었습니다. (캐시백 {cashback}원 적립)\n")

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

    def show_cashback(self):
        print(f"현재 캐시백 총액: {self.cashback_balance}원\n")
