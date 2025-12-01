
class Expense:
    def __init__(self, date, category, description, amount):
        self.date = date
        self.category = category
        self.description = description
        self.amount = amount

    def __str__(self):
        return f"[{self.date}] {self.category} - {self.description}: {self.amount}원"
    
    def setDate(self, newDate, newCategory, newDescription, newAmount): 
        self.date = newDate
        self.category = newCategory
        self.description = newDescription
        self.amount = newAmount