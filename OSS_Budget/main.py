from budget import Budget

def main():
    budget = Budget()

    while True:
        print("==== 간단 가계부 ====")
        print("1. 지출 추가 (단건)")
        print("2. 지출 목록 보기")
        print("3. 총 지출 보기")
        print("4. 지출 일괄 입력")     # [신규 기능 추가]
        print("5. 종료")             # [종료 번호 변경]
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
        # [추가] 일괄 지출 입력 기능 연결 (4번)
        elif choice == "4":
            print("\n[ 일괄 지출 입력 형식: 카테고리 금액 내용; 카테고리 금액 내용 ]")
            input_string = input("지출 문자열 입력 (구분자: ;): ")
            budget.add_multiple_expenses(input_string, delimiter=';')
        # [수정] 종료 번호 변경 (5번)
        elif choice == "5":
            print("가계부를 종료합니다.")
            break

        else:
            print("잘못된 선택입니다.\n")

if __name__ == "__main__":
    main()