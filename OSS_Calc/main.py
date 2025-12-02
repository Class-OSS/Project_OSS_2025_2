import tkinter as tk
from calc import Calculator


if __name__ == "__main__":
    root = tk.Tk()
    root.title("OSS_Calc 계산기")
    root.geometry("300*400")
    root.resizable(False,False)
    root.update_idletasks()
    screen_width=root.winfo_screenwidth()
    screen_height=root.winfo_screenheigtht()
    window_width=root.winfo_width()
    window_height=root.winfo_height()
    x=(screen_width-window_width)//2
    y=(screen_height-window_height)//2
    root.geometry(f"+{x}+{y}")
    calc = Calculator(root)
    root.mainloop()