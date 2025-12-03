import datetime
import random
from expense import Expense

class Budget:
    def __init__(self):
        self.expenses = []

    def add_expense(self, category, description, amount):
        expense = { 'category': category, 'description': description, 'amount': amount}
        self.expenses.append(expense)
        print(f"지출이 추가되었습니다: {description} ({amount}원)\n")

    def list_expenses(self):
        print("\n[ 전체 지출 목록 ]")
        for expense in self.expenses:
            print(f"카테고리: {expense['category']}, 내용: {expense['description']}, 금액: {expense['amount']}원")
        print()

    def total_spent(self):
        total = sum(expense['amount'] for expense in self.expenses)
        print(f"\n총 지출: {total}원\n")

    # 기능: 랜덤 메뉴 추천 추가
    def recommend_bab(self):
        # '식비' 카테고리만 리스트로 저장
        food_descriptions = [
            expense['description']
            for expense in self.expenses
            if expense['category'] == '식비'
        ]
        
        print("\n[ 오늘의 랜덤 메뉴 추천 ]")

        if not food_descriptions:
            print("저장된 '식비' 지출 내역이 없습니다. (1번 메뉴에서 식비로 지출을 추가해 주세요)")
            return

        # 무작위로 '식비' 카테고리 중 설치
        recommended_menu = random.choice(food_descriptions)

        # 3. 결과 출력
        print(f"오늘의 추천 메뉴는 '{recommended_menu}' 입니다! ")
        print()
