import datetime
from budget import Budget

def main():
    budget = Budget() 

    while True:
        print("==== 간단 가계부 ====")
        print("0. 지출 한도 설정")
        print("1. 오늘 날짜로 지출 추가")
        print("2. 날짜 지정하여 지출 추가 (YYYY-MM-DD)")
        print("3. 지출 목록 보기")
        print("4. 총 지출 보기")
        print("5. 종료") 
        
        choice = input("선택 > ")

        if choice == "0":
            try:
                money_limit = int(input("새로운 지출 한도(원)를 입력하세요: "))
                if money_limit < 0:
                    print("한도는 0보다 작을 수 없습니다.\n")
                    continue
                budget.s_limit(money_limit)
            except ValueError:
                print("잘못된 금액입니다. 숫자로 입력해주세요.\n")
                continue

        elif choice == "1": # 오늘 날짜로 지출 추가
            date_add = datetime.date.today().isoformat()
            category = input("카테고리 (예: 식비, 교통 등): ")
            description = input("설명: ")
            try:
                amount = int(input("금액(원): "))
            except ValueError:
                print("잘못된 금액입니다.\n")
                continue
            budget.add_expense(date_add, category, description, amount)

        elif choice == "2": # 날짜 지정하여 지출 추가
            date_input = input("날짜 (YYYY-MM-DD 형식): ")
            try:
                datetime.date.fromisoformat(date_input) 
                date_add = date_input
            except ValueError:
                print("잘못된 날짜 형식입니다. YYYY-MM-DD 형식으로 입력해주세요.\n")
                continue

            category = input("카테고리 (예: 식비, 교통 등): ")
            description = input("설명: ")
            try:
                amount = int(input("금액(원): "))
            except ValueError:
                print("잘못된 금액입니다.\n")
                continue
            
            budget.add_expense(date_add, category, description, amount)

        elif choice == "3":
            budget.list_expenses()

        elif choice == "4":
            budget.total_spent()

        elif choice == "5":
            print("가계부를 종료합니다.")
            break

        else:
            print("잘못된 선택입니다.\n")


if __name__ == "__main__":
    main()