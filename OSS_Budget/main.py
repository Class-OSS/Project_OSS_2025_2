from budget import Budget

def main():
    budget = Budget()

    while True:
        print("==== 공유형 가계부 (OSS_Project) ====") 
        print("1. 지출 추가")
        print("2. 지출 목록 보기")
        print("3. 총 지출 보기")
        print("4. 종료")
        choice = input("선택 > ")

        if choice == "1":
            # 사용자 이름을 먼저 입력받습니다.
            user_name = input("사용자 이름 (예: 나, 엄마, 친구): ")
            category = input("카테고리 (예: 식비, 교통 등): ")
            description = input("설명: ")
            try:
                amount = int(input("금액(원): "))
            except ValueError:
                print("잘못된 금액입니다.\n")
                continue
            
            # 수정된 함수 호출 (user_name 포함)
            budget.add_expense(category, description, amount, user_name)

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
