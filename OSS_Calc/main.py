import tkinter as tk
from calc import Calculator
import threading # GUI와 터미널 입력을 동시에 처리하기 위해 threading 모듈 추가

def run_gui(root):
    """GUI를 메인 스레드에서 실행하는 함수"""
    root.mainloop()

def main():
    root = tk.Tk()
    calc = Calculator(root)
    
    # GUI를 별도의 스레드에서 실행하여 터미널 입력(input())이 막히지 않도록 함
    gui_thread = threading.Thread(target=run_gui, args=(root,), daemon=True)
    gui_thread.start()

    while True:
        print("\n==== 계산기 메뉴 ====")
        print("1. 계산기 창 사용 (GUI)")
        print("2. 기록 저장 (파일)") # PR 2차 기능 추가
        print("3. 기록 보기 (파일)") # PR 2차 기능 추가
        print("4. 종료") 

        choice = input("선택 > ")
        print("-" * 20)

        if choice == "1":
            # GUI 창이 닫혔을 경우 다시 띄우는 로직 (옵션)
            if not gui_thread.is_alive():
                 print("GUI 창이 닫혀있습니다. 다시 실행하려면 프로그램을 재시작하세요.")
            else:
                 print("GUI 창을 사용하세요.")

        elif choice == "2":
            # 기록 저장 기능 호출 (calc.py에 추가된 기능)
            calc.save_history()

        elif choice == "3":
            # 기록 보기 기능 호출 (calc.py에 추가된 기능)
            calc.load_and_display_history()

        elif choice == "4":
            print("계산기를 종료합니다.")
            break

        else:
            print("잘못된 선택입니다.")


if __name__ == "__main__":
    main()