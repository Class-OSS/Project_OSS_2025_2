
class Expense:
    def __init__(self, date, category, description, amount, currency=0):
        self.date = date
        self.category = category
        self.description = description
        self.amount = amount#KRW
        #currency / 0:KRW, 1:USD, 2:EUR, 3:JPY, 4:CNY
        self.currency = currency
        self.__foreign_amount=amount

    def __str__(self):
        currency_suffix=['원','달러','유로','엔','위안']
        if self.currency == 0:
            return f"[{self.date}] {self.category} - {self.description}: {self.amount}원"
        else:
            return f"[{self.date}] {self.category} - {self.description}: {self.amount}원 - {self.__foreign_amount}{currency_suffix[self.currency]}"  