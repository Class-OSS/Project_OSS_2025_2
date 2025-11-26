class Expense:
    # user_name 인자를 추가로 받도록 수정
    def __init__(self, date, category, description, amount, user_name):
        self.date = date
        self.category = category
        self.description = description
        self.amount = amount
        self.user_name = user_name  # 사용자 이름 저장

    def __str__(self):
        return f"[{self.date}] [{self.user_name}] {self.category} - {self.description}: {self.amount}원"
