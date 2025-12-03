import tkinter as tk
from calc import Calculator


if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
    import tkinter as tk
from calc import percentage

def calculate_percentage():
    try:
        value = float(entry_value.get())
        percent = float(entry_percent.get())

        result = percentage(value, percent, round_result=True)
        label_result.config(text=f"Result: {result}")

    except ValueError:
        label_result.config(text="Error: invalid number input")
    except TypeError as e:
        label_result.config(text=f"Error: {str(e)}")
    except Exception as e:
        label_result.config(text=f"Unexpected Error: {str(e)}")

   root = tk.Tk()
   root.title("Percentage Calculator")

   tk.Label(root, text="Value:").pack()
   entry_value = tk.Entry(root)
   entry_value.pack()

  tk.Label(root, text="Percent (%):").pack()
  entry_percent = tk.Entry(root)
  entry_percent.pack()

  btn = tk.Button(root, text="Calculate", command=calculate_percentage)
  btn.pack()

  label_result = tk.Label(root, text="Result: ")
  label_result.pack()

  root.mainloop()
