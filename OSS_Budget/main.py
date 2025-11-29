from budget import Budget


# ============================
#    카테고리 Top3 출력 함수 
# ============================
def show_top3(budget):
    top3, total = budget.get_monthly_category_top3()

    if not top3:
        print("\n이번 달 지출 내역이 없습니다.\n")
        return

    print("\n=== 이번 달 지출 Top3 카테고리 ===")
    for idx, (cat, amt) in enumerate(top3, start=1):
        print(f"{idx}) {cat} - {amt:,}원")
    print(f"\n총 지출: {total:,}원")
    print("=================================\n")


def main():
    budget = Budget()

    while True:
        print("==== 간단 가계부 ====")
        print("1. 지출 추가")
        print("2. 지출 목록 보기")
        print("3. 총 지출 보기")
        print("4. 종료")
        print("5. 이번 달 카테고리별 지출 Top3 보기")  # 추가
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
            print("가계부를 종료합니다.")
            break

        elif choice == "5":   # Top3 함수 호출
            show_top3(budget)

        else:
            print("잘못된 선택입니다.\n")


if __name__ == "__main__":
    main()
