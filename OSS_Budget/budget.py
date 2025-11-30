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

    # ----------------------------------------
    # 추가 기능: 전달 대비 지출 비교
    # ----------------------------------------
    def compare_with_last_month(self):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return
        
        today = datetime.date.today()
        current_month = today.month
        current_year = today.year

        # 전달 계산
        if current_month == 1:
            last_month = 12
            last_year = current_year - 1
        else:
            last_month = current_month - 1
            last_year = current_year

        # 이번 달 지출 합계
        total_now = sum(
            e.amount for e in self.expenses
            if datetime.date.fromisoformat(e.date).month == current_month
            and datetime.date.fromisoformat(e.date).year == current_year
        )

        # 전달 지출 합계
        total_last = sum(
            e.amount for e in self.expenses
            if datetime.date.fromisoformat(e.date).month == last_month
            and datetime.date.fromisoformat(e.date).year == last_year
        )

        print("\n[전달 대비 지출 비교]")
        print(f"이번 달 지출: {total_now}원")
        print(f"전달 지출: {total_last}원")

        if total_last == 0:
            print("전달 지출이 없어 비교할 수 없습니다.\n")
            return

        diff = total_now - total_last
        rate = (diff / total_last) * 100

        if diff > 0:
            print(f"지출이 {diff}원 증가 ({rate:.1f}% 상승)\n")
        elif diff < 0:
            print(f"지출이 {-diff}원 감소 ({abs(rate):.1f}% 감소)\n")
        else:
            print("지출에 변화가 없습니다.\n")
