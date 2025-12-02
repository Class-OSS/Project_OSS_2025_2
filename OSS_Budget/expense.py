
class Expense:
    def __init__(self, month, category, description, amount):
        self.month = month
        self.category = category
        self.description = description
        self.amount = amount

    def __str__(self):
        return f"[{self.month}월] {self.category} - {self.description}: {self.amount}원"
    

class Income:
    def __init__(self, month, source, amount):
        self.month = month
        self.source = source
        self.amount = amount

    def __str__(self):
        return f"[{self.month}월] {self.source}: {self.amount}원"