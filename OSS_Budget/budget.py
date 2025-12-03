# 22212141 김희곤 지출 내역을 치킨 마릿수로 표현현
class BudgetManager:
    def __init__(self):
        self.transactions = []
        self.chicken_price = 20000  # 치킨 1마리 가격 (2만원)

    def add_transaction(self):
        print("\n[수입/지출 입력]")
        date = input("날짜 (예: 2025-12-05): ")
        desc = input("내역 (예: 점심식사): ")
        try:
            amount = int(input("금액 (수입은 +, 지출은 -로 입력): "))
            self.transactions.append({"date": date, "desc": desc, "amount": amount})
            print(">> 입력되었습니다.")
        except ValueError:
            print(">> 금액은 숫자로 입력해주세요.")

    def show_transactions(self):
        print("\n[전체 내역 조회]")
        if not self.transactions:
            print(">> 내역이 없습니다.")
            return
        
        total = 0
        for t in self.transactions:
            print(f"{t['date']} | {t['desc']} : {t['amount']}원")
            total += t['amount']
        print(f"===============\n>> 잔액: {total}원")

    def show_chicken_stats(self):
        # [신박한 기능] 내 지출을 치킨 마리 수로 환산
        print("\n[🍗 치킨 지수 분석 🍗]")
        
        # 지출만 따로 합산 (음수 값만 더해서 절대값 씌움)
        total_expense = 0
        for t in self.transactions:
            if t['amount'] < 0:
                total_expense += abs(t['amount'])
        
        if total_expense == 0:
            print(">> 아직 지출이 없습니다. 치킨을 사드세요!")
        else:
            count = total_expense // self.chicken_price
            print(f">> 현재까지 총 지출: {total_expense}원")
            print(f">> 와우! 프라이드 치킨 약 {count}마리를 사 먹을 수 있는 돈을 썼군요!")
            print(f">> (기준: 치킨 1마리 {self.chicken_price}원)")

    def run(self):
        while True:
            print("\n=== 💰 가계부 프로그램 ===")
            print("1. 내역 입력")
            print("2. 전체 조회")
            print("3. 치킨 지수 분석 (New)")
            print("4. 종료")
            
            choice = input("선택: ")
            
            if choice == '1':
                self.add_transaction()
            elif choice == '2':
                self.show_transactions()
            elif choice == '3':
                self.show_chicken_stats()
            elif choice == '4':
                print("프로그램을 종료합니다.")
                break
            else:
                print("다시 선택해주세요.")

if __name__ == "__main__":
    manager = BudgetManager()
    manager.run()