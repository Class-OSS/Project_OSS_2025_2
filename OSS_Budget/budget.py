import datetime
from expense import Expense
from collections import defaultdict 

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
        
    def list_expenses_by_date_range(self, start_date_str, end_date_str):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return
        
        try:
            start_date = datetime.datetime.strptime(start_date_str, "%y%m%d").date()
            end_date = datetime.datetime.strptime(end_date_str, "%y%m%d").date()
        except ValueError:
            print("잘못된 날짜 형식입니다 (yymmdd 형식으로 입력해주세요).\n")
            return

        print(f"\n[지출 목록] 기간: {start_date.isoformat()} ~ {end_date.isoformat()}")
        
        filtered_expenses = []
        for e in self.expenses:
            expense_date = datetime.date.fromisoformat(e.date)
            
            if start_date <= expense_date <= end_date:
                filtered_expenses.append(e)

        if not filtered_expenses:
            print("해당 기간 내 지출 내역이 없습니다.\n")
            return
        
        for idx, e in enumerate(filtered_expenses, 1):
            print(f"{idx}. {e}")
        print()

    def category_summary(self):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return
        
        category_totals = defaultdict(int)
        for e in self.expenses:
            category_totals[e.category] += e.amount
        
        print("\n[카테고리별 총 지출 요약]")
        for category, total in sorted(category_totals.items()):
            print(f"- {category}: {total}원")
        print()
    
    def filter_expenses_by_category(self, category_to_filter):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return
        
        normalized_category = category_to_filter.strip().lower()
        
        filtered_expenses = [
            e for e in self.expenses 
            if e.category.strip().lower() == normalized_category
        ]

        if not filtered_expenses:
            print(f"'{category_to_filter}' 카테고리의 지출 내역이 없습니다.\n")
            return

        print(f"\n[지출 목록] 카테고리: {category_to_filter}")
        for idx, e in enumerate(filtered_expenses, 1):
            print(f"{idx}. {e}")
        
        category_total = sum(e.amount for e in filtered_expenses)
        print("-" * 30)
        print(f"**{category_to_filter} 카테고리 총 지출: {category_total}원**")
        print()
        
    def edit_expense(self, index, date, category, description, amount):
        if 0 <= index < len(self.expenses):
            self.expenses[index].date = date
            self.expenses[index].category = category
            self.expenses[index].description = description
            self.expenses[index].amount = amount
            print("지출 내역이 성공적으로 수정되었습니다.\n")
            return True
        else:
            print("잘못된 지출 번호입니다.\n")
            return False