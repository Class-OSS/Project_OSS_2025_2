from budget import Budget


def main():
    budget = Budget()

    while True:
        print("==== 간단 가계부 ====")
        print("1. 지출 추가")
        print("2. 지출 목록 보기")
        print("3. 총 지출 보기")
        print("4. 지출 검색 및 삭제")
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
            keyword = input("검색어 입력(카테고리 또는 설명): ")
            search_results = budget.search_expenses(keyword)
            if not search_results:
                print("검색 결과가 없습니다.\n")
                continue
            for display_idx, (real_idx, e) in enumerate(search_results, 1):
                print(f"{display_idx}. {e}")
            print("\n[메뉴] 번호를 입력해 삭제하거나, 0을 눌러 돌아가기")
            try:
                target = int(input("선택 > "))
                if target == 0:
                    continue
                if 1 <= target <= len(search_results):
                    selected_tuple = search_results[target - 1]
                    real_idx_to_delete = selected_tuple[0]
                    budget.delete_expense(real_idx_to_delete)
                else:
                    print("잘못된 선택입니다.\n")
            except ValueError:
                print("숫자를 입력해주세요.\n")

        elif choice == "5":
            print("가계부를 종료합니다.")
            break

        else:
            print("잘못된 선택입니다.\n")


if __name__ == "__main__":
    main()
