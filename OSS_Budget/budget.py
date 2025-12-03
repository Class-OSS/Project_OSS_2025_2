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

    def merge_item(self):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return
        
        grouped = defaultdict(int)
        for e in self.expenses:
            grouped[e.category] += e.amount

        print("# 항목별 합계\n")
        for idx, (category, total) in enumerate(grouped.items(), 1):
            print(f"{idx}. {category}: {total}원")
        print()

    def search_expenses(self, keyword):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return
                
        matches = [
            e for e in self.expenses
            if keyword in e.category or keyword in e.description
        ]

        if not matches:
            print(f"'{keyword}' 관련 지출 내역이 없습니다.\n")
            return
        
        print(f"\n# 검색 결과: '{keyword}'")
        for idx, e in enumerate(matches, 1):
            print(f"{idx}. {e}")

        total = sum(e.amount for e in matches)
        print(f"\n검색된 항목 총 지출: {total}원\n")