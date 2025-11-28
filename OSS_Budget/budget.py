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
    
    def manage_expenses(self):
        if not self.expenses:
            print("수정/삭제할 지출 내역이 없습니다.\n")
            return

        print("\n[수정/삭제 가능한 지출 목록]")
        for idx, expense in enumerate(self.expenses, 1):
            print(f"{idx}. {expense}")
        
        try:
            choice = input("\n번호 입력 (취소: C) > ").upper()
            if choice == 'C': return

            exp_index = int(choice) - 1
            if not (0 <= exp_index < len(self.expenses)): raise ValueError

            expense_to_manage = self.expenses[exp_index]
            action = input(f"'{expense_to_manage.description}' 수정(E) 또는 삭제(D)? (E/D) > ").upper()
            
            if action == 'D':
                deleted = self.expenses.pop(exp_index)
                print(f"지출 내역이 삭제되었습니다: {deleted}\n")
                
            elif action == 'E':
                print(f"--- 지출 내역 수정 ---")
                
                new_category = input(f"새 카테고리 (기존: {expense_to_manage.category}): ") or expense_to_manage.category
                new_description = input(f"새 설명 (기존: {expense_to_manage.description}): ") or expense_to_manage.description
                new_amount_str = input(f"새 금액(원) (기존: {expense_to_manage.amount}): ")
                new_amount = int(new_amount_str) if new_amount_str else expense_to_manage.amount
                
                expense_to_manage.category, expense_to_manage.description, expense_to_manage.amount = \
                    new_category, new_description, new_amount
                
                print(f"지출 내역이 수정되었습니다: {expense_to_manage}\n")
            else:
                print("유효하지 않은 동작입니다.\n")

        except ValueError:
            print("유효하지 않은 입력입니다.\n")
        except Exception as e:
            print(f"처리 중 오류가 발생했습니다: {e}\n")

