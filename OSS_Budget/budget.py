class Budget:
    def __init__(self):
        self.expenses = []
    #단일 지출을 추가
    def add_expense(self, category, description, amount):
        expense = {'category': category, 'description': description, 'amount': amount}
        self.expenses.append(expense)
        print(f"지출이 추가되었습니다: {description} ({amount}원)")
     #전체 지출 목록을 출력.
    def list_expenses(self):
        print("\n[ 전체 지출 목록 ]")
        if not self.expenses:
            print("지출 내역이 없습니다.")
            return

        for expense in self.expenses:
            print(f"카테고리: {expense['category']}, 내용: {expense['description']}, 금액: {expense['amount']}원")
        print()
     #총 지출 금액을 계산하여 출력.
    def total_spent(self):
        total = sum(expense['amount'] for expense in self.expenses)
        print(f"\n총 지출: {total}원\n")
    #한 줄로 입력된 여러 지출을 파싱하여 저장. 형식: '카테고리 금액 내용; 카테고리 금액 내용'
    def add_multiple_expenses(self, input_string, delimiter=';'):
        expenses_list = input_string.split(delimiter)
        successful_count = 0

        print("\n--- 일괄 처리 시작 ---")

        for item in expenses_list:
            item = item.strip()
            if not item:
                continue

            # 공백으로 데이터를 분리
            parts = item.split()

            # 카테고리, 금액, 내용 (총 3개) 필요.
            if len(parts) < 3:
                print(f"경고: '{item}' - 데이터 항목이 부족합니다. (최소 3개 필요: 카테고리, 금액, 내용)")
                continue

            # 데이터 추출
            category = parts[0]
            amount_str = parts[1]
            description = " ".join(parts[2:])

            try:
                amount = int(amount_str)
                self.add_expense(category, description, amount)
                successful_count += 1
            except ValueError:
                print(f"경고: '{item}' - 금액('{amount_str}')이 숫자가 아닙니다. 저장 실패.")
            except Exception as e:
                print(f"경고: '{item}' - 알 수 없는 오류 발생 ({e}). 저장 실패.")

        print(f"--- 일괄 처리 완료 ({successful_count}건 성공) ---\n")

    #특정 카테고리에 해당하는 지출 내역을 검색하고 출력.
    def search_expenses(self, category):
        print(f"\n[ '{category}' 검색 결과 ]")
        result_count = 0
        results = []

        for expense in self.expenses:
            if expense['category'] == category:
                results.append(expense)
                result_count += 1

        if result_count == 0:
            print("검색된 내역이 없습니다.")
        else:
            for expense in results:
                print(f"카테고리: {expense['category']}, 내용: {expense['description']}, 금액: {expense['amount']}원")

        print()
