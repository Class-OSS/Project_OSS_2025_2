import datetime
from expense import Expense
import csv

class Budget:
    def __init__(self):
        self.expenses = []

    def add_expense(self, category, description, amount):
        today = datetime.date.today().isoformat()
        expense = Expense(today, category, description, amount)
        self.expenses.append(expense)
        print("지출이 추가되었습니다.\n")

    def total_spent(self):
        total = sum(e.amount for e in self.expenses)
        print(f"총 지출: {total}원\n")

    def save_to_csv(self, filename="expenses.csv"):
        if not self.expenses:
            print("저장할 지출 내역이 없습니다.\n")
            return

        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["날짜", "카테고리", "설명", "금액"])
            for e in self.expenses:
                writer.writerow([e.date, e.category, e.description, e.amount])

        print(f"CSV 파일로 저장되었습니다: {filename}\n")
        
    def load_from_csv(self, filename):
        self.expenses.clear()

        try:
            with open(filename, "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                next(reader)  # 헤더 건너뛰기

                for row in reader:
                    # row = [날짜, 카테고리, 설명, 금액]
                    if len(row) == 4:
                        date, category, description, amount = row
                        try:
                            amount = int(amount)
                        except ValueError:
                            continue
                        e = Expense(date, category, description, amount)
                        self.expenses.append(e)

            print(f"{filename} 불러오기 완료\n")

        except FileNotFoundError:
            print("파일을 찾을 수 없습니다.\n")
