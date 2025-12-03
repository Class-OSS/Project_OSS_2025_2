import datetime
from expense import Expense
import json # json 모듈 추가

GOAL_FILE = "monthly_goal.json" # 목표 파일 이름 상수 정의

class Budget:
    def __init__(self):
        self.expenses = []
        self.monthly_goal = {} # 목표 저장 변수 추가
        # 지출 내역을 파일에서 불러오는 로직이 원래 없으므로, 목표만 로드
        self.load_goal() 

    # 목표를 파일에서 불러오기
    def load_goal(self):
        try:
            with open(GOAL_FILE, 'r') as f:
                self.monthly_goal = json.load(f)
        except FileNotFoundError:
            self.monthly_goal = {}
        except json.JSONDecodeError:
            self.monthly_goal = {}

    # 목표를 파일에 저장하기
    def save_goal(self):
        with open(GOAL_FILE, 'w') as f:
            json.dump(self.monthly_goal, f, indent=4)
        print("목표가 저장되었습니다.")

    # 월별 목표 설정 함수
    def set_goal(self, year_month, amount):
        self.monthly_goal[year_month] = amount
        self.save_goal()
        print(f"[{year_month}] 목표 금액 {amount}원이 설정되었습니다.\n")

    # 월별 목표 현황 계산 함수
    def get_monthly_goal_status(self):
        # 현재 날짜 (YYYY-MM 형식)
        today = datetime.date.today()
        year_month = today.strftime("%Y-%m")
        
        # 1. 목표 금액 확인
        goal_amount = self.monthly_goal.get(year_month, 0)
        
        # 2. 현재 월의 지출 총합 계산
        current_month_spent = 0
        for e in self.expenses:
            # Expense 객체의 date 형식: YYYY-MM-DD
            if e.date.startswith(year_month):
                current_month_spent += e.amount
                
        # 3. 퍼센트 계산
        percentage = 0
        if goal_amount > 0:
            percentage = (current_month_spent / goal_amount) * 100

        return year_month, goal_amount, current_month_spent, percentage

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