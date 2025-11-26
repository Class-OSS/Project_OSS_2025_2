from budget import Budget


def main():
    budget = Budget()

    while True:
        print("==== 간단 가계부 ====")
        print("1. 지출 추가")
        print("2. 지출 목록 보기")
        print("3. 총 지출 보기")
        print("4. 종료")






        
        choice = input("선택 > ")

        if choice == "1":
            # [수정 후 위치] 여기(1번을 선택한 직후)로 옮겨야 합니다!
            # ============================================
            existing_cats = budget.get_existing_categories()
            if existing_cats:
                print(f"   (현재 생성된 카테고리: {', '.join(existing_cats)})")
            else:
                print("   (아직 등록된 카테고리가 없습니다. 새로 입력하세요.)")
            # ============================================


            category = input("카테고리: ")
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

        else:
            print("잘못된 선택입니다.\n")


if __name__ == "__main__":
    main()
