from budget import Budget


def main():
    budget = Budget()

    while True:
        print("==== 간단 가계부 ====")
        print("1. 지출 추가")
        print("2. 지출 목록 보기")
        print("3. 총 지출 보기")
        print("4. 지출 관리 (삭제/수정)") # main추가
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

            if True:
                print("==== 지출 관리 ====")
                manage_choice = int(input("1. 삭제 / 2. 수정 / 3. 취소\n선택 >> "))

                if(manage_choice == 1):
                    index_to_del = int(input("삭제할 지출 번호 >> "))
                    budget.delete_expense(index_to_del)
                elif(manage_choice == 2):
                    index_to_edit = int(input("수정할 지출의 번호 >> "))
                    print(f"\n--- {index_to_edit}번 지출 수정 ---")
                            
                    # 기존 값 불러오기 (수정하지 않을 경우 대비)
                    expense_to_edit = budget.expenses[index_to_edit - 1]
                    new_category = input(f"새 카테고리 (현재: {expense_to_edit.category}, 변경하고싶지 않음 Enter): ").strip() or expense_to_edit.category
                    new_description = input(f"새 설명 (현재: {expense_to_edit.description}, 변경하고싶지 않음 Enter): ").strip() or expense_to_edit.description
                    new_amount_str = input(f"새 금액(원) (현재: {expense_to_edit.amount}, 변경하고싶지 않음 Enter): ").strip()

                    new_amount = expense_to_edit.amount
                    if new_amount_str:
                        try:
                            new_amount = int(new_amount_str)
                        except ValueError:
                            print("잘못된 금액입니다. 수정이 취소됩니다.\n")
                            continue

                    budget.edit_expense(index_to_edit, new_category, new_description, new_amount)
                else:
                    print("지출 관리를 취소합니다.\n")

        elif choice == "5":
            print("가계부를 종료합니다.")
            break

        else:
            print("잘못된 선택입니다.\n")


if __name__ == "__main__":
    main()
