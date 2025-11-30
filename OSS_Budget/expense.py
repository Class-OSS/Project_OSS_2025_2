
class Expense:
    def __init__(self, date, category, description, amount):
        self.date = date
        self.category = category
        self.description = description
        self.amount = amount

    def __str__(self):
        return f"[{self.date}] {self.category} - {self.description}: {self.amount}원"
    #적금 기능 : 사용자 입력에 따른 적금 계산
    def saving(self,monthly_amount ,months) :
        total_saving = monthly_amount * months
        return total_saving
    