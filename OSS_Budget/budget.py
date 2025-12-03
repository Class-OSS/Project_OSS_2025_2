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

    def analyze_expenses(self):
        if not self.expenses:
            print("아직 등록된 지출이 없습니다.\n")
            return

        record_count = len(self.expenses)
        total_amount = sum(item.amount for item in self.expenses)
        average_amount = total_amount / record_count 

        ranked_list = sorted(
            self.expenses,
            key=lambda item: item.amount,
            reverse=True
        )
        top_limit = 3 if record_count >= 3 else record_count
        top3 = ranked_list[:top_limit]

        print("\n==== 지출 분석 결과 ====")
        print(f"전체 지출 수: {record_count}건")
        print(f"전체 지출 금액: {total_amount}원")
        print(f"평균 지출 금액: {average_amount:.1f}원\n")

        print("[가장 많은 지출 TOP 3]")
        for idx, item in enumerate(top3, start=1):
            print(f"{idx}. {item.category} - {item.description} : {item.amount}원")
        print()