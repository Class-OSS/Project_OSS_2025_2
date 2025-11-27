import datetime
import csv
from collections import defaultdict
from expense import Expense

class Budget:
    def __init__(self, filename="expenses.csv"):
        self.expenses = []
        self.filename = filename
        self.load_file() # 프로그램 시작 시 파일 불러오기

    def load_file(self):
        try:
            with open(self.filename, newline="", encoding="utf-8") as f:
                reader = csv.reader(f)
                for row in reader:
                    if not row:
                        continue
                    # 첫 줄에 헤더가 있으면 건너뛰기
                    if row[0] == "date":
                        continue
                    date, category, description, amount = row
                    try:
                        amount = int(amount)
                    except ValueError:
                        continue
                    self.expenses.append(Expense(date, category, description, amount))
        except FileNotFoundError:
            pass # 첫 실행이면 파일이 없음 -> 새로 작성이기에 이 조건 무시
        
    def save_to_file(self):
        with open(self.filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["date", "category", "description", "amount"])
            for e in self.expenses:
                writer.writerow([e.date, e.category, e.description, e.amount])

    def add_expense(self, category, description, amount):
        today = datetime.date.today().isoformat()
        expense = Expense(today, category, description, amount)
        self.expenses.append(expense)
        self.save_to_file() # 지출 추가마다 파일에 저장
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

    def monthly_summary(self, year, month):
      
        # 연월 별 카테고리, 총 지출 요약,  전 달 대비 지출 증감 출력
 
        monthly_by_cat = defaultdict(int)
        monthly_total = 0

        # 전 달 계산
        prev_year = year
        prev_month = month - 1
        if prev_month == 0:
            prev_month = 12
            prev_year -= 1

        prev_total = 0

        for e in self.expenses:
            try:
                y_str, m_str, _ = e.date.split("-")
                y = int(y_str)
                m = int(m_str)
            except ValueError:
                continue

            if y == year and m == month:
                monthly_by_cat[e.category] += e.amount
                monthly_total += e.amount

            if y == prev_year and m == prev_month:
                prev_total += e.amount

        print(f"\n[{year}년 {month}월 지출 요약]")

        if not monthly_by_cat:
            print("해당 월의 지출 내역이 없습니다.\n")
            return

        # 카테고리별 출력
        for cat, amt in monthly_by_cat.items():
            print(f"{cat}: {amt}원")

        print(f"총 지출: {monthly_total}원")

        # 전 달 대비    
        diff = monthly_total - prev_total

        if prev_total == 0:
            # 지난 달에 지출이 없었던 경우
            print(f"전 달({prev_year}년 {prev_month}월)에는 지출이 0원이었습니다.")
            print(f"전 달 대비 +{monthly_total}원 증가(기준 0원)\n")
        else:
            if diff > 0:
                print(
                    f"전 달({prev_year}년 {prev_month}월) 대비 +{diff}원 증가 "
                    f"(전 달: {prev_total}원 → 이번 달: {monthly_total}원)\n"
                )
            elif diff < 0:
                print(
                    f"전 달({prev_year}년 {prev_month}월) 대비 {abs(diff)}원 감소 "
                    f"(전 달: {prev_total}원 → 이번 달: {monthly_total}원)\n"
                )
            else:
                print(
                    f"전 달({prev_year}년 {prev_month}월)과 동일한 지출 "
                    f"({monthly_total}원, 변동 없음)\n"
                )
