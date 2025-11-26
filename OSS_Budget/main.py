from budget import Budget
from portfolio import Portfolio

def main():
    budget = Budget()
    portfolio = Portfolio()

    while True:
        print("==== 간단 가계부 ====")
        print("1. 지출 추가")
        print("2. 지출 목록 보기")
        print("3. 총 지출 보기")
        print("4. 투자금액 설정")
        print("5. 투자 종목 추가")
        print("6. 포트폴리오 보기")
        print("7. 구매 금액 보기")
        print("8. 종료")
        choice = input("선택 > ")

        if choice == "1":
            category = input("카테고리 (예: 식비, 교통 등): ")
            description = input("설명: ")
            try:
                amount = int(input("금액(원): "))
            except ValueError:
                print("잘못된 금액입니다.\n")
                continue
            budget.add_expense(category, description, amount)

        elif choice == "2":
            budget.list_expenses()

        elif choice == "3":
            budget.total_spent()
            
        elif choice == "4":
            try:   
                money = int(input("투자금액(원): "))
            except ValueError:
                print("잘못된 금액입니다")
                continue
            portfolio.set_investment(money)
            
        elif choice == "5":
            stock = input("주식 이름: ")
            percent = int(input("구매 비율(%): "))
            portfolio.add_stock(stock, percent)
            
        elif choice == "6":
            portfolio.print_portpolio()
            
        elif choice == "7":
            portfolio.buy_stocks()

        elif choice == "8":
            print("가계부를 종료합니다.")
            break

        else:
            print("잘못된 선택입니다.\n")


if __name__ == "__main__":
    main()
