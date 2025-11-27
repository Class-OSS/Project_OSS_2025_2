from budget import Budget

def main():
    budget = Budget()

    while True:
        print("==== 간단 가계부 ====")
        print("1. 지출 추가")
        print("2. 지출 목록 보기")
        print("3. 총 지출 보기")
        print("4. 금액 기준 검색")  
        print("5. 종료")            
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

        # 금액 검색 처리
        elif choice == "4":
            try:
                target = int(input("기준 금액(원): "))
            except ValueError:
                print("잘못된 금액입니다.\n")
                continue
            
            print("1. 이상  2. 이하")
            cond_choice = input("조건 선택 > ")
            
            if cond_choice == "1":
                budget.search_by_amount(target, 'up')
            elif cond_choice == "2":
                budget.search_by_amount(target, 'down')
            else:
                print("잘못된 선택입니다. 메뉴로 돌아갑니다.\n")

        elif choice == "5":
            print("가계부를 종료합니다.")
            break

        else:
            print("잘못된 선택입니다.\n")

if __name__ == "__main__":
    main()
