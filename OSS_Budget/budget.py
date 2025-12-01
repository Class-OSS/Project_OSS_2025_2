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
        
        categories = sorted(set(e.category for e in self.expenses))
        print("---------------------------------------------------------")
        print("[카테고리 목록]")
        for i in categories:
            print(i)
        print("---------------------------------------------------------")

        print("정렬 기준 선택")
        print("1. 카테고리")
        print("2. 금액")
        print("3. 날짜")
        select = input("선택 > ")
        if select not in ("1", "2", "3"):
            print("잘못된 선택.\n")
            return

        order = input("1. 오름차순\n2. 내림차순\n선택 > ").strip().lower()
        if order == "1":
            reverse = False
        elif order == "2":
            reverse = True
        else:
            print("잘못된 선택.\n")
            return
        
        if select == "1":
            keyFunction = self.sortCategory
        elif select == "2":
            keyFunction = self.sortPrice
        elif select == "3":
            keyFunction = self.sortTime
        sortedExpenses = sorted(self.expenses, key=keyFunction, reverse=reverse)
            
        print("\n[지출 목록]")
        for idx, e in enumerate(sortedExpenses, 1):
            print(f"{idx}. {e}")
        print()

    def total_spent(self):
        total = sum(e.amount for e in self.expenses)
        print(f"총 지출: {total}원\n")
        
    def sortCategory(expense):
        return expense.category.lower()
    
    def sortPrice(expense):
        return expense.amount
    
    def sortTime(expense):
        return expense.date