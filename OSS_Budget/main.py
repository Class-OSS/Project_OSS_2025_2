from budget import Budget


def main():
    budget = Budget()

    while True:
        print("==== 간단 가계부 ====")
        print("1. 지출 추가")
        print("2. 지출 목록 보기")
        print("3. 총 지출 보기")
        print("4. 카테고리별 지출 보기")
        print("5. 월별 주요 지출 보기")
        print("6. 월별 평균 지출 / 예산 대비 사용률 보기(추가 기능)")
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
            budget.category_stats()
            
        elif choice == "5":
            ym = input("조회할 월 입력 (YYYY-MM): ")
            budget.month_top_categories(ym)
            
        elif choice == "6":
            ym = input("조회할 월 입력 (YYYY-MM): ")
            budget_input = input("예산 금액 입력 (없으면 Enter): ")
            budget_amount = int(budget_input) if budget_input.strip() else None
            budget.month_avg_and_budget(ym, budget_amount)


        elif choice == "7":
            print("가계부를 종료합니다.")
            break

        else:
            print("잘못된 선택입니다.\n")


if __name__ == "__main__":
    main()
