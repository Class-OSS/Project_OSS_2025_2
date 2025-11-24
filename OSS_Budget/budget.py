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


    #지정한 날짜 사이의 지출 찾기 / 날짜 형식 : yyyy-mm-dd
    def date2date_expense(self, start_date:str = datetime.date.today().isoformat(), end_date:str = datetime.date.today().isoformat()) -> None:
        temp_list=self.expenses
        temp_list.sort(key=lambda x:x.date)
        result_list=[]
        for i in temp_list:
            if(i.date >= start_date and i.date <= end_date):
                result_list.append(i)
        
        if(len(result_list) == 0):
            print(f'{start_date}부터 {end_date}까지 검색된 지출 내역이 없습니다.')
        else:
            print(f'{start_date}부터 {end_date}까지 지출 내역입니다.')
            print('=========================================')
            for r in result_list:
                print(r)
            print('=========================================')
            