import tkinter as tk
from tkinter import filedialog
from select_func import Select_Func
from svg_to_png import convert_files

if __name__ == "__main__":
    root = tk.Tk()
    select_func = Select_Func(root, convert_files)
    root.mainloop()
