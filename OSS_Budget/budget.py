import datetime

class Expense:
    def __init__(self, date, category, description, amount):
        self.date = date
        self.category = category
        self.description = description
        self.amount = amount

    def __str__(self):
        return f"[{self.date}] {self.category} - {self.description}: {self.amount}원"

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

    # [Day 2 신규 기능] 사용자 설정 단위 기반 시각화
    def show_visual_stats(self):
        if not self.expenses:
            print("데이터가 없어 그래프를 그릴 수 없습니다.\n")
            return

        # 1. 사용자에게 단위 입력받기 (예외처리 포함)
        try:
            unit = int(input("\n그래프 1칸(■)당 금액 단위를 입력하세요 (예: 1000): "))
            if unit <= 0:
                print("단위는 1원 이상이어야 합니다. 기본값(1000원)으로 진행합니다.")
                unit = 1000
        except ValueError:
            print("숫자만 입력 가능합니다. 기본값(1000원)으로 진행합니다.")
            unit = 1000

        print(f"\n📊 [카테고리별 지출 시각화] (단위: {unit}원)")
        print("-" * 40)

        # 2. 카테고리별 금액 집계
        stats = {}
        for e in self.expenses:
            stats[e.category] = stats.get(e.category, 0) + e.amount

        # 3. 그래프 그리기 (최대 30칸 제한)
        for category, amount in stats.items():
            # 로직: 금액 // 단위 -> 개수 구하기
            bar_length = amount // unit
            
            # 너무 길어지면 30개에서 자르고 '+' 표시를 붙여줌 (센스 있는 UX)
            if bar_length > 30:
                bar_graph = "■" * 30 + "..."
            else:
                bar_graph = "■" * bar_length
            
            print(f"{category.ljust(6)} | {bar_graph} ({amount:,}원)")
        
        print("-" * 40 + "\n")

def main():
    budget = Budget()

    while True:
        print("==== 간단 가계부 ====")
        print("1. 지출 추가")
        print("2. 지출 목록 보기")
        print("3. 총 지출 보기")
        print("4. 지출 시각화 리포트")
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

        elif choice == "4":
            # [신규 기능 호출]
            budget.show_visual_stats()

        elif choice == "5":
            print("가계부를 종료합니다.")
            break

        else:
            print("잘못된 선택입니다.\n")

if __name__ == "__main__":
    main()