from collections import defaultdict

class BudgetStats:
    def __init__(self, expenses):
        self.expenses = expenses

    def monthly_category_summary(self):
        if not self.expenses:
            print("지출 내역이 없어 통계를 표시할 수 없습니다.\n")
            return

        summary = defaultdict(lambda: defaultdict(int))

        for e in self.expenses:
            month = e.date[:7]  # YYYY-MM (연도-월)
            summary[month][e.category] += e.amount

        print("\n===== 월별 카테고리별 지출 통계 =====\n")
        for month, categories in summary.items():
            print(f"[{month}]")
            for cat, total in categories.items():
                print(f"  - {cat}: {total}원")
            print()
