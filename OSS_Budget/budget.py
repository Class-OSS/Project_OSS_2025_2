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

    def list_expenses_by_date(self, start_date_str, end_date_str):
        """특정 날짜 범위 (start_date_str ~ end_date_str) 내의 지출 내역을 조회합니다."""
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return
            
        try:
            start_date = datetime.date.fromisoformat(start_date_str)
            end_date = datetime.date.fromisoformat(end_date_str)
        except ValueError:
            print("❌ 날짜 형식이 올바르지 않습니다. 'YYYY-MM-DD' 형식으로 입력해주세요.")
            return    
            
        if start_date > end_date:
            print("🚨 시작 날짜가 종료 날짜보다 늦을 수 없습니다.")
            return
       # 범위 내의 지출만 필터링     
        filtered_expenses = []
        for e in self.expenses:
            expense_date = datetime.date.fromisoformat(e.date)
            if start_date <= expense_date <= end_date:
                filtered_expenses.append(e)
                
                
        if not filtered_expenses:
            print(f"\n기간 ({start_date_str} ~ {end_date_str}) 내에 지출 내역이 없습니다.\n")
            return

        print(f"\n[기간별 지출 목록: {start_date_str} ~ {end_date_str}]")
        for idx, e in enumerate(filtered_expenses, 1):
            print(f"{idx}. {e}")
        print()
