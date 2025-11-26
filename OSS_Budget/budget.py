import datetime
from expense import Expense, Income

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
        print(f"총 지출: {total}원")
        return total # 총 지출 값을 사용하기 위해 리턴

    def percentage(self1, self2): # 총 수입에서 몇 퍼센트만큼 지출을 썼는지 확인
        total_expense = self1.total_spent()
        total_income = self2.total_gain()
        if total_income == 0:
            print("총 수입이 없으므로 비율 계산이 안됩니다.\n")
            return
        percentage = (total_expense / total_income) * 100
        print(f"수입 대비 지출 비율 : {percentage:.2f}%\n")
        

class Budget_income: # 수입 클래스 추가, 양식은 위와 동일
    def __init__(self):
        self.incomes = []

    def add_incomes(self, category, description, amount):
        today = datetime.date.today().isoformat()
        income = Income(today, category, description, amount)
        self.incomes.append(income)
        print("수입이 추가되었습니다.\n")

    def list_incomes(self):
        if not self.incomes:
            print("수입 내역이 없습니다.\n")
            return
        print("\n[수입 목록]")
        for idx, e in enumerate(self.incomes, 1):
            print(f"{idx}. {e}")
        print()

    def total_gain(self):
        total = sum(e.amount for e in self.incomes)
        print(f"총 수입: {total}원")
        return total # 총 수입 값을 사용하기 위해 리턴


    
