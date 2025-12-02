from budget import Budget


def main():
    budget = Budget()

    while True:
        print("==== 간단 가계부 ====")
        print("1. 지출 추가")
        print("2. 지출 목록 보기")
        print("3. 총 지출 보기")
        print("4. 예산 설정")
        print("5. 결제 수단별 통계 보기")
        print("6. 종료")
      
        choice = input("선택 > ")

        if choice == "1":
            category = input("카테고리 (예: 식비, 교통 등): ")
            description = input("상세 내용: ")
            payment_method = input("결제 수단 (예: 카드, 현금, 계좌이체): ")
            try:
                amount = int(input("금액(원): "))
            except ValueError:
                print("유효한 금액을 입력하십시오.\n")
                continue
            budget.add_expense(category, description, amount, payment_method)

        elif choice == "2":
            budget.list_expenses()

        elif choice == "3":
            budget.total_spent()

        elif choice == "4":
            try:
                budget_amount = int(input("월별 목표 예산 금액을 입력하십시오 (₩): "))
                budget.set_budget(budget_amount)
            except ValueError:
                print("유효한 금액을 입력하십시오.")

        elif choice == "5":
            budget.report_by_payment_method()

        elif choice == "6": 
            print("가계부 프로그램을 종료합니다.")
            break

        else:
            print("잘못된 선택입니다.\n")


if __name__ == "__main__":
    main()
