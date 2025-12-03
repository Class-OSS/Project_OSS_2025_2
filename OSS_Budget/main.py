from budget import Budget


def main():
    budget = Budget()

    while True:
        print("==== 간단 가계부 ====")
        print("1. 지출 추가")
        print("2. 지출 목록 보기")
        print("3. 총 지출 보기")
        print("4. 카테고리별 분석 (PR 1차 기능)") # 메뉴 4번 (PR 1차 기능)
        print("5. 예산 설정") # PR 3차 기능 추가
        print("6. 예산 상태 확인") # PR 3차 기능 추가
        print("7. 종료") # 메뉴 번호 변경
        
        choice = input("선택 > ")

        if choice == "1":
            category = input("카테고리 (예: 식비, 교통 등): ")
            description = input("설명: ")
            try:
                amount = int(input("금액(원): "))
            except ValueError:
                print("잘못된 금액입니다.\n")
                continue
            budget.add_expense(category, description, amount) # 예산 체크 기능이 이 메서드 내에 추가됨

        elif choice == "2":
            budget.list_expenses()

        elif choice == "3":
            budget.total_spent()
        
        elif choice == "4": 
            budget.summarize_by_category()

        # --- [PR 3차 기능 호출 로직 추가] ---
        elif choice == "5":
            budget.set_category_budget()
        
        elif choice == "6":
            budget.check_budget_status()
        # ------------------------------------

        elif choice == "7": # 종료 메뉴 번호 변경
            print("가계부를 종료합니다.")
            break

        else:
            print("잘못된 선택입니다.\n")


if __name__ == "__main__":
    main()
