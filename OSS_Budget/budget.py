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
        print("[지출 목록]")
        for idx, e in enumerate(self.expenses, 1):
            print(f"{idx}. {e}")
        print()

    def list_delete(self):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return
        self.list_expenses()
        try :
            d_number_str = input("삭제할 항목 번호를 입력하세요 : ")
            d_number = int(d_number_str)
        except ValueError :
            print("숫자를 입력해야 합니다.\n")
            return
        if 1<=d_number<=len(self.expenses):
            deleted = self.expenses.pop(d_number-1)
            print("삭제되었습니다.\n현재목록 : ")
            self.list_expenses()
        else:
            print("올바른 번호가 아닙니다.\n")
            return
        
    
    def total_spent(self):
        total = sum(e.amount for e in self.expenses)
        print(f"총 지출: {total}원\n")


