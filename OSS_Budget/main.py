from budget import Budget


def main():
    budget = Budget()

    while True:
        print("==== 간단 가계부 ====")
        print("1. 지출 추가")
        print("2. 지출 삭제")
        print("3. 지출 수정")
        print("4. 지출 목록 보기")
        print("5. 총 지출 보기")
        print("6. 카테고리별 지출 금액 및 비율")
        print("7. 저축률 보기")
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
            index = int(input("몇 번을 삭제하시겠습니까? "))
            budget.delete_expense(index)
        
        elif choice == "3":
            budget.list_expenses()
            index = int(input("몇 번을 수정하시겠습니까? "))
            category = input("카테고리 (예: 식비, 교통 등): ")
            description = input("설명: ")
            amount = int(input("금액(원): "))
            budget.edit_expense(index,category,description,amount)
             

        elif choice == "4":
            budget.list_expenses()

        elif choice == "5":
            budget.total_spent()

        elif choice == "6":
            budget.category_stats()

        elif choice =="7":
            try:
                income = int(input("이번 달 수입을 입력하세요: "))
                budget.income = income
            except ValueError:
                print("잘못된 금액입니다.\n")
            budget.savings_rate()

        elif choice == "7":
            print("가계부를 종료합니다.")
            break


        else:
            print("잘못된 선택입니다.\n")


if __name__ == "__main__":
    main()
