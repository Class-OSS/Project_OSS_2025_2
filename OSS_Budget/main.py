from budget_csv import budget_as_csv

from budget import Budget


def main():
    budget = Budget()

    while True:
        print("==== 간단 가계부 ====")
        print("1. 지출 추가")
        print("2. 지출 목록 보기")
        print("3. 총 지출 보기")
        print("4. CSV로 내보내기")
        print("5. 지출 분석 결과")
        print("6. 종료하기")
        choice = input("원하는 기능 선택하세요 -> ")

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
            result = budget_as_csv(budget.expenses)
            print("CSV 저장 완료:", result, "\n")

        elif choice == "5":
            budget.analyze_expenses()

        elif choice == "6":
            print("가계부를 종료합니다.")
            break

        else:
            print("잘못된 선택입니다.\n")


if __name__ == "__main__":
    main()
