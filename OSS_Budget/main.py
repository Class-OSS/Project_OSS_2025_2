from budget import Budget

def main():
    budget = Budget()

    while True:
        print("==== 간단 가계부 ====")
        print("1. 지출 추가")
        print("2. 지출 목록 보기")
        print("3. 총 지출 보기")
        print("4. 소비 성향(칭호) 분석")  # 신규 메뉴
        print("5. 종료")
        choice = input("선택 > ")

        if choice == "1":
            # [수정] 카테고리 입력을 선택형으로 변경
            print("\n--- 카테고리 선택 ---")
            print("1. 식비")
            print("2. 교통")
            print("3. 쇼핑")
            print("4. 주거/통신")
            print("5. 기타")
            cat_choice = input("번호를 입력하세요: ")
            
            # 선택에 따른 카테고리 문자열 매핑
            if cat_choice == "1": category = "식비"
            elif cat_choice == "2": category = "교통"
            elif cat_choice == "3": category = "쇼핑"
            elif cat_choice == "4": category = "주거/통신"
            else: category = "기타"
            
            print(f"선택된 카테고리: [{category}]")

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
            # [신규] 분석 기능 호출
            budget.analyze_spending_pattern()

        elif choice == "5":
            print("가계부를 종료합니다.")
            break

        else:
            print("잘못된 선택입니다.\n")

if __name__ == "__main__":
    main()