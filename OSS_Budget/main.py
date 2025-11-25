# main.py
from budget import Budget

def main():
    budget = Budget()

    while True:
        print("==== 간단 가계부 ====")
        print("1. 지출 추가")
        print("2. 지출 목록 보기")
        print("3. 총 지출 보기")
        print("4. 지출 삭제")   # 새로 추가된 항목
        print("5. 종료")        # 종료 번호 변경
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

        # 추가 내용
        elif choice == "4":
            # 삭제 흐름: 먼저 목록 출력 → 인덱스 입력 → 확인 → 삭제 시도
            if not budget.expenses:
                print("삭제할 지출이 없습니다.\n")
                continue

            budget.list_expenses()
            idx_str = input("삭제할 항목 번호를 입력하세요 (취소: Enter): ").strip()
            if idx_str == "":
                print("삭제 취소.\n")
                continue
            try:
                idx = int(idx_str)
            except ValueError:
                print("숫자를 입력하세요.\n")
                continue

            # 삭제 전 확인
            confirm = input(f"{idx}번 항목을 정말 삭제하시겠습니까? (y/n): ").strip().lower()
            if confirm == "y":
                budget.delete_expense(idx)
            else:
                print("삭제 취소.\n")

        elif choice == "5":
            print("가계부를 종료합니다.")
            break

        else:
            print("잘못된 선택입니다.\n")

if __name__ == "__main__":
    main()