import datetime
from budget import Budget


def main():
    budget = Budget()

    while True:
        print("==== 간단 가계부 ====")
        print("1. 지출 추가")
        print("2. 지출 목록 보기")
        print("3. 총 지출 보기")
        print("4. 월별/카테고리별 지출 비교")
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

            date_input = input("날짜 (YYMMDD, 미입력 시 오늘): ").strip()

            if date_input:
                try:
                    if len(date_input) != 6:
                        print("6자리 숫자로 입력하세요. (예: 251128)\n")
                        continue

                    date_formatted = f"20{date_input[:2]}-{date_input[2:4]}-{date_input[4:6]}"
                    datetime.date.fromisoformat(date_formatted)
                    budget.add_expense(category, description, amount, date_formatted)
                except ValueError:
                    print("올바른 날짜 형식으로 입력하세요. (예: 251128)\n")
                    continue
            else:
                budget.add_expense(category, description, amount)

        elif choice == "2":
            budget.list_expenses()

        elif choice == "3":
            month_input = input("특정 월 지출 보기 (YYYY-MM) 또는 Enter(전체): ").strip()

            if month_input:
                try:
                    datetime.date.fromisoformat(f"{month_input}-01")
                    budget.total_spent(month_input)
                except ValueError:
                    print("올바른 년월 형식으로 입력하세요. (예: 2025-11)\n")
            else:
                budget.total_spent()

        elif choice == "4":
            print("\n두 달의 지출 비교")
            print("(예: 2025-08, 2024-12)")
            month1 = input("첫 번째 달: ")
            month2 = input("두 번째 달: ")

            try:
                datetime.date.fromisoformat(f"{month1}-01")
                datetime.date.fromisoformat(f"{month2}-01")
                budget.compare_two_months(month1, month2)
            except ValueError:
                print("올바른 년월 형식으로 입력하세요. (예: 2025-08)\n")

        elif choice == "5":
            print("가계부를 종료합니다.")
            break

        else:
            print("잘못된 선택입니다.\n")


if __name__ == "__main__":
    main()
