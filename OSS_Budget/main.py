from budget import Budget
import datetime 


def main():
    budget = Budget()

    while True:
        print("==== 간단 가계부 ====")
        print("1. 지출 추가")
        print("2. 지출 목록 보기 (전체)")
        print("3. 총 지출 보기")
        print("4. 기간별 지출 목록 보기") 
        print("5. 카테고리별 총 지출 요약") 
        print("6. 특정 카테고리 지출 목록 보기") 
        print("7. 종료") 
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
            start_date_str = input("시작일 (yymmdd): ")
            end_date_str = input("종료일 (yymmdd): ")
            
            if len(start_date_str) == 6 and len(end_date_str) == 6:
                budget.list_expenses_by_date_range(start_date_str, end_date_str)
            else:
                print("날짜는 yymmdd 6자리 형식으로 입력해야 합니다.\n")

        elif choice == "5":
            budget.category_summary()
        
        elif choice == "6":
            category_filter = input("확인할 카테고리 이름을 입력하세요: ")
            budget.filter_expenses_by_category(category_filter)

        elif choice == "7":
            print("가계부를 종료합니다.")
            break

        else:
            print("잘못된 선택입니다.\n")


if __name__ == "__main__":
    main()