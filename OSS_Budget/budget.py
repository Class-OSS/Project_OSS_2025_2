import datetime
from expense import Expense

class Budget:
    def __init__(self):
        self.list = []
        self.limit = 50000

    def add_expense(self, cat, desc, money):
        today = datetime.date.today().isoformat()
        item = Expense(today, cat, desc, money)
        self.list.append(item)
        print("지출이 추가되었습니다.\n")

        used = self.month_total()
        left = self.limit - used

        print(f"이번 달 총 지출: {used}원")
        if left >= 0:
            print(f"남은 용돈: {left}원 (목표: {self.limit}원)\n")
        else:
            print(f"용돈 {self.limit}원을 {abs(left)}원 초과했습니다!\n")

    def month_total(self):
        if not self.list:
            return 0
        ym = datetime.date.today().isoformat()[:7]

        total = 0
        for x in self.list:
            if x.date.startswith(ym):
                total += x.amount

        return total

    def list_expenses(self):
        if not self.list:
            print("지출 내역이 없습니다.\n")
            return
        print("\n[지출 목록]")
        for i, x in enumerate(self.list, 1):
            print(f"{i}. {x}")
        print()

    def total_spent(self):
        total = 0
        for x in self.list:
            total += x.amount
        print(f"총 지출: {total}원\n")
