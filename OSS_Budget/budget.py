import datetime
from expense import Expense

class Budget:
    def __init__(self):
        self.expenses = []

    def add_expense(self, category, description, amount):
        today = datetime.date.today().isoformat()
        expense = Expense(today, category, description, amount)
        self.expenses.append(expense)
        print("지출이 추가되었습니다.\n")

    def list_expenses(self):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return
        print("\n[지출 목록]")
        for idx, e in enumerate(self.expenses, 1):
            print(f"{idx}. {e}")
        print()

    def total_spent(self):
        total = sum(e.amount for e in self.expenses)
        print(f"총 지출: {total}원\n")

#지출 삭제 기능 추가
    def delete_expense(self, index_input):
        try:
            # 1. 입력값이 숫자인지 확인하고 정수로 변환 
            index_to_delete = int(index_input) - 1
            
            if 0 <= index_to_delete < len(self.expenses):
                expense_to_check = self.expenses[index_to_delete]
                
                # 2. 삭제 전 사용자에게 확인 요청
                Check = input(f" '{expense_to_check.description}' ({expense_to_check.amount}원)을 삭제하시겠습니까? (Y/N): ").upper()

                if Check == 'Y':
                    deleted_expense = self.expenses.pop(index_to_delete)
                    print(f" '{deleted_expense.description}' 지출이 성공적으로 삭제되었습니다.\n")
                elif Check == 'N':
                    print("삭제를 취소했습니다.\n")
                else:
                    print("유효하지 않은 입력입니다. 삭제를 취소합니다.\n")
            else:
                print("유효하지 않은 입력입니다. .\n")
                
        except ValueError:
            print("오류: 숫자를 입력하시오.\n")
        except Exception as e:
            print(f"오류 발생 : {e}\n")

