from budget import Budget

def main():
    budget = Budget()

    while True:
        print("==== 간단 가계부 ====")
        print("0. 예산 설정")
        print("1. 지출 추가")
        print("2. 지출 목록 보기")
        print("3. 총 지출 보기")
        print("4. 잔액 보기")
        print("5. 종료")
        choice = input("선택 > ")

        if choice == "0":
            try:
                property = int(input("예산 금액(원):"))
                budget.set_budget(property)
            except ValueError:
                print("\n잘못된 입력입니다.")
                continue

        elif choice == "1":
            if budget.budget_limit is None:
                print("\n예산을 설정하세요.")
                continue

            category = input("지출 카테고리 (예: 식비, 교통 등): ")
            description = input("지출 설명: ")
            try:
                amount = int(input("지출 금액(원): "))
            except ValueError:
                print("잘못된 금액입니다.\n")
                continue
            budget.add_expense(category, description, amount)
            budget.calc_remaining()

        elif choice == "2":
            budget.list_expenses()

        elif choice == "3":
            budget.total_spent()
            budget.calc_remaining()

        elif choice == "4":
            if budget.budget_limit is None:
                print("예산 및 잔액이 없습니다.\n")
                continue
            budget.calc_remaining()

        elif choice == "5":
            print("가계부를 종료합니다.")
            break

        else:
            print("잘못된 선택입니다.\n")


if __name__ == "__main__":
    main()
