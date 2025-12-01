import datetime
from expense import Expense

class Budget:
    def __init__(self):
        self.expenses = []

    def add_expense(self, category, description, amount):
        today = datetime.date.today().isoformat()  # YYYY-MM-DD
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

    # 1) 요일별 지출 패턴 분석 기능
    def analyze_weekday_spending(self):
        if not self.expenses:
            print("지출 기록이 없습니다.\n")
            return

        weekday_sum = [0] * 7  # 월=0, ..., 일=6

        for e in self.expenses:
            date_str = e.date
            amount = e.amount

            try:
                date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
            except:
                print(f"날짜 형식 오류: {date_str}")
                continue

            weekday = date.weekday()
            weekday_sum[weekday] += amount

        weekday_names = ["월", "화", "수", "목", "금", "토", "일"]

        print("\n[요일별 지출 패턴 분석]")
        for i in range(7):
            print(f"{weekday_names[i]}요일: {weekday_sum[i]}원")

        max_spend = max(weekday_sum)
        max_day = weekday_names[weekday_sum.index(max_spend)]
        print(f"\n가장 많이 쓴 요일: {max_day}요일 ({max_spend}원)\n")

    # 2) 연속 소비일 분석 기능
    def analyze_spending_streak(self):
        if not self.expenses:
            print("지출 기록이 없습니다.\n")
            return

        # 날짜만 모아 정렬
        dates = sorted({e.date for e in self.expenses})

        streak = 1
        max_streak = 1

        prev_date = datetime.datetime.strptime(dates[0], "%Y-%m-%d").date()

        for i in range(1, len(dates)):
            current_date = datetime.datetime.strptime(dates[i], "%Y-%m-%d").date()

            # 하루 차이면 streak 증가
            if (current_date - prev_date).days == 1:
                streak += 1
            else:
                streak = 1  # 끊기면 초기화

            max_streak = max(max_streak, streak)
            prev_date = current_date

        print("\n[연속 소비일 분석(Streak)]")
        print(f"최대 연속 소비일: {max_streak}일\n")
