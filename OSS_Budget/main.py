from budget import Budget, Budget_income


def main():
    budget = Budget()
    budget_in = Budget_income()
    
    while True:
        print("==== 간단 가계부 ====")
        print("1. 지출 추가")
        print("2. 지출 목록 보기")
        print("3. 수입 추가") # 기능 추가
        print("4. 수입 목록 보기") # 기능 추가
        print("5. 총 수입 / 총 지출 보기 / 비율 보기") # 기능 추가
        print("6. 종료")
        choice = input("선택 > ")

        if choice == "1": # 지출 추가
            category = input("카테고리 (예: 식비, 교통 등): ")
            description = input("설명: ")
            try:
                amount = int(input("금액(원): "))
            except ValueError:
                print("잘못된 금액입니다.\n")
                continue
            budget.add_expense(category, description, amount)

        elif choice == "2": # 지출 목록 보기
            budget.list_expenses()
            
        elif choice == "3": # 수입 추가
            category = input("카테고리 (예: 용돈, 알바, 배당금 등): ")
            description = input("설명: ")
            try:
                amount = int(input("금액(원): "))
            except ValueError:
                print("잘못된 금액입니다.\n")
                continue
            budget_in.add_incomes(category, description, amount)
            
        elif choice == "4": # 수입 목록 보기
            budget_in.list_incomes()
            
        elif choice == "5": # 총 수입, 총 지출, 비율 한번에 보여주기
            budget.percentage(budget_in)
            
        elif choice == "6":
            print("가계부를 종료합니다.")
            break

        else:
            print("잘못된 선택입니다.\n")


if __name__ == "__main__":
    main()
