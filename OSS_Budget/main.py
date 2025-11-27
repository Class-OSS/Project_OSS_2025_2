from budget import Budget
import datetime

def main():
    budget = Budget()

    while True:
        print("==== 간단 가계부 ====")
        print("1. 지출 추가")
        print("2. 지출 목록 보기")
        print("3. 총 지출 보기")
        print("4. 종료")
        choice = input("선택 > ")

        if choice == "1":
            date = input("날짜 입력(YYYY-MM-DD, 입력하지않는다면 오늘날짜) : ").strip()
            
            if date == " ":
                date = datetime.date.today().isoformat()
            else:
               try:
                   datetime.date.fromisoformat(date)
               except ValueError:
                   print("날짜 형식이 잘못되었습니다. 다시입력해주세요")
                   continue

            category = input("카테고리 (예: 식비, 교통 등): ")
            description = input("설명: ")
            try:
                amount = int(input("금액(원): "))
            except ValueError:
                print("잘못된 금액입니다.\n")
                continue
            budget.add_expense(date,category, description, amount)


        elif choice == "2":
            budget.list_expenses()

        elif choice == "3":
            budget.total_spent()

        elif choice == "4":
            print("가계부를 종료합니다.")
            break

        else:
            print("잘못된 선택입니다.\n")


if __name__ == "__main__":
    main()
