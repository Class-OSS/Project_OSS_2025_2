import datetime
from expense import Expense

class Budget:
    def __init__(self):
        self.expenses = []

    def add_expense(self,  date_str, category, description, amount):
        try:
            date_obj = datetime.date.fromisoformat(date_str)
            date = date_obj.isoformat()
        except ValueError:
            print("날짜 형식이 잘못되었습니다. (예: 2024-10-01)\n")
            return

        expense = Expense(date, category, description, amount)
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

    # 기간 필터 조회 기능
    def filter_by_date(self, start_date, end_date):
        """YYYY-MM-DD 문자열을 받아 해당 기간의 지출만 출력"""
        try:
            start = datetime.date.fromisoformat(start_date)
            end = datetime.date.fromisoformat(end_date)
        except ValueError:
            print("날짜 형식이 잘못되었습니다. (예: 2024-10-01)\n")
            return

        if start > end:
            print("시작 날짜가 종료 날짜보다 늦습니다.\n")
            return

        filtered = [
            e for e in self.expenses
            if start <= datetime.date.fromisoformat(e.date) <= end
        ]

        if not filtered:
            print("해당 기간의 지출이 없습니다.\n")
            return

        print(f"\n[{start_date} ~ {end_date} 지출 목록]")
        for idx, e in enumerate(filtered, 1):
            print(f"{idx}. {e}")

        total = sum(e.amount for e in filtered) #조회기간 동안 지출 총계
        print(f"\n조회 기간 총 지출: {total}원\n")
        #print()


