# -*- coding: cp949 -*-
# Budget 객체를 이용해 지출 삭제 기능을 제공하는 모듈입니다.

def delete_expense_interactive(budget):
    """사용자에게 번호를 입력받아 해당 지출 내역을 삭제합니다."""
    if not budget.expenses:
        print("지출 내역이 없습니다.\n")
        return

    budget.list_expenses()

    try:
        index = int(input("삭제할 지출 번호를 입력하세요: "))
    except ValueError:
        print("잘못된 번호입니다.\n")
        return

    if 1 <= index <= len(budget.expenses):
        removed = budget.expenses.pop(index - 1)
        print(f"삭제된 지출: {removed}\n")
    else:
        print("존재하지 않는 번호입니다.\n")
