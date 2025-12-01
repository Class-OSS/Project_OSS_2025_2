from budget import Budget


def main():
    budget = Budget()

    while True:
        print("-------------------------------------")
        print("             간단 가계부 ")
        print("-------------------------------------")
        print("1. 지출 추가")
        print("2. 지출 목록 보기")
        print("3. 총 지출 보기")
        print("4. 종료")
        print("- - - - - - - - - - - - - - - - - - -")
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
            print("-------------------------------------")
            print("1. 지출 내용 수정하기")
            print("2. 메인 화면으로")
            print("- - - - - - - - - - - - - - - - - - -")
            choice = input("선택 > ")

            if choice == "2" : continue
            elif choice == "1" : 
                if(budget.isEmpty()) : 
                    print("지출 내역이 없습니다.\n")
                    continue
                print("-------------------------------------")
                budget.list_expenses()
                print("-------------------------------------")
                while True:
                    print("수정할 지출 목록의 번호를 입력하세요. (0 입력시 수정 취소)")
                    try:
                        choice = input("선택 > ")
                        if choice == "0": break
                    except ValueError:
                        print("숫자를 입력하세요")
                        continue
#
#                    if not choice.isdigit():
#                        print("숫자를 입력하세요")
#                        print("- - - - - - - - - - - - - - - - - - -")
#                        continue
#
                    choice = int(choice) - 1
                    if choice < 0 or choice >= len(budget.expenses):
                        choice = 0
                        print("잘못된 선택입니다. (음수거나, 지출 목록에 없는 번호임)\n")
                        print("-------------------------------------")
                        continue

                    print("-------------------------------------")
                    category = input("카테고리 (예: 식비, 교통 등): ")
                    description = input("설명: ")
                    try:
                        amount = int(input("금액(원): "))
                    except ValueError:
                        print("잘못된 금액입니다.\n")
                        continue
                    budget.expenses[choice].setDate(budget.time(), category, description, amount)
                    print("수정되었습니다.\n")
                    break
                
            else : 
                print("잘못된 선택입니다.\n")

        elif choice == "3":
            budget.total_spent()

        elif choice == "4":
            print("가계부를 종료합니다.")
            break

        else:
            print("잘못된 선택입니다.\n")

if __name__ == "__main__":
    main()