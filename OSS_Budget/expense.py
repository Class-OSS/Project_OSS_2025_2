
class Expense:
    def __init__(self, date, category, description, amount, payment_method):
        self.date = date
        self.category = category
        self.description = description
        self.amount = amount
        self.payment_method = payment_method

    def __str__(self):
        return f"[{self.date}] ({self.category}) [{self.payment_method}] {self.description}: {self.amount}₩"