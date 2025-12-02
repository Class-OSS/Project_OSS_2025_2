import datetime
import re                            # ← 추가된 부분
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

    # ============================
    #   월별 지출 요약 기능 추가
    # ============================
    def monthly_summary(self, year_month: str | None = None):
        """
        year_month = 'YYYY-MM' 형식이면 해당 월만 합계를 보여주고,
        year_month = None이면 전체 월에 대한 합계를 출력합니다.
        """
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return

        # YYYY-MM 형식인지 검사
        if year_month:
            if not re.fullmatch(r"\d{4}-\d{2}", year_month):
                print("형식은 YYYY-MM 입니다. 예: 2025-12\n")
                return

        # 월별 합산
        sums = {}   # { 'YYYY-MM': total }
        for e in self.expenses:
            ym = e.date[:7]  # 'YYYY-MM'
            if (year_month is None) or (ym == year_month):
                sums[ym] = sums.get(ym, 0) + e.amount

        if not sums:
            print(f"{year_month}에 해당하는 지출이 없습니다.\n")
            return

        print("\n[월별 지출 요약]")
        for ym in sorted(sums.keys()):
            print(f"{ym}: {sums[ym]}원")
        print()



