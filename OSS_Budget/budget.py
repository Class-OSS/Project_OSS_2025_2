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


    #문자열을 반환하도록 수정함
    def list_expenses(self):
        if not self.expenses:
            return ("지출 내역이 없습니다.\n")
        
        outputString = ("[지출 목록]\n")
        for idx, e in enumerate(self.expenses, 1):
            outputString += (f"{idx}. {e} \n")
        return outputString

    #문자열을 반환하도록 수정함
    def total_spent(self):
        total = sum(e.amount for e in self.expenses)
        return (f"총 지출: {total}원\n")
    