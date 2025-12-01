from budget import Budget
<<<<<<< HEAD
from datetime import datetime
=======

>>>>>>> be1efd5 ([기능추가] 지출 카테고리별 캐시백 기능 추가)

def main():
    budget = Budget()

    while True:
        print("==== 간단 가계부 ====")
        print("1. 지출 추가")
        print("2. 지출 목록 보기")
        print("3. 총 지출 보기")
<<<<<<< HEAD
        print("4. 캐시백 총액 확인하기")
        print("5. 가계부 종료")
=======
        print("4. 캐시백 확인하기")
        print("5. 종료")
>>>>>>> be1efd5 ([기능추가] 지출 카테고리별 캐시백 기능 추가)
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
            budget.show_cashback()

        elif choice == "5":
            print("가계부를 종료합니다.")
            break

        else:
            print("잘못된 선택입니다.\n")


if __name__ == "__main__":
    main()
