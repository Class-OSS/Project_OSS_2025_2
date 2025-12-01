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

def add_multiple_expenses(self, input_string, delimiter=';'):
    """
    한 줄로 입력된 여러 지출을 파싱하여 저장합니다.
    형식: '카테고리 금액 내용; 카테고리 금액 내용'
    """
    
    expenses_list = input_string.split(delimiter)
    successful_count = 0
    
    print("\n--- 일괄 처리 시작 ---")
    
    for item in expenses_list:
        item = item.strip()
        if not item:
            continue
            
        # 공백으로 데이터를 분리합니다. (예: ['식비', '15000', '점심 값'])
        parts = item.split()
        
        # 카테고리, 금액, 내용 (총 3개)만 필요
        if len(parts) < 3:
            print(f"경고: '{item}' - 데이터 항목이 부족합니다. (최소 3개 필요: 카테고리, 금액, 내용)")
            continue
            
        # 데이터 추출
        category = parts[0]
        amount_str = parts[1]
        # 내용은 세 번째 항목부터 끝까지 모두 합칩니다. (내용에 공백이 있어도 처리 가능)
        description = " ".join(parts[2:]) 
        
        try:
            amount = int(amount_str)
            # 기존의 add_expense 함수를 호출합니다.
            self.add_expense(category, description, amount)
            successful_count += 1
        except ValueError:
            print(f"경고: '{item}' - 금액('{amount_str}')이 숫자가 아닙니다. 저장 실패.")
        except Exception as e:
            print(f"경고: '{item}' - 알 수 없는 오류 발생 ({e}). 저장 실패.")
            
    print(f"--- 일괄 처리 완료 ({successful_count}건 성공) ---\n")
