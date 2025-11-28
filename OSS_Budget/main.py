from budget import Budget


def main():
    budget = Budget()

    while True:
        print("==== 간단 가계부 ====")
        print("1. 지출 추가")
        print("2. 지출 목록 보기")
        print("3. 총 지출 보기")
        print("4. 기간별 지출 조회")
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

        elif choice == "4":
            print("\n날짜 형식 : YYMMDD (예: 251128)")
            start_date = input("시작 날짜: ")
            end_date = input("종료 날짜: ")

            try:
                import datetime

                # YYMMDD를 YYYY-MM-DD로 변환
                if len(start_date) != 6 or len(end_date) != 6:
                    print("6자리 **숫자**로 입력하세요. (예: 251128)\n")
                    continue

                # YY -> YYYY 변환 (20YY로 가정)
                start_formatted = f"20{start_date[:2]}-{start_date[2:4]}-{start_date[4:6]}"
                end_formatted = f"20{end_date[:2]}-{end_date[2:4]}-{end_date[4:6]}"

                # 날짜 유효성 확인
                datetime.date.fromisoformat(start_formatted)
                datetime.date.fromisoformat(end_formatted)

                if start_formatted > end_formatted:
                    print("시작 날짜가 종료 날짜보다 늦습니다.\n")
                    continue

                budget.list_expenses_by_period(start_formatted, end_formatted)
            except ValueError:
                print("***!!날짜 형식!!***\nYYMMDD 형식으로 입력하세요. (예: 251128)\n")

        elif choice == "5":
            print("가계부를 종료합니다.")
            break

        else:
            print("잘못된 선택입니다.\n")


if __name__ == "__main__":
    main()
