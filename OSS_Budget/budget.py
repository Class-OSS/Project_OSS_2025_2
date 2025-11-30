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
        print("\n[지출 목록]")
        for idx, e in enumerate(self.expenses, 1):
            print(f"{idx}. {e}")
        print()

    def total_spent(self):
        total = sum(e.amount for e in self.expenses)
        print(f"총 지출: {total}원\n")

    # [신규 기능] 소비 성향 분석 메서드
    def analyze_spending_pattern(self):
        if not self.expenses:
            print("\n데이터가 없어 분석할 수 없습니다. 지출을 먼저 추가해주세요.")
            print("당신의 칭호: [무소유의 현자]\n")
            return

        # 1. 기초 데이터 계산
        total = sum(e.amount for e in self.expenses)
        count = len(self.expenses)
        avg = total / count if count > 0 else 0
        
        # 2. 카테고리별 합계 구하기
        cat_sums = {}
        for e in self.expenses:
            cat_sums[e.category] = cat_sums.get(e.category, 0) + e.amount

        # 3. 가장 많이 쓴 카테고리 찾기
        top_cat = max(cat_sums, key=cat_sums.get) 
        top_cat_amount = cat_sums[top_cat]
        top_cat_ratio = top_cat_amount / total

        # 4. 분석 결과 출력
        print(f"\n==== 📊 나의 소비 성향 분석 📊 ====")
        print(f"총 지출액: {total}원 (총 {count}건)")
        print(f"최다 지출: {top_cat} 분야 ({top_cat_amount}원, {int(top_cat_ratio*100)}%)")
        print(f"건당 평균: {int(avg)}원")
        print("-" * 30)

        # 5. 칭호 부여 로직 (재미 요소)
        title = "평범한 시민"
        desc = "균형 잡힌 소비 생활을 하고 계시네요."

        # 조건 1: 한 카테고리에 50% 이상 몰빵
        if top_cat_ratio >= 0.5:
            if top_cat == "식비":
                title = "🍗 맛따라 멋따라 미식가"
                desc = "엥겔지수 폭발! 먹는 게 남는 거죠."
            elif top_cat == "쇼핑":
                title = "🛍️ 지름신이 선택한 자"
                desc = "택배 기사님과 절친이시군요."
            elif top_cat == "교통":
                title = "🚕 프로 역마살러"
                desc = "길바닥에 뿌리는 돈이 절반이 넘네요."
            else:
                title = f"🧐 {top_cat} 외길 인생"
                desc = f"{top_cat}에 진심인 편입니다."
        
        # 조건 2: 평균 지출액이 높음 (큰손)
        elif avg >= 50000:
            title = "💎 영앤리치 빅스펜더"
            desc = "한 번 쓸 때 화끈하게 쓰시는군요!"

        # 조건 3: 짠돌이 (평균 낮음, 횟수 많음)
        elif avg <= 5000 and count >= 5:
            title = "🐿️ 티끌 모아 태산"
            desc = "가성비의 제왕! 소액 결제의 달인입니다."

        print(f"당신의 칭호: ✨ {title} ✨")
        print(f"코멘트: {desc}")
        print("=====================================\n")