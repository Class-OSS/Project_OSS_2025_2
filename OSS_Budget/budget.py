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

    # 가장 많이 지출한 카테고리를 출력하는 메서드
    def get_max_category(self):
        """
        현재 저장된 지출 목록(self.expenses)에서
        가장 많이 지출한 카테고리를 찾아 출력합니다.
        """
        result = max_category_from_list(self.expenses)
        if result is None:
            print("지출 내역이 없습니다.\n")
        else:
            print(f"가장 많이 지출한 카테고리: {result}\n")


# --------- 클래스 밖에 존재하는 유틸 함수 ---------
def max_category_from_list(expense_list):
    """
    지출 리스트에서 카테고리별 총합을 계산하여
    가장 많이 사용한 카테고리를 반환합니다.
    - expense_list: Budget.expenses 리스트 구조에 맞춘 데이터
    """

    if not expense_list:
        return None

    category_sum = {}

    # 카테고리별 금액 합산
    for e in expense_list:
        category_sum[e.category] = category_sum.get(e.category, 0) + e.amount

    # 가장 금액이 높은 카테고리 반환
    return max(category_sum, key=category_sum.get)