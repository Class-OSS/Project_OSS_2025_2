import datetime
from budget import Budget


def main():
    budget = Budget()

    while True:
        print("==== 간단 가계부 ====")
        print("1. 지출 추가")
        print("2. 지출 목록 보기")
        print("3. 총 지출 보기")
        print("4. 목표 저축 금액 설정")
        print("5. 이번달 저축 금액 추가 및 현황 보기")
        print("6. 월별 저축 내역 보기") 
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

        elif choice == "7":
            print("가계부를 종료합니다.")
            break

        elif choice == "4":
            try:
                goal_amount = int(input("목표 저축 금액을 입력하세요: "))
                budget.set_goal_savings(goal_amount)
            except ValueError:
                print("잘못된 금액입니다. 금액을 숫자로 입력하세요.\n")
                continue

        elif choice == "5":
            date_input = input("저축할 연도와 월을 입력하세요 (예시: 2025-11): ")
            
            try:
                datetime.datetime.strptime(date_input, "%Y-%m")
                savings_amount = int(input("추가할 저축 금액을 입력하세요: "))
                budget.add_savings(date_input, savings_amount) 
                
            except ValueError:
                print("입력 형식(YYYY-MM)이 잘못되었거나 금액이 숫자가 아닙니다.\n")
                continue

        elif choice == "6":
            budget.list_monthly_savings()

        else:
            print("잘못된 선택입니다.\n")

if __name__ == "__main__":
    main()
