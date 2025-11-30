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
        
    def list_expenses_by_date_range(self, start_date_str, end_date_str):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return
        
        try:
            # 입력받은 'yymmdd' 문자열 변환
            start_date = datetime.datetime.strptime(start_date_str, "%y%m%d").date()
            end_date = datetime.datetime.strptime(end_date_str, "%y%m%d").date()
        except ValueError:
            print("잘못된 날짜 형식입니다 (yymmdd 형식으로 입력해주세요).\n")
            return

        print(f"\n[지출 목록] 기간: {start_date.isoformat()} ~ {end_date.isoformat()}")
        
        filtered_expenses = []
        for e in self.expenses:
            # Expense 객체의 날짜 문자열을 date 객체로 변환하여 비교
            expense_date = datetime.date.fromisoformat(e.date)
            
            # 지출 날짜가 시작일과 종료일 사이에 있는지 확인
            if start_date <= expense_date <= end_date:
                filtered_expenses.append(e)

        if not filtered_expenses:
            print("해당 기간 내 지출 내역이 없습니다.\n")
            return
        
        for idx, e in enumerate(filtered_expenses, 1):
            print(f"{idx}. {e}")
        print()