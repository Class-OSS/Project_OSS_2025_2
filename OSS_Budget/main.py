from budget import Budget


def main():
    currency_suffix=['원','달러','유로','엔','위안']
    budget = Budget()

    while True:
        print("==== 간단 가계부 ====")
        print("1. 지출 추가")
        print("2. 지출 목록 보기")
        print("3. 총 지출 보기")
        print("4. 종료")
        choice = input("선택 > ")

        if choice == "1":
            category = input("카테고리 (예: 식비, 교통 등): ")
            description = input("설명: ")
            while True:
                currency = int(input("적용할 화폐단위의 변호를 입력해주세요. [0:KRW, 1:USD, 2:EUR, 3:JPY, 4:CNY] : "))
                if(currency >= 0 and currency <= 4):
                    break
            try:
                amount = int(input(f"금액({currency_suffix[currency]}): "))
            except ValueError:
                print("잘못된 금액입니다.\n")
                continue
            budget.add_expense(category, description, amount, currency)
           
        elif choice == "2":
            budget.list_expenses()

        elif choice == "3":
            budget.total_spent()

        elif choice == "4":
            print("가계부를 종료합니다.")
            break

        else:
            print("잘못된 선택입니다.\n")


if __name__ == "__main__":
    main()
