import datetime
from expense import Expense

class Budget:
    def __init__(self):
        self.expenses = []
        self.incomes = []

    def add_expense(self, category, description, amount):
        today = datetime.date.today().isoformat()
        expense = Expense(today, category, description, amount)
        self.expenses.append(expense)
        print("지출이 추가되었습니다.\n")
    
    # 가계부 수입 기능 추가
    
    def add_income(self, category, description, amount):
        today = datetime.date.today().isoformat()
        income = Expense(today, category, description, amount)
        self.incomes.append(income)
        print("수입이 추가되었습니다.\n")

    def list_expenses(self):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return
        print("\n[지출 목록]")
        for idx, e in enumerate(self.expenses, 1):
            print(f"{idx}. {e}")
        print()
    
    # 가계부 수입 목록 기능 추가
    
    def list_incomes(self):
        if not self.incomes:
            print("수입 내역이 없습니다.\n")
            return
        print("\n[수입 목록]")
        for idx, e in enumerate(self.incomes, 1):
            print(f"{idx}. {e}")
        print()
    
    # 수입 기능 추가에 따른 총 지출에서 총 금액으로 변경
    
    def total_money(self):
        total -= sum(e.amount for e in self.expenses)
        total = sum(e.amount for e in self.incomes)
        print(f"총 금액: {total}원\n")


