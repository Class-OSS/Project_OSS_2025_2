import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from budget import Budget


def run_budget_gui(budget: Budget):
    root = tk.Tk()
    root.title("지출 미리보기 / CSV 저장 & 불러오기")
    root.geometry("700x400")

    # 테이블 생성
    columns = ("date", "category", "description", "amount")
    tree = ttk.Treeview(root, columns=columns, show="headings")

    tree.heading("date", text="날짜")
    tree.heading("category", text="카테고리")
    tree.heading("description", text="설명")
    tree.heading("amount", text="금액")

    tree.column("date", width=100, anchor="center")
    tree.column("category", width=100, anchor="center")
    tree.column("description", width=370, anchor="w")
    tree.column("amount", width=100, anchor="e")

    tree.pack(fill="both", expand=True, padx=10, pady=10)

    # 초기 데이터 채우기 (없으면 빈 상태)
    def refresh_table():
        for row in tree.get_children():
            tree.delete(row)

        for e in budget.expenses:
            tree.insert("", "end", values=(e.date, e.category, e.description, e.amount))

    refresh_table()

    # 버튼 영역
    btn_frame = tk.Frame(root)
    btn_frame.pack(fill="x", padx=10, pady=10)

    # CSV 저장
    def on_save_csv():
        filename = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV 파일", "*.csv"), ("모든 파일", "*.*")],
            initialfile="expenses.csv"
        )
        if filename:
            budget.save_to_csv(filename)
            messagebox.showinfo("완료", "CSV 저장 완료!")

    # CSV 불러오기
    def on_load_csv():
        filename = filedialog.askopenfilename(
            filetypes=[("CSV 파일", "*.csv"), ("모든 파일", "*.*")]
        )
        if filename:
            budget.load_from_csv(filename)
            refresh_table()
            messagebox.showinfo("완료", "CSV 불러오기 완료!")

    load_btn = tk.Button(btn_frame, text="CSV 불러오기", command=on_load_csv)
    save_btn = tk.Button(btn_frame, text="CSV 저장", command=on_save_csv)
    close_btn = tk.Button(btn_frame, text="닫기", command=root.destroy)

    load_btn.pack(side="left", padx=5)
    save_btn.pack(side="left", padx=5)
    close_btn.pack(side="right", padx=5)

    root.mainloop()
