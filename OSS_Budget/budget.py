import datetime
from expense import Expense
from income import Income

class Budget:
    def __init__(self):
        self.expenses = []
        self.incomes = []  # Income 객체 저장

    # 지출 추가하는 함수
    def add_expense(self, date, category, description, amount):
        if not self._validate_date(date):
            print("날짜 형식 오류.\n")
            return

        self.expenses.append(Expense(date, category, description, amount))
        print("지출이 추가되었습니다.\n")

    # 수입 추가하는 함수
    def add_income(self, date, category, description, amount):
        if not self._validate_date(date):
            print("날짜 형식 오류.\n")
            return

        self.incomes.append(Income(date, category, description, amount))
        print("수입이 추가되었습니다.\n")

    # 지출 목록 조회하는 함수 
    def list_expenses(self):
        if not self.expenses:
            print("지출 내역 없음.\n")
            return
        print("\n[지출 목록]")
        for idx, e in enumerate(self.expenses, 1):
            print(f"{idx}. {e}")
        print()

    # 총 지출 계산하는 함수
    def total_spent(self):
        total = sum(e.amount for e in self.expenses)
        print(f"총 지출: {total}원\n")

    # 기간별 지출하는 함수
    def show_period_expenses(self, start, end):
        start_date, end_date = self._parse_dates(start, end)
        if start_date is None:
            return

        print(f"\n[{start} ~ {end}] 지출 내역")
        total = 0
        for e in self.expenses:
            d = datetime.date.fromisoformat(e.date)
            if start_date <= d <= end_date:
                print(e)
                total += e.amount

        print(f"\n총 지출: {total}원\n")

    # 기간별 전체 보고서 텍스트 파일 저장하는 함수
    def save_period_to_file(self, start, end):
        start_date, end_date = self._parse_dates(start, end)
        if start_date is None:
            return

        filename = f"report_{start}_to_{end}.txt"

        # 필터링
        period_expenses = [e for e in self.expenses
                           if start_date <= datetime.date.fromisoformat(e.date) <= end_date]

        period_incomes = [i for i in self.incomes
                          if start_date <= datetime.date.fromisoformat(i.date) <= end_date]

        total_exp = sum(e.amount for e in period_expenses)
        total_inc = sum(i.amount for i in period_incomes)
        balance = total_inc - total_exp

        status = "흑자" if balance > 0 else ("균형" if balance == 0 else "적자")

        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"=== {start} ~ {end} 기간 내역 보고서 ===\n\n")

            f.write("■ 지출\n")
            if period_expenses:
                for e in period_expenses:
                    f.write(str(e) + "\n")
            else:
                f.write("지출 없음\n")
            f.write(f"\n총 지출: {total_exp}원\n\n")

            f.write("■ 수입\n")
            if period_incomes:
                for i in period_incomes:
                    f.write(str(i) + "\n")
            else:
                f.write("수입 없음\n")
            f.write(f"\n총 수입: {total_inc}원\n\n")

            f.write("■ 재정 상태\n")
            f.write(f"잔액: {balance}원 ({status})\n")

        print(f"파일 저장 완료: {filename}\n")

    # 날짜 검증하는 함수 
    def _validate_date(self, date_str):
        try:
            datetime.date.fromisoformat(date_str)
            return True
        except ValueError:
            return False

    def _parse_dates(self, start, end):
        try:
            return (datetime.date.fromisoformat(start),
                    datetime.date.fromisoformat(end))
        except ValueError:
            print("날짜 형식 오류. YYYY-MM-DD를 사용하세요.\n")
            return None, None
