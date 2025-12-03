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
        
    # --- [PR 1차 추가 기능 시작] ---
    def summarize_by_category(self):
        """
        현재 저장된 모든 지출 내역을 카테고리별로 집계하여 총액을 출력합니다.
        """
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return

        category_summary = {}
        for expense in self.expenses:
            category = expense.category
            amount = expense.amount
            
            # 딕셔너리에 카테고리별 금액을 누적
            category_summary[category] = category_summary.get(category, 0) + amount

        print("\n[카테고리별 총 지출]")
        
        # 결과를 금액이 큰 순서대로 정렬하여 출력
        sorted_summary = sorted(category_summary.items(), key=lambda item: item[1], reverse=True)
        
        for category, total in sorted_summary:
            print(f" - {category}: {total}원")
            
        print("-" * 20)
        self.total_spent() # 기존 총 지출 메서드 호출로 전체 합계도 출력
    # --- [PR 1차 추가 기능 끝] ---
