import datetime
import json
from expense import Expense

class Budget:
    def __init__(self):
        self.expenses = []
        self.filename = "budget_data.json"	# 저장할 파일 이름
        self.load_data()	# 파일 불러오기

    def add_expense(self, category, description, amount):
        today = datetime.date.today().isoformat()
        expense = Expense(today, category, description, amount)
        self.expenses.append(expense)
        print("지출이 추가되었습니다.\n")
        self.save_data()	# 지출 저장

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
	
    def save_data(self):
        data_to_save = []
        for e in self.expenses:
            data_to_save.append(e.to_dict())
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(data_to_save, f, ensure_ascii=False, indent=4)

    def load_data(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                data_list = json.load(f)
                self.expenses = []
                for item in data_list:
                    e = Expense(
                        item['date'],
                        item['category'],
                        item['description'],
                        item['amount']
                    )
                    self.expenses.append(e)
        except FileNotFoundError: # 파일이 없으면 그냥 넘어감
            pass