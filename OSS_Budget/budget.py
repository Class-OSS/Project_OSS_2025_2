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

    def _get_sentiment(self, description):
        SENTIMENT_KEYWORDS = {
            '기쁨/만족 (소비)': ['선물', '여행', '맛집', '성공', '취미'],
            '스트레스/충동': ['충동', '과소비', '홧김', '스트레스', '술'],
            '필수/의무 (생존)': ['월세', '보험', '공과금', '납부', '필수', '교통', '식비'],
        }
        
        desc_lower = description.lower()
        for sentiment, keywords in SENTIMENT_KEYWORDS.items():
            for keyword in keywords:
                if keyword in desc_lower:
                    return sentiment
        return '기타/미분류'

    def sentiment_summary(self):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return

        sentiment_totals = {}
        for e in self.expenses:
            sentiment = self._get_sentiment(e.description)
            
            if sentiment not in sentiment_totals:
                sentiment_totals[sentiment] = 0
            sentiment_totals[sentiment] += e.amount
        
        print("\n[지출 감정/목적별 요약]")
        for sentiment, total in sentiment_totals.items():
            print(f"- {sentiment}: {total}원")
        
        total_spent = sum(e.amount for e in self.expenses)
        print(f"\n총 지출: {total_spent}원\n")