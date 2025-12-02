from budget import Budget


def main():
    budget = Budget()

    while True:
        print("==== 간단 가계부 ====")
        print("1. 지출 추가")
        print("2. 지출 목록 보기")
        print("3. 총 지출 보기")
        print("4. 지출 삭제")
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
            budget.list_expenses()

            if budget.expenses:
                index_input = input("삭제할 지출의 번호(숫자)를 입력하시오 : ").strip()
 
                if index_input:
                    budget.delete_expense(index_input)
                else:
                    print("입력값이 비어있으므로 삭제를 취소합니다.")
        
        elif choice == '5':
            print("가계부를 종료합니다.")
            break 

        else:
            print("잘못된 선택입니다.\n")

if __name__ == "__main__":
    main()