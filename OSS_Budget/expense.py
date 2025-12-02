
class Expense:
    def __init__(self, date, category, description, amount):
        self.date = date
        self.category = category
        self.description = description
        self.amount = amount

    def __str__(self):
        return f"[{self.date}] {self.category} - {self.description}: {self.amount}원"
    
class Income:
    def __init__(self1, date, category, description, amount):
        self1.date = date
        self1.category = category
        self1.description = description
        self1.amount = amount

    def __str__(self1):
        return f"[{self1.date}] {self1.category} + {self1.description}: {self1.amount}원"