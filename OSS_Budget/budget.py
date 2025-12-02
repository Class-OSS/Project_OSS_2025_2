import datetime
from expense import Expense
from collections import defaultdict

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
   def print_category_summary(records):
    """
    Print income/expense summary by category.
    amount > 0 → income
    amount < 0 → expense
    """
    income_by_cat = defaultdict(float)
    expense_by_cat = defaultdict(float)

    for r in records:
        category = r['category']
        amount = float(r['amount'])

        if amount > 0:
            income_by_cat[category] += amount
        elif amount < 0:
            expense_by_cat[category] += -amount

    print("=" * 40)
    print("카테고리별 수입/지출 요약")
    print("-" * 40)
    print(f"{'카테고리':<15}{'수입 합계':>10}{'지출 합계':>10}{'순이익':>10}")
    print("-" * 40)

    all_categories = set(income_by_cat.keys()) | set(expense_by_cat.keys())

    for cat in sorted(all_categories):
        total_income = income_by_cat.get(cat, 0.0)
        total_expense = expense_by_cat.get(cat, 0.0)
        net = total_income - total_expense
        print(f"{cat:<15}{total_income:>10.0f}{total_expense:>10.0f}{net:>10.0f}")

    print("=" * 40)
def menu_category_summary():
    records = load_records()
    if not records:
        print("저장된 내역이 없습니다.")
        return
     category = input("조회할 카테고리를 입력하세요: ")
        list_expenses_by_category(records, category)
        print_category_summary(records)
def list_expenses_by_category(records, category):
    found = False
    print(f"\n[{category} 카테고리 지출 내역]")
    for r in records:
        if r['category'] == category:
            print(f"- {r['date']} / {r['description']} / {r['amount']}원")
            found = True

    if not found:
        print("해당 카테고리 지출 내역이 없습니다.\n")
    else:
        print()

def main():
    while True:
        print("1. 내역 추가")
        print("2. 내역 조회")
        print("3. 파일 저장")
        print("4. 종료")
        print("5. 카테고리별 수입/지출 요약 보기")
        print("6. 특정 카테고리 지출 내역 조회")
        
        choice = input("메뉴를 선택하세요: ")

        if choice == "1":
            add_record()
        elif choice == "2":
            list_records()
        elif choice == "3":
            save_records()
        elif choice == "4":
            break
        elif choice == "5":
            menu_category_summary()
        elif choice == "6":
            menu_list_by_category()



