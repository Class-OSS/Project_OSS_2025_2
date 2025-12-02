
class Expense:
    def __init__(self, date, category, description, amount):
        self.date = date
        self.category = category
        self.description = description
        if not isinstance(amount,(int,float)):
           raise ValueError("금액은 숫자 타입이어야 합니다")
        if amount<=0:
           raise ValueError("지출 금액은 음수 또는 0일 수 없습니다")
        self.amount = amount

    def __str__(self):
        return f"[{self.date}] {self.category} - {self.description}: {self.amount}원"