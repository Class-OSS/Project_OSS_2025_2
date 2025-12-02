from budget import Budget


def main():
    budget = Budget()

    while True:
        print("==== 간단 가계부 ====")
        print("1. 지출 추가")
        print("2. 지출 목록 보기")
        print("3. 총 지출 보기")
        print("4. 고정 지출 등록")
        print("5. 고정 지출 목록 보기")
        print("6. 고정 지출 활성/비활성 전환")
        print("7. 종료")
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
            print("\n==== 고정 지출 등록 ====")
            category = input("카테고리 (예: 구독료, 통신비 등): ")
            description = input("설명 (예: 넷플릭스, 휴대폰 요금): ")
            try:
                amount = int(input("금액(원): "))
                day = int(input("매월 몇 일에 지출되나요? (1-31): "))
                if not 1 <= day <= 31:
                    print("날짜는 1~31 사이여야 합니다.\n")
                    continue
            except ValueError:
                print("잘못된 입력입니다.\n")
                continue
            budget.add_fixed_expense(category, description, amount, day)

        elif choice == "5":
            budget.list_fixed_expenses()

        elif choice == "6":
            budget.list_fixed_expenses()
            if budget.fixed_expenses:
                try:
                    num = int(input("활성/비활성 전환할 번호 > "))
                    budget.toggle_fixed_expense(num - 1)
                except ValueError:
                    print("잘못된 입력입니다.\n")

        elif choice == "7":
            print("가계부를 종료합니다.")
            break

        else:
            print("잘못된 선택입니다.\n")


if __name__ == "__main__":
    main()
