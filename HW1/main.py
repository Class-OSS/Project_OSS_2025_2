import tkinter as tk
from calc import ScientificCalculator

if __name__ == "__main__":
    root = tk.Tk()
    calc = ScientificCalculator(root)
    root.mainloop()