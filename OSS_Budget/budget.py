import datetime
from expense import Expense

class Budget:
    def __init__(self):
        self.expenses = []
        self.incomes = []   # ⭐ 수입 리스트 추가

    def add_expense(self, date_str, category, description, amount):
        try:
            date_obj = datetime.date.fromisoformat(date_str)
            date = date_obj.isoformat()
        except ValueError:
            print("날짜 형식이 잘못되었습니다. (예: 2024-10-01)\n")
            return

        expense = Expense(date, category, description, amount)
        self.expenses.append(expense)
        print("지출이 추가되었습니다.\n")

    # 수입 입력 기능 함수 
    def add_income(self, date_str, source, amount):
        try:
            date_obj = datetime.date.fromisoformat(date_str)
            date = date_obj.isoformat()
        except ValueError:
            print("날짜 형식이 잘못되었습니다. (예: 2024-10-01)\n")
            return
        
        self.incomes.append({"date": date, "source": source, "amount": amount})
        print("수입이 추가되었습니다.\n")

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
        return total

    # 총 수입 계산 함수
    def total_income(self):
        total = sum(i["amount"] for i in self.incomes)
        print(f"총 수입: {total}원\n")
        return total

    # 재정 상태 계산 함수 (수입 대비 지출 비율)
    def financial_status(self):
        total_in = self.total_income()
        total_ex = self.total_spent()

        if total_in == 0:
            print("수입이 없어 재정 상태를 평가할 수 없습니다.\n")
            return

        ratio = total_ex / total_in

        print("=== 재정 상태 평가 ===")
        print(f"수입 대비 지출 비율: {ratio * 100:.1f}%")

        # 1~5 단계 분류
        if ratio < 0.3:
            level = 1; msg = "아주 건강한 재정 상태입니다!"
        elif ratio < 0.6:
            level = 2; msg = "건전한 수준입니다."
        elif ratio < 0.9:
            level = 3; msg = "보통 수준입니다. 지출 조절이 필요할 수 있습니다."
        elif ratio < 1.2:
            level = 4; msg = "주의 단계입니다. 지출을 줄여야 합니다."
        else:
            level = 5; msg = "위험! 적자 상태입니다!"

        print(f"재정 상태: {level}단계")
        print(msg + "\n")
