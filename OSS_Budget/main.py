from budget import Budget

def main():
    budget = Budget()

    while True:
        print("==== 간단 가계부 ====")
        print("1. 지출 추가")
        print("2. 지출 목록 보기")
        print("3. 총 지출 보기")
        print("4. 요일별 지출 보기")  # 메뉴 추가
        print("5. 종료")        # 번호 변경
        choice = input("선택 > ")

        if choice == "1":
            category = input("카테고리 (예: 식비, 교통 등): ")
            description = input("설명: ")
            
            try:
                amount = int(input("금액(원): "))
            except ValueError:
                print("잘못된 금액입니다.\n")
                continue
            
            # 요일 입력 받기
            day = input("요일 (예: 월, 화, 수, 목, 금, 토, 일): ")

            # 함수 이름, 개수 조정
            budget.add_expense(category, description, amount, day)

        elif choice == "2":
            budget.list_expenses()

        elif choice == "3":
            budget.total_spent()

        # 요일별 보기 기능 연결
        elif choice == "4":
            day = input("조회할 요일 (예: 월, 화, 수, 목, 금, 토, 일): ")
            budget.view_by_day(day)

        # 종료 번호 변경 (4 -> 5)
        elif choice == "5":
            print("가계부를 종료합니다.")
            break

        else:
            print("잘못된 선택입니다.\n")

if __name__ == "__main__":
    main()
