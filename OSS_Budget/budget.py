import datetime
from expense import Expense

class Budget:
    def __init__(self):
        self.expenses = []
        self.income_total = 0           # 총 수입 누적
        self.savings_rate = 20          # 기본 저축 20%
        self.fixed_savings_rate = 10     # 기본 적금 10%
        print("스마트 가계부 시작!")
        print(f"수입 들어올 때마다 자동으로 저축 {self.savings_rate}%, 적금 {self.fixed_savings_rate}% 분류됩니다.\n")

    def add_expense(self, category, description, amount):
        today = datetime.date.today().isoformat()
        expense = Expense(today, category, description, amount)
        self.expenses.append(expense)
        print("지출이 추가되었습니다.\n")

    def add_income(self, amount):
        try:
            amount = int(amount)
            if amount <= 0:
                print("수입은 0보다 커야 합니다.\n")
                return

            self.income_total += amount
            savings = int(amount * self.savings_rate / 100)
            fixed = int(amount * self.fixed_savings_rate / 100)
            remain = amount - savings - fixed

            today = datetime.date.today().isoformat()
            if savings > 0:
                self.expenses.append(Expense(today, "저축", "자동 저축", savings))
            if fixed > 0:
                self.expenses.append(Expense(today, "적금", "자동 적금", fixed))

            print(f"수입 {amount:,}원 입금 완료!")
            print(f"   ├─ 저축: {savings:,}원 ({self.savings_rate}%)")
            print(f"   ├─ 적금: {fixed:,}원 ({self.fixed_savings_rate}%)")
            print(f"   └─ 실질 사용 가능 금액: {remain:,}원\n")

        except ValueError:
            print("숫자를 제대로 입력해주세요!\n")

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
        print(f"총 지출: {total:,}원\n")

    # 핵심: 잔고 보기
    def show_balance(self):
        total_spent = sum(e.amount for e in self.expenses)
        balance = self.income_total - total_spent
        print("\n" + "═" * 45)
        print(f"     총 수입:       {self.income_total:,}원")
        print(f"     총 지출:       {total_spent:,}원")
        print(f"─" * 45)
        print(f"     실질 잔고:     {balance:,}원 ")
        print("═" * 45 + "\n")

    # 비율 설정
    def set_savings_rate(self):
        print(f"현재 저축 비율: {self.savings_rate}%")
        try:
            new = int(input("새 저축 비율 (%): "))
            if 0 <= new <= 100:
                self.savings_rate = new
                print(f"저축 비율이 {new}%로 변경되었습니다!\n")
            else:
                print("0~100 사이로 입력해주세요!\n")
        except:
            print("숫자만 입력해주세요!\n")

    def set_fixed_savings_rate(self):
        print(f"현재 적금 비율: {self.fixed_savings_rate}%")
        try:
            new = int(input("새 적금 비율 (%): "))
            if 0 <= new <= 100:
                self.fixed_savings_rate = new
                print(f"적금 비율이 {new}%로 변경되었습니다!\n")
            else:
                print("0~100 사이로 입력해주세요!\n")
        except:
            print("숫자만 입력해주세요!\n")