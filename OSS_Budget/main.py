from budget import Budget

def main():
    budget = Budget()

    while True:
        print("==== 감정 기반 가계부 ====")
        print("1. 지출 추가")
        print("2. 지출 목록 보기")
        print("3. 총 지출 금액")
        print("4. 감정 기반 지출 분석")
        print("5. 종료")
        choice = input("선택 > ")

        if choice == "1":
            category = input("카테고리 (예: 식비, 교통, 취미 등): ")
            description = input("설명: ")
            amount = int(input("금액(원): "))
            mood = input("지출 당시 감정 (예: 행복, 스트레스, 충동, 보통 등): ")

            budget.add_expense(category, description, amount, mood)

        elif choice == "2":
            budget.list_expenses()

        elif choice == "3":
            budget.total_spent()

        elif choice == "4":
            budget.analyze_by_mood()

        elif choice == "5":
            print("가계부를 종료합니다.")
            break

        else:
            print("잘못된 선택입니다.\n")

if __name__ == "__main__":
    main()
