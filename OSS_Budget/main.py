from budget import Budget

def main():
    budget = Budget()

    while True:
        print("==== 간단 가계부 ====")
        print("1. 지출 추가")
        print("2. 지출 목록 보기")
        print("3. 총 지출 보기")
        print("4. 통화 변환")
        print("5. 종료")

        choice = input("선택 > ")

        if choice == "1":
            category = input("카테고리: ")
            description = input("내용: ")
            amount = int(input("금액: "))
            budget.add_expense(category, description, amount)

        elif choice == "2":
            budget.list_expenses()

        elif choice == "3":
            budget.total_spent()

        elif choice == "4":
            amount = float(input("금액: "))
            from_cur = input("현재 통화 (KRW, USD, EUR, JPY): ").upper()
            to_cur = input("변환할 통화 (KRW, USD, EUR, JPY): ").upper()

            result = budget.convert_currency(amount, from_cur, to_cur)
            if result is not None:
                print(f"{amount} {from_cur} → {result:.2f} {to_cur}\n")

        elif choice == "5":
            print("가계부 종료합니다.")
            break

        else:
            print("잘못된 선택입니다.\n")

if __name__ == "__main__":
    main()
