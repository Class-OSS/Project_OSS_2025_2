import datetime
from expense import Expense

class Budget:
    def __init__(self, limit=100):
        self.expenses = []
        self.limit = limit

    def s_limit(self, money_limit):
        self.limit = money_limit
        print(f"지출 한도가 {money_limit}원으로 설정되었습니다.\n")
        
    def get_total_spent(self):
        return sum(e.amount for e in self.expenses)

    def add_expense(self, date, category, description, amount): 
        expense = Expense(date, category, description, amount)
        self.expenses.append(expense)
        print("지출이 추가되었습니다.\n")
        current_money = self.get_total_spent()
        if current_money >= self.limit:
            print(f"총 지출액이 지출 한도({self.limit}원)를 초과했습니다! (누적: {current_money}원)\n")

    def list_expenses(self):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return
        sorted_expenses = sorted(self.expenses, key=lambda e: e.date)
        print("\n[지출 목록]")
        for idx, e in enumerate(self.expenses, 1):
            print(f"{idx}. {e}")
        print()

    def total_spent(self):
        total = sum(e.amount for e in self.expenses)
        print(f"총 지출: {total}원\n")


