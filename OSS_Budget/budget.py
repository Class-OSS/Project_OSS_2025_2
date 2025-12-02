from expense import Expense

class Budget:
    def __init__(self):
        self.expenses = []

    # -----------------------------
    # 지출 추가
    # -----------------------------
    def add_expense(self):
        print("\n[지출 추가]")
        name = input("지출명: ")
        amount = int(input("금액: "))
        category = input("카테고리: ")

        expense = Expense(name, amount, category)
        self.expenses.append(expense)

        print("지출이 추가되었습니다.\n")

    # -----------------------------
    # 지출 목록 출력
    # -----------------------------
    def show_expenses(self):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return

        print("\n[지출 목록]")
        for idx, e in enumerate(self.expenses, 1):
            print(f"{idx}. {e}")
        print()

    # -----------------------------
    # 월별 요약 기능 (PR1 기능 - 그대로 유지)
    # -----------------------------
    def monthly_summary(self):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return

        total = sum(e.amount for e in self.expenses)
        print(f"\n이번 달 총 지출: {total}원\n")

    # -----------------------------
    # PR2 신규 기능: 카테고리별 소비 비율 계산
    # -----------------------------
    def category_summary(self):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return

        print("\n[카테고리별 소비 비율]")

        total = sum(e.amount for e in self.expenses)
        categories = {}

        for e in self.expenses:
            categories[e.category] = categories.get(e.category, 0) + e.amount

        for category, amount in categories.items():
            ratio = (amount / total) * 100
            print(f"- {category}: {ratio:.2f}% ({amount}원)")

        print()

