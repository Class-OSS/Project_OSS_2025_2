from budget import Budget


def main():
    budget = Budget()

    while True:
        print("==== 간단 가계부 ====") 
        print("1. 수입 추가") 
        print("2. 지출 추가")
        print("3. 전체 내역 보기 (수입:월별합계 / 지출:상세)") 
        print("4. 월별 통계 (수입/지출/잔액)") 
        print("5. 지출 분석 (최다 카테고리)") 
        print("6. 종료")
        choice = input("선택 > ")

        if choice == "1": 
            source = input("수입원 (예: 월급, 용돈): ")
            try:
                amount = int(input("금액(원): "))
            except ValueError:
                print("잘못된 금액입니다.\n")
                continue
            
            month_input = input("날짜(월)를 입력하세요. (예: 05 / 엔터 입력 시 이번 달로 기입됩니다.): ")
            if month_input.strip() == "":
                budget.add_income(source, amount) 
            else:
                budget.add_income(source, amount, month_input)

        elif choice == "2": 
            category = input("카테고리 (예: 식비, 교통): ")
            description = input("설명: ")
            try:
                amount = int(input("금액(원): "))
            except ValueError:
                print("잘못된 금액입니다.\n")
                continue
            
            date_input = input("날짜(월)를 입력하세요. (예: 12 / 엔터 입력 시 이번 달로 기입됩니다.): ")
            if date_input.strip() == "":
                budget.add_expense(category, description, amount) 
            else:
                budget.add_expense(category, description, amount, date_input) 

        elif choice == "3":
            budget.list_incomes()
            budget.list_expenses()

        elif choice == "4": 
            month_input = input("통계를 확인할 월을 입력하세요 (예: 12): ")
            budget.show_month_stats(month_input)

        elif choice == "5": 
            budget.show_top_category()

        elif choice == "6":
            print("가계부를 종료합니다.")
            break

        else:
            print("잘못된 선택입니다.\n")

if __name__ == "__main__":
    main()