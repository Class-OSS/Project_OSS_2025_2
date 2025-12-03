from budget import Budget
import datetime # datetime 모듈 추가

# 목표 현황판 출력 함수
def display_goal_status(budget):
    # Budget 클래스에서 현황 정보 가져오기
    year_month, goal, spent, percent = budget.get_monthly_goal_status()
    
    # 현황 출력
    print("========================")
    print(f"  [ {year_month} 목표 현황 ]  ")
    print("========================")
    print(f"  목표 금액: {goal:,}원")
    print(f"  현재 지출: {spent:,}원")
    
    if goal > 0:
        if percent > 100:
            status_text = "초과"
            diff_amount = spent - goal
        else:
            status_text = "잔여"
            diff_amount = goal - spent
            
        print(f"  사용률: {percent:.2f}% ({status_text} 금액: {diff_amount:,}원)")
    else:
        print("  사용률: 목표가 설정되지 않았습니다.")
    print("========================\n")


def main():
    budget = Budget()

    while True:
        display_goal_status(budget) # 현황판 실시간 출력

        print("==== 간단 가계부 ====")
        print("1. 지출 추가")
        print("2. 지출 목록 보기")
        print("3. 총 지출 보기")
        print("4. 월별 목표 설정") # 4. 메뉴 추가
        print("5. 종료") # 5. 종료로 변경
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
        
        # 4. 목표 설정 기능 로직 추가
        elif choice == "4":
            year_month = input("목표 설정 월 (예: 2025-12): ")
            try:
                # 입력 형식 YYYY-MM 검증
                if len(year_month) != 7 or year_month[4] != '-':
                    raise ValueError
                amount = int(input(f"[{year_month}] 목표 금액(원): "))
                if amount <= 0:
                    raise ValueError
            except ValueError:
                print("잘못된 형식 또는 금액입니다. (예: 2025-12, 금액은 0보다 커야 함)\n")
                continue
            budget.set_goal(year_month, amount)

        elif choice == "5": # 5. 종료
            print("가계부를 종료합니다.")
            break

        else:
            print("잘못된 선택입니다.\n")


if __name__ == "__main__":
    main()