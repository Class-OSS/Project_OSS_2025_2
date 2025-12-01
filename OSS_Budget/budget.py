import datetime
from expense import Expense

class Budget:
    def __init__(self):
        self.expenses = []

    # day 변수 추가.
    def add_expense(self, category, description, amount, day):
        # day 키 추가.
        expense = { 'category': category,  'description': description, 'amount': amount, 'day': day}
        self.expenses.append(expense)
        print(f"지출이 추가되었습니다: {description} ({amount}원) - {day}요일\n")

    def list_expenses(self):
        print("\n[ 전체 지출 목록 ]")
        for expense in self.expenses:
            # 출력 시 요일 정보도 함께 표시
            print(f"[{expense['day']}] {expense['category']}: {expense['description']} ({expense['amount']}원)")
        print()

    def total_spent(self):
        total = sum(expense['amount'] for expense in self.expenses)
        print(f"총 지출: {total}원\n")

    # 요일별 지출 보기 함수 추가
    def view_by_day(self, day):
        print(f"\n[ {day}요일 지출 내역 ]")
        daily_total = 0
        count = 0
        for expense in self.expenses:
            if expense['day'] == day:
                print(f"카테고리: {expense['category']}, 내용: {expense['description']}, 금액: {expense['amount']}원")
                daily_total += expense['amount']
                count += 1
        
        if count == 0:
            print("해당 요일의 지출 내역이 없습니다.")
        else:
            print(f"-> {day}요일 총 지출: {daily_total}원")
        print()
