from budget import Budget


def main():
    budget = Budget()

    while True:
        print("==== 간단 가계부 ====")
        print("1. 지출 추가")
        print("2. 지출 목록 보기")
        print("3. 총 지출 보기")
        print("4. 고정 지출(즐겨찾기)")
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
            print("\n--- 고정 지출 관리 ---")
            print("1. 즐겨찾기 등록")
            print("2. 즐겨찾기 적용(지출 추가)")
            sub_choice = input("선택 > ")

            if sub_choice == "1":
                print("[새로운 즐겨찾기 등록]")
                alias = input("별칭 (예: 월세, 넷플릭스, 점심): ")
                category = input("카테고리: ")
                desc = input("설명: ")
                try:
                    amount = int(input("금액: "))
                    budget.register_favorite(alias, category, desc, amount)
                except ValueError:
                    print("금액은 숫자여야 합니다.\n")

            elif sub_choice == "2":
                print("[즐겨찾기 적용]")
                if budget.list_favorites():
                    try:
                        idx = int(input("적용할 번호를 선택하세요: "))
                        budget.apply_favorite(idx - 1)
                    except ValueError:
                        print("숫자를 입력하세요.\n")
            else:
                print("잘못된 선택입니다.\n")

        elif choice == "5":
            print("가계부를 종료합니다.")
            break

        else:
            print("잘못된 선택입니다.\n")


if __name__ == "__main__":
    main()
