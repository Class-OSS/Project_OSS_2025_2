import datetime
from expense import Expense

class Budget:
    def __init__(self):
        self.expenses = []

    def add_expense(self, category, description, amount, date = None):
        if date is None:
            date = datetime.date.today().isoformat()
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

    def total_spent(self, year_month = None):
        if year_month:
            expenses, total = self.get_monthly_expenses(year_month)
            print(f"\n{year_month} 총 지출: {total:,}원\n")
        else:
            total = sum(e.amount for e in self.expenses)
            print(f"\n총 지출: {total:,}원\n")

    def get_monthly_expenses(self, year_month):
        start_date = f"{year_month}-01"
        year, month = map(int, year_month.split('-'))

        if month == 12:
            next_month = datetime.date(year + 1, 1, 1)
        else:
            next_month = datetime.date(year, month + 1, 1)
        end_date = (next_month - datetime.timedelta(days=1)).isoformat()

        monthly_expenses = [e for e in self.expenses if start_date <= e.date <= end_date]
        return monthly_expenses, sum(e.amount for e in monthly_expenses)

    def compare_two_months(self, month1, month2):
        expenses1, total1 = self.get_monthly_expenses(month1)

        expenses2, total2 = self.get_monthly_expenses(month2)

        print(f"\n{'=' * 50}")
        print(f"월별/카테고리별 지출 비교")
        print(f"{'=' * 50}")
        print(f"\n * {month1}")
        print(f"   총 지출: {total1:,}원")
        print(f"   지출 건수: {len(expenses1)}건")

        print(f"\n * {month2}")
        print(f"   총 지출: {total2:,}원")
        print(f"   지출 건수: {len(expenses2)}건")

        print(f"\n{'=' * 50}")

        diff = total2 - total1

        if diff > 0:
            percent = (diff / total1 * 100) if total1 > 0 else 0
            print(f"{month2}월 에 {diff:,}원 더 많이 지출했습니다. (+{percent:.1f}%)")
        elif diff < 0:
            percent = (abs(diff) / total1 * 100) if total1 > 0 else 0
            print(f"{month2}월 에 {abs(diff):,}원 덜 지출했습니다. (-{percent:.1f}%)")
        else:
            print(f"두 달의 지출이 동일합니다.")

        print(f"{'=' * 50}\n")

        if expenses1 or expenses2:
            self._compare_categories(month1, expenses1, month2, expenses2)

    def _compare_categories(self, month1, month1_expenses, month2, month2_expenses):
        month1_by_category = {}
        for e in month1_expenses:
            month1_by_category[e.category] = month1_by_category.get(e.category, 0) + e.amount

        month2_by_category = {}
        for e in month2_expenses:
            month2_by_category[e.category] = month2_by_category.get(e.category, 0) + e.amount

        all_categories = set(month1_by_category.keys()) | set(month2_by_category.keys())

        if all_categories:
            print(f"카테고리별 비교")
            print(f"{'-' * 50}")
            print(f"{'카테고리':<15} {month1:<15} {month2:<15}")
            print(f"{'-' * 50}")

            for category in sorted(all_categories):
                month1_amt = month1_by_category.get(category, 0)
                month2_amt = month2_by_category.get(category, 0)
                print(f"{category:<15} {month1_amt:>12,}원  {month2_amt:>12,}원")

            print(f"{'-' * 50}\n")


