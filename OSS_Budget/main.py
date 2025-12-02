from budget import Budget

def main():
    budget = Budget()

    while True:
        print("==== 나만의 가계부 ====")
        print("1. 지출 추가")
        print("2. 지출 목록 보기")
        print("3. 총 지출 보기")
        print("4. 금액순 정렬 보기")
        print("5. 종료")
        choice = input("선택하세요 > ")

        if choice == "1":
            category = input("카테고리 (식비/교통 등): ")
            description = input("내용 설명: ")
            try:
                amount = int(input("금액을 입력하세요: "))
            except ValueError:
                print("숫자만 입력 가능합니다.\n")
                continue
            budget.add_expense(category, description, amount)

        elif choice == "2":
            budget.list_expenses()

        elif choice == "3":
            budget.total_spent()

        elif choice == "4":
            budget.sort_by_amount()

        elif choice == "5":
            print("프로그램을 종료합니다. 안녕히 가세요.")
            break

        else:
            print("올바른 번호를 선택해주세요.\n")

if __name__ == "__main__":
    main()