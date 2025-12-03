import datetime
from expense import Expense

class Budget:
    def __init__(self):
        self.expenses = []
        self.budgets = {} # <--- PR 3차 추가: 예산 설정을 위한 딕셔너리 추가

    def add_expense(self, category, description, amount):
        today = datetime.date.today().isoformat()
        expense = Expense(today, category, description, amount)
        self.expenses.append(expense)
        print("지출이 추가되었습니다.\n")
        # 추가: 지출 추가 시 예산 초과 여부를 바로 확인
        self.check_budget_status(single_category=category) 

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
        
    def summarize_by_category(self):
        # PR 1차 기능 (PR 3차 제출 시 이 코드가 main 브랜치에 있다고 가정하고 작성)
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return

        category_summary = {}
        for expense in self.expenses:
            category = expense.category
            amount = expense.amount
            category_summary[category] = category_summary.get(category, 0) + amount

        print("\n[카테고리별 총 지출]")
        sorted_summary = sorted(category_summary.items(), key=lambda item: item[1], reverse=True)
        
        for category, total in sorted_summary:
            print(f" - {category}: {total}원")
            
        print("-" * 20)
        self.total_spent()
        
    # --- [PR 3차 추가 기능 시작] ---
    def set_category_budget(self):
        """사용자 입력으로 특정 카테고리에 예산을 설정합니다."""
        category = input("예산을 설정할 카테고리: ")
        try:
            amount = int(input(f"[{category}] 예산 금액 설정(원): "))
            if amount <= 0:
                print("[오류] 예산은 0보다 커야 합니다.")
                return
            self.budgets[category] = amount
            print(f"\n[성공] [{category}] 예산이 {amount}원으로 설정되었습니다.")
        except ValueError:
            print("[오류] 금액이 올바르지 않습니다.")
        
    def check_budget_status(self, single_category=None):
        """현재 지출을 기반으로 예산 초과 상태를 확인하고 경고합니다."""
        if not self.budgets:
            if not single_category:
                 print("\n[알림] 설정된 예산이 없습니다. 먼저 예산을 설정하세요.")
            return

        # 1. 카테고리별 현재 지출 합산 (PR 1차 기능 로직 재활용)
        current_spent = {}
        categories_to_check = self.budgets.keys()
        
        # 특정 카테고리만 확인하는 경우
        if single_category and single_category not in categories_to_check:
             # 설정되지 않은 카테고리는 검사하지 않음
             return
        
        # 전체 지출을 순회하여 합산
        for expense in self.expenses:
            category = expense.category
            if category in categories_to_check:
                 current_spent[category] = current_spent.get(category, 0) + expense.amount
        
        # 2. 예산과 비교하여 상태 출력
        print("\n--- 카테고리별 예산 상태 ---")
        
        for category, limit in self.budgets.items():
            if single_category and category != single_category:
                continue # 특정 카테고리만 검사
                
            spent = current_spent.get(category, 0)
            
            if spent > limit:
                # 예산 초과 경고
                print(f"[ 초과] {category}: {spent}원 / 예산 {limit}원 ({- (limit - spent)}원 초과)")
            elif spent > limit * 0.8:
                # 임박 경고 (80% 이상 사용)
                print(f"[ 경고] {category}: {spent}원 / 예산 {limit}원 (잔액: {limit - spent}원 남음)")
            else:
                print(f"[정상] {category}: {spent}원 / 예산 {limit}원 (잔액: {limit - spent}원 남음)")
        print("----------------------------\n")
    # --- [PR 3차 추가 기능 끝] ---

