# -*- coding: cp949 -*-

from collections import defaultdict
from expense import Expense


def print_monthly_summary(expenses):
    """
    지출 내역을 월(YYYY-MM) 단위로 묶어서 총 지출을 출력합니다.
    """
    if not expenses:
        print("지출 내역이 없습니다.\n")
        return

    monthly_totals = defaultdict(int)

    for e in expenses:
        month = e.date[:7]
        monthly_totals[month] += e.amount

    print("\n[월별 지출 통계]")
    for month in sorted(monthly_totals.keys()):
        total = monthly_totals[month]
        print(f"{month}: {total}원")
    print()


def print_category_summary(expenses):
    """
    지출 내역을 카테고리별로 묶어서 총 지출을 출력합니다.
    """
    if not expenses:
        print("지출 내역이 없습니다.\n")
        return

    category_totals = defaultdict(int)

    for e in expenses:
        category_totals[e.category] += e.amount

    print("\n[카테고리별 지출 통계]")
    for category, total in category_totals.items():
        print(f"{category}: {total}원")
    print()
