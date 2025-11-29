from collections import defaultdict
from datetime import datetime
import datetime
from expense import Expense


class Budget:
    def __init__(self):
        self.expenses = []

    def add_expense(self, category, description, amount):
        today = datetime.date.today().isoformat()  # "YYYY-MM-DD"
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

    # ================================
    #   카테고리별 지출 Top3 기능 추가
    # ================================
    def get_monthly_category_top3(self, year=None, month=None):
        """
        이번 달 또는 지정된 연/월 기준으로
        카테고리별 지출 합계를 계산하여
        Top3와 총 지출액을 반환한다.
        """

        # 기본값: 오늘 날짜
        if year is None or month is None:
            today = datetime.date.today()
            year = today.year
            month = today.month

        category_totals = defaultdict(int)

        for e in self.expenses:
            # 날짜 파싱
            try:
                d = datetime.datetime.strptime(e.date, "%Y-%m-%d").date()
            except Exception:
                continue

            # 해당 월만 집계
            if d.year != year or d.month != month:
                continue

            # amount는 지출(+) 기준 → 양수 그대로 더함
            spend = e.amount if e.amount > 0 else -e.amount

            category_totals[e.category] += spend

        # 지출 내역 없음
        if not category_totals:
            return [], 0

        # 내림차순 정렬
        sorted_items = sorted(
            category_totals.items(),
            key=lambda x: x[1],
            reverse=True
        )

        # 상위 3개
        top3 = sorted_items[:3]
        total = sum(category_totals.values())

        return top3, total
