import datetime
from expense import Expense

class Budget:
    def __init__(self):
        self.expenses = []
        self.fixed_expenses = []

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

    def add_fixed_expense(self, category, description, amount, day_of_month):
        new_fixed = {
            "category": category,
            "description": description,
            "amount": amount,
            "day": day_of_month,
            "active": True
        }
        self.fixed_expenses.append(new_fixed)
        print("고정 지출이 등록되었습니다.\n")

    def list_fixed_expenses(self):
        if not self.fixed_expenses:
            print("등록된 고정 지출이 없습니다.\n")
            return

        print("\n==== 고정 지출 목록 ====")
        for idx, f in enumerate(self.fixed_expenses, 1):
            status = "활성" if f["active"] else "비활성"
            print(f"{idx}. [매달 {f['day']}일] {f['category']} - {f['description']}: {f['amount']}원 ({status})")
        print()

    def toggle_fixed_expense(self, index):
        if 0 <= index < len(self.fixed_expenses):
            f = self.fixed_expenses[index]
            f["active"] = not f["active"]
            status = "활성화" if f["active"] else "비활성화"
            print(f"'{f['description']}'이(가) {status}되었습니다.\n")
        else:
            print("잘못된 번호입니다.\n")

