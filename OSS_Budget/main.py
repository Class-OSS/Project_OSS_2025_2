from budget import Budget

def main():
    budget = Budget()

    while True:
        print("==============")
        print("     가계부")
        print("==============")
        print("1. 지출 추가")
        print("2. 지출 목록 보기")
        print("3. 월별 요약 보기")
        print("4. 종료")
        print("5. 카테고리별 소비 비율 보기")   # ← PR2 기능 추가
        print("==============")

        choice = input("메뉴 선택: ")

        if choice == "1":
            budget.add_expense()

        elif choice == "2":
            budget.show_expenses()

        elif choice == "3":
            budget.monthly_summary()

        elif choice == "5":
            budget.category_summary()   # ← PR2 기능 호출

        elif choice == "4":
            print("프로그램을 종료합니다.")
            break

        else:
            print("잘못된 입력입니다.\n")


if __name__ == "__main__":
    main()
