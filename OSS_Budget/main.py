from budget import Budget


def main():
    budget = Budget()

    while True:
        print("==== 간단 가계부 ====")
        print("1. 지출 추가")
        print("2. 지출 목록 보기")
        print("3. 총 지출 보기")
        print("4. 카테고리별 지출 비율 보기")
        print("5. 종료")
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
        
        # 카테고리별 비율 보기 로직
        elif choice == "4": 
            result = budget.get_category_ratio()

            if isinstance(result, str):
                print(result + "\n")
            else:
                # 반환값을 3개로 받음 ratios, total_spent, category_totals
                ratios, total_spent, category_totals = result 
                print("\n[카테고리별 지출 비율 분석]")
                print(f"총 지출 금액: {total_spent}원")
                print("-" * 30)
                for category, ratio in ratios.items():
                    # 금액은 category_totals에서 가져온 실제 금액을 사용
                    actual_amount = category_totals[category] 
                    print(f"- {category}: {actual_amount}원 ({ratio}%)") 
                print("-" * 30)
                print()

        elif choice == "5":
            print("가계부를 종료합니다.")
            break

        else:
            print("잘못된 선택입니다.\n")


if __name__ == "__main__":
    main()
