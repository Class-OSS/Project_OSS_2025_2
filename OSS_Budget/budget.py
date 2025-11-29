import datetime
from expense import Expense

class Budget:
    def __init__(self):
        self.expenses = []
        self.favorites = []

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

    # (추가1) 즐겨찾기 등록
    def register_favorite(self, alias, category, description, amount):
        fav_item = {
            "alias": alias, 
            "category": category,
            "description": description,
            "amount": amount
        }
        self.favorites.append(fav_item)
        print(f"즐겨찾기 '{alias}'이(가) 등록되었습니다.\n")

    # (추가2) 즐겨찾기 목록 보여주기
    def list_favorites(self):
        if not self.favorites:
            print("등록된 즐겨찾기가 없습니다.\n")
            return False
        
        print("\n[고정 지출 즐겨찾기 목록]")
        for idx, fav in enumerate(self.favorites, 1):
            print(f"{idx}. [{fav['alias']}] {fav['category']} - {fav['description']} : {fav['amount']}원")
        print()
        return True

    # (추가3) 즐겨찾기를 실제 지출로 적용
    def apply_favorite(self, index):
        if index < 0 or index >= len(self.favorites):
            print("잘못된 번호입니다.\n")
            return

        fav = self.favorites[index]
        today = datetime.date.today().isoformat()
        new_expense = Expense(today, fav['category'], fav['description'], fav['amount'])
        
        self.expenses.append(new_expense)
        print(f"'{fav['alias']}' 항목이 오늘 지출로 추가되었습니다!\n")


