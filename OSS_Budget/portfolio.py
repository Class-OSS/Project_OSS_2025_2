from stock import Stock

class Portfolio:
    def __init__(self):
        self.stocks = []
        self.spare_money = 0
        
    def set_investment(self, money):
        self.spare_money = money
        print(f"투자금액: {self.spare_money}\n")
    
    def add_stock(self, stock, percent):
        total_percent = sum(s.percent for s in self.stocks)
        if total_percent + percent > 100:
            print(f"전체 비중이 100%를 넘습니다")
        
        stock = Stock(stock, percent)
        self.stocks.append(stock)
        print(f"[{stock}] 종목이 추가되었습니다.")
        
    def print_portpolio(self):
        if not self.stocks:
            print("포트폴리오가 비어있습니다.\n")
            return

        print("\n[내 포트폴리오]")
        for i, s in enumerate(self.stocks, 1):
            print(f"{i}. {s}")
        print()
        
    def buy_stocks(self):
        if self.spare_money == 0:
            print("먼저 투자 금액을 설정해주세요.")
            return

        print(f"\n[투자 배분 계획 (총 {self.spare_money}원)]")
        total_percent = 0
        
        for stock in self.stocks:
            allocation = self.spare_money * (stock.percent / 100)
            print(f"- {stock.name}: {int(allocation)}원 ({stock.percent}%)")
            total_percent += stock.percent
            
        print(f"------------------")
        print(f"비중 합계: {total_percent}%")
        
        if total_percent < 100:
            remain = self.spare_money * ((100 - total_percent) / 100)
            print(f"현금 보유 (나머지): {int(remain)}원 ({100 - total_percent}%)")
        print()