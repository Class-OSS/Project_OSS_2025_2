import tkinter as tk
import datetime # 날짜/시간 처리를 위해 추가

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("300x400")
        self.expression = ""
        self.entry = tk.Entry(root, width=16, font=('Arial', 24))
        self.entry.grid(row=0, column=0, columnspan=4)
        
        # --- [PR 2차 추가 기능 시작] ---
        self.history = [] # 계산 기록을 저장할 리스트 추가
        # --- [PR 2차 추가 기능 끝] ---
        
        self.create_buttons() # 버튼 생성 메서드가 있다고 가정

    # ... (기존 메서드들: create_buttons, button_click, calculate 등 유지) ...

    # --- [PR 2차 추가 기능 시작] ---
    def update_history(self, expression, result):
        """계산 결과를 내부 리스트에 저장"""
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        record = f"[{now}] {expression} = {result}"
        self.history.append(record)

    def save_history(self, filename="calc_history.txt"):
        """저장된 기록을 파일에 저장"""
        if not self.history:
            print("\n[알림] 저장할 계산 기록이 없습니다.")
            return

        try:
            with open(filename, 'w', encoding='utf-8') as f:
                for record in self.history:
                    f.write(record + '\n')
            print(f"\n[성공] 총 {len(self.history)}건의 기록이 '{filename}'에 저장되었습니다.")
        except Exception as e:
            print(f"\n[오류] 기록 저장 중 오류 발생: {e}")

    def load_and_display_history(self, filename="calc_history.txt"):
        """파일에서 기록을 불러와 출력"""
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                records = f.readlines()
            
            print("\n--- 계산 기록 목록 ---")
            if records:
                for record in records:
                    # GUI 환경이므로 터미널 대신 별도의 창이나 위젯에 출력할 수 있지만, 여기서는 간편하게 터미널(콘솔) 출력
                    print(record.strip()) 
            else:
                print("기록 파일이 비어 있습니다.")
            print("-----------------------\n")

        except FileNotFoundError:
            print(f"\n[알림] 기록 파일 '{filename}'이 존재하지 않습니다. 먼저 저장하세요.")
        except Exception as e:
            print(f"\n[오류] 기록 불러오기 중 오류 발생: {e}")
    # --- [PR 2차 추가 기능 끝] ---

# ... (기존 코드의 calculate 메서드가 결과를 낼 때마다 self.update_history(exp, result)를 호출하도록 수정 필요)
# 이 부분은 기존 코드가 없으므로 main.py에서 별도의 메뉴로 호출하도록 구성합니다.

