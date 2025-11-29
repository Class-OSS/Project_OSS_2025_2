from budget import Budget
import datetime


def main():
    budget = Budget()

    while True:
        print("==== 간단 가계부 ====")
        print("1. 지출 추가")
        print("2. 지출 목록 보기")
        print("3. 총 지출 보기")
        print("4. 월별 예산 설정")
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
            default_month = datetime.date.today().strftime("%Y-%m")
            month = input(f"예산을 설정할 월 (YYYY-MM, 기본값: {default_month}) > ") or default_month
            try:
                amount = int(input("월 예산 금액(원) 입력 > "))
                budget.set_budget(month, amount)
            except ValueError:
                print("잘못된 금액입니다.\n")
                continue
 
        elif choice == "5":
            print("가계부를 종료합니다.")
            break

        else:
            print("잘못된 선택입니다.\n")


if __name__ == "__main__":
    main()
