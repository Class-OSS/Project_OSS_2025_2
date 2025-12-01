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

+    def category_summary(self):
+        if not self.expenses:
+            print("지출 내역이 없습니다.\n")
+            return
+
+        summary = {}
+        for e in self.expenses:
+            summary[e.category] = summary.get(e.category, 0) + e.amount
+
+        print("\n[카테고리별 지출 합계]")
+        for cat, total in summary.items():
+            print(f"{cat}: {total}원")
+        print()


