import datetime
from expense import Expense
import matplotlib.pyplot as plt
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

    def budgetViz(self):  # 가계부 내역 시각화
        if not self.expenses:
            print("내역이 존재하지 않습니다.")
            return
        category_sums = defaultdict(int)
        for e in self.expenses:
            category_sums[e.category] += e.amount

        categories = list(category_sums.keys())
        amounts = list(category_sums.values())
    
        plt.figure(figsize=(10, 10))
        plt.pie(
            amounts,
            labels=categories,
            autopct='%1.1f%%',
            startangle=90,
            wedgeprops={'edgecolor': 'black', 'linewidth': 1, 'antialiased': True}
        )
        plt.title("지출 내역 파이그래프") #한글이 깨질 수 있음
        plt.axis('equal')
        plt.show()
    
    def total_spent(self):
        total = sum(e.amount for e in self.expenses)
        print(f"총 지출: {total}원\n")


