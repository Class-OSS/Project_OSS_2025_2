import datetime
from expense import Expense

class Budget:
    def __init__(self):
        self.expenses = []

    def add_expense(self, category, description, amount, mood):
        today = datetime.date.today().isoformat()
        expense = Expense(today, category, description, amount, mood)
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

    def analyze_by_mood(self):
        if not self.expenses:
            print("지출 내역이 없어 분석할 수 없습니다.\n")
            return

        mood_stats = {}

        for e in self.expenses:
            if e.mood not in mood_stats:
                mood_stats[e.mood] = 0
            mood_stats[e.mood] += e.amount

        print("\n[감정 기반 지출 분석]")
        for mood, total in mood_stats.items():
            print(f"- {mood} 상태에서 지출한 금액: {total}원")
        print()
