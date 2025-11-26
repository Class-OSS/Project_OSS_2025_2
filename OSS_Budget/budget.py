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

    # 반환값에 카테고리별 총액(category_totals)을 추가
    def get_category_ratio(self):
        if not self.expenses:
            return "지출 내역이 없어 비율을 계산할 수 없습니다."

        # 1. 총 지출 금액 계산
        total_spent = sum(e.amount for e in self.expenses)
        if total_spent == 0:
            return "총 지출 금액이 0원입니다."

        # 2. 카테고리별 지출 총액 집계 (총액을 저장)
        category_totals = {}
        for expense in self.expenses:
            category = expense.category
            amount = expense.amount
            category_totals[category] = category_totals.get(category, 0) + amount

        # 3. 카테고리별 비율 계산
        ratios = {}
        for category, total in category_totals.items():
            # 비율은 소수점 두 자리까지 반올림하여 출력용으로 사용
            ratio = round((total / total_spent) * 100, 2) 
            ratios[category] = ratio

        # ratios, total_spent, category_totals 세 가지를 반환
        return ratios, total_spent, category_totals
