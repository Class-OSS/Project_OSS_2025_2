from budget import Budget


def main():
    budget = Budget()

    while True:
        print("==== 간단 가계부 ====")
        print("1. 지출 추가")
        print("2. 지출 목록 보기")
        print("3. 총 지출 보기")
        print("4. 종료")
	print("5. 지난달과 차액 계산")
        print("6. 지출 삭제")
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
	 elif choice == "5":  # ★ 추가: 지난달 대비 차액 계산
            try:
                last_month = int(input("지난달 총 지출(원): "))
            except ValueError:
                print("잘못된 금액입니다.\n")
                continue

            current_total = sum(e.amount for e in budget.expenses)
            diff = current_total - last_month

            if diff > 0:
                print(
                    f"이번달이 지난달보다 {diff:,}원 더 썼습니다. "
                    f"(이번달 {current_total:,}원 / 지난달 {last_month:,}원)\n"
                )
            elif diff < 0:
                print(
                    f"이번달이 지난달보다 {abs(diff):,}원 덜 썼습니다. "
                    f"(이번달 {current_total:,}원 / 지난달 {last_month:,}원)\n"
                )
            else:
                print(f"두 달의 지출이 같습니다. (각 {current_total:,}원)\n")
        elif choice == "6":  # 지출 삭제
            budget.list_expenses()
            if not budget.expenses:
                continue
            try:
                idx = int(input("삭제할 지출 번호 입력: "))
                budget.delete_expense(idx)
            except ValueError:
                print("번호는 숫자만 입력 가능합니다.\n")

        else:
            print("잘못된 선택입니다.\n")


if __name__ == "__main__":
    main()
