from budget import Budget


def main():
    budget = Budget()
    while True:
        print("(최초 1회 입력) 당신의 한도액을 설정하세요.\n")
        try:
            limit = int(input("입력 > "))
        except ValueError:
            print("잘못된 금액입니다.\n")
            continue
        break
    while True:
        print(f"==== 간단 가계부 (현재 잔여 한도: {limit}원)====")
        print("1. 지출 추가")
        print("2. 지출 목록 보기")
        print("3. 총 지출 보기")
        print("4. 종료")
        choice = input("선택 > ")

        if choice == "1":
            category = input("카테고리 (예: 식비, 교통 등): ")
            description = input("설명: ")
            try:
                amount = int(input("금액(원): "))
            except ValueError:
                print("잘못된 금액입니다.\n")
                continue
            limit = limit - amount
            if limit < 0:
                print("한도액을 넘어섰으므로 추가되지 않습니다.")
                limit = limit + amount
                continue
            else:
                budget.add_expense(category, description, amount)

        elif choice == "2":
            budget.list_expenses()

        elif choice == "3":
            budget.total_spent()

        elif choice == "4":
            print("가계부를 종료합니다.")
            break

        else:
            print("잘못된 선택입니다.\n")


if __name__ == "__main__":
    main()
