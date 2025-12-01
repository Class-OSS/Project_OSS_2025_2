from budget import Budget

def main():
    manager = Budget()

    while True:
        print("==== 간단 가계부 ====")
        print("1. 지출 추가")
        print("2. 지출 목록 보기")
        print("3. 총 지출 보기")
        print("4. 기간별 지출 조회")
        print("5. 수입 추가")
        print("6. 기간별 전체 내역 텍스트로 저장")
        print("7. 종료")

        choice = input("선택 > ")

        if choice == "1":
            date = input("지출 날짜(YYYY-MM-DD): ")
            category = input("카테고리: ")
            description = input("설명: ")
            try:
                amount = int(input("금액(원): "))
            except ValueError:
                print("금액은 숫자로 입력하세요.\n")
                continue
            manager.add_expense(date, category, description, amount)

        elif choice == "2":
            manager.list_expenses()

        elif choice == "3":
            manager.total_spent()

        elif choice == "4":
            start = input("조회 시작 날짜(YYYY-MM-DD): ")
            end = input("조회 종료 날짜(YYYY-MM-DD): ")
            manager.show_period_expenses(start, end)

        elif choice == "5": 
            date = input("수입 날짜(YYYY-MM-DD): ")
            category = input("수입 카테고리(월급/용돈 등): ")
            description = input("설명: ")
            try:
                amount = int(input("수입 금액(원): "))
            except ValueError:
                print("금액은 숫자로 입력하세요.\n")
                continue
            manager.add_income(date, category, description, amount)

        elif choice == "6":
            start = input("저장 시작 날짜(YYYY-MM-DD): ")
            end = input("저장 종료 날짜(YYYY-MM-DD): ")
            manager.save_period_to_file(start, end)

        elif choice == "7":
            print("가계부를 종료합니다.")
            break

        else:
            print("잘못된 선택입니다.\n")


if __name__ == "__main__":
    main()
