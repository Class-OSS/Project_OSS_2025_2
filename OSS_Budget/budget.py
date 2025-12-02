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

    def filte_by_date_range(self,start_data,end_date):
        start=datetime.date.fromisoformat(start_data)
        end=datetime.date.fromisoformat(end_data)
        filter=[
            e for e in self.expense
            if start<=datetime.date.fromisoformat(e.data)<=end
        ]
        if not filtered:
            print(f"{start_date}~{end_data}기간의 지출이 없습니다.\n")
            return
            print(f"\n{start_date}~{end_data}기간 지출 목록")
            for idx,e in enumerate(filtered,1):
               print(f"{idx}.{e}")
            date_total=sum(e.amount for e in filtered)
            print (f"\n기간 총 지출:{date_total}원\n")