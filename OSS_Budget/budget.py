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
    
    def monthly_summary(self): #월별 지출 내역 & 합계
        if not self.expenses:
            print("지출 내역이 없습니다. \n")
            return
            
        monthly_data = {}
        
        for i in self.expenses:
            month = i.date[:7]
            if month not in monthly_data:
                monthly_data[month] = {"total": 0, "items": []}
            monthly_data[month] ["total"] += i.amount
            monthly_data[month] ["items"].append(i)
            
        print("\n [월별 지출 내역]")
        for month in sorted(monthly_data.keys()):
            print(f"{month} | 총 지출 {monthly_data[month] ['total']}원")
            print("---상세 지출 내역---")
            for i, item in enumerate(monthly_data[month]["items"], 1):
                print(f" {i}. {item}")
            print()
