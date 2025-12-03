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
        
    def category_stats(self):
        if not self.expenses:
            print("지출 기록이 없습니다.\n")
            return
        from collections import defaultdict
        stats = defaultdict(int)
        
        for e in self.expenses:
            stats[e.category] += e.amount
            
            print("\n[카테고리별 지출]")
            for cat, amount in stats.items():
                print(f"- {cat}: {amount}원")
                print()
                
    def month_top_categories(self, ym, top_n=3):
        month_expenses = [e for e in self.expenses if e.date.startswith(ym)]
        if not month_expenses:
            print(f"{ym}월 지출 기록이 없습니다.\n")
            return
        
        from collections import defaultdict
        stats = defaultdict(int)
        for e in month_expenses:
            stats[e.category] += e.amount
            
            sorted_stats = sorted(stats.items(), key=lambda x: x[1], reverse=True)
            
            print(f"\n[{ym}월 주요 지출 카테고리]")
            total = sum(stats.values())
            print(f"총 지출: {total}원")
            for i, (cat, amount) in enumerate(sorted_stats[:top_n], 1):
                print(f"{i}. {cat}: {amount}원")
                print()
                
    def month_avg_and_budget(self, ym, budget_amount=None):
        month_expenses = [e for e in self.expenses if e.date.startswith(ym)]
        if not month_expenses:
            print(f"{ym}월 지출 기록이 없습니다.\n")
            return
        
        total = sum(e.amount for e in month_expenses)
        avg = total / len(month_expenses)
        
        print(f"\n[{ym}월 지출 통계]")
        print(f"- 총 지출: {total}원")
        print(f"- 지출 건수: {len(month_expenses)}건")
        print(f"- 평균 지출: {avg:.2f}원")
        
        if budget_amount is not None:
            ratio = total / budget_amount * 100
            print(f"- 예산 대비 사용률: {ratio:.2f}% (예산: {budget_amount}원)")
            print()








