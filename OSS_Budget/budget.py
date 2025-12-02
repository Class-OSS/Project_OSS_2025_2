import datetime
from expense import Expense, Income

class Budget:
    def __init__(self):
        self.expenses = []
        self.incomes = []


    def add_income(self, source, amount, month=None):
        if month is None:
            month = datetime.date.today().month
        
        month = str(month).zfill(2)

        income = Income(month, source, amount)
        self.incomes.append(income)
        print("수입이 추가되었습니다.\n")

    # 수입 내역을 월별로 합산하여 출력하는 함수
    def list_incomes(self):
        if not self.incomes:
            print("수입 내역이 없습니다.\n")
            return
        # 월별 합계 계산
        month_incomes_sum = {}
        for i in self.incomes:
            if i.month not in month_incomes_sum:
                month_incomes_sum[i.month] = 0
            month_incomes_sum[i.month] += i.amount

        print("\n[월별 수입 현황]")
        for month, total in sorted(month_incomes_sum.items()):
            print(f"[{month}월] 총 수입: {total}원")
        print()

    def add_expense(self, category, description, amount, month=None):
        if month is None:
            month = datetime.date.today().month
        
        month = str(month).zfill(2)

        expense = Expense(month, category, description, amount)
        self.expenses.append(expense)
        print("지출이 추가되었습니다.\n")

    def list_expenses(self):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return
        sorted_expenses = sorted(self.expenses, key=lambda x: x.month)

        print("\n[지출 목록 (월별 정렬)]")
        for idx, e in enumerate(sorted_expenses, 1):
            print(f"{idx}. {e}")
        print()

    def show_month_stats(self, month):
        target_month = str(month).zfill(2)
    
        print(f"\n[{target_month}월 수입 내역]")
        month_incomes_total = 0
        income_found = False
        
        for i in self.incomes:
            if i.month == target_month:
                print(i) 
                month_incomes_total += i.amount
                income_found = True
 
        if not income_found:
            print("해당 월의 수입 내역이 없습니다.")

        print(f"\n[{target_month}월 지출 내역]")
        month_expense_total = 0
        expense_found = False
        for e in self.expenses:
            if e.month == target_month:
                print(e)
                month_expense_total += e.amount
                expense_found = True
        if not expense_found:
            print("해당 월의 지출 내역이 없습니다.")

        print("-" * 30)
        print(f"{target_month}월 총 수입: {month_incomes_total}원")
        print(f"{target_month}월 총 지출: {month_expense_total}원")
        print(f"{target_month}월 잔액: {month_incomes_total - month_expense_total}원\n")

    def show_top_category(self):
        if not self.expenses:
            print("분석할 지출 데이터가 없습니다.\n")
            return

        category_totals = {}
        for e in self.expenses:
            if e.category in category_totals:
                category_totals[e.category] += e.amount
            else:
                category_totals[e.category] = e.amount
        
        top_category = max(category_totals, key=category_totals.get)
        top_amount = category_totals[top_category]
        
        print(f"\n[지출 분석]")
        print(f"가장 돈을 많이 쓴 곳은 '{top_category}' 입니다.")
        print(f"금액: {top_amount}원\n")