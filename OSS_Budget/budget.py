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

    def export_to_html(self):
        if not self.expenses:
            print("저장할 지출 내역이 없습니다.\n")
            return

        filename = "budget_report.html"
        try:
            with open(filename, "w", encoding="utf-8") as f:
                f.write("<html><head><meta charset='utf-8'>")
                f.write("<style>")
                f.write("table { width: 100%; border-collapse: collapse; }")
                f.write("th, td { border: 1px solid #ddd; padding: 8px; text-align: center; }")
                f.write("th { background-color: #f2f2f2; }")
                f.write("</style></head><body>")
                
                f.write("<h1>💰 나의 가계부 리포트</h1>")
                f.write("<table>")
                f.write("<tr><th>날짜</th><th>카테고리</th><th>내용</th><th>금액</th></tr>")

                total = 0
                for expense in self.expenses:
                    f.write(f"<tr>")
                    f.write(f"<td>{expense.date}</td>")
                    f.write(f"<td>{expense.category}</td>")
                    f.write(f"<td>{expense.description}</td>")
                    f.write(f"<td>{expense.amount}원</td>")
                    f.write(f"</tr>")
                    total += expense.amount
                
                f.write("</table>")
                f.write(f"<h3>총 지출 합계: {total}원</h3>")
                f.write("</body></html>")
                
            print(f"'{filename}' 파일이 생성되었습니다! 웹브라우저에서 열어보세요.\n")
            
        except Exception as e:
            print(f"파일 저장 중 오류가 발생했습니다: {e}\n")


