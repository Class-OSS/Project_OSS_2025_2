from budget import Budget

def main():
    budget = Budget()

    while True:
        print("==== 간단 가계부 ====")
        print("1. 지출 추가")
        print("2. 지출 목록 보기")
        print("3. 총 지출 보기")
        print("4. 월 지출 한도 설정")
        print("5. 지출 삭제")
        print("6. 종료")

        choice = input("선택 > ")

        # 1. 지출 추가
        if choice == "1":
            category = input("카테고리 (예: 식비, 교통 등): ")
            description = input("설명: ")
            try:
                amount = int(input("금액(원): "))
            except ValueError:
                print("잘못된 금액입니다.\n")
                continue
            budget.add_expense(category, description, amount)

        # 2. 지출 목록 보기
        elif choice == "2":
            budget.list_expenses()

        # 3. 총 지출 보기
        elif choice == "3":
            budget.total_spent()

        # 4. 월 지출 한도 설정
        elif choice == "4":
            try:
                limit = int(input("월 지출 한도 금액(원): "))
            except ValueError:
                print("잘못된 금액입니다.\n")
                continue
            budget.set_limit(limit)

        # 5. 지출 삭제
        elif choice == "5":
            budget.list_expenses()
            if not budget.expenses:
                continue
            try:
                index = int(input("삭제할 항목 번호: "))
            except ValueError:
                print("번호를 숫자로 입력해주세요.\n")
                continue
            budget.delete_expense(index)

        # 6. 종료
        elif choice == "6":
            print("가계부를 종료합니다.")
            break

        else:
            print("잘못된 선택입니다.\n")


if __name__ == "__main__":
    main()
