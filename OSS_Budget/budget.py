import datetime
import budget

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
    
    # 카테고리별 지출 합 계산함수
    def get_month_category_sum(self, year, month):
        result = {}
        for e in self.expenses:
            e_year, e_month, _ = map(int, e.date.split("-"))
            if e_year == year and e_month == month:
                result[e.category] = result.get(e.category, 0) + e.amount
        return result
    
    #  전달 대비 이번달의 지출변화율 % 계산함수

    def compare_last_month(self):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return
        today = datetime.date.today()
        this_year = today.year
        this_month = today.month

    # 전달 계산
        if this_month == 1:
            last_year = this_year - 1
            last_month = 12
        else:
            last_year = this_year
            last_month = this_month - 1

    # 카테고리별 합계
        this_month_sum = self.get_month_category_sum(this_year, this_month)
        last_month_sum = self.get_month_category_sum(last_year, last_month)

        print("\n[카테고리별 전달 대비 이번달 변화율]\n")

    # 모든 카테고리 목록 합치기
        categories = set(this_month_sum.keys()) | set(last_month_sum.keys())

        for cat in categories:
            last_val = last_month_sum.get(cat, 0)
            this_val = this_month_sum.get(cat, 0)

            if last_val == 0 and this_val == 0:
                print(f"{cat}: 변화 없음 (0원)")
            elif last_val == 0:
                print(f"{cat}: 전달 0원 → 이번달 {this_val}원 (신규 지출)")
            else:
                rate = ((this_val - last_val) / last_val) * 100
                sign = "+" if rate >= 0 else ""
                print(f"{cat}: {sign}{rate:.1f}%")
        print()


