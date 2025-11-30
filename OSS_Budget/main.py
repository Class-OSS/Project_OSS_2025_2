# main.py
from budget import Budget

def main():
    # 기본 파일명은 'expenses.txt' (원하시면 변경 가능)
    budget = Budget(filename="expenses.txt", auto_load=True)

    while True:
        print("==== 간단 가계부 ====")
        print("1. 지출 추가")
        print("2. 지출 목록 보기")
        print("3. 날짜별 정렬해서 보기 (최신순)")
        print("4. 카테고리별 요약")
        print("5. 총 지출 보기")
        print("6. 지출 삭제")
        print("7. 파일로 저장 (기본: expenses.txt)")
        print("8. 파일 불러오기 (기본: expenses.txt, 불러오면 메모리 덮어쓰기)")
        print("9. 백업 생성")
        print("10. 종료")
        choice = input("선택 > ").strip()

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
            # 정렬 옵션: 최신순(기본) or 오래된순
            ord_choice = input("정렬 옵션: 1) 최신순  2) 오래된순 (기본: 최신순): ").strip()
            if ord_choice == "2":
                budget.list_expenses_sorted(reverse=False)
            else:
                budget.list_expenses_sorted(reverse=True)

        elif choice == "4":
            budget.category_summary()

        elif choice == "5":
            budget.total_spent()

        elif choice == "6":
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
            confirm = input(f"{idx}번 항목을 정말 삭제하시겠습니까? (y/n): ").strip().lower()
            if confirm == "y":
                budget.delete_expense(idx)
            else:
                print("삭제 취소.\n")

        elif choice == "7":
            fname = input(f"저장할 파일명 입력 (기본: {budget.filename}): ").strip()
            if fname == "":
                fname = budget.filename
            try:
                # save_to_file은 기존 파일이 있으면 자동으로 백업을 만듭니다.
                budget.save_to_file(fname)
            except Exception as e:
                print(f"저장 실패: {e}\n")

        elif choice == "8":
            fname = input(f"불러올 파일명 입력 (기본: {budget.filename}): ").strip()
            if fname == "":
                fname = budget.filename
            confirm = input(f"{fname}에서 불러오면 현재 데이터가 덮어써집니다. 계속하시겠습니까? (y/n): ").strip().lower()
            if confirm != "y":
                print("불러오기 취소.\n")
                continue
            success = budget.load_from_file(fname)
            if not success:
                print("불러오기 실패 또는 파일 없음.\n")

        elif choice == "9":
            fname = input(f"백업 대상 파일명 (기본: {budget.filename}): ").strip()
            if fname == "":
                fname = budget.filename
            try:
                bak = budget.create_backup(fname)
                print(f"백업 파일 생성: {bak}\n")
            except Exception as e:
                print(f"백업 실패: {e}\n")

        elif choice == "10":
            print("가계부를 종료합니다.")
            break

        else:
            print("잘못된 선택입니다.\n")

if __name__ == "__main__":
    main()
