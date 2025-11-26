from budget import Budget


def main():
    budget = Budget()

    while True:
        print("==== 간단 가계부 ====")
        print("1. 지출 추가")
        print("2. 지출 목록 보기")
        print("3. 총 지출 보기")
        print("4. 수입 추가")       # 신규 기능 추가
        print("5. 재정 상태 확인")  # 신규 기능 추가
        print("6. 종료")
        choice = input("선택 > ")

        if choice == "1":
            date = input("지출 날짜 (YYYY-MM-DD): ")
            category = input("카테고리 (예: 식비, 교통 등): ")
            description = input("설명: ")
            try:
                amount = int(input("금액(원): "))
            except ValueError:
                print("잘못된 금액입니다.\n")
                continue
            budget.add_expense(date, category, description, amount)

        elif choice == "2":
            budget.list_expenses()

        elif choice == "3":
            budget.total_spent()

        elif choice == "4":
            date = input("수입 날짜 (YYYY-MM-DD): ")
            source = input("수입 출처(예: 용돈, 알바 등): ")
            try:
                amount = int(input("금액(원): "))
            except:
                print("잘못된 금액입니다.\n")
                continue
            budget.add_income(date, source, amount)

        elif choice == "5":
            budget.financial_status()
        elif choice == "6":
            print("가계부를 종료합니다.")
            break

        else:
            print("잘못된 선택입니다.\n")


if __name__ == "__main__":
    main()
