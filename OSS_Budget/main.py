# 간단 가계부 프로그램의 메인 메뉴를 제공하고 지출 및 통계 기능을 실행하는 모듈입니다.

from budget import Budget
from budget_stats import print_monthly_summary, print_category_summary


def main():
    budget = Budget()

    while True:
        print("==== 간단 가계부 ====")
        print("1. 지출 추가")
        print("2. 지출 목록 보기")
        print("3. 총 지출 보기")
        print("4. 종료")
        print("5. 월별 지출 통계 보기")
        print("6. 카테고리별 지출 통계 보기")
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
            print("가계부를 종료합니다.")
            break

        elif choice == "5":
            print_monthly_summary(budget.expenses)

        elif choice == "6":
            print_category_summary(budget.expenses)

        else:
            print("잘못된 선택입니다.\n")


if __name__ == "__main__":
    main()
