from budget import Budget

def main():
    budget = Budget()

    while True:
        print("\n" + "="*40)
        print("     스마트 가계부 (저축 자동 분류)")
        print("="*40)
        print("1. 지출 추가")
        print("2. 수입 입력 (자동 저축/적금 분류)")
        print("3. 지출 목록 보기")
        print("4. 잔고 및 저축 현황 보기")  
        print("5. 저축 비율 설정")
        print("6. 적금 비율 설정")
        print("7. 종료")
        print("-"*40)
        choice = input("선택 > ")

        if choice == "1":
            category = input("카테고리 (식비/교통 등): ")
            description = input("설명: ")
            try:
                amount = int(input("금액(원): "))
                budget.add_expense(category, description, amount)
            except:
                print("숫자를 입력해주세요!\n")

        elif choice == "2":
            amount = input("수입 금액(원): ")
            budget.add_income(amount)

        elif choice == "3":
            budget.list_expenses()

        elif choice == "4":
            budget.show_balance()     
        elif choice == "5":
            budget.set_savings_rate()

        elif choice == "6":
            budget.set_fixed_savings_rate()

        elif choice == "7":
            budget.show_balance()      
            print("가계부를 종료합니다.")
            break

        else:
            print("잘못된 선택입니다.\n")

if __name__ == "__main__":
    main()