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

    def convert_currency(self, amount, from_currency, to_currency):
        rates = {
            "USD": 1465,  # 1 USD = 1465원
            "EUR": 1710,  # 1 EUR = 1710원
            "JPY": 9.4,   # 1 JPY = 9.4원
            "KRW": 1
        }

        if from_currency not in rates or to_currency not in rates:
            print("지원하지 않는 통화입니다.\n")
            return None

        # 먼저 KRW 기준으로 계산
        if from_currency == "KRW":
            krw_value = amount
        else:
            krw_value = amount * rates[from_currency]

        # KRW -> 다른 통화
        result = krw_value / rates[to_currency]
        return result
